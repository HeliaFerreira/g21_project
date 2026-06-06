# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:30:12 2026

@author: up202506781
"""

from flask import Flask, render_template, request, session 
from classes.curator import Curator 
from classes.exhibit import Exhibit 
from classes.gclass import Gclass 
from classes.museum import Museum 
from classes.specialty import Specialty 
from classes.visitors import Visitors 
from classes.userlogin import Userlogin 


import datetime
import sqlite3
import pandas as pd
import plotly.express as px

app = Flask(__name__)


Museum.read('data/database.db')
Specialty.read('data/database.db') 
Exhibit.read('data/database.db')
Curator.read('data/database.db')
Visitors.read('data/database.db')
Userlogin.read('data/database.db')

@app.route("/")
def bem_vindo():
    return render_template("home.html")

@app.route("/hello")
def hello_world():
    data = datetime.datetime.today()
    return render_template("hello.html", data=data)

@app.route("/about")
def about():
    return render_template("about.html") 

@app.route("/museus")
def listar_museus():
    lista_de_museus = list(Museum.obj.values())
    return render_template("museus.html", museus=lista_de_museus)

@app.route("/exposicoes")
def listar_exposicoes():
    lista_de_exposicoes = list(Exhibit.obj.values())
    return render_template("exposicoes.html", exposicoes=lista_de_exposicoes)

@app.route("/curadores")
def listar_curadores():
    lista_de_curadores = list(Curator.obj.values())
    return render_template("curadores.html", curadores=lista_de_curadores)

@app.route("/visitantes")
def listar_visitantes():
    lista_de_visitantes = list(Visitors.obj.values())
    return render_template("visitantes.html", visitantes=lista_de_visitantes)


@app.route('/ranking-exposicoes')
def ranking_exposicoes():

    conn = sqlite3.connect('data/database.db')
    

    query1 = """
        SELECT Exhibit.title as Titulo, SUM(Visitors."nº visitors") as Total_Visitantes
        FROM Exhibit
        JOIN Visitors ON Exhibit.id = Visitors.id_exhibit
        GROUP BY Exhibit.id
        ORDER BY Total_Visitantes DESC
        LIMIT 10
    """
    df1 = pd.read_sql_query(query1, conn)
    
    fig1 = px.bar(df1, x='Total_Visitantes', y='Titulo', orientation='h',
                 title='Top 10 Exposições com Mais Visitantes',
                 labels={'Total_Visitantes': 'Número de Visitantes', 'Titulo': 'Exposição'},
                 color='Total_Visitantes', color_continuous_scale='Viridis')
    fig1.update_layout(yaxis={'categoryorder':'total ascending'})
    grafico1_html = fig1.to_html(full_html=False)


    query2 = """
        SELECT category as Categoria, COUNT(id) as Quantidade
        FROM Exhibit
        WHERE category != '' 
        GROUP BY category
    """
    df2 = pd.read_sql_query(query2, conn)
    
    fig2 = px.pie(df2, values='Quantidade', names='Categoria', 
                  title='Distribuição de Exposições por Categoria',
                  color_discrete_sequence=px.colors.qualitative.Pastel)
    
    fig2.update_traces(textposition='inside', textinfo='percent+label')
    grafico2_html = fig2.to_html(full_html=False)

    conn.close()

    return render_template('ranking.html', grafico_barras=grafico1_html, grafico_circular=grafico2_html)

@app.route("/login")
def login():
    return render_template("login.html", id= 0, user= "", password="", ulogin=session.get("user"),resul = "")

@app.route("/logoff")
def logoff():
    session.pop("user",None)
    return render_template("index.html", ulogin=session.get("user"))

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        return render_template("index.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)

@app.route("/Userlogin", methods=["post","get"])
def userlogin():
    global prev_option
    msg = ""
    ulogin=session.get("user")
    if (ulogin != None):
        user_id = Userlogin.get_user_id(ulogin)
        group = Userlogin.obj[user_id].usergroup
        if group != "admin":
            Userlogin.current(user_id)
        butshow = "enabled"
        butedit = "disabled"
        option = request.args.get("option")
        if option == "edit":
            butshow = "disabled"
            butedit = "enabled"
        elif option == "delete":
            obj = Userlogin.current()
            if obj.id != user_id:
                Userlogin.remove(obj.id)
                if not Userlogin.previous():
                    Userlogin.first()
            else:
                msg = 'You cannot delete the same user'
        elif option == "insert":
            butshow = "disabled"
            butedit = "enabled"
        elif option == 'cancel':
            pass
        elif prev_option == 'insert' and option == 'save':
            user = request.form["user"]
            if len(Userlogin.find(user, 'user')) == 0:
                usergroup = request.form["usergroup"]
                password =  request.form["password"]
                obj = Userlogin(0, user, usergroup, Userlogin.set_password(password))
                Userlogin.insert(obj.id)
                Userlogin.last()
            else:
                msg = 'duplicate username'
                Userlogin.current()
        elif prev_option == 'edit' and option == 'save':
            obj = Userlogin.current()
            if group == "admin":
                obj.usergroup = request.form["usergroup"]
            if request.form["password"] != "":
                obj.password = Userlogin.set_password(request.form["password"])
            Userlogin.update(obj.id)
        elif option == "first":
            Userlogin.first()
        elif option == "previous":
            Userlogin.previous()
        elif option == "next":
            Userlogin.nextrec()
        elif option == "last":
            Userlogin.last()
        elif option == 'exit':
            return render_template("index.html", ulogin=session.get("user"))
        prev_option = option
        obj = Userlogin.current()
        if option == 'insert' or len(Userlogin.lst) == 0:
            id = 0
            user = ""
            usergroup = ""
            password = ""
        else:
            id = obj.id
            user = obj.user
            usergroup = obj.usergroup
            password = ""
        return render_template("userlogin.html", butshow=butshow, butedit=butedit, msg=msg,id=id, user=user,
                               usergroup = usergroup,password=password,ulogin=session.get("user"), group=group)
    else:
        return render_template("index.html", ulogin=ulogin)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

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
from subs.apps_gform import apps_gform 
from subs.apps_subform import apps_subform 
from subs.apps_userlogin import apps_userlogin 



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
prev_option = ""
app.secret_key = 'BAD_SECRET_KEY'


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

@app.route("/specialties")
def list_specialties():
    lista_esp = list(Specialty.obj.values())
    return render_template("specialties.html", specialties=lista_esp)

@app.route("/curadores1")
def list_curadores():
    lista_de_curadores = list(Curator.obj.values())
    return render_template("curadores1.html", curadores=lista_de_curadores)

@app.route("/visitantes1")
def list_visitantes():
    lista_de_visitantes = list(Visitors.obj.values())
    return render_template("visitantes1.html", visitantes=lista_de_visitantes)



@app.route("/gform/<cname>", methods=["post","get"] )
def gform(cname):
    return apps_gform(cname)


@app.route("/subform/<cname>",methods=["post","get"])
def subform(cname):
    return apps_subform(cname)



@app.route('/ranking-exposicoes')
def ranking_exposicoes():

    conn = sqlite3.connect('data/database.db')
    

    query1 = """
        SELECT Exhibit.title as Title, SUM(Visitors."nº visitors") as Total_Visitors
        FROM Exhibit
        JOIN Visitors ON Exhibit.id = Visitors.id_exhibit
        GROUP BY Exhibit.id
        ORDER BY Total_Visitors DESC
        LIMIT 10
    """
    df1 = pd.read_sql_query(query1, conn)
    
    fig1 = px.bar(df1, x='Total_Visitors', y='Title', orientation='h',
                 title='Top 10 Exhibits with more Visitors',
                 labels={'Total_Visitors': 'Number of Visitors', 'Title': 'Exhibit'},
                 color='Total_Visitors', color_continuous_scale='Viridis')
    fig1.update_layout(yaxis={'categoryorder':'total ascending'})
    grafico1_html = fig1.to_html(full_html=False)


    query2 = """
        SELECT category as Category, COUNT(id) as Quantity
        FROM Exhibit
        WHERE category != '' 
        GROUP BY category
    """
    df2 = pd.read_sql_query(query2, conn)
    
    fig2 = px.pie(df2, values='Quantity', names='Category', 
                  title='Distribuition of Exhibits by Category',
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
    return render_template("home.html", ulogin=session.get("user"))

@app.route("/chklogin", methods=["post","get"])
def chklogin():
    user = request.form["user"]
    password = request.form["password"]
    resul = Userlogin.chk_password(user, password)
    if resul == "Valid":
        session["user"] = user
        if resul == "Valid":
            session["user"] = user
            session["group"] = Userlogin.obj[Userlogin.get_user_id(user)].usergroup
        return render_template("layout1.html", ulogin=session.get("user"))
    return render_template("login.html", user=user, password = password, ulogin=session.get("user"),resul = resul)

@app.route("/Userlogin", methods=["post","get"])
def userlogin(): 
    return apps_userlogin()


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

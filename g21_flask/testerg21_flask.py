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

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

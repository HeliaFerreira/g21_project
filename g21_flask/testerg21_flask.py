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

app = Flask(__name__) 


@app.route("/")
def bem_vindo():
    return "<h1>Bem-vindo!</h1>"


@app.route("/hello")
def hello_world():
    data = datetime.datetime.today()
    return render_template("hello.html", data = data)


@app.route("/about")
def about():
    return render_template("about.html") 


if __name__ == '__main__':
    app.run()
    
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:30:12 2026

@author: up202506781
"""

from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")

def bem_vindo():
    return "<h1>Bem-vindo!</h1>"


@app.route("/hello")
def hello_world():
    data = datetime.datetime.today()
    return render_template("hello.html", data = data)

if __name__ == '__main__':
    app.run() 
    
@app.route("/about")
def about():
    return render_template("about.html") 


if __name__ == '__main__':
    app.run()
    
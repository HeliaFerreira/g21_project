# -*- coding: utf-8 -*-
"""
Created on Tue May 19 15:30:12 2026

@author: up202506781
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")

def bem_vindo():
    return "<h1>Bem-vindo!<h1>"

if __name__ == '__main__':
    app.run()
    

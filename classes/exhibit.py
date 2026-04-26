# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:53:00 2026

@author: marti
"""

from classes.gclass import Gclass
import datetime

class Exhibit(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    
    # Lista de atributos
    att = ['_id', '_creation_date', '_title', '_category']
    
    # Título do cabeçalho da classe
    header = 'Exhibits'
    
    # Descrição dos campos 
    des = ['Id', 'Creation Date', 'Title', 'Category']
    
# Construtor
    def __init__(self, id, creation_date, title, category):
        super().__init__()
        
        # Atributos do objeto
        id = Exhibit.get_id(id)
        self._id = id
        
        # Converte a data diretamente
        self._creation_date = datetime.date.fromisoformat(str(creation_date))
        
        self._title = str(title)
        self._category = str(category)
        
        # Adicionar o novo objeto ao dicionário de objetos
        Exhibit.obj[id] = self
        
        # Adicionar o id à lista de ids 
        if id not in Exhibit.lst:
            Exhibit.lst.append(id)

    # Métodos Getter e Setter para a propriedade 'id'
    @property
    def id(self):
        return self._id
        
    @id.setter
    def id(self, id):
        self._id = id

    # Métodos Getter e Setter para a propriedade 'creation_date'
    @property
    def creation_date(self):
        return self._creation_date
        
    @creation_date.setter
    def creation_date(self, creation_date):
        self._creation_date = creation_date

    # Métodos Getter e Setter para a propriedade 'title'
    @property
    def title(self):
        return self._title
        
    @title.setter
    def title(self, title):
        self._title = title

    # Métodos Getter e Setter para a propriedade 'category'
    @property
    def category(self):
        return self._category
        
    @category.setter
    def category(self, category):
        self._category = category

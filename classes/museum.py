# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 15:05:55 2026

@author: jpfca
"""

from classes.gclass import Gclass

class Museum(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    
    att = ['_id','_name']
    header = 'Museum'
    des = ['Id','Museum Name']
    
    def __init__(self, id, name):
        super().__init__()
        
        id = Museum.get_id(id)
        self._id = int(id)
        self._name = name
        
        Museum.obj[id] = self
        Museum.lst.append(id)
    
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
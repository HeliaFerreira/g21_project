# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 09:00:00 2026

@author: g21
"""

# Class Specialty
# Import the generic class
from classes.gclass import Gclass

class Specialty(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

    att = ['_id','_specialty_name']

    header = 'Specialty'

    des = ['Id','Specialty Name']

    def __init__(self, id, specialty_name):
        super().__init__()

        # Object attributes
        id = Specialty.get_id(id)
        self._id = id
        self._specialty_name = specialty_name

        Specialty.obj[id] = self
        Specialty.lst.append(id)

    # Object properties
    @property
    def id(self):
        return self._id

    @property
    def specialty_name(self):
        return self._specialty_name
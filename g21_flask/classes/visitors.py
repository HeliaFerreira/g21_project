# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:25:53 2026

@author: hsff2
"""

# Class Visitors
from classes.exhibit import Exhibit
from classes.museum import Museum
# Import the generic class
from classes.gclass import Gclass
# product = museum 
#customer_order/order = exhibit


class Visitors(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier id, attribute must be the first on the list
    att = ['_id', '_id_exhibit','_id_museum','_conclusion_date','_n_visitors']
    # Class header title
    header = 'Visitors'
    # field description for use in, for example, input form
    des = ['Id','Id_Exhibit','Id_Museum','Conclusion_date','N_visitors']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, id_exhibit, id_museum, conclusion_date, n_visitors):
        super().__init__()
        # Object attributes
        # Check the exhibit and museum referential integrity
        id_exhibit = int(id_exhibit)
        id_museum = int(id_museum)
        if id_exhibit in Exhibit.lst:
            if id_museum in Museum.lst:
                id = Visitors.get_id(id)
                self._id = id
                self._id_exhibit = id_exhibit
                self._id_museum = id_museum
                self._conclusion_date = str(conclusion_date)
                self._n_visitors = int(n_visitors)
                # Add the new object to the Visitors list
                Visitors.obj[id] = self
                Visitors.lst.append(id)
            else:
                print('Museum ', id_museum, ' not found')
        else:
            print('Exhibit ', id_exhibit, ' not found')
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    
    # id_exhibit property getter method
    @property
    def id_exhibit(self):
        return self._id_exhibit
    
    # id_museum property getter method
    @property
    def id_museum(self):
        return self._id_museum
    
    # conclusion_date property getter method
    @property
    def conclusion_date(self):
        return self._conclusion_date
    
    # n_visitors property getter method
    @property
    def n_visitors(self):
        return self._n_visitors

        
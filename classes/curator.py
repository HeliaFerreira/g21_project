"""
@author: António Brito / Carlos Bragança (2025)
#objective: class Product
"""""
# Class Curator
# Import the generic class
from classes.gclass import Gclass

class Curator(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_extra_info','_id_museum','_id_specialty']
    # Class header title
    header = 'Curator'
    # field description for use in, for example, input form
    des = ['Id','Extra_Info','Id_Museum','Id_Specialty']
    # Constructor: Called when an object is instantiated
    def __init__(self, id, extra_info, id_museum, id_specialty):
        super().__init__()
        # Object attributes
        id = Curator.get_id(id)
        self._id = id
        self._extra_info = extra_info
        self._id_museum = id_museum
        self._id_specialty = id_specialty 
        # Add the new object to the Curator list
        Curator.obj[id] = self
        Curator.lst.append(id)
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # extra_info property getter method
    @property
    def extra_info(self):
        return self._extra_info

    # id_museum property getter method
    @property
    def id_museum(self):
        return self._id_museum

    # id_specialty property getter method
    @property
    def id_specialty(self):
        return self._id_specialty
"""
@author: António Brito / Carlos Bragança (2025)
#objective: class Customer_login
"""
# Class Utente
# import datetime
# Import the generic class
from classes.gclass import Gclass

class Curator(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # class attributes, identifier attribute 'id' must be the first on the list
    att = ['_id','_extra_info','_specialty']
    # Class header title
    header = 'Curators'
    # field description for use in, for example, input form
    des = ['Id_Curator','Extra_Info','Specialty']
    # Constructor: Called when an object is instantiated
    def __init__(self,id,extra_info,specialty, id_museum, id_specialty):
        super().__init__(id_museum, id_specialty)
        # Object attributes
        id = Curator.get_id(id)
        self._id = id
        self._extra_info = extra_info
        self._specialty = specialty
        # self._telefone = telefone
        # self._data_nascimento = datetime.date.fromisoformat(data_nascimento)
        # Add the new object to the Customer's list
        Curator.obj[id] = self
        Curator.lst.append(id)
    # Object properties
    # id property getter method
    @property
    def id(self):
        return self._id
    # name property getter method
    @property
    def extra_info(self):
        return self._extra_info
    # name property setter method
    # @nome.setter
    # def nome(self, nome):
    #     self._nome = nome
    # # address property getter method
    @property
    def specialty(self):
        return self._specialty
    # address property setter method
    # @morada.setter
    # def morada(self, morada):
    #     self._morada = morada
    # phone property getter method
    # @property
    # def telefone(self):
    #     return self._telefone
    # # phone property setter method
    # @telefone.setter
    # def telefone(self, telefone):
    #     self._telefone = telefone 
    
    # @property 
    # def data_nascimento(self):
    #     return self._data_nascimento 
    

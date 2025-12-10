from abc import *
from controle_parc_vehicle_python.vehicule import *

# Class with information on rentable bike
class Moto(ABC):
    def __init__(self, cylindree, type_moto):
        self.cylindree=cylindree
        self.type_moto=type_moto

    def get_cylindree(self):
        return self.cylindree
    
    def set_cylindree(self, cylindree):
        if cylindree=="":
            raise ValueError("Trop petit")
        else:
            self.cylindree=cylindree

    def get_type_moto(self):
        return self.type_moto
    
    def set_type_moto(self, type_moto):
        if type_moto !="sportive" or type_moto!="routière" or type_moto!="custom" or type_moto!="trail":
            raise ValueError("Pas correct")
        else:
            self.type_moto=type_moto
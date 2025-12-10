from abc import *
from controle_parc_vehicle_python.vehicule import *
from controle_parc_vehicle_python.assurable import *

# Class with information on rentable car
class Voiture(ABC):
    def __init__ (self, nombres_places, type_carburant, coffre_litres):
        self.nombres_places=nombres_places
        self.type_carburant=type_carburant
        self.coffre_litres=coffre_litres
    
    def get_nombres_places(self):
        return self.nombres_places
    
    def set_nombres_places(self, nombres_places):
        if nombres_places<2 or nombres_places>9:
            raise ValueError("Le nombre de places ne convient pas")
        else:
            self.nombres_places=nombres_places
    
    def get_type_carburant(self):
        return self.type_carburant
    
    def set_type_carburant(self, type_carburant):
        if type_carburant != "essence" or type_carburant!="diesel" or type_carburant!="électrique" or type_carburant!="hybride":
            raise ValueError("Le carburant ne convient pas")
        else:
            self.type_carburant=type_carburant

    def get_coffre_litres(self):
        return self.coffre_litres

    def set_coffre_litres(self, coffre_litres):
        if coffre_litres=="":
            raise ValueError("Le coffre est trop petit")
        else:
            self.coffre_litres=coffre_litres

    
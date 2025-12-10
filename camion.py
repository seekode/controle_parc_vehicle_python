from abc import *
from controle_parc_vehicle_python.vehicule import *
from controle_parc_vehicle_python.assurable import *

# Class with information on rentable truck 
class Camion(ABC):
    def __init__(self, charge_utile, volume_benne, permis_requis):
        self.charge_utile=charge_utile
        self.volume_benne=volume_benne
        self.permis_requis=permis_requis

    def get_charge_utile(self):
        return self.charge_utile
    
    def set_charge_utile(self, charge_utile):
        if charge_utile=="":
            raise ValueError ("Ne doit pas être vide")
        else:
            self.charge_utile=charge_utile
    
    def get_volume_benne(self):
        return self.volume_benne
    
    def set_volume_benne(self, volume_benne):
        if volume_benne=="":
            raise ValueError ("Ne doit pas être vide")
        else:
            self.volume_benne=volume_benne
    
    def get_permis_requis(self):
        return self.permis_requis
    
    def set_permis_requis(self, permis_requis):
        if permis_requis=="":
            raise ValueError ("Ne doit pas être vide")
        else:
            self.permis_requis=permis_requis
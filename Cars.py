from Insurable import Insurable
from Vehicule import Vehicule


class Cars(Vehicule, Insurable):
    def __init__(self, brand, modele, year, registration, kilometer, available, number_places, 
fuel_type, trunk_liters):
        super().__init__(brand, modele, year, registration, kilometer, available)
        self._number_places = number_places
        self._fuel_type = fuel_type
        self._trunk_liters = trunk_liters
    
    # Creation of setter and getter
    @property
    def number_places(self):
        return self._number_places
    
    @number_places.setter
    def number_places(self,value):
        self._number_places = value
        
    @property
    def fuel_type(self):
        return self._fuel_type
    
    @fuel_type.setter
    def fuel_type(self,value):
        self._fuel_type = value

    @property
    def trunk_liters(self):
        return self._trunk_liters
    
    @trunk_liters.setter
    def trunk_liters(self,value):
        self._trunk_liters = value

    def calculate_daily_rate(self):
        return None
    def calculate_insurance_premium(self):
        return None
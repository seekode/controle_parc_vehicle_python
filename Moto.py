from Vehicule import Vehicule


class Moto(Vehicule):
    def __init__(self, brand, modele, year, registration, kilometer, available, cylindree, type_moto):
        super().__init__(brand, modele, year, registration, kilometer, available)
        self._cylindree = cylindree
        self._type_moto = type_moto

    @property
    def cylindree(self):
        return self._cylindree
    
    @cylindree.setter
    def cylindree(self, value):
        self._cylindree = value

    @property
    def type_moto(self):
        return self._type_moto
    
    @type_moto.setter
    def type_moto(self, value):
        self._type_moto = value

    def calculate_daily_rate(self):
        return None
    
    
moto = Moto('suzuki','gsx 8r ', 2024,45454454,4520, True, None, 'suzuki' )

print(str(moto))
        
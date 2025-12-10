from abc import ABC, abstractmethod


class Vehicule(ABC):

    def __init__(self, brand, modele, year, registration, kilometer, available):
        self._brand = brand
        self._modele = modele
        self._year = year
        self._registration = registration
        self._kilometer = kilometer
        self._available = available
    
    # Creation of setter and getter
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value
        
    @property
    def modele(self):
        return self._modele

    @modele.setter
    def modele(self, value):
        self._modele = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = value

    @property
    def registration(self):
        return self._registration

    @registration.setter
    def registration(self, value):
        self._registration = value

    @property
    def kilometer(self):
        return self._kilometer

    @kilometer.setter
    def kilometer(self, value):
        self._kilometer = value
    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value

    def display_details(self):
        print(self.brand)
        print(self.modele)
        print(self.year)
        print(self.registration)
        print(self.kilometer)
        print(self.available)
# methode magique 
    def __str__(self):
        return self.brand + " "+self.modele
    
    # def __repr__(self):
    #     return 
    
    @abstractmethod
    def calculate_daily_rate(self):
        pass

# vehicule = Vehicule("v","1e",2000, 56454654654,45100,None)
# print(str(vehicule))
# print(repr(vehicule))
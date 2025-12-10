from datetime import datetime
from sqlite3 import Date
from Client import Client
from Vehicule import Vehicule

class Location:

    def __init__(self,lastname, name, license_number, birth_date, email,brand, modele, year, registration, kilometer, available, date_debut, date_end, kilometer_depart, return_kilometer, cout_total):


        self._client = Client.__init__(self,lastname, name, license_number, birth_date, email)

        self._vehicule = Vehicule.__init__(self,brand, modele, year, registration, kilometer, available)
        
        self._date_debut = date_debut
        self._date_end = date_end
        self._kilometer_depart = kilometer_depart
        self._return_kilometer = return_kilometer
        self._cout_total = cout_total

    @property
    def date_debut(self):
        return self._date_debut
    
    @date_debut.setter
    def date_debut(self, value):
        if Date(value) == True :
            self._date_debut = value
    
    @property
    def date_end(self):
        return self._date_end
    
    @date_end.setter
    def date_debut(self, value):
        if Date(value) == True :
            self._date_end = value
    
    @property
    def kilometer_depart(self):
        return self._kilometer_depart
    
    @kilometer_depart.setter
    def kilometer_depart(self, value):
        self._kilometer_depart = value
    
    @property
    def return_kilometer(self):
        return self._return_kilometer
    
    @return_kilometer.setter
    def return_kilometer(self, value):
        self._return_kilometer = value
    
    @property
    def cout_total(self):
        return self._cout_total
    
    @cout_total.setter
    def cout_total(self, value):
        self._cout_total = value

    def calculate_duration(self):
        debut = datetime(self.date_debut)
        end = datetime(self.date_end)
        result = end - debut
        return result
    
    def calculate_cout(self, tarif_journey, duree, insurance):
        result = tarif_journey * duree + insurance
        self.cout_total = result
        return self.cout_total
    
    def finsih_location(self, return_kilometer):
        if self.return_kilometer == None or self.return_kilometer == "":
            self.return_kilometer = return_kilometer
        else:
            print('This location period has already ended.')

    def __str__(self):
        return self.date_debut + " "+ self.date_end
    

location = Location('od', 'o',2115315151,'29/11/2006','aerfzg@zrg.com','er','zerfgh',2005,451248512845,95629562,True,'15/12/2024','03/05/2025',21231654,1365488,0)
print(str(location))
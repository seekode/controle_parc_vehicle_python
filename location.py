from controle_parc_vehicle_python.GestionnaireTarifs import *
# Class for location of vehicle) 
class Location:
    def __init__(self, client, vehicule, date_debut, date_fin, kilometrage_depart, kilometrage_retour, cout_total):
        self.client=client
        self.vehicule=vehicule
        self.date_debut=date_debut
        self.date_fin=date_fin
        self.kilometrage_depart=kilometrage_depart
        self.kilometrage_retour=kilometrage_retour
        self.cout_total=cout_total
    
    def calculer_duree(self):
        return 10
    
    def calculer_cout(self):
        return 10
    
    def terminer_location(kilometrage_retour):
        return 10

    def __str__(self):
        pass
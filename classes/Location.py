import Vehicule
import Client

class Location:
    # Initialisation
    def __init__(self, client:Client, vehicule:Vehicule, date_debut, date_fin, kilometrage_depart, kilometrage_retour, cout_total):
        self.client = client
        self.vehicule = vehicule
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.kilometrage_depart = kilometrage_depart
        self.kilometrage_retour = kilometrage_retour
        self.cout_total = cout_total

    # Getters
    @property
    def get_client(self) -> Client:
        return self.client
    
    @property
    def get_vehicule(self) -> Vehicule:
        return self.vehicule
    
    @property
    def get_date_debut(self):
        return self.date_debut
    
    @property
    def get_date_fin(self):
        return self.date_fin
        

    #  Méthodes
    def calculer_duree(self):
        return (self.date_fin - self.date_debut)
        
    def calculer_cout(self):
        if self.cout_total is not None:
            return self.cout_total 

           
    # Méthode
    def terminer_location(self):
        if self.date_fin is not None:
            raise Exception("Erreur : Cette location est déjà terminée.")
        return self.kilometrage_retour
        
    # Méthode magique
    def __str__(self):
        return f"Location de {self.vehicule} par {self.client} du {self.date_debut} au {self.date_fin}, Kilométrage départ: {self.kilometrage_depart}, Kilométrage retour: {self.kilometrage_retour}, Coût total: {self.cout_total}€"
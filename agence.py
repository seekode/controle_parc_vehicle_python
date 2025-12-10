from controle_parc_vehicle_python.camion import *
from controle_parc_vehicle_python.voiture import *
from controle_parc_vehicle_python.moto import *


class Agence:
    def __init__(
        self, nom, parc_vehicules, locations_en_cours, locations_terminees, clients
    ):
        self.nom = nom
        self.parc_vehicules = parc_vehicules
        self.locations_en_cours = locations_en_cours
        self.locations_terminees = locations_terminees
        self.clients = clients

    def ajouter_vehicule(self, vehicule):
        self.parc_vehicules.append(vehicule)

    def enregistrer_client(self, client):
        self.clients.append(client)

    def louer_vehicule(self, client, vehicule, date_debut):
        if vehicule in self.parc_vehicules:
            print("Le véhicule est disponible")
            self.clients.append(client)
            self.locations_en_cours.append(date_debut)
        else:
            raise ValueError("Vehicule indisponible")

    def retourner_vehicule(self, location, kilometrage_retour, date_fin):
        self.location_terminees.append(location, kilometrage_retour, date_fin)

    def afficher_vehicules_disponibles(self):
        return self.parc_vehicules

    def calculer_chiffres_affaires():
        return 10

    def vehicule_le_plus_loue():
        return "vroum"

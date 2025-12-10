from Location import Location
from exceptions import VehiculeIndisponible


class Agence:
    def __init__(self, nom):
        self.nom = nom
        self.parc_vehicules = []
        self.locations_en_cours = []
        self.locations_terminees = []
        self.clients = []

    def ajouter_vehicule(self, vehicule):
        self.parc_vehicules.append(vehicule)

    def enregistrer_client(self, client):
        self.clients.append(client)

    def louer_vehicule(self, client, vehicule, date_debut):
        if vehicule in [loc.vehicule for loc in self.locations_en_cours]:
            raise VehiculeIndisponible(f"Le véhicule {vehicule} n'est pas disponible.")

        location = Location(
            client=client,
            vehicule=vehicule,
            date_debut=date_debut,
            kilometrage_depart=vehicule.kilometrage,
        )

        self.locations_en_cours.append(location)
        return location

    def retourner_vehicule(self, location, kilometrage_retour, date_fin=None):
        if location not in self.locations_en_cours:
            raise ValueError("Cette location n'est pas en cours.")

        location.terminer_location(kilometrage_retour, date_fin)

        self.locations_en_cours.remove(location)
        self.locations_terminees.append(location)

    def afficher_vehicules_disponibles(self):
        vehicules_loues = [loc.vehicule for loc in self.locations_en_cours]
        for vehicule in self.parc_vehicules:
            if vehicule not in vehicules_loues:
                print(vehicule)

    def calculer_chiffre_affaires(self):
        return sum(loc.cout_total for loc in self.locations_terminees if loc.cout_total)

    def vehicule_le_plus_loue(self):
        from collections import Counter

        compteur = Counter(loc.vehicule for loc in self.locations_terminees)
        return compteur.most_common(1)[0][0] if compteur else None

import Location
class Agence(Location):
    # Initialisation
    def __init__(self, nom: str, parc_vehicules: str, location_en_cours: str, locations_terminees: str, clients: str):
        self.nom = nom
        self.parc_vehicules = parc_vehicules
        self.location_en_cours = location_en_cours
        self.locations_terminees = locations_terminees
        self.clients = clients

    # Méthodes
    def ajouter_vehicule(self, vehicule):
        self.parc_vehicules.append(vehicule)

    def enregistrer_client(self, client):
        self.clients.append(client)

    def louer_vehicule(self, client, vehicule, date_debut):
        if vehicule.get_est_disponible():
            location = Location(client, vehicule, date_debut, vehicule.get_kilometrage(), None, None)
            self.location_en_cours.append(location)
            vehicule.set_disponibilite(False)
            return location()
        else:
            raise Exception("Le véhicule est indisponible pour la location.")
        
    def retourner_vehicule(self, location, date_fin, kilometrage_retour):
        if location in self.location_en_cours:
            location.date_fin = date_fin
            location.kilometrage_retour = kilometrage_retour
            cout_total = location.calculer_cout()
            location.cout_total = cout_total
            self.location_en_cours.remove(location)
            self.locations_terminees.append(location)
            vehicule = location.get_vehicule()
            vehicule.set_disponibilite(True)
            vehicule.set_kilometrage(kilometrage_retour)
            return cout_total
        else:
            raise Exception("Cette location est déjà terminée ou n'existe pas.")
        
    def afficher_vehicules_disponibles(self):
        disponibles = [v for v in self.parc_vehicules if v.get_est_disponible()]
        return disponibles
    
    def calculer_chiffre_affaires(self):
        total = sum(location.cout_total for location in self.locations_terminees)
        return total
    
    def vehicule_le_plus_loue(self):
        compteur_locations = {}
        for location in self.locations_terminees:
            vehicule = location.get_vehicule()
            if vehicule in compteur_locations:
                compteur_locations[vehicule] += 1
            else:
                compteur_locations[vehicule] = 1
        if compteur_locations:
            vehicule_plus_loue = max(compteur_locations, key=compteur_locations.get)
            return vehicule_plus_loue
        return None
    
    # Méthode magique
    def __str__(self):
        return f"Agence: {self.nom}, Véhicules: {len(self.parc_vehicules)}, Locations en cours: {len(self.location_en_cours)}, Locations terminées: {len(self.locations_terminees)}, Clients: {len(self.clients)}"  
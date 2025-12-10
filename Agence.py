from Voiture import Voiture
from Moto import Moto
from Camion import Camion


# gère tous les véhicules, locations et clients
class Agence:
    def __init__(
        self, nom, parc_vehicules, locations_en_cours, locations_terminees, clients
    ):
        self.nom = nom
        self.parc_vehicules = parc_vehicules
        self.locations_en_cours = locations_en_cours
        self.locations_terminees = locations_terminees
        self.clients = clients

    def ajouter_vehicule(
        self,
        vehicule,
        marque,
        modele,
        annee,
        immatriculation,
        kilometrage,
        disponible,
        nombre_places,
        type_carburant,
        coffre_litres,
        charge_utile,
        volume_benne,
        permis_requis,
        cylindre,
        type_moto,
    ):
        if vehicule == "Voiture":
            self.parc_vehicules.push(
                Voiture(
                    marque,
                    modele,
                    annee,
                    immatriculation,
                    kilometrage,
                    disponible,
                    nombre_places,
                    type_carburant,
                    coffre_litres,
                )
            )
        elif vehicule == "Moto":
            self.parc_vehicules.push(
                Moto(
                    marque,
                    modele,
                    annee,
                    immatriculation,
                    kilometrage,
                    disponible,
                    cylindre,
                    type_moto,
                )
            )
        elif vehicule == "Camion":
            self.parc_vehicules.push(
                Camion(
                    marque,
                    modele,
                    annee,
                    immatriculation,
                    kilometrage,
                    disponible,
                    charge_utile,
                    volume_benne,
                    permis_requis,
                )
            )

    def ajouter_client(self, client):
        self.clients.push(client)

    def louer_vehicule(self, client, vehicule, date_debut):
        if vehicule.__disponible == True:
            self.vehicule.__disponible == False
        else:
            raise Exception("Désolé, le véhicule n'est pas disponible")

    def retourner_vehicule(location, kilometrage_retour, date_fin):
        if location == True:
            location = False
        return location

    def afficher_vehicules_disponibles(self):
        print(self.parc_vehicules)

    def calculer_chiffre_affaires(self):
        ca = 0
        for location in self.locations_en_cours:
            ca += location.calculer_cout()

    def vehicule_le_plus_loue(self):
        vehicule_le_plus_loue = self.parc_vehicules[0]
        for vehicule in self.parc_vehicules:
            if vehicule.nombre_locations > vehicule_le_plus_loue.nombre_locations:
                vehicule_le_plus_loue = vehicule
        return vehicule_le_plus_loue

from Client import Client
from GestionnaireTarifs import GestionnaireTarifs
from Voiture import Voiture
from Moto import Moto
from Camion import Camion


class Location(GestionnaireTarifs):
    def __init__(
        self,
        nom,
        prenom,
        numero_permis,
        date_naissance,
        email,
        type_vehicule,
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
        date_debut,
        date_fin,
        kilometrage_depart,
        kilometrage_retour,
        cout_total,
    ):
        self.client = Client(nom, prenom, numero_permis, date_naissance, email)
        if type_vehicule == "voiture":
            self.vehicule = Voiture(
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
        elif type_vehicule == "camion":
            self.vehicule = Camion(
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
        elif type_vehicule == "moto":
            self.vehicule = Moto(
                marque,
                modele,
                annee,
                immatriculation,
                kilometrage,
                disponible,
                cylindre,
                type_moto,
            )
        elif type_vehicule == "camion":
            self.vehicule = Camion(
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
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.kilometrage_depart = kilometrage_depart
        self.kilometrage_retour = kilometrage_retour
        self.cout_total = cout_total

    # calcule la durée de location
    def calculer_duree(
        self,
    ):
        return self.date_fin - self.date_debut

    # calcul la somme qui doit être versée
    def calculer_cout(self, tarif_journalier, assurance):
        print(self.vehicule)

        (
            GestionnaireTarifs.get_tarif_base(self.type_vehicule)
            * self.calculer_duree()
            + GestionnaireTarifs.get_tarif_base(self.type_vehicule)
        )

    # termine la location
    def terminer_location(self, kilometrage_retour):
        if not (self.vehicule.disponible == False):
            raise Exception("Le véhicule est déjà emprunté")
        else:
            self.vehicule.kilometrage += kilometrage_retour - self.vehicule.kilometrage
            self.vehicule.disponible = True

    def __str__(self):
        print(self.client + " a loué " + self.vehicule)


location = Location(
    "fefe",
    "ygfeyufe",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
    "fygèeyfue",
)
print(location)

from datetime import date

from GestionnaireTarifs import GestionnaireTarifs
from Agence import Agence
from Client import Client
from Voiture import Voiture
from Moto import Moto
from Camion import Camion
from exceptions import VehiculeIndisponible, LocationDejaTerminee


def main():
    tarifs1 = GestionnaireTarifs()
    tarifs2 = GestionnaireTarifs()
    print("Instance 1 :", id(tarifs1))
    print("Instance 2 :", id(tarifs2))
    print("Même instance ?", tarifs1 is tarifs2)

    tarifs1.modifier_tarif("Voiture", 60)
    tarifs1.appliquer_saison_haute(True)
    print("Tarif voiture (saison haute) :", tarifs1.get_tarif_base("Voiture"))

    agence = Agence("SuperLocation")

    v1 = Voiture(
        marque="Toyota",
        modele="Corolla",
        annee=2022,
        immatriculation="AB-123-CD",
        kilometrage=15000,
        disponible=True,
        nombre_places=5,
        type_carburant="Essence",
        coffre_litres=400,
    )

    v2 = Voiture(
        marque="Renault",
        modele="Clio",
        annee=2019,
        immatriculation="XY-987-ZT",
        kilometrage=40000,
        disponible=True,
        nombre_places=5,
        type_carburant="Diesel",
        coffre_litres=300,
    )

    v3 = Moto(
        marque="Yamaha",
        modele="MT-07",
        annee=2021,
        immatriculation="MOTO-123",
        kilometrage=12000,
        disponible=True,
        cylindree="689cc",
        type_moto="Roadster",
    )

    v4 = Camion(
        marque="Mercedes",
        modele="Actros",
        annee=2018,
        immatriculation="CAM-456",
        kilometrage=90000,
        disponible=True,
        charge_utile="10t",
        volume_benne="20m3",
        permis_requis="C",
    )

    v5 = Moto(
        marque="Honda",
        modele="CBR500",
        annee=2022,
        immatriculation="MOTO-789",
        kilometrage=8000,
        disponible=True,
        cylindree="500cc",
        type_moto="Sportive",
    )

    for veh in [v1, v2, v3, v4, v5]:
        agence.ajouter_vehicule(veh)

    print("Véhicules ajoutés :", [v.marque + " " + v.modele for v in agence.parc_vehicules])

    c1 = Client(nom="Cooper", email="alice@mail.com", prenom="Alice", numero_permis="12345", date_naissance="01/01/1990")
    c2 = Client(nom="Lennon", email="bob@mail.com", prenom="Bob", numero_permis="23456", date_naissance="02/02/1985")
    c3 = Client(nom="Chaplin", email="charlie@mail.com", prenom="Charlie", numero_permis="34567", date_naissance="03/03/1980")

    for c in [c1, c2, c3]:
        agence.enregistrer_client(c)

    print("Clients enregistrés :", [c.nom for c in agence.clients])

    loc1 = agence.louer_vehicule(c1, v1, date(2025, 2, 1))
    loc2 = agence.louer_vehicule(c2, v3, date(2025, 2, 3))
    loc3 = agence.louer_vehicule(c3, v4, date(2025, 2, 5))

    print("Locations en cours :", [str(loc) for loc in agence.locations_en_cours])

    agence.retourner_vehicule(loc1, kilometrage_retour=15500, date_fin=date(2025, 2, 5))
    agence.retourner_vehicule(loc2, kilometrage_retour=15000, date_fin=date(2025, 2, 7))

    print("Locations terminées :", [str(loc) for loc in agence.locations_terminees])

    ca = agence.calculer_chiffre_affaires()
    print("Chiffre d’affaires total :", ca)

    try:
        agence.louer_vehicule(c1, v4, date(2025, 2, 10))
    except VehiculeIndisponible as e:
        print("Exception capturée :", e)

    print("Tarif voiture via instance 2 :", tarifs2.get_tarif_base("Voiture"))
    print("Même valeur donc Singleton OK")


if __name__ == "__main__":
    main()

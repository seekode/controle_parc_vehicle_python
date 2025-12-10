from Assurable import Assurable
from Vehicule import Vehicule


class Voiture(Vehicule, Assurable):
    def __init__(
        self,
        marque,
        modele,
        annee,
        immatriculation,
        kilometrage,
        disponible,
        nombre_locations,
        nombre_places,
        type_carburant,
        coffre_litres,
    ):
        super().__init__(
            marque,
            modele,
            annee,
            immatriculation,
            kilometrage,
            disponible,
            nombre_locations,
        )
        self.nombre_places = nombre_places
        self.type_carburant = type_carburant
        self.coffre_litres = coffre_litres

    def calculer_prime_assurance(self):
        self.prime_assurance = 100
        return self.prime_assurance

    def calculer_tarif_journalier(self):
        return 10

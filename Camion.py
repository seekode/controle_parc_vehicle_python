from Assurable import Assurable
from Vehicule import Vehicule


class Camion(Vehicule, Assurable):
    def __init__(
        self,
        marque,
        modele,
        annee,
        immatriculation,
        kilometrage,
        disponible,
        nombre_locations,
        charge_utile,
        volume_benne,
        permis_requis,
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
        self.charge_utile = charge_utile
        self.volume_benne = volume_benne
        self.permis_requis = permis_requis

    def calculer_prime_assurance(self):
        self.prime_assurance = 200
        return self.prime_assurance

    def calculer_tarif_journalier(self):
        return 10

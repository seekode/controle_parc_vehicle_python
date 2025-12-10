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
        charge_utile,
        volume_benne,
        permis_requis,
    ):
        super().__init__(
            marque, modele, annee, immatriculation, kilometrage, disponible
        )
        self._charge_utile = charge_utile
        self._volume_benne = volume_benne
        self._permis_requis = permis_requis

    # Début Getters et Setters

    @property
    def charge_utile(self):
        return self._charge_utile

    @charge_utile.setter
    def charge_utile(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._charge_utile = value

    @property
    def volume_benne(self):
        return self._volume_benne

    @volume_benne.setter
    def volume_benne(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._volume_benne = value

    @property
    def permis_requis(self):
        return self._permis_requis

    @permis_requis.setter
    def permis_requis(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._permis_requis = value

    # Fin Getters et Setters

    def calculer_prime_assurance(self):
        print(0)

import Vehicule
import Assurable


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

    @property
    def charge_utile(self):
        return self._charge_utile

    @charge_utile.setter
    def charge_utile(self, value):
        if value is None:
            raise ValueError("ses vide")
        self._charge_utile = value

    @property
    def volume_benne(self):
        return self._volume_benne

    @volume_benne.setter
    def volume_benne(self, value):
        if value is None:
            raise ValueError("ses vide")
        self._volume_benne = value

    @property
    def permis_requis(self):
        return self._permis_requis

    @permis_requis.setter
    def permis_requis(self, value):
        if value is None:
            raise ValueError("ses vide")
        self._permis_requis = value

    def calculer_prime_assurance():
        return 0

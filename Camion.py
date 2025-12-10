from Vehicule import Vehicule
from Assurable import Assurable
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
        self.charge_utile = charge_utile
        self.volume_benne = volume_benne
        self.permis_requis = permis_requis

    @property
    def charge_utile(self):
        return self._charge_utile

    @charge_utile.setter
    def charge_utile(self, valeur):
        if not valeur or not isinstance(valeur, str):
            raise ValueError("La charge utile ne doit pas être vide.")
        self._charge_utile = valeur

    @property
    def volume_benne(self):
        return self._volume_benne

    @volume_benne.setter
    def volume_benne(self, valeur):
        if not valeur or not isinstance(valeur, str):
            raise ValueError("Le volume de la benne ne doit pas être vide.")
        self._volume_benne = valeur

    @property
    def permis_requis(self):
        return self._permis_requis

    @permis_requis.setter
    def permis_requis(self, valeur):
        if not valeur or not isinstance(valeur, str):
            raise ValueError("Le permis requis ne doit pas être vide.")
        self._permis_requis = valeur

    def calculer_prime_assurance(self):
        return 500  

    def calculer_tarif_journalier(self):
        return 50  
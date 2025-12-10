from Vehicule import Vehicule
from Assurable import Assurable

class Voiture(Vehicule, Assurable):
    def __init__(
        self,
        marque,
        modele,
        annee,
        immatriculation,
        kilometrage,
        disponible,
        nombre_places,
        type_carburant,
        coffre_litres,
    ):
        super().__init__(
             marque, modele, annee, immatriculation, kilometrage, disponible
        )
        self.nombre_places = nombre_places
        self.type_carburant = type_carburant
        self.coffre_litres = coffre_litres

    @property
    def nombre_places(self):
        return self._nombre_places

    @nombre_places.setter
    def nombre_places(self, valeur):
        if not valeur or not isinstance(valeur, int):
            raise ValueError("Le nombre de places ne doit pas être vide.")
        self._nombre_places = valeur

    @property
    def type_carburant(self):
        return self._type_carburant

    @type_carburant.setter
    def type_carburant(self, valeur):
        if not valeur or not isinstance(valeur, str):
            raise ValueError("Le type de carburant ne doit pa sêtre vide.")
        self._type_carburant = valeur

    @property
    def coffre_litres(self):
        return self._coffre_litres

    @coffre_litres.setter
    def coffre_litres(self, valeur):
        if not valeur or not isinstance(valeur, int):
            raise ValueError("Le nombre de litre disponible dans le coffre ne doit pas être vide.")
        self._coffre_litres = valeur

    def calculer_prime_assurance(self):
        return 500  

    def calculer_tarif_journalier(self):
        return 50  
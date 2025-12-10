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
        nombre_places,
        type_carburant,
        coffre_litres,
    ):
        super().__init__(
            marque, modele, annee, immatriculation, kilometrage, disponible
        )
        self._nombre_places = nombre_places
        self._type_carburant = type_carburant
        self._coffre_litres = coffre_litres

    # Début Getters et Setters

    @property
    def nombre_places(self):
        return self._nombre_places

    @nombre_places.setter
    def nombre_places(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._nombre_places = value

    @property
    def type_carburant(self):
        return self._type_carburant

    @type_carburant.setter
    def type_carburant(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._type_carburant = value

    @property
    def coffre_litres(self):
        return self._coffre_litres

    @coffre_litres.setter
    def coffre_litres(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._coffre_litres = value

    # Fin Getters et Setters

    def calculer_prime_assurance(self):
        print(0) 

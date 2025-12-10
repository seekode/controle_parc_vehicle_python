from Vehicule import Vehicule


class Moto(Vehicule):
    def __init__(
        self,
        marque,
        modele,
        annee,
        immatriculation,
        kilometrage,
        disponible,
        cylindree,
        type_moto,
    ):
        super().__init__(
            marque, modele, annee, immatriculation, kilometrage, disponible
        )
        self._cylindree = cylindree
        self._type_moto = type_moto

    # Début Getters et Setters

    @property
    def cylindree(self):
        return self._cylindree

    @cylindree.setter
    def cylindree(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._cylindree = value

    @property
    def type_moto(self):
        return self._type_moto

    @type_moto.setter
    def type_moto(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._type_moto = value

    # Fin Getters et Setters

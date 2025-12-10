import Vehicule


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
        self._cylindre = cylindree
        self._type_moto = type_moto

    @property
    def cylindree(self):
        return self._cylindre

    @cylindree.setter
    def cylindree(self, value):
        if value is None:
            raise ValueError("ses vide")
        self._cylindre = value

    @property
    def type_moto(self):
        return self._type_moto

    @type_moto.setter
    def type_moto(self, value):
        if value is None:
            raise ValueError("ses vide")
        self._type_moto = value

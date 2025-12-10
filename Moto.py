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
        self.cylindree = cylindree
        self.type_moto = type_moto

    @property
    def cylindree(self):
        return self._cylindree

    @cylindree.setter
    def cylindree(self, valeur):
        if not valeur or not isinstance(valeur, str):
            raise ValueError("Le cylindrée ne doit pas être vide.")
        self._cylindree = valeur
        
    @property
    def type_moto(self):
        return self._type_moto

    @type_moto.setter
    def type_moto(self, valeur):
        if not valeur or not isinstance(valeur, str):
            raise ValueError("Le type de moto ne doit pas être vide.")
        self._type_moto = valeur
        
    def calculer_tarif_journalier(self):
        return 50  
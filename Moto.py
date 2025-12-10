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
        nombre_locations,
        cylindree,
        type_moto,
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
        self.cylindree = cylindree
        self.type_moto = type_moto

    def calculer_tarif_journalier(self):
        return 10

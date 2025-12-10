from abc import ABC, abstractmethod


class Vehicule(ABC):
    def __init__(
        self,
        marque,
        modele,
        annee,
        immatriculation,
        kilometrage,
        disponible,
        nombre_locations,
    ):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__immatriculation = immatriculation
        self.__kilometrage = kilometrage
        self.__disponible = disponible
        self.nombre_locations = nombre_locations

    @abstractmethod
    def calculer_tarif_journalier():
        pass

    def afficher_infos():
        print("self")

    @property
    def marque(self):
        return self.__marque

    @marque.setter
    def marque(self, value):
        # if (type(value)) == "str":
        self.__marque = value

    # else:
    #     print("La marque doit être saisi sous forme de chaîne de caractère")
    #     exit()

    @property
    def modele(self):
        return self.__modele

    @modele.setter
    def modele(self, value):
        # if type(value) == "str":
        self.__modele = value

    # else:
    #     print("Le modèle doit être saisi sous forme de chaîne de caractère")
    #     exit()

    @property
    def annee(self):
        return self.__annee

    @annee.setter
    def annee(self, value):
        # if type(value) == "datetime.datetime":
        self.__annee = value

    # else:
    #     print("Le format doit être une date")
    #     exit()

    @property
    def immatriculation(self):
        return self.__immatriculation

    @immatriculation.setter
    def immatriculation(self, value):
        # vérification avec un regex pour vérifier la plaque
        self.__immatriculation = value

    @property
    def kilometrage(self):
        return self.__kilometrage

    @kilometrage.setter
    def kilometrage(self, value):
        self.__kilometrage = value

    @property
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, value):
        self.__disponible = value

    def __str__(self):
        print(
            self.marque
            + " "
            + self.modele
            + " "
            + self.immatriculation
            + " avec "
            + self.kilometrage
            + "km au compteur"
        )

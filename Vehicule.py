from abc import ABC, abstractmethod


class Article(ABC):
    def __init__(self, marque, modele, annee, immatriculation, kilometrage, disponible):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._immatriculation = immatriculation
        self._kilometrage = kilometrage
        self._disponible = disponible

    @abstractmethod
    def calculer_tarif_journalier(self):
        pass

    def afficher_infos(self):
        print(self._marque)
        print(self._modele)
        print(self._annee)
        print(self._immatriculation)
        print(self._kilometrage)
        print(self._disponible)

    def __str__(self):
        return (
            self._marque
            + " "
            + self._modele
            + " "
            + self._annee
            + " "
            + self._immatriculation
            + " "
            + self._kilometrage
            + " "
            + self._disponible
        )

    def __repr__(self):
        return "Utilisateur(prenom='{}',nom='{}'"

    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._marque = value

    @property
    def modele(self):
        return self._modele

    @modele.setter
    def modele(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._modele = value

    @property
    def annee(self):
        return self._annee

    @annee.setter
    def annee(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._annee = value

    @property
    def immatriculation(self):
        return self._immatriculation

    @immatriculation.setter
    def immatriculation(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._immatriculation = value

    @property
    def kilometrage(self):
        return self._kilometrage

    @kilometrage.setter
    def kilometrage(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._kilometrage = value

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")

        self._disp = value

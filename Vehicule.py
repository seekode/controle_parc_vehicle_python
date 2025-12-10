from abc import ABC, abstractmethod


class Vehicule(ABC):
    def __init__(self, marque, modele, annee, immatriculation, kilometrage, disponible):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.immatriculation = immatriculation
        self.kilometrage = kilometrage
        self.disponible = disponible

    @property
    def marque(self):
        return self._marque

    @marque.setter
    def marque(self, valeur):
        if not valeur or not isinstance(valeur, str):
            raise ValueError("La marque doit être une chaîne non vide.")
        self._marque = valeur

    @property
    def modele(self):
        return self._modele

    @modele.setter
    def modele(self, valeur):
        if not valeur or not isinstance(valeur, str):
            raise ValueError("Le modèle doit être une chaîne non vide.")
        self._modele = valeur

    @property
    def annee(self):
        return self._annee

    @annee.setter
    def annee(self, valeur):
        if (
            not isinstance(valeur, int) or valeur < 1886
        ):  # La première voiture a été créée en 1886
            raise ValueError("L'année doit être un entier supérieur ou égal à 1886.")
        self._annee = valeur

    @property
    def immatriculation(self):
        return self._immatriculation

    @immatriculation.setter
    def immatriculation(self, valeur):
        if not valeur or not isinstance(valeur, str):
            raise ValueError("L'immatriculation doit être une chaîne non vide.")
        self._immatriculation = valeur

    @property
    def kilometrage(self):
        return self._kilometrage

    @kilometrage.setter
    def kilometrage(self, valeur):
        if not isinstance(valeur, (int, float)) or valeur < 0:
            raise ValueError("Le kilométrage doit être un nombre positif.")
        self._kilometrage = valeur

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, valeur):
        if not isinstance(valeur, bool):
            raise ValueError("Disponible doit être un booléen.")
        self._disponible = valeur

    @abstractmethod
    def calculer_tarif_journalier(self):
        pass

    def afficher_infos(self):
        print(f"Marque: {self.marque}")
        print(f"Modèle: {self.modele}")
        print(f"Année: {self.annee}")
        print(f"Immatriculation: {self.immatriculation}")
        print(f"Kilométrage: {self.kilometrage} km")
        print(f"Disponible: {'Oui' if self.disponible else 'Non'}")

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee}) - Immat: {self.immatriculation}"

    def __repr__(self):
        return (
            f"Vehicule(marque={self.marque!r}, modele={self.modele!r}, "
            f"annee={self.annee!r}, immatriculation={self.immatriculation!r}, "
            f"kilometrage={self.kilometrage!r}, disponible={self.disponible!r})"
        )

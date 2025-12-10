from abc import ABC, abstractmethod

class Vehicule(ABC):
    # Initialisation
    def __init__(self, marque:str , modele:str, annee:int, immatriculation:str, kilometrage:int, disponible:bool):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.immatriculation = immatriculation
        self.kilometrage = kilometrage
        self.disponible = disponible

    # abstract method
    @abstractmethod
    def calculer_tarif_journalier(self) -> float:
        pass
    
    # Getters
    @property
    def get_marque(self) -> str:
        return self.marque
    
    @property
    def get_modele(self) -> str:
        return self.modele
    
    @property
    def get_annee(self) -> int:
        return self.annee
    
    @property
    def get_immatriculation(self) -> str:
        return self.immatriculation
    
    @property
    def get_kilometrage(self) -> int:
        return self.kilometrage
    
    @property
    def get_est_disponible(self) -> bool:
        return self.disponible
    

    # Setters
    def set_marque(self, marque:str):
        if not isinstance(marque, str) or len(marque.strip()) < 1:
            raise ValueError("La marque doit être une chaîne de caractères non vide.")
        self._marque = marque.strip()

    def set_modele(self, modele:str):
        if not isinstance(modele, str) or len(modele.strip()) < 1:
            raise ValueError("Le modèle doit être une chaîne de caractères non vide.")
        self.modele = modele

    def set_annee(self, annee:int):
        if not isinstance(annee, int):  
            raise ValueError("L'année doit être un entier valide supérieur.")
        self.annee = annee

    def set_immatriculation(self, immatriculation:str):
        if not isinstance(immatriculation, str) or len(immatriculation.strip()) < 1:
            raise ValueError("L'immatriculation doit être une chaîne de caractères non vide.")

    def set_kilometrage(self, kilometrage:int):
        if not isinstance(kilometrage, int) or kilometrage < 0:
            raise ValueError("Le kilométrage doit être un entier positif.")
        self.kilometrage = kilometrage

    def set_disponibilite(self, disponible:bool):
        if not isinstance(disponible, bool):
            raise ValueError("La disponibilité doit être un booléen.")
        self.disponible = disponible



    # Méthodes magiques
    def afficher_infos(self) -> str:
        return (f"Marque: {self.get_marque()}, Modèle: {self.get_modele()}, Année: {self.get_annee()}, "
                f"Immatriculation: {self.get_immatriculation()}, Kilométrage: {self.get_kilometrage()} km, "
                f"Disponible: {self.get_est_disponible()}")


    def __str__(self) -> str:
        return self.afficher_infos()
    
    def __repr__(self) -> str:
        return (f"Vehicle(marque={self.get_marque()}, modele={self.get_modele()}, annee={self.get_annee()}, "
                f"immatriculation={self.get_immatriculation()}, kilometrage={self.get_kilometrage()}, "
                f"disponible={self.get_est_disponible()})")
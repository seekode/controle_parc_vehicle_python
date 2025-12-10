from abc import *

# Class with information from `Voiture`, `Moto` and `Camion`
class Vehicule (ABC):
    def __init__(self, marque, modele, annee, immatriculation, kilometrage, disponible):
        self.marque=marque
        self.modele=modele
        self.annee=annee
        self.immatriculation=immatriculation
        self.kilometrage=kilometrage
        self.disponible=disponible
    
    def get_marque(self):
        return self.marque
    
    def set_marque(self, marque):
        if marque != "":
            self.marque=marque
        else:
            raise ValueError("Il doit y avoir un nom de marque")
        
    def get_modele(self):
        return self.modele
    
    def set_modele(self, modele):
        if modele != "":
            self.modele=modele
        else:
            raise ValueError("Il doit y avoir un modele")
    
    def get_annee(self):
        return self.annee
    
    def set_annee(self, annee):
        if annee <= 2025:
            self.annee=annee
        else:
            raise ValueError("Le véhicule n'existe pas")
    
    def get_immatriculation(self):
        return self.immatriculation
    
    def set_immatriculation(self, immatriculation):
        if immatriculation != "":
            self.immatriculation=immatriculation
        else:
            raise ValueError("Il n'y a pas d'immatriculation")
    
    def get_kilometrage(self):
        return self.kilometrage
    
    def set_kilometrage(self, kilometrage):
        if kilometrage >= 0 :
            self.kilometrage=kilometrage
        else:
            raise ValueError("Le kilometrage ne peut être négatif")

    def get_disponible(self):
        return self.disponible
    
    def set_disponible(self, disponible):
        if disponible== True or disponible==False:
            self.disponible=disponible
        else:
            raise ValueError("Disponible ou non?")

    @abstractmethod
    def calculer_tarif_journalier(self):
        return 10

    def afficher_infos(self):
        pass

    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()
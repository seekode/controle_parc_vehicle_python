import Vehicule
import Assurable

class Camion(Vehicule, Assurable):
    # Initialisation
    def __init__(self, marque:str , modele:str, annee:int, immatriculation:str, kilometrage:int, disponible:bool , charge_utile:int, volume_benne:int, permis_requis:str):
        super().__init__(marque , modele, annee, immatriculation, kilometrage, disponible)
        self.charge_utile = charge_utile
        self.volume_benne = volume_benne

    # Getters
    @property
    def get_charge_utile(self) -> int:
        return self.charge_utile
    
    @property
    def get_volume_benne(self) -> int:
        return self.volume_benne
    
    @property
    def get_permis_requis(self) -> str:
        return self.permis_requis
    
    # Setters
    def set_charge_utile(self, charge_utile:int):
        if not isinstance(charge_utile, int) or charge_utile <= 0:
            raise ValueError("La charge utile doit être un entier positif.")
        self.charge_utile = charge_utile

    def set_volume_benne(self, volume_benne:int):
        if not isinstance(volume_benne, int) or volume_benne <= 0:
            raise ValueError("Le volume de la benne doit être un entier positif.")  
        self.volume_benne = volume_benne

    def set_permis_requis(self, permis_requis:str):
        if not isinstance(permis_requis, str) or len(permis_requis.strip()) < 1:
            raise ValueError("Le permis requis doit être une chaîne de caractères non vide.")
        self.permis_requis = permis_requis

    # Méthode magique
    def __str__(self):
        return f"Camion: {self.marque} {self.modele}, Année: {self.annee}, Immatriculation: {self.immatriculation}, Kilométrage: {self.kilometrage} km, Disponible: {self.disponible}, Charge Utile: {self.charge_utile} kg, Volume Benne: {self.volume_benne} m³, Permis Requis: {self.permis_requis}"
    
        
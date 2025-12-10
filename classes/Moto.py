import Vehicule

class Moto(Vehicule):
    # Initialisation
    def __init__(self, marque:str , modele:str, annee:int, immatriculation:str, kilometrage:int, disponible:bool , type_moto:str, cylindree:int):
        super().__init__(marque , modele, annee, immatriculation, kilometrage, disponible)
        self.type_moto = type_moto
        self.cylindree = cylindree
    # Getters
    @property
    def get_type_moto(self) -> str:
        return self.type_moto
    
    @property
    def get_cylindree(self) -> int:
        return self.cylindree
    
    # Setters
    def set_type_moto(self, type_moto:str):
        if not isinstance(type_moto, str) or len(type_moto.strip()) < 1:
            raise ValueError("Le type de moto doit être une chaîne de caractères non vide.")

    def set_cylindree(self, cylindree:int):
        if not isinstance(cylindree, int) or cylindree <= 0:
            raise ValueError("La cylindrée doit être un entier positif.")
        
    # Méthode magique
    def __str__(self):
        return f"Moto: {self.marque} {self.modele}, Année: {self.annee}, Immatriculation: {self.immatriculation}, Kilométrage: {self.kilometrage} km, Disponible: {self.disponible}, Type: {self.type_moto}, Cylindrée: {self.cylindree} cc"
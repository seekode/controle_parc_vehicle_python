import Vehicule
import Assurable

class Voiture(Vehicule, Assurable):
    # Initialisation
    def __init__(self, marque:str , modele:str, annee:int, immatriculation:str, kilometrage:int, disponible:bool , nombre_places:int, type_carburant:str, coffre_litre:int):
        super().__init__(marque , modele, annee, immatriculation, kilometrage, disponible)
        self.nombre_places = nombre_places
        self.type_carburant = type_carburant
        self.coffre_litre = coffre_litre

    # Getters
    @property
    def get_nombre_places(self) -> int:
        return self.nombre_places
    
    @property
    def get_type_carburant(self) -> str:
        return self.type_carburant
    
    @property
    def get_coffre_litre(self) -> int:
        return self.coffre_litre
    

    # Setters
    def set_nombre_places(self, nombre_places:int):
        if not isinstance(nombre_places, int) or nombre_places <= 0:
            raise ValueError("Le nombre de places doit être un entier positif.")
        self.nombre_places = nombre_places

    def set_type_carburant(self, type_carburant:str):
        if not isinstance(type_carburant, str) or len(type_carburant.strip()) < 1:
            raise ValueError("Le type de carburant doit être une chaîne de caractères non vide.")
        self.type_carburant = type_carburant

    def set_coffre_litre(self, coffre_litre:int):
        if not isinstance(coffre_litre, int) or coffre_litre < 0:
            raise ValueError("La capacité du coffre doit être un entier positif.")
        self.coffre_litre = coffre_litre


    # Méthode magique
    def __str__(self):
        return f"Voiture: {self.marque} {self.modele}, Année: {self.annee}, Immatriculation: {self.immatriculation}, Kilométrage: {self.kilometrage} km, Disponible: {self.disponible}, Places: {self.nombre_places}, Carburant: {self.type_carburant}, Coffre: {self.coffre_litre} L"  
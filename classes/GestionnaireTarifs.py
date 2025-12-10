class GestionnaireTarifs:
    # Attributs de classe
    _instance = None
    
    def __init__(self):   
        # Initialisation 
        self._tarifs_base = {"Voiture": 50.0, "Moto": 30.0, "Camion": 100.0}
        self._tarif_assurance = {"Voiture": 10.0, "Camion": 25.0}
        self._coefficient_saison_haute = 1.5

    # Méthodes
    def get_tarif_base(self, type_vehicule: str) -> float:
        tarif = self._tarifs_base.get(type_vehicule, 0.0)
        if self._saison_haute_active:
            return tarif * self._coefficient_saison_haute
        return tarif
    
    def get_tarif_assurance(self, type_vehicule: str) -> float:
        return self._tarif_assurance.get(type_vehicule, 0.0)

    def appliquer_saison_haute(self, activer: bool):
        self._saison_haute_active = activer
        
    def modifier_tarif(self, type_vehicule: str, nouveau_tarif: float):
        if type_vehicule in self._tarifs_base and nouveau_tarif > 0:
            self._tarifs_base[type_vehicule] = nouveau_tarif
        else:
            raise ValueError("Type de véhicule inconnu ou tarif invalide.")
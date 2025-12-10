class GestionnaireTarifs:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GestionnaireTarifs, cls).__new__(cls)
            cls._instance.tarifs_base = {"Voiture": 50, "Moto": 30, "Camion": 100}
            cls._instance.coefficient_saison_haute = 1.5
            cls._instance.tarif_assurance = {"Voiture": 10, "Camion": 25}
            cls._instance.saison_haute_active = False
        return cls._instance

    def get_tarif_base(self, type_vehicule):
        tarif = self.tarifs_base.get(type_vehicule)
        if tarif is None:
            raise ValueError(f"Type de véhicule inconnu : {type_vehicule}")
        if self.saison_haute_active:
            return tarif * self.coefficient_saison_haute
        return tarif

    def get_tarif_assurance(self, type_vehicule):
        tarif = self.tarif_assurance.get(
            type_vehicule, 0
        ) 
        return tarif

    def appliquer_saison_haute(self, activer: bool):
        self.saison_haute_active = activer

    def modifier_tarif(self, type_vehicule, nouveau_tarif):
        if type_vehicule not in self.tarifs_base:
            raise ValueError(
                f"Impossible de modifier un tarif inexistant pour {type_vehicule}"
            )
        self.tarifs_base[type_vehicule] = nouveau_tarif

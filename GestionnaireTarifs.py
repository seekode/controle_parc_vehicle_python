class GestionnaireTarifs():
    def __new__(self, tarifs_base, coefficient_saison_haute, tarif_assurance):
        self.tarifs_base=tarifs_base
        self.coefficient_saison_haute=coefficient_saison_haute
        self.tarif_assurance=tarif_assurance

    tarifs_base={"Voiture": 50, "Moto": 30, "Camion": 100}
    coefficient_saison_haute=1.5
    tarif_assurance={"Voiture": 10, "Camion": 25}

    def get_tarif_base(self, type_vehicule):
        return self.tarifs_base[type_vehicule]
    
    def get_tarif_assurance(self, type_vehicule):
        return self.tarif_assurance[type_vehicule]
    
    def appliquer_saison_haute(self, activer):
        if activer==True:
            return self.tarifs_base * self.coefficient_saison_haute
        else:
            return self.tarifs_base
        
    def modifier_tarif(self, type_vehicule, nouveau_tarif):
        self.tarifs_base[type_vehicule]=nouveau_tarif
        return self.tarifs_base[type_vehicule]
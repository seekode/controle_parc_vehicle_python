# gère l'ensemble des tarifs
class GestionnaireTarifs(object):
    def __new__(cls, tarif_base, coefficient_saison_haute, tarif_assurance):
        if not hasattr(cls, "instance"):
            cls.tarif_base = tarif_base
            cls.coefficient_saison_haute = coefficient_saison_haute
            cls.tarif_assurance = tarif_assurance
            cls.instance = super(GestionnaireTarifs, cls).__new__(cls)
        return cls.instance

    # permet d'obtenir le prix pour chaque véhicule
    def get_tarif_base(self, type_vehicule):
        if type_vehicule == "Voiture":
            return self.tarif_base[type_vehicule]
        elif type_vehicule == "Moto":
            return self.tarif_base[type_vehicule]
        elif type_vehicule == "Camion":
            return self.tarif_base[type_vehicule]

    # permet d'obtenir le prix de l'assurance pour chaque véhicule
    def get_tarif_assurrance(self, type_vehicule):
        if type_vehicule == "Voiture":
            return self.tarif_assurance[type_vehicule]
        elif type_vehicule == "Camion":
            return self.tarif_assurance[type_vehicule]

    # gère le coefficient du tarif
    def appliquer_saison_haute(self, activer, multiplicateur):
        if activer == True:
            self.coefficient_saison_haute = multiplicateur
        else:
            self.coefficient_saison_haute = 1

    # modifie un tarif
    def modifier_tarif(self, type_vehicule, nouveau_tarif):
        self.tarif_base[type_vehicule] = nouveau_tarif


# singleton = GestionnaireTarifs(10, 1.5, 10)
# new_singleton = GestionnaireTarifs(10, 1.5, 10)

# print(singleton is new_singleton)

# singleton.singl_variable = "Singleton Variable"
# print(new_singleton.singl_variable)

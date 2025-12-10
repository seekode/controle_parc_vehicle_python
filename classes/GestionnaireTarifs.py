def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class GestionnaireTarifs:
    def __init__(self, tarif_base, tarif_assurance):
        self._tarif_base = tarif_base
        self._tarif_assurance = tarif_assurance


# Début Getters et Setters


@property
def tarif_base(self):
    return self._tarif_base


@tarif_base.setter
def tarif_base(self, value):
    if value is None:
        raise ValueError("Value is empty")
    self._tarif_base = value


@property
def tarif_assurance(self):
    return self._tarif_assurance


@tarif_assurance.setter
def tarif_assurance(self, value):
    if value is None:
        raise ValueError("Value is empty")
    self._tarif_assurance = value


# Fin Getters et Setters


def get_tarif_base(self, type_vehicule):
    pass


def get_tarif_assurance(self, type_vehicule):
    pass


def appliquer_saison_haute(self, activer):
    pass


def modifier_tarif(type_vehicule, nouveau_tarif):
    pass

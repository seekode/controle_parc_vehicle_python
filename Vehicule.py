from abc import ABC, abstractmethod


class Vehicule(ABC):
    # construtor
    def __init__(self, brand, model, year, immat, mileage, available):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__immat = immat
        self.__mileage = mileage
        self.__available = available

    # getter and setter
    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str):
            self.__brand = value
        else:
            "La dmarque n'est pas valide"

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if isinstance(value, str):
            self.__model = value
        else:
            "Le modèle n'est pas valide"

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if isinstance(value, int):
            self.__year = value
        else:
            "L'année de mise en circulation n'est pas valide"

    @property
    def immat(self):
        return self.__immat

    @immat.setter
    def immat(self, value):
        if isinstance(value, int):
            self.__immat = value
        else:
            "L'immatriculation n'est pas valide"

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, value):
        if isinstance(value, int):
            self.__mileage = value
        else:
            "Le kilométrage n'est pas valide"

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, value):
        if value == True or value == False:
            self.__available = value

    # display vehicule's information
    def display_infos(self):
        print(self.brand)
        print(self.model)

    def __str__(self):
        return "Mon véhicule est " + self.model + " de la marque " + self.brand

    def __repr__(self):
        return "Vehicule(marque='{}', modele='{}')".format(self.brand, self.model)

    @abstractmethod
    def calculate_daily_rate(self):
        pass




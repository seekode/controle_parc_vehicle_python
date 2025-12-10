from Vehicule import Vehicule


class Car(Vehicule):
    # constructor
    def __init__(
        self,
        brand,
        model,
        year,
        immat,
        mileage,
        available,
        place_number,
        fuel_type,
        liter_trunk,
    ):
        super().__init__(brand, model, year, immat, mileage, available)
        self.__place_number = place_number
        self.__fuel_type = fuel_type
        self.__liter_trunk = liter_trunk

    # getter and setter
    @property
    def place_number(self):
        return self.__place_number

    @place_number.setter
    def place_number(self, value):
        if isinstance(value, int):
            self.__place_number = value
        else:
            "Le nombre de place n'est pas valide"

    @property
    def fuel_type(self):
        return self.__fuel_type

    @fuel_type.setter
    def fuel_type(self, value):
        if isinstance(value, str):
            self.__fuel_type = value
        else:
            "Le type de fuel n'est pas valide"

    @property
    def liter_trunk(self):
        return self.__liter_trunk

    @liter_trunk.setter
    def liter_trunk(self, value):
        if isinstance(value, int):
            self.__liter_trunk = value
        else:
            "La date de naissance n'est pas valide"

    def calculate_daily_rate(self):
        return "prix voiture "

    def calculate_insurance_prenium(self):
        return "prix de l'assurance"


test = Car("Renaud", "Capture", 1255, 12, 21, False, 2, "essence", 12)
print(test.place_number)
print(test.calculate_daily_rate())
print(test.calculate_insurance_prenium())

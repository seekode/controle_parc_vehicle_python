from Insurable import Insurable
from Vehicule import Vehicule


class Truck(Vehicule, Insurable):
    # constructor
    def __init__(
        self,
        brand,
        model,
        year,
        immat,
        mileage,
        available,
        payload,
        trash_volume,
        permit_required,
    ):
        super().__init__(brand, model, year, immat, mileage, available)
        self.__payload = payload
        self.__trash_volume = trash_volume
        self.__permit_required = permit_required

    # getter and setter
    @property
    def permit_required(self):
        return self.__permit_required

    @permit_required.setter
    def permit_required(self, value):
        if isinstance(value, str):
            self.__permit_required = value
        else:
            "Le permis n'est pas valide"

    @property
    def payload(self):
        return self.__payload

    @payload.setter
    def payload(self, value):
        if isinstance(value, int):
            self.__payload = value
        else:
            "La charge utile n'est pas valide"

    @property
    def trash_volume(self):
        return self.__trash_volume

    @trash_volume.setter
    def trash_volume(self, value):
        if isinstance(value, int):
            self.__trash_volume = value
        else:
            "Le volume de la benne n'est pas valide"

    def calculate_daily_rate(self):
        return "prix camion "

    def calculate_insurance_prenium(self):
        return "prix de l'assurance"


test = Truck("Renaud", "Capture", 1255, 12, 21, False, 2, 4, "C")
print(test.permit_required)
print(test.calculate_daily_rate())
print(test.calculate_insurance_prenium())

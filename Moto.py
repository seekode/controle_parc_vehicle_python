from Vehicule import Vehicule


class Moto(Vehicule):
    # constructor
    def __init__(
        self,
        brand,
        model,
        year,
        immat,
        mileage,
        available,
        cylindree,
        moto_type,
    ):
        super().__init__(brand, model, year, immat, mileage, available)
        self.__cylindree = cylindree
        self.__moto_type = moto_type

    # getter and setter
    @property
    def cylindree(self):
        return self.__cylindree

    @cylindree.setter
    def cylindree(self, value):
        self.__cylindree = value

    @property
    def moto_type(self):
        return self.__moto_type

    @moto_type.setter
    def moto_type(self, value):
        self.__moto_type = value

    def calculate_daily_rate(self):
        print("prix moto")


test = Moto("Renaud", "Capture", 1255, 12, 21, False, 2, 14, "sportive")
print(test.cylindree)
print(test.calculate_daily_rate())

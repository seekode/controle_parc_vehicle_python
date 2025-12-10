class RateManager:
    def __init__(self):
        self.__low_price = {"Voiture": 50, "Moto": 30, "Camion": 100}
        self.__high_season_coef = 1.5
        self.__insurance_price = {"Voiture": 10, "Camion": 25}

    @property
    def low_price(self):
        return self.__low_price

    @property
    def insurance(self):
        return self.__insurance_price

    def get_low_price(self, vehicule_type):
        for i in self.low_price.values():
            for j in self.low_price.keys():
                if vehicule_type == j:
                    return i

    def get_insurance_price(self, vehicule_type):
        for i in self.insurance.values():
            for j in self.insurance.keys():
                if vehicule_type == j:
                    return i


test = RateManager()
print(test.get_low_price("Moto"))
print(test.get_insurance_price("Voiture"))

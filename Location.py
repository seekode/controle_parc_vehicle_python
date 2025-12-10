import Client
import Vehicule


class Location(Client, Vehicule):
    def __init__(self, start_date, end_date, start_mileage, end_mileage):
        self.client = Client()
        self.vehicule = Vehicule()
        self.__start_date = start_date
        self.__end_date = end_date
        self.__start_mileage = start_mileage
        self.__end_mileage = end_mileage
        self.__total_price = self.calculate_price()

    # getter and setter
    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, value):
        if isinstance(value, int):
            self.__start_date = value
        else:
            "La date de début n'est pas valide"

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, value):
        if isinstance(value, int):
            self.__end_date = value
        else:
            "Le date de fin n'est pas valide"

    @property
    def start_mileage(self):
        return self.__start_mileage

    @start_mileage.setter
    def start_mileage(self, value):
        if isinstance(value, int):
            self.__start_mileage = value
        else:
            "Le kilométrage de début n'est pas valide"

    @property
    def end_mileage(self):
        return self.__end_mileage

    @end_mileage.setter
    def end_mileage(self, value):
        if isinstance(value, int):
            self.__end_mileage = value
        else:
            "Le kilométrage de fin n'est pas valide"

    @property
    def total_price(self):
        return self.__total_price

    @total_price.setter
    def total_price(self, value):
        if isinstance(value, int):
            self.__total_price = value
        else:
            "Le prix total n'est pas valide"

    def calculate_duration(self):
        duration = self.end_date - self.start_date
        return duration

    def calculate_mileage(self):
        current_mileage = self.end_mileage
        return current_mileage

    def calculate_price(self):
        total_price = 10 * self.calculate_duration + 20
        return total_price

    def __str__(self):
        return self.total_price


test = Location(10,20,10,20)

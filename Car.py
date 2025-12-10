from Vehicle import Vehicle
from Insurance import Insurance


class Car(Vehicle, Insurance):
    def __init__(
        self,
        brand,
        model,
        year,
        registration,
        mileage,
        available,
        number_places,
        gas_type,
        trunk_litres,
    ):
        self._number_places = number_places
        self._gas_type = gas_type
        self._trunk_litres = trunk_litres
        super().__init__(brand, model, year, registration, mileage, available)

    def insurance_prime_amount(self):
        pass

    @property
    def number_places(self):
        return self._number_places

    @number_places.setter
    def number_places(self, value):
        if value != None:
            self._number_places = value

    @property
    def gas_type(self):
        return self._gas_type

    @gas_type.setter
    def gas_type(self, value):
        if value != None:
            self._gas_type = value

    @property
    def trunk_litres(self):
        return self._trunk_litres

    @trunk_litres.setter
    def trunk_litres(self, value):
        if value != None:
            self._trunk_litres = value


Vehicle.register(Car)

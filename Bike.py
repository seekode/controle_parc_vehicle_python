from Vehicle import Vehicle


class Bike(Vehicle):
    def __init__(
        self, brand, model, year, registration, mileage, available, cylinder, bike_type
    ):
        self._cylinder = cylinder
        self._bike_type = bike_type
        super().__init__(brand, model, year, registration, mileage, available)

    @property
    def cylinder(self):
        return self._cylinder

    @cylinder.setter
    def cylinder(self, value):
        if value != None:
            self._cylinder = value

    @property
    def bike_type(self):
        return self._bike_type

    @bike_type.setter
    def bike_type(self, value):
        if value != None:
            self._bike_type = value


Vehicle.register(Bike)

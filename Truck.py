from Vehicle import Vehicle


class Truck(Vehicle):
    def __init__(
        self,
        brand,
        model,
        year,
        registration,
        mileage,
        available,
        used_weight,
        volume,
        licence,
    ):
        self._used_weight = used_weight
        self._volume = volume
        self._licence = licence
        super().__init__(brand, model, year, registration, mileage, available)

    def insurance_prime_amount(self):
        pass





    @property
    def used_weight(self):
        return self._used_weight

    @used_weight.setter
    def used_weight(self, value):
        if value != None:
            self._used_weight = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        if value != None:
            self._volume = value

    @property
    def licence(self):
        return self._licence

    @licence.setter
    def licence(self, value):
        if value != None:
            self._licence = value

Vehicle.register(Truck)
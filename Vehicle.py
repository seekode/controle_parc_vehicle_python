from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, model, year, registration, mileage, available):
        self._brand = brand
        self._model = model
        self._year = year
        self._registration = registration
        self._mileage = mileage
        self._available = available
        pass

    @abstractmethod
    def daily_tarif(self):
        return self

    def display_infos(self):
        print(
            self._brand,
            self._model,
            self._year,
            self._registration,
            self._mileage,
            self._available,
        )
        pass

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return super().__repr__()

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if value != None:
            self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if value != None:
            self._model = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value != None:
            self._year = value

    @property
    def registration(self):
        return self._registration

    @registration.setter
    def registration(self, value):
        if value != None:
            self._registration = value

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value != None:
            self._mileage = value

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        if value != None:
            self.available = value

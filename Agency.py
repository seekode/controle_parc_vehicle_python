from Rental import Rental
from Vehicle import Vehicle
from Client import Client


class Agency:

    def __init__(self, name, vehicle_park, rental_in_use, rental_ended, clients):
        self._name = name
        self._vehicle_park = vehicle_park
        self._rental_in_use = rental_in_use
        self._rental_ended = rental_ended
        self._clients = clients
        pass

    def add_vehicle(self, vehicle: Vehicle):
        self._vehicle_park.append(vehicle)

    def register_client(self, client: Client):
        self._clients.append(client)

    def rent_vehicle(self, client: Client, vehicle: Vehicle, start_date):
        if vehicle.available == False:
            raise ("Erreur, le vehicule est en location")
        return self._rental_in_use.append[
            Rental(client, vehicle, start_date, None, 2500, None, None)
        ]

    def return_vehicle(self, rental: Rental, mileage_end, end_date):
        rental._mileage_end = mileage_end
        rental._end_date = end_date
        self._rental_ended.append[rental]

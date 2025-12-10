from Client import Client
from Vehicle import Vehicle
from Car import Car

class Rental:
    def __init__(
        self,
        client,
        vehicle,
        start_date,
        end_date,
        mileage_start,
        mileage_end,
        total_cost,
    ):
        if client == None:
            self._client = Client("Planet","Corentin","54852017","24-10-2006","corentin@gmail.com")
        self._client = client
        if vehicle == None:
            self._vehicle = Car("Renault","308","2010","DN-903-NR",2500,False,4,"Diesel",2000)
        self._vehicle = vehicle
        self._start_date = start_date
        self._end_date = end_date
        self._mileage_start = mileage_start
        if self._end_date == None:
            self._mileage_end = None
        else:
            self._mileage_end = mileage_end
        self._total_cost = total_cost
        pass

    def length_calc(self):
        pass

    def cost_calc(self):
        pass

    def end_rental(self,date, mileage_end):
        if self._end_date != None:
            self._end_date = date
            self._vehicle.mileage = mileage_end
            self._vehicle.available = True
        else:
            raise("Location deja termine")
        pass

    def __str__(self):
        pass

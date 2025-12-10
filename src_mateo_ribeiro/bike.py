from vehicule import vehicule


class bike(vehicule):
	def __init__(self, brand, model, year, plate, km_done, available,power,bike_type):
		super().__init__(brand, model, year, plate, km_done, available)
		self._power = power
		self._bike_type = bike_type

	def calculate_daily_price(self):
		return None
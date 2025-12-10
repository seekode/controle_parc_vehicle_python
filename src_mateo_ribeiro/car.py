from vehicule import vehicule
from warenty import warenty


class car(vehicule,warenty):
	def __init__(self, brand, model, year, plate, km_done, available,seat_nb,gas_type,trunk_volume):
		super().__init__(brand, model, year, plate, km_done, available)
		self._seat_nb = seat_nb
		self._gas_type = gas_type
		self._trunk_volume = trunk_volume

	def calculate_daily_price(self):
		return None
	
	def calculate_warenty_price(self):
		return None
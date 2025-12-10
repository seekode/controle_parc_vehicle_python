from vehicule import vehicule
from warenty import warenty


class truck(vehicule,warenty):
	def __init__(self, brand, model, year, plate, km_done, available,capacity,volume,license_requiered):
		super().__init__(brand, model, year, plate, km_done, available)
		self._capacity = capacity
		self._volume = volume
		self._licen_required = license_requiered

	def calculate_daily_price(self):
		return None
	
	def calculate_warenty_price(self):
		return None
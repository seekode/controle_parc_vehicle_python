from vehicule import vehicule
from client import client

class rent:
	def __init__(self,client,vehicule,date_start,date_end,km_done_start,km_done_end,total_cost):
		self._client = client
		self._vehicule = vehicule
		self._date_start = date_start
		self._date_end = date_end
		self._km_done_start = km_done_start
		self._km_done_end = km_done_end
		self._total_cost = total_cost

	def __str__(self):
		pass
	
	def calculate_duration(self):
		return None
	
	def calculate_cost(self):
		return None
	
	def end_rent(self,km_done_end,date_end):
		if self._date_end !=None:
			print("can't end rent twice")
		else:
			self._date_end = date_end
			self._km_done_end = km_done_end
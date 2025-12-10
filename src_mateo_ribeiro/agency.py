from vehicule import vehicule
from client import client
from rent import rent
from bike import bike
from car import car
from truck import truck
from price_manager import price_manager

class agency:
	def __init__(self,name,vehicule_park,ongoing_rent,rent_ended,clients):
		self._name = name
		self._vehicule_park = vehicule_park
		self._ongoing_rent = ongoing_rent
		self._rent_ended = rent_ended
		self._clients = clients
	
	def add_vehicule(self,vehicule):
		self._vehicule_park.append(vehicule)
	
	def register_client(self,client):
		self._clients.append(client)

	def rent_vehicule(self,client,vehicule,date_start):
		if vehicule._available:
			if type(vehicule)==bike:
				self._ongoing_rent.append(rent(client,vehicule,date_start,None,vehicule._km_done,None,price_manager._instance["base_price"]["bike"]))	
			elif type(vehicule)==car:
				self._ongoing_rent.append(rent(client,vehicule,date_start,None,vehicule._km_done,None,price_manager._instance["base_price"]["car"]))
			elif type(vehicule)==truck:
				self._ongoing_rent.append(rent(client,vehicule,date_start,None,vehicule._km_done,None,price_manager._instance["base_price"]["truck"]))
			else:
				print("unknown vehicule type")
		else:
			print("vehicule unavailable")

	def return_vehicule(self,rent,km_done_end,date_end):
		if rent in self._ongoing_rent:
			rent.end_rent(km_done_end,date_end)
			self._rent_ended.append(self._ongoing_rent.pop(self._ongoing_rent.index(rent)))
		else:
			print("rent not found")

	def display_available_vehicule(self):
		for i in self._vehicule_park:
			if i.available:
				print(i)

	def calculate_benefits(self):
		print("3")

	def most_rented_vehicule(self):
		print("info unavailable")
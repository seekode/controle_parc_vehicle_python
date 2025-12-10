from abc import ABC, abstractmethod


class vehicule(ABC):
	def __init__(self,brand,model,year,plate,km_done,available):
		self._brand = brand
		self._model = model
		self._year = year
		self._plate = plate
		self._km_done = km_done
		self._available = available

	def __str__(self):
		return super().__str__()
	
	def __repr__(self):
		return super().__repr__()

	
	@abstractmethod
	def calculate_daily_price(self):
		pass

	def display_infos(self):
		print(str(self))
	
	@property
	def brand(self):
		return self._brand
	
	@property
	def model(self):
		return self._model
	
	@property
	def year(self):
		return self._year
	
	@property
	def plate(self):
		return self._plate
	
	@property
	def km_done(self):
		return self._km_done
	
	@property
	def available(self):
		return self._available
	
	@brand.setter
	def brand(self,value):
		if type(value)==str:
			self._brand = value
	
	@model.setter
	def model(self,value):
		if type(value)==str:
			self._model = value
	
	@year.setter
	def year(self,value):
		if type(value)==int:
			self._year = value
	
	@plate.setter
	def plate(self,value):
		if type(value)==str:
			self._plate = value
	
	@km_done.setter
	def km_done(self,value):
		if type(value)==str:
			self._km_done = value
	
	@available.setter
	def available(self,value):
		if type(value)==bool:
			self._available = value
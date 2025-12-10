from abc import ABC, abstractmethod


class warenty(ABC):
	@abstractmethod
	def calculate_warenty_price(self):
		pass
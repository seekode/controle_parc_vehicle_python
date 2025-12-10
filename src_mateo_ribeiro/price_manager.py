class price_manager:

	_instance = {}
	_is_high_season = False

	def __init__(self):
		if price_manager._instance == {}:
			price_manager._instance["base_price"] = {"car": 50, "bike": 30, "truck": 100}
			price_manager._instance["high_season_coefficient"] = 1.5
			price_manager._instance["warenty_price"] = {"car": 10, "truck": 25}
	
	def get_base_price(self,vehicule_type):
		if vehicule_type in price_manager._instance["base_price"]:
			return price_manager._instance["base_price"][vehicule_type]
		print("unknown vehicule type")
		return None
	
	def get_warenty_price(self,vehicule_type):
		if vehicule_type in price_manager._instance["warenty_price"]:
			return price_manager._instance["warenty_price"][vehicule_type]
		print("unknown vehicule type")
		return None
	
	def apply_high_season(self,activate):
		if type(activate)==bool:
			price_manager._is_high_season = activate
		else:
			print("invalid value")

	def update_price(self,vehicule_type,new_price):
		if vehicule_type in price_manager._instance["base_price"]:
			if type(new_price)==int:
				price_manager._instance["base_price"][vehicule_type] = new_price
			else:
				print("invalid value")
		else:
			print("unknown vehicule type")
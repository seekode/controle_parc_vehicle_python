class CostsManager:
    
    def __init__(self, high_season_coeff,insurance_tarifs):
        self._base_tarifs = None
        self._high_season_coeff = high_season_coeff
        self._insurance_tarifs = insurance_tarifs
        pass
    
    def __new__(cls, vehicle, costs):
        if cls._base_tarifs is None:
            cls._base_tarifs = super().__new__(cls, vehicle, costs)
        return cls._base_tarifs

   

    def get_base_tarifs(self,vehicle_type):
        return self._base_tarifs(vehicle_type)
    
    def get_insurance_tarifs(self,vehicle_type):
        return self._insurance_tarifs(vehicle_type)
    
    def apply_high_season(self,apply):
        if apply == True:
            return self._high_season_coeff
        
    def modify_tarifs(self,vehicle_type,new_tarif):
        self._base_tarifs[vehicle_type] = new_tarif
        return self._base_tarifs 
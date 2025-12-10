class ManagerPrices:

    def __init__(self, coefficient_season_high, ):
        self._basic_rates = {"Voiture": 50, "Moto": 30, "Camion": 100}
        self._coefficient_season_high = coefficient_season_high
        self._insurance_price ={"Voiture": 10, "Camion": 25}

    @property
    def basic_rates(self):
        return self._basic_rates
    
    @basic_rates.setter
    def basic_rates (self, value):
        self._basic_rates = value
    
    @property
    def coefficient_season_high(self):
        return self._coefficient_season_high
    
    @coefficient_season_high.setter
    def coefficient_season_high(self, value):
        self._coefficient_season_high = value
    
    @property
    def insurance_price(self):
        return self._insurance_price
    
    @insurance_price.setter
    def insurance_price(self, value):
        self._insurance_price =  value
    
    def get_tarif_base(self,type_vehicule):
        
        print(self.basic_rates[type_vehicule])

    def get_tarif_assurance(self,type_vehicule):

        print(self.insurance_price[type_vehicule])

    def appliquer_saison_haute(self,activer):
        if activer == True :
            self.coefficient_season_high = 1.5
        else:
            self.coefficient_season_high = 1
        return self.coefficient_season_high
    
    def modifier_tarif(self, type_vehicule, nouveau_tarif):
        self.basic_rates[type_vehicule] = nouveau_tarif
        return self.basic_rates
    
    

test = ManagerPrices(True)
print(test.get_tarif_base('Voiture'))
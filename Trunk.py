from Insurable import Insurable
from Vehicule import Vehicule


class Trunk(Vehicule, Insurable):

    def __init__(self, brand, modele, year, registration, kilometer, available, payload, volume_in, permit_required):
        super().__init__(brand, modele, year, registration, kilometer, available)
        self._payload = payload
        self._volume_in = volume_in
        self._permit_required = permit_required
     
    # Creation of setter and getter
    @property
    def payload(self):
        return self._payload
    
    @payload.setter
    def payload(self, value):
        self._payload = value

    @property
    def volume_in(self):
        return self._volume_in
    
    @volume_in.setter
    def volume_in(self, value):
        self._volume_in = value
    
    @property
    def permit_required(self):
        return self._permit_required
    
    @permit_required.setter
    def permit_required(self, value):
        self._permit_required = value

    def calculate_daily_rate(self):
        return None
    def calculate_insurance_premium(self):
        return None
    
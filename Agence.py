class Agence:
    def __init__(
        self,
        nom,
        parc_vehicules,
        location_en_cours,
        location_terminees,
        clients,
    ):
        self._nom = nom
        self._parc_vehicules = parc_vehicules
        self._location_en_cours = location_en_cours
        self._location_terminees = location_terminees
        self._clients = clients

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        if value is None:
            raise ValueError("ses vide")
        self._nom = value

    @property
    def parc_vehiules(self):
        return self._parc_vehicules

    @parc_vehiules.setter
    def parc_vehicules(self, value):
        if value is None:
            raise ValueError("ses vide")
        self._parc_vehicules = value

    @property
    def location_en_cours(self):
        return self._location_en_cours

    @location_en_cours.setter
    def location_en_cours(self, value):
        if value is None:
            raise ValueError("ses vide")
        self._location_en_cours = value

    @property
    def location_terminees(self):
        return self._location_terminees

    @location_terminees.setter
    def location_terminees(self, value):
        if value is None:
            raise ValueError("ses vide")
        self._location_terminees = value

    @property
    def clients(self):
        return self._clients

    @clients.setter
    def location_terminees(self, value):
        if value is None:
            raise ValueError("ses vide")
        self._clients = value

    def ajouter_vehicule(self, vehicule):
        self.parc_vehicules.append(vehicule)
    def enregistrer_client(self,client):
        self.clients.append(client)
    def retourner_vehicule(location, kilometrage_retour, date_fin) :
        pass

    def afficher_vehicules_disponibles(self):
        print(self.parc_vehicules)
        pass
    def calculer_chiffre_affaires():
        pass
    def vehicule_le_plus_loue():
        pass


    

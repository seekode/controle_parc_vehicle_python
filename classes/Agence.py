class Agence:
    def __init__(
        self, nom, parc_vehicules, locations_en_cours, locations_terminees, clients
    ):
        self._nom = nom
        self._parc_vehicules = parc_vehicules
        self._locations_en_cours = locations_en_cours
        self._locations_terminees = locations_terminees
        self._clients = clients

    # Début Getters et Setters

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._nom = value

    @property
    def parc_vehicules(self):
        return self._parc_vehicules

    @parc_vehicules.setter
    def parc_vehicules(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._parc_vehicules = value

    @property
    def locations_en_cours(self):
        return self._locations_en_cours

    @locations_en_cours.setter
    def locations_en_cours(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._locations_en_cours = value

    @property
    def locations_terminees(self):
        return self._locations_terminees

    @locations_terminees.setter
    def locations_terminees(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._locations_terminees = value

    @property
    def clients(self):
        return self._clients

    @clients.setter
    def clients(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._clients = value

    # Début Getters et Setters

    def ajouter_vehicule(self, vehicule):
        self.parc_vehicules.append(vehicule)

    def enregistrer_client(self, client):
        self.clients.append(client)
        
    def louer_vehicule(self, client, vehicule, date_debut):
      pass
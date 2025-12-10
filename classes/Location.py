class Location:
    def __init__(
        self,
        client,
        vehicule,
        date_debut,
        date_fin,
        kilometrage_depart,
        kilometrage_retour,
        cout_total,
    ):
        self._client = client
        self._vehicule = vehicule
        self._date_debut = date_debut
        self._date_fin = None
        self._kilometrage_depart = kilometrage_depart
        self._kilometrage_retour = None
        self._cout_total = None

    # Début Getters et Setters

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._client = value

    @property
    def vehicule(self):
        return self._vehicule

    @vehicule.setter
    def vehicule(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._vehicule = value

    @property
    def date_debut(self):
        return self._date_debut

    @date_debut.setter
    def date_debut(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._date_debut = value

    @property
    def date_fin(self):
        return self._date_fin

    @date_fin.setter
    def date_fin(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._date_fin = value

    @property
    def kilometrage_depart(self):
        return self._kilometrage_depart

    @kilometrage_depart.setter
    def kilometrage_depart(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._kilometrage_depart = value

    @property
    def kilometrage_retour(self):
        return self._kilometrage_retour

    @kilometrage_retour.setter
    def kilometrage_retour(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._kilometrage_retour = value

    @property
    def cout_total(self):
        return self._cout_total

    @cout_total.setter
    def cout_total(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._cout_total = value

    # Début Getters et Setters

    def calculer_duree(self):
        return "durée"

    def calculer_cout(self):
        self.cout_total = 100
        return 100

    def terminer_location(self):
        return "terminer location"

    def __str__(self):
        return (
            self._client
            + " "
            + self._vehicule
            + " "
            + self._date_debut
            + " "
            + self._date_fin
            + " "
            + self._kilometrage_retour
            + " "
            + self._kilometrage_depart
            + " "
            + self._cout_total
        )

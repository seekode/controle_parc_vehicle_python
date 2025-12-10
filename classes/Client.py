class Client:
    def __init__(self, nom, prenom, numero_permis, date_naissance, email):
        self._nom = nom
        self._prenom = prenom
        self._numero_permis = numero_permis
        self._date_naissance = date_naissance
        self._email = email

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
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._prenom = value

    @property
    def numero_permis(self):
        return self._numero_permis

    @numero_permis.setter
    def numero_permis(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._numero_permis = value

    @property
    def date_naissance(self):
        return self._date_naissance

    @date_naissance.setter
    def date_naissance(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._date_naissance = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value is None:
            raise ValueError("Value is empty")
        self._email = value

    # Fin Getters et Setters

    def __str__(self):
        return (
            self._nom
            + " "
            + self._prenom
            + " "
            + self._numero_permis
            + " "
            + self._date_naissance
            + " "
            + self._email
        )

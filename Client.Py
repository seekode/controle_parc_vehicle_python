class Client:
    def __init__(self, nom, prenom, numero_permis, date_naissance, email):
        self._nom = nom
        self._prenom = prenom
        self._numero_permis = numero_permis
        self._date_naissance = date_naissance
        self._email = email

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

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._nom = value

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def modele(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._prenom = value

    @property
    def numero_permis(self):
        return self._numero_permis

    @numero_permis.setter
    def numero_permis(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._numero_permis = value

    @property
    def date_naissance(self):
        return self._date_naissance

    @date_naissance.setter
    def date_naissance(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._date_naissance = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._email = value

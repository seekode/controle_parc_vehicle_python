import re


class Client:
    def __init__(self, nom, prenom, numero_permis, date_naissance, email):
        self.nom = nom
        self.prenom = prenom
        self.numero_permis = numero_permis
        self.date_naissance = date_naissance
        self.email = email

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        if not valeur or not isinstance(valeur, str):
            raise ValueError("Le nom ne doit pas être vide.")
        self._nom = valeur

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, valeur):
        if not valeur or not isinstance(valeur, str):
            raise ValueError("Le prénom ne doit pas être vide.")
        self._prenom = valeur

    @property
    def numero_permis(self):
        return self._numero_permis

    @numero_permis.setter
    def numero_permis(self, valeur):
        if not valeur or not isinstance(valeur, str):
            raise ValueError("Le numéro de permis ne doit pas être vide.")
        self._numero_permis = valeur

    @property
    def date_naissance(self):
        return self._date_naissance

    @date_naissance.setter
    def date_naissance(self, valeur):
        if not valeur or not isinstance(valeur, str):
            raise ValueError("La date de naissance ne doit pas être vide.")
        self._date_naissance = valeur

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valeur):
        regex = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        if not valeur or not isinstance(valeur, str):
            raise ValueError("Le mail ne doit pas être vide.")
        if not re.fullmatch(regex, valeur):
            raise ValueError("L'email doit respecter le format d'email pour être valide.")

        self._email = valeur

    def __str__(self):
        return f"Nom: {self.nom}, Prénom: {self.prenom}, Numéro de permis: {self.numero_permis}, Date de naissance: {self.date_naissance}, email: {self.email}"

from datetime import date
import Assurable


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
        self._date_fin = date_fin
        self._kilometrage_depart = kilometrage_depart
        self._kilometrage_retour = kilometrage_retour
        self._cout_total = cout_total

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._client = value

    @property
    def vehicule(self):
        return self._prenom

    @vehicule.setter
    def vehicule(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._vehicule = value

    @property
    def date_debut(self):
        return self._date_debut

    @date_debut.setter
    def date_debut(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._date_debut = value

    @property
    def date_fin(self):
        return self._date_fin

    @date_fin.setter
    def date_fin(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._date_fin = value

    @property
    def kilometrage_debut(self):
        return self._email

    @kilometrage_debut.setter
    def kilometrage_debut(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._kilometrage_depart = value

    @property
    def kilometrage_retour(self):
        return self._email

    @kilometrage_retour.setter
    def kilometrage_retour(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._kilometrage_retour = value

    @property
    def cout_total(self):
        return self._email

    @cout_total.setter
    def cout_total(self, value):
        if len(value) == 0:
            raise ValueError("ses vide")
        self._cout_total = value

    def calsuler_duree(self):

        return (self.date_debut - self.date_fin).days

    def calculer_cout(self):
        if ():
            cout = self.calculer_duree() * 0 * self._vehicule.calculer_prime_assurance()
            return cout
        cout = self.calculer_duree() * 0
        self._cout_total = cout
        return cout

    def terminer_location(self, kilometrage_retour):
        if self._date_fin is not None:
            raise Exception("La location est déjà terminée")

        self._vehicule.kilometrage = kilometrage_retour

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
            + self._kilometrage_depart
            + " "
            + self._kilometrage_retour
            + " "
            + self._cout_total
        )

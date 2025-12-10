from exceptions import LocationDejaTerminee
from datetime import date


class Location:
    def __init__(
        self,
        client,
        vehicule,
        date_debut,
        kilometrage_depart,
        date_fin=None,
        kilometrage_retour=None,
    ):
        self.client = client
        self.vehicule = vehicule
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.kilometrage_depart = kilometrage_depart
        self.kilometrage_retour = kilometrage_retour
        self.cout_total = None

    def calculer_duree(self):
        if self.date_fin is None:
            today = date.today()
            duree = (today - self.date_debut).days + 1
        else:
            duree = (self.date_fin - self.date_debut).days + 1
        return duree

    def calculer_cout(self):
        duree = self.calculer_duree()
        cout = duree * self.vehicule.calculer_tarif_journalier()
        if hasattr(self.vehicule, "calculer_prime_assurance"):
            cout += self.vehicule.calculer_prime_assurance()
        self.cout_total = cout
        return self.cout_total

    def terminer_location(self, kilometrage_retour, date_fin=None):
        if self.date_fin is not None:
            raise LocationDejaTerminee("La location est déjà terminée.")
        self.date_fin = date_fin if date_fin else date.today()
        self.kilometrage_retour = kilometrage_retour
        self.vehicule.kilometrage = kilometrage_retour
        self.calculer_cout()

    def __str__(self):
        statut = "en cours" if self.date_fin is None else f"terminée le {self.date_fin}"
        cout = self.cout_total if self.cout_total is not None else "non calculé"
        return f"Location de {self.client.nom} pour le véhicule {self.vehicule.marque} du {self.date_debut} ({statut}), coût total: {cout}"

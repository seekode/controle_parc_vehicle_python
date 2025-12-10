# Class for information on each client
class Client:
    def __init__(self, nom, prenom, numero_permis, date_naissance, email):
        self.nom=nom
        self.prenom=prenom
        self.numero_permis=numero_permis
        self.date_naissance=date_naissance
        self.email=email

    def get_nom(self):
        return self.nom
    
    def set_nom(self, nom):
        if nom=="":
            raise ValueError("Ne doit pas être vide")
        else:
            self.nom=nom
    
    def get_prenom(self):
        return self.prenom
    
    def set_nom(self, prenom):
        if prenom=="":
            raise ValueError("Ne doit pas être vide")
        else:
            self.prenom=prenom
    
    def get_numero_permis(self):
        return self.numero_permis
    
    def set_nom(self, numero_permis):
        if numero_permis=="":
            raise ValueError("Ne doit pas être vide")
        else:
            self.numero_permis=numero_permis
    
    def get_date_naissance(self):
        return self.date_naissance
    
    def set_nom(self, date_naissance):
        if date_naissance=="":
            raise ValueError("Ne doit pas être vide")
        else:
            self.date_naissance=date_naissance
    
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        if email=="":
            raise ValueError("Ne doit pas être vide")
        else:
            self.email=email

    def __str__(self):
        pass
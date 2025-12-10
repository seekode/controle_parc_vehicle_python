class Client:
    def __init__(self, nom, prenom, numero_permis, date_naissance, email):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_permis = numero_permis
        self.__date_naissance = date_naissance
        self.__email = email

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        if value != " ":
            self.__nom = value

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, value):
        if value != " ":
            self.__prenom = value

    @property
    def numero_permis(self):
        return self.__numero_permis

    @numero_permis.setter
    def numero_permis(self, value):
        if value != " ":
            self.__numero_permis = value

    @property
    def date_naissance(self):
        return self.__date_naissance

    @date_naissance.setter
    def date_naissance(self, value):
        if value != " ":
            self.__date_naissance = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        # également possible d'utiliser des regex
        if value != " ":
            self.__email = value

    def __str__(self):
        print(
            self.prenom
            + " "
            + self.nom
            + " "
            + self.email
            + " né le "
            + self.date_naissance
            + " dont le numéro de permis est "
            + self.numero_permis
        )

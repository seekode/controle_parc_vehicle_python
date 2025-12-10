class Client:
    # constructor
    def __init__(self, lastname, firstname, permit_number, birth_date, email):
        self.__lastname = lastname
        self.__firstname = firstname
        self.__permit_number = permit_number
        self.__birth_date = birth_date
        self.__email = email

    # getter and setter
    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, value):
        if isinstance(value, str):
            self.__lastname = value
        else:
            "Le nom n'est pas valide"

    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, value):
        if isinstance(value, str):
            self.__firstname = value
        else:
            "Le prénom n'est pas valide"

    @property
    def permit_number(self):
        return self.__permit_number

    @permit_number.setter
    def permit_number(self, value):
        if isinstance(value, int):
            self.__permit_number = value
        else:
            "Le numéro de permis est pas un nombre"

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value):
        if isinstance(value, str):
            self.__birth_date = value
        else:
            "La date de naissance n'est pas valide"

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if isinstance(value, str):
            self.__email = value
        else:
            "L'email n'est pas valide"

    def __str__(self):
        return (
            self.firstname
            + " "
            + self.lastname
            + " a le permis "
            + str(self.permit_number)
        )


client = Client("Martin", "Jean", 1234, 1985, "rse")
print(client.firstname)
print(client.lastname)
print(client.permit_number)
print(client.__str__())

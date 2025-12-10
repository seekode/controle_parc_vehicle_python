class Client:
    def __init__(self, lastname, firstname, licence_number, birthdate, email):
        self._lastname = lastname
        self._firstname = firstname
        self._licence_number = licence_number
        self._birthdate = birthdate
        self._email = email
        pass

    def __str__(self):
        pass
    

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        if value != None:
            self._lastname = value

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        if value != None:
            self._firstname = value

    @property
    def licence_number(self):
        return self._licence_number

    @licence_number.setter
    def licence_number(self, value):
        if value != None:
            self._licence_number = value

    @property
    def birthdate(self):
        return self._birthdate

    @birthdate.setter
    def birthdate(self, value):
        if value != None:
            self._birthdate = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value != None:
            self._email = value

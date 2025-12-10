import re
from sqlite3 import Date


class Client:

    def __init__(self, lastname, name, license_number, birth_date, email):
        self._lastname = lastname
        self._name = name
        self._license_number = license_number
        self._birth_date = birth_date
        self._email = email

    # Creation of setter and getter
    @property
    def lastname(self):
        return self._lastname 
    
    @lastname.setter
    def lastname (self, value):
        self._lastname = value
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name (self, value):
        self._name = value
    
    @property
    def license_number(self):
        return self._license_number 
    
    @license_number.setter
    def license_number (self, value):
        if isinstance(value, (int)) == True :
            self._license_number = value
    
    @property
    def birth_date(self):
        return self._birth_date
    
    @birth_date.setter
    def birth_date (self, value):
        if Date(value) == True:
            self._birth_date = value

    @property
    def email(self):
        return self._email
    
    @email.setter
    def set_email (self, value):
        EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if not EMAIL_REGEX.match(value):
            self._email = value
        else:
            print('Invalide Email')
            self.set_email

    def __str__(self):
        return self.lastname + " " + self.name +" "+ self.birth_date+ " "+ self.email
    

client = Client('D', 'o', 4545155, '29/11/2006','fghj@fcvgbhjn.com')

print(str(client))
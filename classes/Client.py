class Client():
    # Initialisation
    def __init__(self, nom: str, prenom: str, numero_permis: int, date_naissance: str, email: str):
        self.nom = nom
        self.prenom = prenom
        self.numero_permis = numero_permis
        self.date_naissance = date_naissance
        self.email = email

    # Getters
    @property
    def get_nom(self) -> str:
        return self.nom

    @property
    def get_prenom(self) -> str:
        return self.prenom

    @property
    def get_numero_permis(self) -> int:
        return self.numero_permis

    @property
    def get_date_naissance(self) -> str:
        return self.date_naissance

    @property
    def get_email(self) -> str:
        return self.email   

    # Setters
    def set_nom(self, nom: str):
        if not isinstance(nom, str) or len(nom.strip()) < 1:
            raise ValueError("Le nom doit être une chaîne de caractères non vide.")
        self.nom = nom.strip()

    def set_prenom(self, prenom: str):
        if not isinstance(prenom, str) or len(prenom.strip()) < 1:
            raise ValueError("Le prénom doit être une chaîne de caractères non vide.")
        self.prenom = prenom.strip()

    def set_numero_permis(self, numero_permis: int):   
        if not isinstance(numero_permis, int) or numero_permis <= 0:
            raise ValueError("Le numéro de permis doit être un entier positif.")
        self.numero_permis = numero_permis

    def set_date_naissance(self, date_naissance: str):
        if not isinstance(date_naissance, str) or len(date_naissance.strip()) < 1:
            raise ValueError("La date de naissance doit être une chaîne de caractères non vide.")
        self.date_naissance = date_naissance.strip()

    def set_email(self, email: str):
        if not isinstance(email, str) or len(email.strip()) < 1:
            raise ValueError("L'email doit être une chaîne de caractères non vide.")
        self.email = email.strip()

    # Méthode magique
    def __str__(self):
        return f"Client: {self.prenom} {self.nom}, Permis n°: {self.numero_permis}, Date de naissance: {self.date_naissance}, Email: {self.email}"
    
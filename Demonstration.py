from Agence import Agence
from Camion import Camion
from GestionnaireTarifs import GestionnaireTarifs
from Moto import Moto
from Voiture import Voiture
from Client import Client


tarifs = GestionnaireTarifs(
    {"Voiture": 50, "Moto": 30, "Camion": 100}, 2, {"Voiture": 10, "Camion": 25}
)

agence = Agence(
    [
        Voiture(
            "feufe",
            "feufe",
            "feufe",
            "feufe",
            "feufe",
            "feufe",
            "feufe",
            "feufe",
            "feufe",
            "feufe",
        ),
        Voiture(
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
        ),
        Voiture(
            "azerr",
            "azerr",
            "azerr",
            "azerr",
            "azerr",
            "azerr",
            "azerr",
            "azerr",
            "azerr",
            "azerr",
        ),
        Camion(
            "poirzr",
            "poirzr",
            "poirzr",
            "poirzr",
            "poirzr",
            "poirzr",
            "poirzr",
            "poirzr",
            "poirzr",
            "poirzr",
        ),
        Moto(
            "mpzppo",
            "mpzppo",
            "mpzppo",
            "mpzppo",
            "mpzppo",
            "mpzppo",
            "mpzppo",
            "mpzppo",
            "mpzppo",
        ),
    ],
    [
        Moto(
            "mpzppo",
            "mpzppo",
            "mpzppo",
            "mpzppo",
            "mpzppo",
            "mpzppo",
            "mpzppo",
            "mpzppo",
            "mpzppo",
        ),
        Camion(
            "poirzr",
            "poirzr",
            "poirzr",
            "poirzr",
            "poirzr",
            "poirzr",
            "poirzr",
            "poirzr",
            "poirzr",
            "poirzr",
        ),
    ],
    [
        Voiture(
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
            "yfuzeygufyuhfz",
        ),
    ],
    [Client("fefe", "reyry", "feyyfhe" "feyefyfe", "fyeuyfe", "yfeyfe")],
)

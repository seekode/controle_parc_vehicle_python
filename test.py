from Voiture import Voiture

def main():
    try:
        ma_voiture = Voiture(
            marque="Toyota",
            modele="Corolla",
            annee=2022,
            immatriculation="AB-123-CD",
            kilometrage=15000,
            disponible=True,
            nombre_places=5,
            type_carburant="Essence",
            coffre_litres="400"
        )

        print("Marque :", ma_voiture.marque)
        print("Modèle :", ma_voiture.modele)
        print("Nombre de places :", ma_voiture.nombre_places)
        print("Type de carburant :", ma_voiture.type_carburant)
        print("Coffre en litres :", ma_voiture.coffre_litres)

        try:
            ma_voiture.nombre_places = 0 
        except ValueError as e:
            print("Erreur attendue :", e)

    except Exception as e:
        print("Erreur lors de la création de la voiture :", e)


if __name__ == "__main__":
    main()
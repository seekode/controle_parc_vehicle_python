# Fichier programme_test.py
from datetime import date, timedelta
from GestionnaireTarifs import GestionnaireTarifs
from Vehicule import Vehicule 
from Voiture import Voiture
from Moto import Moto
from Camion import Camion
from Client import Client
from Agence import Agence
from Exceptions import VehiculeIndisponible, LocationDejaTerminee

# --- Dates référence ---
AUJOURDHUI = date.today()
DEBUT_LOC_1 = AUJOURDHUI - timedelta(days=5)
FIN_LOC_1 = AUJOURDHUI - timedelta(days=2)
DEBUT_LOC_2 = AUJOURDHUI - timedelta(days=1)
FIN_LOC_2 = AUJOURDHUI 
DEBUT_LOC_3 = AUJOURDHUI

print("--- 1. Configuration du Gestionnaire de Tarifs (Singleton) ---")
# 1. Crée une instance de GestionnaireTarifs et configure les tarifs
tarifs = GestionnaireTarifs()
tarifs.modifier_tarif("Voiture", 55.0) # Modifie le tarif
tarifs.appliquer_saison_haute(True) # Active la saison haute
print(f"Tarif Voiture (Saison Haute): {tarifs.get_tarif_base('Voiture'):.2f}€/jour")
print(f"Tarif Assurance Camion: {tarifs.get_tarif_assurance('Camion'):.2f}€/jour")

print("\n--- 8. Vérification du Singleton ---")
# Test 8: Vérifie que le singleton fonctionne
tarifs_bis = GestionnaireTarifs()
print(f"tarifs est tarifs_bis (même objet): {tarifs is tarifs_bis}") # DOIT être True
print(f"Tarif Voiture via tarifs_bis: {tarifs_bis.get_tarif_base('Voiture'):.2f}€/jour")


print("\n--- 2. Création de l'Agence et 5 Véhicules ---")
agence = Agence("Auto Location Pro", [], [], [], [])

v1 = Voiture("Renault", "Clio", 2022, "AA-123-BB", 10000, True, 5, "Essence", 391)
v2 = Voiture("Tesla", "Model 3", 2024, "CC-456-DD", 500, True, 5, "Électrique", 425)
m1 = Moto("Yamaha", "MT-07", 2021, "EE-789-FF", 8000, True, "Routière", 689)
m2 = Moto("Kawasaki", "ZX-10R", 2023, "GG-012-HH", 200, True, "Sportive", 998)
c1 = Camion("Mercedes", "Actros", 2018, "II-345-JJ", 150000, True, 8000, 30.5, "CE")

agence.ajouter_vehicule(v1)
agence.ajouter_vehicule(v2)
agence.ajouter_vehicule(m1)
agence.ajouter_vehicule(m2)
agence.ajouter_vehicule(c1)
print(f"Parc Agence créé : {len(agence.parc_vehicules)} véhicules")


print("\n--- 3. Enregistrement de 3 Clients ---")
c_dupont = Client("Dupont", "Jean", 123456789, "1985-05-15", "jean.dupont@mail.com")
c_martin = Client("Martin", "Sophie", 987654321, "1990-08-20", "sophie.martin@email.fr")
c_leblanc = Client("Leblanc", "Marc", 112233445, "1975-01-10", "marc.leblanc@loc.com")

agence.enregistrer_client(c_dupont)
agence.enregistrer_client(c_martin)
agence.enregistrer_client(c_leblanc)
print(f"Clients enregistrés : {len(agence.clients)}")


print("--- 4. Exécution de 3 Locations ---")

# Location 1 : Voiture (avec assurance)
loc1 = agence.louer_vehicule(c_dupont, v1, DEBUT_LOC_1)
print(f"Création: {loc1}")

# Location 2 : Moto (sans assurance)
loc2 = agence.louer_vehicule(c_martin, m1, DEBUT_LOC_2)
print(f"Création: {loc2}")

# Location 3 : Camion (avec assurance, en cours)
loc3 = agence.louer_vehicule(c_leblanc, c1, DEBUT_LOC_3)
print(f"Création: {loc3}")

print("--- Affichage des véhicules disponibles (V2 et M2) ---")
for v in agence.afficher_vehicules_disponibles():
    print(v)


print("--- 5. Terminer 2 Locations ---")
try:
    # Termine la loc 1
    agence.retourner_vehicule(loc1, FIN_LOC_1, v1.kilometrage + 300)
    print(f"Terminée: {loc1}")
    
    # Termine la loc 2
    agence.retourner_vehicule(loc2, FIN_LOC_2, m1.kilometrage + 150)
    print(f"Terminée: {loc2}")

except (LocationDejaTerminee, ValueError) as e:
    print(f"Erreur lors du retour : {e}")

# Location supplémentaire pour le calcul du véhicule le plus loué
loc4 = agence.louer_vehicule(c_dupont, v1, AUJOURDHUI)
agence.retourner_vehicule(loc4, AUJOURDHUI + timedelta(days=1), v1.kilometrage + 50)
print(f"Terminée: {loc4}")


print("--- 6. Calcul du Chiffre d'Affaires ---")
ca_total = agence.calculer_chiffre_affaires()
print(f"Chiffre d'Affaires total des locations terminées: {ca_total:.2f}€")


print("--- 7. Test des Exceptions ---")
# Test 7.1 : Tentative de louer un véhicule indisponible (le camion est toujours en cours)
try:
    agence.louer_vehicule(c_dupont, c1, AUJOURDHUI)
except VehiculeIndisponible as e:
    print(f"Succès exception 1 : {e}")

# Test 7.2 : Tentative de terminer une location déjà terminée
try:
    # On essaie de terminer loc1 à nouveau
    agence.retourner_vehicule(loc1, AUJOURDHUI, v1.kilometrage + 50)
except LocationDejaTerminee as e:
    print(f"Succès exception 2 : {e}")
except ValueError as e:
    # Peut lever une ValueError si le kilométrage n'augmente pas ou autre
    print(f"Erreur lors du test (non LocationDejaTerminee) : {e}")


print("--- Véhicule le plus loué ---")
v_prefere = agence.vehicule_le_plus_loue()
if v_prefere:
    print(f"Véhicule le plus loué (2 locations) : {v_prefere}")
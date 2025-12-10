# Contrôle POO Python - Système de gestion de parc de véhicules

## Contexte

Vous êtes chargé(e) de développer un système de gestion pour une agence de location de véhicules. L'application doit permettre de gérer différents types de véhicules, les clients, et les locations.

## Cahier des charges

### 1. Classe abstraite `Vehicule`

Créer une classe abstraite `Vehicule` avec les attributs suivants :

- `marque` : marque du véhicule
- `modele` : modèle du véhicule
- `annee` : année de mise en circulation
- `immatriculation` : numéro d'immatriculation (unique)
- `kilometrage` : kilométrage actuel
- `disponible` : booléen indiquant si le véhicule est disponible

Méthodes à implémenter :

- Méthode abstraite `calculer_tarif_journalier()` qui retourne le tarif de location par jour
- Méthode `afficher_infos()` qui affiche les informations du véhicule
- Méthodes magiques `__str__()` et `__repr__()`
- Getters et setters appropriés avec validation

### 2. Classes concrètes de véhicules

Implémenter au moins 3 types de véhicules différents :

**`Voiture`** avec attributs supplémentaires :

- `nombre_places` : nombre de places (2 à 9)
- `type_carburant` : essence, diesel, électrique, hybride
- `coffre_litres` : volume du coffre en litres

**`Moto`** avec attributs supplémentaires :

- `cylindree` : cylindrée en cm³
- `type_moto` : sportive, routière, custom, trail

**`Camion`** avec attributs supplémentaires :

- `charge_utile` : charge utile maximale en kg
- `volume_benne` : volume de la benne en m³
- `permis_requis` : type de permis nécessaire (C, CE, etc.)

### 3. Interface `Assurable`

Créer une classe abstraite `Assurable` avec la méthode abstraite :

- `calculer_prime_assurance()` : calcule le montant de l'assurance journalière

Les véhicules `Voiture` et `Camion` doivent implémenter cette interface.  
Les `Moto` n'ont pas besoin d'assurance dans ce système.

### 4. Classe `Client`

Attributs :

- `nom` : nom du client
- `prenom` : prénom du client
- `numero_permis` : numéro de permis de conduire
- `date_naissance` : date de naissance
- `email` : email du client

Méthodes :

- Getters et setters avec validation (email valide, permis non vide, etc.)
- Méthode magique `__str__()`

### 5. Classe `Location`

Attributs :

- `client` : instance de Client
- `vehicule` : instance de Vehicule
- `date_debut` : date de début de location
- `date_fin` : date de fin de location (peut être None si en cours)
- `kilometrage_depart` : kilométrage au départ
- `kilometrage_retour` : kilométrage au retour (None si en cours)
- `cout_total` : coût total de la location (calculé)

Méthodes :

- `calculer_duree()` : calcule la durée en jours
- `calculer_cout()` : calcule le coût total (tarif journalier × durée + assurance si applicable)
- `terminer_location(kilometrage_retour)` : termine la location et met à jour le kilométrage du véhicule
- Gestion d'exception si on essaie de terminer une location déjà terminée
- Méthode magique `__str__()`

### 6. Classe `GestionnaireTarifs` (Singleton)

**Important : Cette classe doit être implémentée comme un Singleton.**

Attributs :

- `tarifs_base` : dictionnaire des tarifs de base par type de véhicule
  - Ex: `{"Voiture": 50, "Moto": 30, "Camion": 100}`
- `coefficient_saison_haute` : coefficient multiplicateur pour la saison haute (ex: 1.5)
- `tarif_assurance` : dictionnaire des tarifs d'assurance par type
  - Ex: `{"Voiture": 10, "Camion": 25}`

Méthodes :

- `get_tarif_base(type_vehicule)` : retourne le tarif de base pour un type de véhicule
- `get_tarif_assurance(type_vehicule)` : retourne le tarif d'assurance pour un type
- `appliquer_saison_haute(activer)` : active/désactive le coefficient de saison haute
- `modifier_tarif(type_vehicule, nouveau_tarif)` : modifie un tarif de base

**Justification du Singleton :** Il ne doit exister qu'une seule source de vérité pour les tarifs dans toute l'application. Tous les véhicules et toutes les locations doivent utiliser la même instance de `GestionnaireTarifs`.

### 7. Classe `Agence`

Attributs :

- `nom` : nom de l'agence
- `parc_vehicules` : liste de tous les véhicules
- `locations_en_cours` : liste des locations en cours
- `locations_terminees` : liste des locations terminées
- `clients` : liste des clients enregistrés

Méthodes :

- `ajouter_vehicule(vehicule)` : ajoute un véhicule au parc
- `enregistrer_client(client)` : enregistre un nouveau client
- `louer_vehicule(client, vehicule, date_debut)` : crée une nouvelle location
  - Doit vérifier que le véhicule est disponible
  - Doit lever une exception `VehiculeIndisponible` si le véhicule n'est pas disponible
- `retourner_vehicule(location, kilometrage_retour, date_fin)` : termine une location
- `afficher_vehicules_disponibles()` : affiche tous les véhicules disponibles
- `calculer_chiffre_affaires()` : calcule le CA total des locations terminées
- `vehicule_le_plus_loue()` : retourne le véhicule le plus loué

### 8. Exceptions personnalisées

Créer au moins 2 exceptions personnalisées :

- `VehiculeIndisponible` : levée quand on tente de louer un véhicule non disponible
- `LocationDejaTerminee` : levée quand on tente de terminer une location déjà terminée

## Contraintes techniques

- **Encapsulation** : Utiliser des attributs privés (convention `_attribut`) avec des propriétés `@property` ou des getters/setters
- **Validation** : Valider les données entrées (années cohérentes, kilométrage positif, etc.)
- **Méthodes magiques** : Implémenter au minimum `__str__()` et `__repr__()` sur au moins 3 classes
- **Héritage** : Utiliser correctement `super()` dans les constructeurs
- **Singleton** : La classe `GestionnaireTarifs` DOIT être un singleton fonctionnel
- **Documentation** : Commenter les parties importantes du code

## Programme de test

Créer un programme de démonstration qui :

1. Crée une instance de `GestionnaireTarifs` et configure les tarifs
2. Crée une agence avec au moins 5 véhicules différents
3. Enregistre au moins 3 clients
4. Effectue au moins 3 locations (dont au moins une avec assurance)
5. Termine au moins 2 locations
6. Affiche le chiffre d'affaires de l'agence
7. Teste les exceptions (tentative de location d'un véhicule indisponible)
8. Vérifie que le singleton fonctionne (deux références pointent vers la même instance)


## Livrables

Plusieurs fichiers Python contenant :

1. Toutes les classes demandées
2. Le programme de test/démonstration
3. Des commentaires pertinents

## Conseils

- Lisez TOUT le sujet avant de commencer
- Commencez par les classes de base avant les fonctionnalités avancées
- Testez régulièrement votre code au fur et à mesure
- N'oubliez pas le Singleton pour `GestionnaireTarifs` !

**Bon courage !**

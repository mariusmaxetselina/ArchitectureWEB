# ArchitectureWEB
Réalisation du projet d'architecture web réalisé par Marius Riviere, Alexandre Pradere-Niquet et Elliot Candale.

Il est tout d'abord nécessaire d'avoir créé un environnement virtuel et d'avoir installé django.

### Installation des packages nécéssaire

Pour utiliser le site vous devez installer les packages requis dans le dossier de l'environnement virtuel:

    pip install -r requirements.txt

### Créer la base de données

Il est nécessaire de créer la base de données :

    python manage.py makemigrations Enigme
    
    python manage.py sqlmigrate Enigme 0001
    
    python manage.py migrate
    
Mettre yes
 
### Démarrer le serveur

Il est conseillé pour une bonne utilisation du site de mettre la commande exact :

    python manage.py runserver localhost:8000

### Finalisation

Site en cours de développement.

### Quelques remarques

* Base de données
	* des comptes admin ont été créés
	* seul X compte utilisateurs ont été créés
	* seulement quelques enigmes ont été 

# ArchitectureWEB
Réalisation du projet d'architecture web réalisé par  Alexandre Pradere-Niquet ,Elliot Candale et Marius Riviere.

Il est nécessaire d'avoir créé un environnement virtuel et d'avoir installé django.

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

### Partage des taches au sein du groupe

Elliot et Alexandre ont réalisé le site. Tout ce qui est du css, création de la base de données et l'inscription ont été réalisés par ces derniers.

Elliot s'est occupé de la connexion et la déconnexion.

Alexandre s'est occupé des liens entre la base User et Enigmes notamment dans l'inscription, puis la gestion de ce qui est affiché selon condition de si l'on est co ou non.

Marius a réalisé un jeu en python qui se trouve dans Enigma/mysite/JeuPython.

### Quelques remarques

* Base de données
	* des comptes admin ont été créés
	* seulement quelques comptes utilisateurs ont été créés
	* seulement 10 enigmes ont été rentrées dans la base de données
	* lors de l'inscription l'utilisateur est connecté avec pour level 1
	* pour acceder aux devinettes il faut etre connecté puis aller sur http://127.0.0.1:8000/devinette/1  (actuellement on peut aller jusqu'a 10) OU dans l'onglet enigme cliquer sur le lien "lien Enigmes"


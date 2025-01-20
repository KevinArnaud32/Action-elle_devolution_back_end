
## Description

Ce projet test q été réalisé avec le framework python django 

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- [Python](https://www.python.org/) (version >= X.X)
- [pip](https://pip.pypa.io/en/stable/) (installé avec Python)

## Installation

1. Clonez le dépôt : git clone https://github.com/KevinArnaud32/Action-elle_devolution_back_end.git
2. supprimer l'environnement virtuel. Pour ce fait supprimer le dossier nommé env ou venv
3. récrer vous même votre propre environnement virtuel avec la commande : pyton -m venv env / pyton -m venv venv
4. activer l'environnement virtuel en exécutant le chemin qui mène vers activate.bat généralement dans env/Scripts/
5. vous trouverez un fichier requirements.txt, installer les dépendances. Pour ce fait déplacer vous dans le dossier où se trouve le fichier requiremnts.txt et exécuter la commande pip install -r requirements.txt.
Cette commande installera toutes les dépendances nécéssaires pour exécuter le projet django
6. déplacer vous dans le dossier src/ là où se trouve normalement le fichier manage.py
7. Dans le dossier vous verez le dossier ActionElles/ dans lequel se trouve le fichier settings comportant les paramètres de l'application django
8. Dans ce fichier, vous verez un objet DATABASE = {} pour le configuration de la base de données, veuillez configurer votre base de données tout en suivant la documentation suivante en fonction de votre base de données utilisé : https://docs.djangoproject.com/en/5.1/ref/databases/
9. Toujours le fichier où se trouve le fichier manage.py exécuter cette : pyton manage.py makemigrations. Cela initialisera les migrations
Aprés exécution de la commande si vous voyez apparaitre le message "no changes detected" passer directement à la migration
10. exécuter la commande python manage.py migrate pour faire la migration. Cela créera les tables dans votre base de données
11. exécuter maintenant l'application. Pour ce fait exécuter la commande python manage.py runserver . Cela lancera le serveur pour démmarer le projet Django

# le serveur etant lancé, vous pouvez maintenant exécuter le front

## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/lisa367/OPC-Projet_13-fork.git`

#### Architecture simplifiée du projet

<pre>
OPC-Projet_13-fork/
  | lettings/
  | profiles/
  | oc_lettings_site/

  | templates/
  | static/

  | doc/
  | .circleci/

  | manage.py
  | oc-lettings-site.sqlite3
  | requirements.txt
  | Dockerfile

</pre>

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Couverture de tests

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `coverage run -m pytest`
- `coverage report --format=html -fail-under=80`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


### Déploiement
- A chaque nouveau commit poussé sur GitHub, le pipeline CI/CD se lance :
    - les tests sont effectués
    - une nouvelle image Docker est créée et poussée sur DockerHub
    - un nouveau conteneur est déployé sur Render

- Créer un compte sur les plateformes de Render et CircleCI
- Sur Render
    - créer un nouveau service web (onglet  'Web Service')
    - dans la configuration du projet, ajouter un nom et positionner le 'Runtime' sur Docker
    - cliquer sur le bouton 'Advanced' et s'assurer que 'Auto Derploy' est bien positionné sur "No"
    - définir les variables d'environnement pour DEBUG, SECRET_KEY et DSN
    - dans l'onglet 'Settings', copier le 'Deploy Hook'

- Sur CircleCI
    - suivre le répertoire Github associé au projet et sélectionner la branche master
    - définir les variables d'environnement pour DOCKER_USERNAME, DOCKER_TOKEN, IMAGE_NAME et WEBHOOK (le hook récupéré précédemment sur Render)
# GrandPy Bot le papy-robot

<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/javascript%20-%23323330.svg?&style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/> <img src="https://img.shields.io/badge/html5%20-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white"/> <img src="https://img.shields.io/badge/css3%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white"/>

## Pour commencer
### Pré-requis:
Vous avez besoin de : 
  * Python3
  * pip
  * venv
  * Git
  * Un compte heroku
  * Heroku CLI
  * tout ce que le fichier .zip contient
  
### Installation : 

1. Créer un dossier qui contiendra l'application.
2. Entrer dans le dossier grâce au terminal.
```
~$ cd chemin/vers/le_dossier
```
3. Créer un nouvel environnement virtuel.
```
~$ python3 -m venv newenv
```
4. Activer le.
```
~$ source newenv/bin/activate
```
5. Se loger à Heroku.
```
~$ heroku login
```
Un message demandant d'entrer n'importe quelle lettre (sauf "q") apparait.  
Entrer n'importe quelle lettre.
Un fenêtre internet s'ouvre.  
Cliquer sur __"Log in"__.

6. Créer un clone du dépôt P7_GrandPy_Bot suivant : 
[Liens vers le dépôt P7_GrandPy_Bot](https://github.com/micktymoon/P7_GrandPy_Bot.git)
```
~$ git clone https://github.com/micktymoon/P7_GrandPy_Bot.git
~$ cd P7_GrandPy_Bot
```
7. Installer le fichier requierement.txt
```
~$ pip install -r requirements.txt
```
8. Créer une application Heroku.
```
~$ heroku create
```
9. Faire un Git Push vers Heroku main.
```
~$ git push heroku main
```
10. S'assurer qu'au moins une instance de l'application est en cours d'exécution.
```
~$ heroku ps:scale web=1
```
11. Visiter l'application à l'URL générée par son nom d'application. Ou utilisez le raccourci pratique suivant:
```
~$ heroku open
```
12. ajouter "/home" à l'url en haut de la page.

## Démarrage

Dans un navigateur :
1. Entrer l'url de l'application heroku en y ajoutant "/home"  
ex : https://pacific-ocean-97327.herokuapp.com/home

2. Vous pouvez maintenant échanger avec GrandPy Bot.

## Fabriqué avec

   * Pycharm - IDE Python
   *  <img src="https://img.shields.io/badge/flask%20-%23000.svg?&style=for-the-badge&logo=flask&logoColor=white"/> - Micro framework open-source de développement web en Python.
   *  <img src="https://img.shields.io/badge/heroku%20-%23430098.svg?&style=for-the-badge&logo=heroku&logoColor=white"/> - Plateforme en tant que service permettant de déployer des applications sur le Cloud.
 
## Versions
<img src="https://img.shields.io/badge/git%20-%23F05033.svg?&style=for-the-badge&logo=git&logoColor=white"/> <img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/>

Voici le lien vers la version stable : 
[Liens vers le dépot P7_GrandPy_Bot](https://github.com/micktymoon/P7_GrandPy_Bot)

## Auteurs

Céline PELLETIER alias @micktymoon

## Remerciements

Je tiens à remercier la communauté d'OpenClassRooms et mon mentor de m'avoir soutenu dans ce projet.

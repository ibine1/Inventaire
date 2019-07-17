<center> <h1>Script d'inventaire Windows 10 </h1> </center>

## Langage utilisé ##  
- Powershell
- Python
## Prerequis ##
- Vous devez avoir les droits administrateurs  
- Un environnement Python, vous pouvez télécharger Python 3.7 [ici](  https://www.python.org/ftp/python/3.7.4/python-3.7.4.exe)

## Présentation ##  
Ce script a été écrit avec python 3.7.4,  il est donc fonctionnel avec l'environnement Python 3.7.4 ou plus.  

Ce script a pour but de faire l'inventaire des applications installées sur le poste de travail, puis d'insérer le résultat de cet inventaire dans un fichier en ".CSV". 
## Installation ##

- Télécharger Python 3.X via le lien fourni ci-dessus.
- Installer Python avec les droits admin
- Vérifier que le path pour python a bien été créé.

## Exemple d'utilisation ##

Lancez votre cmd en mode admin 

![Screenshot](0.png)

Rendez-vous dans le répertoire du script inventaire.py via l'invite de commande. Puis tapez " python Inventaire.py", afin de lancer le script. 

![Screenshot](1.png)

Le script vous demande de renseigner le nom ou l'adresse IP de la machine.

![Screenshot](2.png)

Une fois le nom renseigné, le script vérifie la disponibilité du poste. Si le poste répond au ping, le script vous indique que le poste est joignable, et il fait l'inventaire du poste. Le fichier inventaire du poste se crée dans le répertoire courant .

![Screenshot](3.png)

Sinon le script vous demandera de vérifier la disponibilité du poste et le hostname ou IP.

![Screenshot](4.png)

## Authors ##

Ibine && Moussi13 

## Licence ##

Ce projet est sous la licence MIT  -- Pour plus de détails cliquez [ici](https://choosealicense.com/licenses/)
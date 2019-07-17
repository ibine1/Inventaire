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

![0](https://user-images.githubusercontent.com/52750872/61367275-8d890b00-a88b-11e9-9912-617ed32df633.PNG)

Rendez-vous dans le répertoire du script inventaire.py via l'invite de commande. Puis tapez " python Inventaire.py", afin de lancer le script. 

![1](https://user-images.githubusercontent.com/52750872/61367276-8d890b00-a88b-11e9-9f85-f6bef16fecd8.PNG)

Le script vous demande de renseigner le nom ou l'adresse IP de la machine.

![2](https://user-images.githubusercontent.com/52750872/61367270-8cf07480-a88b-11e9-9503-5789ec88b2fb.PNG)

Une fois le nom renseigné, le script vérifie la disponibilité du poste. Si le poste répond au ping, le script vous indique que le poste est joignable, et il fait l'inventaire du poste. Le fichier inventaire du poste se crée dans le répertoire courant .

![3](https://user-images.githubusercontent.com/52750872/61367271-8d890b00-a88b-11e9-869d-066bcd120bad.PNG)

Sinon le script vous demandera de vérifier la disponibilité du poste et le hostname ou IP.

![4](https://user-images.githubusercontent.com/52750872/61367273-8d890b00-a88b-11e9-9333-4192af7eb947.PNG)

## Authors ##

Ibine && Moussi13 

## Licence ##

Ce projet est sous la licence MIT  -- Pour plus de détails cliquez [ici](https://choosealicense.com/licenses/)

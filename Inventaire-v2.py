#les différents modules
import os
import subprocess, sys



print('Début du scipt ')

# Donnez le nom de la machine concerné et insérez la valeur dans hostname 

Hostname = input('Quel est le nom ou @IP de la machine concerné par la demande ')

#La fonction ci-dessous vérifie si le poste et joignable via un ping (on le voit en )

response = os.system("ping -c 1 " + Hostname)

#Si le poste est joignable 
if response == 0:
  print(Hostname, 'est joignable sur le réseau')

# Si vous souhaiter prendre la main sur un poste distant c'est ici que vous devez codé la fonction d'authentification 
# avec les droit admin et la commande Get-WmiObject -Class Win32_Product | Select-Object -Property Name
#                                             ici
#
#########################################################################################

  #Le script ouvre une console powershell et execute la commande ci-dessous
  p = subprocess.Popen(["powershell.exe", 
    "Get-WmiObject -Class Win32_Product | Select-Object -Property Name "],  
    stdout=subprocess.PIPE, universal_newlines=True)
  sortie = p.communicate()[0]

  #permet de creer le fichier  "monFichier.csv" en mode ecriture
  f = open('monFichier.csv', 'w')
  
  # Cette boucle permet de supprimé les lignes vides. Elle parcoure les ligne et supprime les lignes vides
  for ligne in sortie.splitlines():
    if len(ligne) < 1:
      del ligne
    elif  len(ligne.split())<1 :
      del ligne
    else:
      
      f.write(ligne+'\n')
  #Fermeture du fichier csv
  f.close    
     
        

  print( "Le fichier CSV de l'inventaire est créé ")
# Si le poste est injoignable 
else:
  print(Hostname, "est injoignable sur le réseau, merci de vérifier la disponibilité et le hostname ou l'@ IP ")
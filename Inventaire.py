#les différents module
import os
import subprocess, sys



print('Début du scipt ')

# Donner le nom de la machine concerne et insérer la valeur dans hostname 

Hostname = input('Quel est le nom ou @IP de la machine concerné par la demande ')

#SI hostname existe (on le voit en )
 #example
response = os.system("ping -c 1 " + Hostname)

#and then check the response...
if response == 0:
  print(Hostname, 'est joignable sur le réseau')

      #recuperer la liste des appli en 32 > liste_32 et recuperer la liste des appli en 64 > liste_64
      #liste_32 + liste_64 = ttes_appli
  p = subprocess.Popen(["powershell.exe", 
    "Get-WmiObject -Class Win32_Product | Select-Object -Property Name "],  
    stdout=subprocess.PIPE, universal_newlines=True)
  sortie = p.communicate()[0]

  #permet de creer le fichier  "monFichier.csv" en mode ecriture
  f = open('monFichier.csv', 'w')
  
  
  for ligne in sortie.splitlines():
    if len(ligne) < 1:
      del ligne
    elif  len(ligne.split())<1 :
      del ligne
    else:
      
      f.write(ligne+'\n')
  
  f.close    
     
        

  print( "Le fichier CSV de l'inventaire est créé ")
else:
  print(Hostname, "est injoignable sur le réseau, merci de vérifier la disponibilité et le hostname ou l'@ IP ")

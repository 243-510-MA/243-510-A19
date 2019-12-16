from picamera import PiCamera
import time
import os, fnmatch
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


msg = MIMEMultipart()
msg['From'] = "alerteserre@gmail.com"					# adresse de l'enoyeur
msg['To'] = "nini12lego@gmail.com.com"					# adresse destinataire A CHANGER SVP PLSS MA PAUVRE BOITE MAIL
password = "wikitge2019"								# mot de passe de l'envoyeur
msg['Subject'] = "Attention!"							# sujet du mail
#body est le contenu du mail
body = "Alerte, un mouvement à été détecté! C'est peut-être un animal, ou pas. Tu peut mettre l'adresse Ip du Raspberry + :8081 (le port) .  La bise"
msg.attach(MIMEText(body, 'html'))						# crée le mail

i = 0
      
listOfFiles = os.listdir('/Vakanc_a_kebec/ete_1999/') 	# permet de savoir le nombre de fichiers de type .mkv dans le dossier spécifié
pattern = "*.mkv"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
        i = i +1
nbrfichier = i											# nombre de fichiers

while True:
    listOfFiles = os.listdir('/Vakanc_a_kebec/ete_1999/')
    pattern = "*.mkv"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            i = i +1
        if nbrfichier != i:								# si un nouveau fichier a été ajouté, donc qu'un mouvement a été détecté
            nbrfichier = i								# met a jour le nombre de fichier
            server = smtplib.SMTP("smtp.gmail.com", 587)	# le reste du code permet de se connecter au serveur de google pour envoyer le mail
            server.starttls()
            server.login(msg['From'], password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()
            print(nbrfichier)
    

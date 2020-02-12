#pip install pyserial
import os
import time
import threading

from programme_outil_db import*

import serial
import time

##################################################################
#Récuperation temp ext
def sms_tempext(num):
    #lecture etat de la chaudiere
    variable_input = "temperature_exterieur"
    lecture_db(variable_input)
    temperature_ext= lecture_db(variable_input)
        
    #envoie temperature ext
    numero = num
    Text_sms=("Temperature exterieur : "+str(temperature_ext)+" degres")
    Envoyer_sms(Text_sms,numero)
    
##################################################################
#Récuperation etat chaudière
def sms_etat(num):
    #lecture etat de la chaudiere
    variable_input = "etat_chaudiere"
    lecture_db(variable_input)
    etat_chaudiere= lecture_db(variable_input)
    if etat_chaudiere ==0:
        etat_chaudiere = "La chaudiere est eteinte"
    elif etat_chaudiere ==1:
        etat_chaudiere = "La chaudiere est allumee"
        
    #envoie de l'état de la chaudière
    numero = num
    Text_sms=str(etat_chaudiere)
    Envoyer_sms(Text_sms,numero)

##################################################################
#Allumage en mode manuel
def sms_allumage(num):
    #ecriture sur la db manu =1
    variable_input = "mode_manu"
    variable_etat = 2
    update_db(variable_input, variable_etat)
    #ecriture de la duree sur la base
    variable_input = "tempo_manu"
    variable_etat = 1
    update_db(variable_input, variable_etat)

    #envoie sms confirmation
    numero = num
    Text_sms="Allumage en cours, une confirmation sera envoyee"
    Envoyer_sms(Text_sms,numero)
    time.sleep(8)
    #confirmation état chaudiere
    sms_etat(num)
    time.sleep(5)

##################################################################
#Eteindre en mode manuel
def sms_coupure(num):
    #ecriture sur la db manu =0
    variable_input = "mode_manu"
    variable_etat = 0
    update_db(variable_input, variable_etat)
    #mise a 0 du compteur manu
    variable_input = "tempo_manu"
    variable_etat = 0
    update_db(variable_input, variable_etat)
    #envoie sms confirmation
    numero = num
    Text_sms="Coupure en cours, une confirmation sera envoyee"
    Envoyer_sms(Text_sms,numero)
    time.sleep(8)
    #confirmation état chaudiere
    sms_etat(num)
    time.sleep(5)

###################################################################
#fonction Envoyer un sms
def Envoyer_sms(Text_sms,numero):
    time.sleep(1)
    text =('AT+CMGF=1'+"\r\n").encode('utf-8')
    ser.write(text)
    time.sleep(0.1)
    text =('AT+CMGS=\"'+ numero + '\"'+"\r\n").encode('utf-8')
    ser.write(text)
    time.sleep(0.1)
    text =(Text_sms+"\r\n").encode('utf-8')
    ser.write(text)
    time.sleep(0.1)
    text =(chr(26)+"\r\n").encode('utf-8')
    ser.write(text)
    pass


###################################################################
#lecture des sms recus
def read():
    text =('AT+CMGL=\"REC UNREAD\"'+"\r\n").encode('utf-8')
    ser.write(text)
    time.sleep(0.5)
    reply = ser.read(ser.inWaiting())
    #détermination nombre charactere
    nombre_char = len(reply)
    #affichage uniquement si nouveau message
    if nombre_char>115:
        #Affichage du numero
        numero=reply[81:93]
        numero = numero.decode('utf-8')
        num=numero
        print("le numero : " +numero)
        #Affichage du message uniquement
        fin_chaine =int(nombre_char)-8
        sms_fin = (reply[122:fin_chaine])
        sms_fin = sms_fin.decode('utf-8')
        print(sms_fin)

        #traitement du sms_fin
        #affichage de l'aide
        if sms_fin == ("Help"):
            print("help identifie")
            Text_sms = "Commandes :\n- Etat chaudiere : Etat \n- Demarrer chaudiere : Demarre \n- Eteindre chaudiere : Eteindre \n- Temperature exterieur : Tempext\n- Temperature interieur : Tempint"
            Envoyer_sms(Text_sms,numero)
        #affichage etat chaudière
        elif sms_fin == ("Etat"):
            sms_etat(num)
        #affichage temp interieur
        elif sms_fin ==("Tempint"):
            sms_tempext(num)
        elif sms_fin ==("Tempext"):
            sms_tempext(num)
        elif sms_fin ==("Demarre"):
            sms_allumage(num)
            time.sleep(5)
        elif sms_fin ==("Eteindre"):
            sms_coupure(num)
            time.sleep(5)
        '''else:
            Text_sms = "Je n'ai pas compris ta commande :(\n \nHelp pour obtenir les commandes\n \nToujours attendre la reception d'un sms avant d'envoyer une nouvelle commande !"
            Envoyer_sms(Text_sms,numero)
            nombre_char =0'''

    else:
        sms_fin=""
    #effacer sms
    text =('AT+CMGD=1,4'+"\r\n").encode('utf-8')
    ser.write(text)




###################################################################
#programme main
def start_server_gsm():
    global ser
    print("Démarrage du serveur GSM")
    #définition du port serie
    ser = serial.Serial("com3",115200)
    text =('AT'+"\r\n").encode('utf-8')
    ser.write(text)

    #Text à envoyer
    Text_sms = "Bonjour serveur GSM demarre \nEnvoyer Help pour les commandes"
    numero = "+33643779286"
    Envoyer_sms(Text_sms,numero)
    #pause avant 2eme sms
    time.sleep(5)
    numero = "+33631253131"
    Envoyer_sms(Text_sms,numero)

    #lancement de la boucle
    while 1:
        read()
        time.sleep(3)

    #Text à envoyer
    Text_sms = "Bonjour serveur GSM ferme"
    numero = "+33643779286"
    #Envoyer_sms(Text_sms,numero)

    ser.close()
    print("Fermeture du serveur")
    time.sleep(2)

#######################################################################
def serveur_gsm():
    t123 = threading.Thread(target=start_server_gsm)
    t123.start()




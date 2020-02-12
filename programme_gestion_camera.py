#!/usr/bin/env /usr/bin/python
#!/usr/bin/python

#pip install rtsp
# pip install opencv-contrib-python
import cv2
import os
import time
import threading
import shutil
from programme_outil_db import*


###################################################################################
def garage_vision():
    cap0 = cv2.VideoCapture("rtsp://admin:julien00@192.168.1.111:554/ch1-s1?tcp")
    #verification ouverture cam
    if (cap0.isOpened() == True):
        print("connexion ouverte cam garage")
        
    #taille image
    frame_width = int(cap0.get(3))
    frame_height = int(cap0.get(4))

    while(cap0.isOpened()):
        ret0, frame = cap0.read()
        if ret0==True:
            #affichage video
            cv2.imshow('Camera Garage',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
     
    # Release everything if job is finished
    cap0.release()
    cv2.destroyAllWindows()

###################################################################################
def interieur_vision():
    print("test ouverture")
    cap2 = cv2.VideoCapture("rtsp://admin@192.168.1.10:554//Streaming/Channels/1?tcp")
    #verification ouverture cam
    if (cap2.isOpened() == True):
        print("connexion ouverte cam interieur")
        
    #taille image
    frame_width = int(cap2.get(3))
    frame_height = int(cap2.get(4))

    while(cap2.isOpened()):
        ret2, frame = cap2.read()
        if ret2==True:
            #affichage video
            cv2.imshow('Camera Interieur',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
     
    # Release everything if job is finished
    cap2.release()
    cv2.destroyAllWindows()
    
###################################################################################
def garage_save():
    i=1

    #boucle de sauvegarde video
    while (i==1):
        #pause pour changement d'heure
        time.sleep(1)
        maintenant = datetime.now()
        jour=str(maintenant.day)
        mois=str(maintenant.month)
        annee=str(maintenant.year)
        heure=str(maintenant.hour)
        date=str(annee+"_"+mois+"_"+jour)
        #nom du fichier
        nom_video='Garage_'+date+"_h"+heure+'.avi'
        #adresse de connection 
        vcap = cv2.VideoCapture("rtsp://admin:julien00@192.168.1.111:554/ch1-s1?tcp")
        #verification ouverture cam
        if (vcap.isOpened() == True):
            print("Sauvegarde de la caméra garage")
            
        #taille image
        frame_width = int(vcap.get(3))
        frame_height = int(vcap.get(4))

        #sauvegarde
        out = cv2.VideoWriter(nom_video,cv2.VideoWriter_fourcc('M','J','P','G'), 3, (frame_width,frame_height))

        while(vcap.isOpened()):
            #récupération heure pour video
            maintenant = datetime.now()
            tpshm = maintenant.minute
            tpshs = maintenant.second
            tpshs=int(tpshs)
            tpshm=int(tpshm)
        
            ret, frame = vcap.read()
            if ret==True:
                # sauvegarde video
                out.write(frame)
                if (tpshm == 59 and tpshs ==59) :
                   break
            else:
                print("Camera garage erreur récupération image");
                vcap.release()
                vcap = cv2.VideoCapture("rtsp://admin:julien00@192.168.1.111:554/ch1-s1?tcp")
                
         
        # Release everything if job is finished
        vcap.release()
        out.release()
        #Deplacement de la video
        shutil.move("C:/Users/home/Desktop/Programme_Domotic_v1/"+nom_video,"D:/"+nom_video)
        
        
###################################################################################
def interieur_save():
    i=1

    #boucle de sauvegarde video
    while (i==1):
        #pause pour changement d'heure
        time.sleep(1)
        maintenant = datetime.now()
        jour=str(maintenant.day)
        mois=str(maintenant.month)
        annee=str(maintenant.year)
        heure=str(maintenant.hour)
        date=str(annee+"_"+mois+"_"+jour)
        #nom du fichier
        nom_video='Interieur_'+date+"_h"+heure+'.avi'
        #adresse de connection
        print("truc1")
        videocap = cv2.VideoCapture("rtsp://admin:julien00@192.168.1.112:554/ch1-s1?tcp")
        print("truc")
        #verification ouverture cam
        if (videocap.isOpened() == True):
            print("Sauvegarde de la caméra interieur")
            
        #taille image
        frame_width = int(videocap.get(3))
        frame_height = int(videocap.get(4))

        #sauvegarde
        out = cv2.VideoWriter(nom_video,cv2.VideoWriter_fourcc('M','J','P','G'), 3, (frame_width,frame_height))

        while(videocap.isOpened()):
            #récupération heure pour video
            maintenant = datetime.now()
            tpshm = maintenant.minute
            tpshs = maintenant.second
            tpshs=int(tpshs)
            tpshm=int(tpshm)
        
            ret, frame = vcap.read()
            if ret==True:
                # sauvegarde video
                out.write(frame)
                if (tpshm == 59 and tpshs ==59) :
                   break
            else:
                print("Camera interieur erreur récupération image");
                videocap.release()
                videocap = cv2.VideoCapture("rtsp://admin:julien00@192.168.1.112:554/ch1-s1?tcp")
                
         
        # Release everything if job is finished
        videocap.release()
        out.release()
        #Deplacement de la video
        shutil.move("C:/Users/home/Desktop/Programme_Domotic_v1/"+nom_video,"D:/"+nom_video)
        
 



#################################################################
# Démarrage des programmes depuis l'interface
def cam_garage_vision():
    t1 = threading.Thread(target=garage_vision)
    t1.start()
def cam_garage_save():
    t2 = threading.Thread(target=garage_save)
    t2.start()
    #i=0
def cam_interieur_save():
    t3 = threading.Thread(target=interieur_save)
    t3.start()
def cam_interieur_vision():
    t4 = threading.Thread(target=interieur_vision)
    t4.start()


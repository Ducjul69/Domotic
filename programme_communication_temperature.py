#!/usr/bin/env /usr/bin/python
import socket
import os
from programme_outil_db import*
import threading
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SHUT_WR, SO_REUSEADDR



class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket

    def run(self): 
   
        print("Connexion de %s %s" % (self.ip, self.port, ))

        response = self.clientsocket.recv(2048)
        response = response.decode("utf-8")
        print(response)
        #cas de la reception temp ext
        if response[0:7]=="tempext":
                response = (response[7:len(response)])
                #verification temp
                if int(response) < -30 or int(response) > 70:
                    response = "--"
                #sauvegarde sur base de donnée
                variable_input = "temperature_exterieur"
                variable_etat = response
                update_db(variable_input, variable_etat)
        if response[0:6]=="humext":
                response = (response[6:len(response)])
                if int(response) < 0 or int(response) > 100:
                    response = "--"
                #sauvegarde sur base de donnée
                variable_input = "hygrometrie_exterieur"
                variable_etat = response
                update_db(variable_input, variable_etat)
        print("Client déconnecté...")



############################################
def communication_esp_temperature():
        tcpsock = socket(AF_INET, SOCK_STREAM)
        tcpsock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        tcpsock.bind(("",8765))

        while True:
                tcpsock.listen(10)
                print( "En écoute...")
                (clientsocket, (ip, port)) = tcpsock.accept()
                newthread = ClientThread(ip, port, clientsocket)
                newthread.start()

############################################
def com_esp_temperature():
    time.sleep(5)
    #demarrage du thread
    t1= threading.Thread(target=communication_esp_temperature)
    t1.start()
############################################

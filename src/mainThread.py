#! /usr/bin/python
# -*- coding: utf-8 -*-

from random import *
import sys
from threading import Thread
import time
from math import *

from request import *
import main

class MainThread(Thread):
    
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while 1:
            if len(main.clients) != 0:
#                sys.stdout.write("[Clients non vide]\n")
            
                for id, client in main.clients.items():
#                    sys.stdout.write("(" + str(client.request_type) + ")n")
#                    sys.stdout.flush()
                    if client.request_type == 0: # Le client vient d'arriver
                        requete = Request(id, 1)
                        main.requetes.append(requete)
                        client.request_type = 0.5
                    elif client.request_type == 0.5:
                        break
                    elif client.request_type == 1: # La requête de type 1 est terminée
                        requete = Request(id, 2)
                        main.requetes.append(requete)
                        client.request_type = 1.5
                    elif client.request_type == 1.5:
                        break
                    elif client.request_type == 2: # Le client a fini et part
                        del main.clients[id]
                        sys.stdout.write("Client " + str(id) + " terminé  !!\n")
                        sys.stdout.flush()
                    else: # Ne doit jamais arriver
                        sys.stdout.write("ERROR de request_type !!\n")
                        sys.stdout.flush()
            else:
#                sys.stdout.write("[Clients vide]\n")
#                sys.stdout.flush()
                i += 1
            
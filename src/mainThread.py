#! /usr/bin/python
# -*- coding: utf-8 -*-

import main
from math import *
from random import *
from request import *
import sys
from threading import RLock
from threading import Thread

verrou = RLock()

class MainThread(Thread):
    
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        while 1:
#            sys.stdout.write("\t\t{TOUR}\n")
#            sys.stdout.flush()           
#            with verrou:
            for id, client in main.clients.items():
                if client.request_type == 0: # Le client vient d'arriver
                    requete = Request(id, 1)
                    main.requetes.append(requete)
                    client.request_type = 0.5
                elif client.request_type == 0.5:
                    continue
                elif client.request_type == 1: # La requête de type 1 est terminée
                    requete = Request(id, 2)
                    main.requetes.append(requete)
                    client.request_type = 1.5
                elif client.request_type == 1.5:
                    continue
                elif client.request_type == 2: # Le client a fini et part
                    with verrou:
                        del main.clients[id]
                        sys.stdout.write("\t\tClient " + str(id) + " terminé  !!\n")
                        sys.stdout.flush()
                else: # Ne doit jamais arriver
                    sys.stdout.write("ERROR de request_type !!\n")
                    sys.stdout.flush()
            
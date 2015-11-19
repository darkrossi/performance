#! /usr/bin/python
# -*- coding: utf-8 -*-

import main
from math import *
from random import *
import sys
from threading import RLock
from threading import Thread
import time

verrou = RLock()

class ServerTreatmentThread(Thread):
    
    # Paramètre p pour la distribution exponentielle
    # Paramètres uMin et uMax qui sont les min et max de la distribution uniforme

    def __init__(self, p, uMin, uMax):
        Thread.__init__(self)
        self.p = p
        self.uMin = uMin
        self.uMax = uMax

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while 1:
            if len(main.requetes) != 0:
                requete = main.requetes.pop(0)
                if requete.type == 1:
                    attente = self.treatment1()
                elif requete.type == 2:
                    attente = self.treatment2()
                else:
                    sys.stdout.write("Problème de type")
                    sys.stdout.flush()
                    continue
                    
                with verrou:
                    sys.stdout.write("\tSTART (type." + str(requete.type) + ", id." + str(requete.id_client) + ", " + str(attente) + "ms)...\n")
                    sys.stdout.flush()
                    
                attente = ((attente + 6) / 1000) * main.fact_time_treat # +6 pour le RTT/2
                time.sleep(attente)
                
                with verrou:
                    main.clients[requete.id_client].request_type = requete.type 
                    sys.stdout.write("\tEND (type." + str(requete.type) + ", id." + str(requete.id_client) + ")...\n")
                    sys.stdout.flush()

            
    def treatment1(self): # Loi uniforme
        return randint(self.uMin, self.uMax)
    
    def treatment2(self): # Loi exponentielle de paramètre p
        return expovariate(self.p)
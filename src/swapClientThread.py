#! /usr/bin/python
# -*- coding: utf-8 -*-

from client import *
import main
from random import *
import sys
from threading import RLock
from threading import Thread
import time

verrou = RLock()

class SwapClientThread(Thread):

    # Paramètre l (lambda) de la distribution de Poisson
    # Paramètre id_courant

    def __init__(self, l, nb_client):
        Thread.__init__(self)
        self.l = l
        self.id_courant = 0
        self.nb_client = nb_client

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        while 1 and self.id_courant < self.nb_client:
            attente = self.poisson()
            attente_2 = attente
            attente = (attente / 1000) * main.fact_time_swap
            time.sleep(attente)
            
            client = Client()
            with verrou:
                main.clients[self.id_courant] = client
                sys.stdout.write("[SWAP_CLIENT (t." + str(attente_2) + "ms, id." + str(self.id_courant) + ")]\n")
                sys.stdout.flush()
            
            self.id_courant += 1
            
    def poisson(self):
        t = 1.0 / expovariate(self.l)
        return int(t)
        
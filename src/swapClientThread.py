#! /usr/bin/python
# -*- coding: utf-8 -*-

from random import *
import sys
from threading import Thread
import time
from client import *

import main

class SwapClientThread(Thread):

    # Paramètre l (lambda) de la distribution de Poisson
    # Paramètre id_courant

    def __init__(self, l):
        Thread.__init__(self)
        self.l = l
        self.id_courant = 0

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        i = 0
        while 1 and self.id_courant < 2:
            attente = self.poisson()
            attente = attente/1000
            time.sleep(attente)
            
#            sys.stdout.write("[Un client vient de swapper (avec lambda = " + str(attente) + " et id_courant = " + str(self.id_courant) + ")]\n")
#            sys.stdout.flush()
            
            client = Client()
            main.clients[self.id_courant] = client
            self.id_courant += 1
            i += 1
            
    def poisson(self):
        t=1.0/expovariate(self.l)
        return int(t)
        
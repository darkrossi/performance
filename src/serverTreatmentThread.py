#! /usr/bin/python
# -*- coding: utf-8 -*-

import random
import sys
from threading import Thread
import time

class ServerTreatmentThread(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
#        i = 0
#        while i < 20:
#            sys.stdout.write(self.lettre)
#            sys.stdout.flush()
#            attente = 0.2
#            attente += random.randint(1, 60) / 100
#            time.sleep(attente)
#            i += 1
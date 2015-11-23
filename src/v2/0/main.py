#! /usr/bin/python
# -*- coding: utf-8 -*-

from Queue import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from random import *

__author__ = "oswald"
__date__ = "$23 nov. 2015 14:17:49$"

if __name__ == "__main__":

    def uniforme(uMin, uMax): # Loi uniforme
        return randint(uMin, uMax)
    
    def exponentiel(p): # Loi exponentielle de paramètre p
        return int(expovariate(p))
    
    def poisson(l):
        return int(np.random.poisson(l))
    
    def simul_server(param_lambda, time_out):
        
        #initialization
        q = PriorityQueue()
        q.put((10, 'arrival'))
        state = 0

        # param_lambda = 15 # 24 = stable ?, 25 = stable
        param_expon = 0.1

        block_time = 0
        rtt_2 = 6
        current_time = 0

        axe_x = []
        axe_y = []

        #simulation
        while not q.empty() and current_time < time_out:
            event = q.get()
            current_time = event[0]
            axe_x.append(current_time)
            axe_y.append(state)

            if (event[1] == 'arrival'): # Si le client vient d'arriver on l'envoie au serveur
                state += 1
                q.put ((current_time + poisson(param_lambda), 'arrival')) # On envoie un autre client
                q.put ((current_time + rtt_2, 'type1_sent')) # On envoie une requête de type 1 au serveur

            elif(event[1] == 'type1_sent'): # Si une requête de type 1 arrive au serveur
                if(block_time > current_time):
                    q.put ((current_time + 1, 'type1_sent')) # On envoie une requête de type 1 au serveur
                else:
                    t = current_time + uniforme(0, 30)
                    q.put ((t, 'type1_treatment')) # On traite la requête de type 1
                    block_time = t

            elif(event[1] == 'type1_treatment'): # Si une requête de type 1 a été traitée par le serveur
                q.put ((current_time + rtt_2, 'type1_answer')) # On envoie la réponse au client

            elif(event[1] == 'type1_answer'): # Si la réponse d'une requête de type 1 a été reçueée par le client
                q.put ((current_time + rtt_2, 'type2_sent')) # On envoie une requête de type 2 au serveur

            elif(event[1] == 'type2_sent'): # Si la réponse d'une requête de type 1 a été reçueée par le client
                if(block_time > current_time):
                    q.put ((current_time + 1, 'type2_sent')) # On envoie une requête de type 1 au serveur
                else:
                    t = current_time + exponentiel(param_expon)
                    q.put ((t, 'type2_treatment')) # On traite la requête de type 1
                    block_time = t

            elif(event[1] == 'type2_treatment'): # Si la réponse d'une requête de type 1 a été reçueée par le client
                q.put ((current_time + rtt_2, 'departure')) # On envoie une requête de type 2 au serveur

            elif(event[1] == 'departure'):
                state -= 1
            # print (event, state)
            
        return (axe_x, axe_y)
        
        
    time_out = 2000
    simul1 = simul_server(15, time_out)
    simul2 = simul_server(23, time_out)
    simul3 = simul_server(50, time_out)
    
    plt.plot(simul1[0], simul1[1], 'r--', simul2[0], simul2[1], 'bs', simul3[0], simul3[1], 'g^')
    plt.show() # affiche la figure a l'ecran
    
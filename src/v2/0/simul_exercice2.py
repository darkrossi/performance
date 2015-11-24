#! /usr/bin/python
# -*- coding: utf-8 -*-

from main import *

def simul_server(param_lambda, time_out, a, m):
        
    #initialization
    last_id = 0
        
    q = PriorityQueue()
    q.put((10, 'arrival', last_id))
        
    dico_client = {}
    dico_client[last_id] = (10, 0)
        
    state = 0

    # param_lambda = 15 # 24 = stable ?, 25 = stable

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
            
        id = event[2]

        if (event[1] == 'arrival'): # Si le client vient d'arriver on l'envoie au serveur
            state += 1
            last_id += 1
            dico_client[id] = (current_time, 0)
            q.put ((current_time + poisson(param_lambda), 'arrival', last_id)) # On envoie un autre client
            q.put ((current_time + rtt_2, 'type1_sent', id)) # On envoie une requête de type 1 au serveur

        elif(event[1] == 'type1_sent'): # Si une requête de type 1 arrive au serveur
            if(block_time > current_time):
                q.put ((current_time + 1, 'type1_sent', id)) # On envoie une requête de type 1 au serveur
            else:
                t = current_time + uniforme(0, 30)
                q.put ((t, 'type1_treatment', id)) # On traite la requête de type 1
                block_time = t

        elif(event[1] == 'type1_treatment'): # Si une requête de type 1 a été traitée par le serveur
            q.put ((current_time + rtt_2, 'type1_answer', id)) # On envoie la réponse au client

        elif(event[1] == 'type1_answer'): # Si la réponse d'une requête de type 1 a été reçueée par le client
            q.put ((current_time + rtt_2, 'type2_sent', id)) # On envoie une requête de type 2 au serveur

        elif(event[1] == 'type2_sent'): # Si la réponse d'une requête de type 1 a été reçueée par le client
            if(block_time > current_time):
                q.put ((current_time + 1, 'type2_sent', id)) # On envoie une requête de type 1 au serveur
            else:
                t = current_time + pareto(a, m)
                q.put ((t, 'type2_treatment', id)) # On traite la requête de type 1
                block_time = t

        elif(event[1] == 'type2_treatment'): # Si la réponse d'une requête de type 1 a été reçueée par le client
            q.put ((current_time + rtt_2, 'departure', id)) # On envoie une requête de type 2 au serveur

        elif(event[1] == 'departure'):
            state -= 1
            dico_client[id] = (current_time - dico_client[id][0], 1)
            # print "\t id = " + str(id) + " : " + str(dico_client[id])
        # print (event, state)
            
    return (axe_x, axe_y, dico_client)
    
def do(param_lambda1, param_lambda2, param_lambda3, time_out, a, m):
    
    # simu pour 2000 : 
        # lambda = 15 -> 
        # lambda = 23 -> 
        # lambda = 50 -> 
    # simu pour 20000 : 
        # lambda = 15 -> 1018ms
        # lambda = 23 -> 765ms
        # lambda = 50 -> 51ms
    
    simul = []
    simul.append(simul_server(param_lambda1, time_out, a, m))
    simul.append(simul_server(param_lambda2, time_out, a, m))
    simul.append(simul_server(param_lambda3, time_out, a, m))
    #    simul.append(simul_server(27, time_out))
    #    simul.append(simul_server(28, time_out))
    
    for i in range(0, len(simul)):
        simul_var = simul[i]
        temp_sum_time = 0
        j = 0
        for valeur in simul_var[2].values():
            if valeur[1] == 1:
                j += 1
                temp_sum_time += valeur[0]
                # print "\t " + str(valeur[0])
        average_time = temp_sum_time / j
        print "Le temps moyen pour la simu n°" + str(i) + " est de " + str(average_time) + "ms. (j = " + str(j) + ")"
    
    plt.plot(simul[0][0], simul[0][1], 'r--', simul[1][0], simul[1][1], 'bs', simul[2][0], simul[2][1], 'g^')
    plt.show() # affiche la figure a l'ecran
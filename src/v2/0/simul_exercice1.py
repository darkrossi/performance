#! /usr/bin/python
# -*- coding: utf-8 -*-

from main import *

def simul_server(param_lambda, time_out, param_expon):

    #initialization
    last_id = 0

    q = PriorityQueue()
    q.put((10, ('arrival', last_id)))

    dico_client = {}
    dico_client[last_id] = 10

    liste_temps_execution = []

    state = 0

    block_time = 0
    rtt_2 = 6
    current_time = 0

    axe_x = []
    axe_y = []

    #simulation
    while current_time < time_out:
        event = q.get()
        current_time = event[0]
        axe_x.append(current_time)
        axe_y.append(state)

        id = event[1][1]

        if (event[1][0] == 'arrival'): # Si le client vient d'arriver on l'envoie au serveur
            state += 1
            last_id += 1
            dico_client[id] = current_time
            q.put ((current_time + poisson(param_lambda), ('arrival', last_id))) # On envoie un autre client
            q.put ((current_time + rtt_2, ('type1', id))) # On envoie une requête de type 1 au serveur

        elif(event[1][0] == 'type1'): # Si une requête de type 1 arrive au serveur
            if(block_time > current_time):
                q.put ((current_time + 1, ('type1', id))) # On envoie une requête de type 1 au serveur
            else:
                t = current_time + uniforme(0, 30)
                q.put ((t + 2 * rtt_2, ('type2', id))) # On traite la requête de type 1
                block_time = t

        elif(event[1][0] == 'type2'): # Si la réponse d'une requête de type 1 a été reçueée par le client
            if(block_time > current_time):
                q.put ((current_time + 1, ('type2', id))) # On envoie une requête de type 2 au serveur
            else:
                t = current_time + exponentiel(param_expon)
                q.put ((t + rtt_2, ('departure', id))) # On traite la requête de type 2
                block_time = t

        elif(event[1][0] == 'departure'):
            state -= 1
            liste_temps_execution.append(current_time - dico_client[id])

    return (axe_x, axe_y, liste_temps_execution)

def do(param_lambda1, param_lambda2, param_lambda3, time_out, param_expon, nb_sigma_precision):

    list_param_lambda = [param_lambda1, param_lambda2, param_lambda3]

    simul = []
    simul.append(simul_server(param_lambda1, time_out, param_expon))
    if param_lambda2 != -1:
        simul.append(simul_server(param_lambda2, time_out, param_expon))
    else:
        simul.append([[], [], {}])
    if param_lambda3 != -1:
        simul.append(simul_server(param_lambda3, time_out, param_expon))
    else:
        simul.append([[], [], {}])

    for i in range(0, len(simul)):
        simul_var = simul[i]
        if len(simul_var[0]) != 0:
            temp_sum_time = 0
            for valeur in simul_var[2]:
                temp_sum_time += valeur
            mediane_var = mediane(simul_var[2])
            average_time = temp_sum_time / len(simul_var[2])
            ecart_type_var = ecart_type(simul_var[2], average_time)

            intervalle_de_confiance_mediane_var = intervalle_de_confiance_mediane(nb_sigma_precision, simul_var[2])
            xj_mediane = intervalle_de_confiance_mediane_var[0]
            xk_mediane = intervalle_de_confiance_mediane_var[1]
            intervalle_de_confiance_moyenne_var = intervalle_de_confiance_moyenne(nb_sigma_precision, ecart_type_var, len(simul_var[2]), average_time)
            xj_moyenne = intervalle_de_confiance_moyenne_var[0]
            xk_moyenne = intervalle_de_confiance_moyenne_var[1]

            print "Le temps moyen pour lambda = " + str(list_param_lambda[i]) + " est de {0:.1f}ms et la médiane est {1:.1f}.".format(average_time, mediane_var)
            print("\t L'intervalle de confiance de la moyenne vaut [{0:.1f}, {1:.1f}].".format(xj_moyenne, xk_moyenne))
            print("\t L'intervalle de confiance de la mediane vaut [{0:.1f}, {1:.1f}].".format(xj_mediane, xk_mediane))

    plt.plot(simul[0][0], simul[0][1], 'r--', label="$\lambda = %d$" % param_lambda1)
    if(len(simul[1][0]) != 0):
        plt.plot(simul[1][0], simul[1][1], 'bs', label="$\lambda = %d$" % param_lambda2)
    if(len(simul[2][0]) != 0):
        plt.plot(simul[2][0], simul[2][1], 'g^', label="$\lambda = %d$" % param_lambda3)
    plt.xlabel(u"Date (en ms)")
    plt.ylabel(u"Nombre de clients dans le systeme")
    plt.legend(shadow=True, fancybox=True)  
    plt.show() # affiche la figure a l'ecran

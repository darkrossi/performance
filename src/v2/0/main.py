#! /usr/bin/python
# -*- coding: utf-8 -*-

from Queue import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from random import *

dico_sigma = {}
dico_sigma[1] = (1, 68) # (Nombre de sigma de différence, pourcentage de précision associé)
dico_sigma[2] = (1.96, 95)
dico_sigma[3] = (3, 99.7)

def uniforme(uMin, uMax): # Loi uniforme
    return randint(uMin, uMax)

def exponentiel(p): # Loi exponentielle de paramètre p
    return int(expovariate(p))

def poisson(l):
    return int(np.random.poisson(l))

def pareto(a, m):
    return (np.random.pareto(a) + 1) * m

def ecart_type(echantillon, moyenne):
    sum_temp = 0
    for valeur in echantillon:
        sum_temp += (valeur - moyenne) ** 2
    sum_temp = sum_temp / len(echantillon)
    return sqrt(sum_temp)

def mediane(list):
    new_list = sorted(list)
    return new_list[int(len(new_list) / 2)]

def intervalle_de_confiance_moyenne(nb_sigma_precision, ecart_type, taille):
    return dico_sigma[nb_sigma_precision][0] * ecart_type / sqrt(taille)

def intervalle_de_confiance_mediane(nb_sigma_precision, taille):
    return dico_sigma[nb_sigma_precision][0] * sqrt(taille) / 2

if __name__ == "__main__":

    import simul_exercice1 as s1
    import moyenne_pareto as mp
    import simul_exercice2 as s2


    # initialisation des générateurs de nombres aléatoires
    seed(1)
    np.random.seed(1)

    s1.do(40, 60, -1, 80000, 0.1, 1)
#    mp.do(1.25, 2)
#    s2.do(40, 60, -1, 80000, 1.25, 2, 1)

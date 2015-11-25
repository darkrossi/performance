#! /usr/bin/python
# -*- coding: utf-8 -*-

from Queue import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from random import *

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
        sum_temp += (valeur - moyenne)**2
    sum_temp = sum_temp/len(echantillon)
    return sqrt(sum_temp)

def mediane(list):
    new_list = sorted(list)
    return new_list[int(len(new_list)/2)]

def intervalle_de_confiance(ecart_type, taille):
    return ecart_type/sqrt(taille)

if __name__ == "__main__":
        
    import simul_exercice1 as s1
    import moyenne_pareto as mp
    import simul_exercice2 as s2
    
    
    s1.do(23, 24, 25, 50000, 0.1)
#! /usr/bin/python
# -*- coding: utf-8 -*-

from Queue import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from random import *

def uniforme(uMin, uMax): # Loi uniforme
    return randint(uMin, uMax)

def ecart_type_uniforme(uMin, uMax):
    return (uMax-uMin)/sqrt(12)
    
def exponentiel(p): # Loi exponentielle de paramètre p
    return int(expovariate(p))

def ecart_type_exponentiel(p):
    return 1/p

def poisson(l):
    return int(np.random.poisson(l))

def ecart_type_poisson(l):
    return sqrt(l)

def pareto(a, m):
    return (np.random.pareto(a) + 1) * m

def ecart_type_pareto(a, m):
    return (m/(a-1))*sqrt(a/(a-2))

def mediane(list):
    new_list = sorted(list)
    return new_list[int(len(new_list)/2)]

def intervalle_de_confiance(moyenne, ecart_type, taille): # intervalle de confiance à 95%
    return (moyenne - 1.96*ecart_type/sqrt(taille), moyenne + 1.96*ecart_type/sqrt(taille))

if __name__ == "__main__":
    
    import simul_exercice1 as s1
    import moyenne_pareto as mp
    import simul_exercice2 as s2
    
    
    s1.do(50, 60, 70, 40000, 0.1)
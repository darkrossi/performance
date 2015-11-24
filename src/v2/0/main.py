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

def mediane(list):
    new_list = sorted(list)
    return new_list[int(len(new_list)/2)]

if __name__ == "__main__":
    
    import simul_exercice1 as s1
    import moyenne_pareto as mp
    import simul_exercice2 as s2
    
    
    s1.do(50, 60, 70, 40000, 0.1)
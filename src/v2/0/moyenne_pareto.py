#! /usr/bin/python
# -*- coding: utf-8 -*-

from main import *

def moyenne_pareto_f(size_echantillon, a, m):
    n = 0
    for i in range(0, size_echantillon):
        n += pareto(a, m)
    return n/size_echantillon

def do(a, m):
    size_echantillon = [100, 1000, 1000000]
    for valeur in size_echantillon:
        moyenne_pareto = moyenne_pareto_f(valeur, a, m)
        print "La moyenne de pareto pour une taille de " + str(valeur) +" est : " + str(moyenne_pareto)
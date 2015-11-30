#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import simul_exercice1 as s1
import simul_exercice2 as s2
from random import *
import numpy as np

if __name__ == "__main__":

    seed(1)
    np.random.seed(1)

    if len(sys.argv) != 0:

        num_graph = int(sys.argv[1])
        if num_graph == 1: # Exercice 1, 3.1
            s1.do(24, 25, 26, 80000, 0.1, 1)
        elif num_graph == 2: # Exercice 1, 3.2
            s1.do(20, 30, -1, 10000, 0.1, 1)
        elif num_graph == 3: # Exercice 2, 2.1
            s2.do(24, 25, 26, 40000, 1.25, 2, 1)
        elif num_graph == 4: # Exercice 2, 2.2
            s2.do(20, 30, -1, 40000, 1.25, 2, 1)
            print "out"
        elif num_graph == 5:
            print "out"
        elif num_graph == 6:
            print "out"
        else:
            print "out"

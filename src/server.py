#! /usr/bin/python
# -*- coding: utf-8 -*-

class Server:
    """Classe définissant une personne caractérisée par :
    - son clock ;"""

    def __init__(self):
        """Constructeur de notre classe"""
        self._clock = 0;
        
    def _get_clock(self):        
        print("On accède à l'attribut lieu_residence !")
        return self._clock
    
    def _set_clock(self, time):        
        print("On accède à l'attribut lieu_residence !")
        self._clock = self._clock + time
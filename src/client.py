#! /usr/bin/python
# -*- coding: utf-8 -*-

class Client:
    """Classe définissant une personne caractérisée par :
    - son id ;
    - son request_type 0 si non, 1 pour type 1 et 2 pour type 2"""

    def __init__(self):
        """Constructeur de notre classe"""
        self.request_type = 0;

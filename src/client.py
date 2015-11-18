#! /usr/bin/python
# -*- coding: utf-8 -*-

class Client:
    """Classe définissant une personne caractérisée par :
    - son id ;
    - son request_type 0 si non, 1 pour type 1 et 2 pour type 2"""

    def __init__(self, id):
        """Constructeur de notre classe"""
        self.__id = id;
        self.__requesy_type = 0;
        
    def _get_id(self):
        """Méthode qui sera appelée quand on souhaitera accéder en lecture à l'attribut 'lieu_residence'"""
        
        print("On accède à l'attribut lieu_residence !")
        return self.__id
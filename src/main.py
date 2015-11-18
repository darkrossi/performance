#! /usr/bin/python
# -*- coding: utf-8 -*-

clients = {}
requetes = []

if __name__ == "__main__":

    from client import *
    from server import *
    from request import *
    from swapClientThread import *
    from serverTreatmentThread import *
    from mainThread import *

    # Création des threads
    thread_main = MainThread()
    thread_swap_client = SwapClientThread(0.1)
    thread_server = ServerTreatmentThread(0.1, 0, 30)

    # Lancement des threads
    thread_server.start()
    thread_swap_client.start()
    thread_main.start()

    # Attend que les threads se terminent
    thread_swap_client.join()
    thread_server.join()
    thread_main.join()
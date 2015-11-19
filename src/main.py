#! /usr/bin/python
# -*- coding: utf-8 -*-

clients = {}
requetes = []

fact_time = 1
fact_time_swap = fact_time
fact_time_treat = fact_time
nb_clients = 100

if __name__ == "__main__":

    from client import *
    from server import *
    from request import *
    from swapClientThread import *
    from serverTreatmentThread import *
    from mainThread import *

    # Création des threads
    thread_main = MainThread()
    thread_swap_client = SwapClientThread(10, nb_clients)
    thread_server = ServerTreatmentThread(0.1, 0, 30)

    # Lancement des threads
    thread_main.start()
    thread_server.start()
    thread_swap_client.start()

    # Attend que les threads se terminent
    thread_swap_client.join()
    thread_server.join()
    thread_main.join()
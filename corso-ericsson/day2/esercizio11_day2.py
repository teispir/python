'''
Scrivere del codice in Python per chiedere all’utente di inserire una base b e un
esponente e per poi calcolare be. Il calcolo del risultato deve essere eseguito
tramite la corrispondente funzione della libreria math.
'''
import math
base = int(input("Inserire base:"))
esponente = int(input("Inserire esponente:"))

risultatoPotenza = pow(base, esponente)
print("Potenza:", risultatoPotenza)
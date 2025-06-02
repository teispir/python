'''
Si scriva un programma Python che genera una lista di lunghezza 100 contenente
numeri interi casuali compresi tra 1 e 100 e la stampa a schermo.
'''
import random

listaRandom = [random.randint(1, 100) for i in range(100)]
print(listaRandom)
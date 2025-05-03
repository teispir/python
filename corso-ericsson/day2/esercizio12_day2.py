'''
Scrivere del codice in Python per calcolare la radice quadrata di un numero intero
e > 0 inserito da tastiera.

Esempio:

>>> Inserire un numero intero (> 0): 25
>>> Radice quadrata di 25: 5.0
'''
import math

def calcola_radice_quadrata(a):
    return math.sqrt(a)

numero = int(input("Inserire numero intero > 0:"))
print("Radice quadrata del numero inserito:", calcola_radice_quadrata(numero))
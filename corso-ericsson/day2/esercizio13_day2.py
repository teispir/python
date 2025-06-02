'''
Modificare il codice soluzione dell’esercizio precedente per gestire situazioni in
cui numero inserito da tastiera non sia intero e > 0.
'''
import math

def calcola_radice_quadrata(a):
    return math.sqrt(a)

numero = int(input("Inserire numero intero > 0:"))

print("type(numero):",type(numero))
# verificare che il numero inserito sia intero

if numero < 0:
    print("Il numero inserito non è > 0")
else:
    print("Radice quadrata del numero inserito:", calcola_radice_quadrata(numero))
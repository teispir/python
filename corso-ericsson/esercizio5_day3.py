'''
Si scriva del codice Python che:

➢ riceve in input un numero intero dim (gestendo eventuali eccezioni < 0
oppure non interi)
➢ genera una lista di lunghezza pari a dim contenente numeri interi casuali tra 1
e 100
➢ ne identifica il massimo (senza utilizzare la funzione built-in max() )
➢ ne identifica il minimo (senza utilizzare la funzione built-in min() )
➢ stampa questi due valori trovati.
'''
import random

dim = int(input("Inserisci dimensione della lista:"))

if dim < 0:
    print("Errore: il numero dim non può essere negativo")
else:        
    listaRandom = [random.randint(1, 100) for i in range(dim)]

print(listaRandom)

max = listaRandom[0]
min = listaRandom[0]

for elem in listaRandom:
    if (elem > max):
        max = elem
    if (elem < min):
        min = elem

print("Il valore massimo è:", max)
print("Il valore minimo è:", min)
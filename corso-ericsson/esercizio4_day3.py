'''
Si scriva del codice Python che:

➢ genera una lista di lunghezza pari a 20 contenente numeri interi casuali tra 1 e
100
➢ somma tra loro tutti gli elementi della lista
➢ moltiplica tra loro tutti gli elementi della lista
➢ stampa i risultati di somma e moltiplicazione ottenuti precedentemente.
'''
import random

def prodotto(lista):
    risultato = 1
    for numero in lista:
        risultato *= numero
    return risultato

listaRandom = [random.randint(1, 100) for i in range(20)]
print(listaRandom)

sommaLista = sum(listaRandom)
print("La somma degli elementi della lista è:", sommaLista)

prodottoLista = prodotto(listaRandom)
print("Il prodotto degli elementi della lista è:", prodottoLista)
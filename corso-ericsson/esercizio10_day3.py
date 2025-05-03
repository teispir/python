'''
Si scriva del codice Python che:

➢ riceve in input un numero intero dim (gestendo eventuali eccezioni < 0
oppure non interi)
➢ genera una lista di lunghezza pari a dim contenente numeri interi casuali tra 1
e 20
➢ stampa un istogramma per riga per ognuno di questi numeri usando degli
asterischi per disegnarlo (ad esempio per il numero 4 stampa ****)
'''
import random

dim = int(input("Inserire dimensione della lista:"))
listaRandom = [random.randint(1, 20) for i in range(dim)]

for elem in listaRandom:
    print("*" * elem)
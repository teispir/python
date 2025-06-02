'''
riceve in input una stringa in cui l’utente dovrà indicare il valore «pari» o
«dispari» (gestendo eventuali eccezioni di valori differenti)
➢ genera una lista di lunghezza 20 contenente numeri interi casuali tra 1 e 100
➢ stampa tutti i numeri pari se l’input dell’utente è uguale a «pari», tutti i
numeri dispari se l’input dell’utente è uguale a «dispari».
'''
import random

pariDispari = input("Inserisci se numero pari o dispari:")

if pariDispari != "pari" and pariDispari != "dispari":
    print("Errore: inserisci pari o dispari")

listaRandom = [random.randint(1, 100) for i in range(20)]

for elem in listaRandom:
    if elem % 2 == 0:
        if pariDispari == "pari":
            print(elem)
    else:
        if pariDispari == "dispari":
            print(elem)
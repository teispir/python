'''
Scrivere un programma che legga da tastiera un numero intero e stampi il
numero inserito e i suoi due numeri successivi.

Esempio:

Inserire numero: 3
'''
numero = int(input("Inserire numero: "))

i = numero

while (i <= numero +2):
    print(i)
    i = i + 1

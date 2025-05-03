'''
Scrivere un programma che legga da tastiera una stringa e un numero
intero e stampi la stringa inserita un numero di volte pari al numero
inserito.

Esempio:

Inserire stringa: Ciao
Inserire numero: 3

>>> Ciao
>>> Ciao
>>> Ciao
'''
stringa = input("Inserire stringa:")
numero  = int(input("inserire numero:"))

i = 1
while i <= numero:
    print(stringa)
    i = i + 1
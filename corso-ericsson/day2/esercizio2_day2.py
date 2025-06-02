'''
Scrivere un programma che legga da tastiera un numero intero e stampi a
video se esso è pari o dispari.

Esempio:

Inserire numero: 5
'''
numero = int(input("Inserire numero pari o dispari:"))

if numero % 2 == 0:
    print("Il numero", numero, "e' pari")
else:
    print("Il numero", numero, "e' dispari")
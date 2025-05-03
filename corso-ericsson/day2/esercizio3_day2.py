'''
Scrivere un programma che legga da tastiera due numeri interi,
dividendo e divisore, e stampi a video se il primo è divisibile per il
secondo.

Esempio:

Inserire dividendo: 25
Inserire divisore: 5
'''

dividendo = int(input("Inserisci dividendo: "))
divisore = int(input("Inserisci divisore: "))

# Il numero 25 è divisibile per 5

if dividendo % divisore == 0:
    print("Il numero", dividendo, "è divisibile per", divisore)
else:
    print("Il numero", dividendo, "NON è divisibile per", divisore)
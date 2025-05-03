'''
Scrivere un programma che legga da tastiera 3 numeri interi e stampi a
video il maggiore e il minore tra essi.

Esempio:

Inserire il primo numero: 4
Inserire il secondo numero: 12
Inserire il terzo numero: 9
'''
primo = int(input("Inserire il primo numero: "))
secondo = int(input("Inserire il secondo numero: "))
terzo = int(input("Inserire il terzo numero: "))

if primo > secondo:
    print("primo > secondo")
    if (primo > terzo):
        print("primo > terzo")
        maggiore = primo
        if secondo > terzo:
            minore = terzo
        else:
            minore = secondo
    else:
        print("primo < terzo")
        maggiore = terzo
        minore = secondo
else:
    print("primo < secondo")
    if secondo > terzo:
        print("secondo > terzo")
        maggiore = secondo
        minore = primo
    else:
        print("secondo < terzo")
        maggiore = terzo
        if primo > terzo:
            minore = terzo
        else:
            minore = primo

print ("Numero maggiore : ", maggiore)
print ("Numero minore : ", minore)

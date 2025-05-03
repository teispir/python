from random import randint

dim = float(input('Inserire numero intero: '))

if dim < 0 and dim % 1 != 0:
    print("Il numero inserito è minore di 0 e non è intero")
elif dim < 0:
    print("Il numero inserito è minore di 0")
elif dim % 1 != 0:
    print("Il numero inserito non è intero")
else:
    listaNumeri = []
    massimo = 0
    minimo = 101
    for index in range(int(dim)):
        randomValue = randint(1, 100)
        listaNumeri.append(randomValue)
        if randomValue > massimo:
            massimo = randomValue
        if randomValue < minimo:
            minimo = randomValue
    print("Lista generata:", listaNumeri)
    print("Massimo:", massimo)
    print("Minimo:", minimo)
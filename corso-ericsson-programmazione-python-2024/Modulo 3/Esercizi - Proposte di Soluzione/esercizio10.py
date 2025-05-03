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
    for index in range(1, int(dim) + 1):
        randomValue = randint(1, 20)
        listaNumeri.append(randomValue)

    print("Lista numeri random:", listaNumeri)

    for numRandom in listaNumeri:
        istogramma = ""
        for indexIstogramma in range(numRandom):
            istogramma += "*"
        print(istogramma)

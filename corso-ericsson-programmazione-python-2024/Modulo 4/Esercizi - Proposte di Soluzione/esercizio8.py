from random import randint


def genera_distinti(n, a, b):
    if n <= 0 or a <= 0 or b <= 0:
        raise ValueError("Almeno uno tra i valori inseriti non è maggiore di 0")
    elif n % 1 != 0 or a % 1 != 0 or b % 1 != 0:
        raise ValueError("Almeno uno tra i valori inseriti non è intero")
    elif a >= b:
        raise ValueError("Almeno uno tra i valori inseriti non è intero")

    listaNumeriRandom = []
    while len(listaNumeriRandom) < int(n):
        numRandom = randint(int(a), int(b))
        if numRandom not in listaNumeriRandom:
            listaNumeriRandom.append(numRandom)

    return listaNumeriRandom


nInput = float(input("Inserire il valore n: "))
aInput = float(input("Inserire il valore a: "))
bInput = float(input("Inserire il valore b: "))
print(genera_distinti(nInput, aInput, bInput))

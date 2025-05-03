from random import randint

pariDispari = input("Indicare il valore pari o dispari: ").lower()

if pariDispari != "pari" and pariDispari != "dispari":
    print("Inserire un valore tra pari e dispari")
else:
    listaInteri = []
    listaPariDispari = []

    for index in range(20):
        randomValue = randint(1, 100)
        listaInteri.append(randomValue)
        if pariDispari == "pari" and randomValue % 2 == 0:
            listaPariDispari.append(randomValue)
        elif pariDispari == "dispari" and randomValue % 2 == 1:
            listaPariDispari.append(randomValue)

    print("Lista random completa:", listaInteri)
    print("Lista random con soli numeri " + pariDispari + ":", listaPariDispari)
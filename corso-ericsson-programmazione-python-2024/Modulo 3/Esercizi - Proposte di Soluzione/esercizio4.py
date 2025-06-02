from random import randint

listaNumeri = []
sommaLista = 0
prodottoLista = 1

for numRandom in range(3):
    randomValue = randint(1, 100)
    listaNumeri.append(randomValue)
    sommaLista += randomValue
    prodottoLista *= randomValue

print("Lista generata:", listaNumeri)
print("Somma:", sommaLista)
print("Prodotto:", prodottoLista)
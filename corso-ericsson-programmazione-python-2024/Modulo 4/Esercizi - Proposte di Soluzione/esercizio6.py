from functions import genera_numeri_random2
from functions import fattoriale

numInput = int(input("Inserire un numero intero: "))
listaNumRandom = genera_numeri_random2(numInput)

for numRandom in listaNumRandom:
    print("Il fattoriale di", numRandom, "è", fattoriale(numRandom))


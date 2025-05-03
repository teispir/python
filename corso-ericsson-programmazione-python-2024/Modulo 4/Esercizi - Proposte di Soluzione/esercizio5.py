from functions import genera_numeri_random
from functions import calcola_pari_dispari

interoInput = int(input("Inserisci un numero intero: "))
listaNumRandom = genera_numeri_random(interoInput)

for numRandom in listaNumRandom:
    print("Il numero", numRandom, "è", calcola_pari_dispari(numRandom))
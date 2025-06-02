'''
Si scriva del codice Python che controlla tutti i numeri da 2 a 100 e per ciascuno
di essi stampa “X è primo” (dove X è il valore del numero a cui è arrivato) se il
valore di X è un numero primo, oppure stampa “X NON è primo” altrimenti.
'''
import random
def is_primo(n):
    # I numeri minori di 2 non sono primi
    if n < 2:
        return False
    # Controlla divisori fino alla radice quadrata di n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

listaRandom = [random.randint(2, 100) for i in range(2, 100)]

for elem in listaRandom:
    if is_primo(elem):
        print("elem", elem, "è primo")
    else:
        print("elem", elem, "NON è primo")        
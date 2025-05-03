from random import randint


def is_numero_primo(a):
    for index in range(2, a):
        if a % index == 0:
            return False
    return True


def stampa_numeri_primi(a, b):
    print("Lista numeri primi compresi tra", a, "e", b, ": ", end="")
    for numero in range(a, b + 1):
        if is_numero_primo(numero):
            print(numero, end=" ")


def controlla_alfanumerico(stringa):
    alfanumerico = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    for carattere in stringa:
        if carattere not in alfanumerico:
            return False
    return True


def stampa_controllo_alfanumerico(listaStringhe):
    for stringa in listaStringhe:
        if controlla_alfanumerico(stringa):
            print("Il valore di'", stringa, "'è alfanumerico")
        else:
            print("Il valore di'", stringa, "'non è alfanumerico")


def genera_numeri_random(dim):
    listaNumeriRandom = []
    for index in range(0, dim):
        listaNumeriRandom.append(randint(1, 100))
    return listaNumeriRandom


def genera_numeri_random2(dim):
    listaNumeriRandom = []
    for index in range(0, dim):
        listaNumeriRandom.append(randint(1, 10))
    return listaNumeriRandom


def fattoriale(n):
    if n == 1:
        return 1
    return n * fattoriale(n - 1)


def calcola_pari_dispari(numero):
    if numero % 2 == 0:
        return "pari"
    else:
        return "dispari"

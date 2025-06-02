from math import *
from random import *

# Funzione print()
# print("Ciao", "come", "stai", sep="-", end="-->FINE<--")

# Funzione input()
# nomeInput = input("Inserisci nome e cognome: ")
# print("Il tuo nome e cognome sono:", nomeInput)

# Funzione type()
# print(type(False))

# Funzione len()
lunghezzaVariabile = len("Stringa complessa")
# print(lunghezzaVariabile)

# Funzione abs()
valoreAssolutoNumero = abs(-12.2)
# print(valoreAssolutoNumero)

# Casting esplicito
# Funzione str()
valoreNumerico = 15
valoreNumericoTrasformato = str(valoreNumerico)
# print("Numero trasformato: " + valoreNumericoTrasformato)

valoreBooleano = True
valoreBooleanoTrasformato = str(valoreBooleano)
# print("Booleano trasformato: " + valoreBooleanoTrasformato)

#Funzione int()
numeroFrazionario = 5.5
stringaNumerica = "42"
numeroFrazionarioConvertito = int(numeroFrazionario)
stringaNumericaConvertita = int(stringaNumerica)

# print("Numero frazionario convertito (con errore):", numeroFrazionarioConvertito)
# print(stringaNumericaConvertita + 5)

numeroIntero = 5
stringaNumerica = "4.2"
numeroInteroConvertito = float(numeroIntero)
stringaNumericaConvertita = float(stringaNumerica)

# print(numeroInteroConvertito)
# print(stringaNumericaConvertita + 5)

# Esempio di utilizzo di input, cast a int e a str
# etaInput = input("Inserisci la tua età: ")
# anniMancanti = 100 - int(etaInput)
# print("Anni mancanti per arrivare a 100: " + str(anniMancanti))

# Funzioni della libreria math
valoreExp = exp(3)
# print("Risultato esponenziale (math):", valoreExp)

valoreLn = log(3)
# print("Risultato logaritmo base n (math):", valoreLn)

valorePotenza = pow(3, 3) # Produce un float, mentre operatore ** produce un int
# print("Risultato potenza (math):", valorePotenza)

valoreRadice = sqrt(81)
# print("Risultato radice quadrata (math):", valoreRadice)

# Funzioni della libreria random
numeroRandom = random()
# print("Numero generato randomicamente:", numeroRandom)

numeroRandomIntervallo = uniform(1, 90)
# print("Numero generato randomicamente tra 1 e 90 (non compreso):", numeroRandomIntervallo)

numeroRandomInteroIntervallo = randint(1, 3)
# print("Numero intero generato randomicamente tra 1 e 90:", numeroRandomInteroIntervallo)

# Metodi delle stringhe
# Metodo startswith()
# stringaDaVerificare = input("Inserisci stringa: ")
# print(stringaDaVerificare.startswith("buon"))

# Metodo endswith()
# stringa2DaVerificare = input("Inserisci stringa: ")
# print(stringa2DaVerificare.endswith("fine"))

# Metodo upper()
# stringaMinuscola = input("Inserisci stringa: ")
# print(stringaMinuscola.upper())

# Metodo lower()
# stringaMaiuscola = input("Inserisci stringa: ")
# print(stringaMaiuscola.lower())

# Metodo isalnum()
# stringaIsAlNum = input("Inserisci stringa: ")
# print(stringaIsAlNum.isalnum())

# Metodo isalpha()
# stringaIsAlpha = input("Inserisci stringa: ")
# print(stringaIsAlpha.isalpha())

# Metodo isdecimal()
# stringaIsDecimal = input("Inserisci stringa: ")
# print("La stringa è un numero decimale? Risposta:", stringaIsDecimal.isdecimal())

# OPERATORI DI CONFRONTO
primoNumero = 2
secondoNumero = 2
confrontoTraNumeri = primoNumero >= secondoNumero
# print("Risultato confronto tra ", primoNumero, " e ", secondoNumero, ". Risposta: ", confrontoTraNumeri, sep="")

stringa1 = "ciao"
stringa2 = "ciao2"
confrontoTraStringhe = stringa1 < stringa2
# print("Risultato confronto tra '", stringa1, "' e '", stringa2, "'. Risposta: ", confrontoTraStringhe, sep="")

booleano1 = True
booleano2 = False
confrontoTraBooleani = booleano1 != booleano2
# print("Risultato confronto tra ", booleano1, " e ", booleano2, ". Risposta: ", confrontoTraBooleani, sep="")

# Espressione condizionale composta: verifico se un numero è < 5 oppure >= 10
# numeroDaControllare = int(input("Inserire un numero intero: "))
# risultatoControllo = numeroDaControllare < 5 or numeroDaControllare >= 10
# print("Risultato confronto sul numero ", numeroDaControllare, ": ", risultatoControllo, sep="")

# ISTRUZIONE CONDIZIONALE IF-ELSE
'''
if risultatoControllo:
    print("Il numero inserito è < 5 oppure >= 10")
    print("FINE BLOCCO IF")
else:
    print("Il numero inserito NON è < 5 E NON è >= 10")
    print("FINE BLOCCO ELSE")
'''

# Variante if-elif-else
'''
if numeroDaControllare < 10:
    print("Il numero", numeroDaControllare, "è < 10")
elif numeroDaControllare >= 10 and numeroDaControllare < 20:
    print("Il numero", numeroDaControllare, "è >= 10 e < 20")
elif numeroDaControllare >= 20 and numeroDaControllare < 30:
    print("Il numero", numeroDaControllare, "è >= 20 e < 30")
else:
    print("Il numero", numeroDaControllare, "è >= 30")
'''

# Caso particolare: più di una condizione verificata a True
'''
if numeroDaControllare < 10:
    print("Il numero", numeroDaControllare, "è < 10")
elif numeroDaControllare < 20:
    print("Il numero", numeroDaControllare, "è < 20")
else:
    print("Il numero", numeroDaControllare, "è >= 20")
'''

# CICLO WHILE
'''
contatore = 1
limite = int(input("Inserisci un numero limite: "))
while contatore <= limite:
    print(contatore)
    contatore += 1
'''

# Caso con continue
'''
contatore = 0
limite = 100
while contatore < limite:
    contatore += 1
    if contatore > 50 and contatore <= 60:
        continue
    print(contatore)
'''

# Variante while con else
'''
i = 1
while i < 6:
    print(i)
    i += 1
else:
	print("i non è più < 6")
'''
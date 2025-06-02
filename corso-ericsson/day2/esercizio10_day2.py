'''
Scrivere del codice in Python per calcolare il numero delle ore corrispondenti
all’età di una persona (espressa in anni).

In particolare, il codice deve permettere di:

➢ Richiedere all’utente di inserire la propria età in anni
➢ Stampare a video il numero di ore corrispondenti

Si assuma che valga sempre 1 anno = 365 giorni
'''
eta = int(input("inserisci la tua eta': "))
giorni = eta * 365
ore = giorni * 24

print("Il numero di ore corrispondente alla propria eta':", ore)
'''
Si scriva del codice Python che:

➢ riceve in input 5 stringhe inserite dall’utente
➢ restituisce in output una lista di numeri interi che rappresentano la lunghezza
delle parole contenute nella lista di stringhe.
'''
stringList = []

for elem in range(5):
    stringList.append(input("Inserisci stringa:"))

print(stringList)

lenStringList = []

for elem2 in stringList:
    lenStringList.append(len(elem2))

print(lenStringList)
'''
Si scriva un codice Python che riceva come input da tastiera un intero n
e disegni sullo schermo un numero di caratteri ' * ' pari ad n gestendo eventuali
valori in input diversi da un numero intero.
'''
caratteri = input("Inserisci il numero di caratteri:")

asterisco = ""

if caratteri.isdecimal():
    i = int(caratteri)
    j = 1

    while j <= i:
        asterisco = asterisco + "*"
        j = j + 1
else:
    print("Il numero inserito non è intero")

print(asterisco)
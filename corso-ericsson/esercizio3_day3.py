'''
prende in input una stringa
➢ calcola e stampa la lunghezza della stringa senza fare uso della funzione
built-in len().
'''
count = 0
stringa = input("Inserisci una stringa:")
for i in stringa:
    count += 1

print("La stringa è lunga", count)
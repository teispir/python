a = int(input('Inserisci un numero intero positivo o negativo: '))

if a >= 0:
    print('Il numero è positivo')
    if a > 100:
        print('Ed è anche maggiore di 100')
    else:
        print('ma non è maggiore di 100')
else:
    print('Il numero è negativo')

year = 0
if year % 100 == 0 and year % 400 == 0: 
    print("True")
else:
    print("False")

if year % 4 == 0:
    print("True")
else:
    print("False")
'''
Scrivere un programma che legga da tastiera due numeri interi, start e
amount, e stampi il numero inserito e tanti numeri successivi quanto
indicato da amount.

Esempio:

Inserire start: 3
Inserire amount: 1
'''
start = int(input("Inserire start: "))
amount = int(input("Inserire amount: "))

i = start
j = 1
while j <= amount:
    print(start+j)
    j = j + 1
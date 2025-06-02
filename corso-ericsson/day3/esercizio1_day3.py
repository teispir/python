'''
Si scriva un programma Python che riceve come input da tastiera due valori interi
a e b, con b > a, e che genera una lista contenente tutti i numeri da a a b
inseriti in maniera ordinata stampandola poi a schermo.
'''
a = int(input("Inserisci numero a:"))
b = int(input("Inserisci numero b:"))

# genera lista compresa tra a e b
if a > b:
    print("Inserire b maggiore di a")
else:    
    lista = list(range(a,b))
    print(lista)
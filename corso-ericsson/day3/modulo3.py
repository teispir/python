# COLLECTIONS
# Liste
lista1 = [7, -2.2, "Ciao", -2.2, 84, -12, "Ciao"]
lista2 = [-2.2, 7, [1, [45, 3.2, 12], 6]]
listaNumeri = [4, 2, -4, 13]
listaStringhe = ["hello", "world", "python"]
matrice = [[4, 2, 18], [-2.3, 13, 7]] # Associamo a un concetto di matrice

# print(lista1 == lista2)
# print(2 in lista2)
# print(lista1 + lista2)
# print(lista1[3])

# print(lista2[2][1][2])
# Operatori di indicizzazione in accesso e assegnazione
'''
print(matrice[0][1])
matrice[0][1] = 10
print(matrice[0][1])
'''

# Operatore di slicing
# print(lista1[1:10])

# Modifiche sulle liste
'''
print(lista1)
lista1.append(True)
print(lista1)
lista1.remove(14)
print(lista1)
print(lista1)
elementoRimosso = lista1.pop(1)
print(elementoRimosso)
del lista1[1:4]
print(lista1)
print(len(lista1))
print(sum(listaNumeri))
print(list(range(10)))
'''

# TUPLE
tupla1 = (5, 6.6, -2, "ciao", False, 3)
tuplaNumeri = (5, 3, 12.2)
tuplaStringhe = ("hello", "world")
'''
print(tupla1)
print(tupla1[1:3])
print("Lunghezza tupla:", len(tupla1))
print("Massimo valore tupla di numeri:", max(tuplaNumeri))
print("Minimo valore tupla di stringhe:", min(tuplaStringhe))
print("Somma valori tupla di numeri:", sum(tuplaNumeri))
print(tuple(range(0, 10, 2)))
'''

# SET
'''
set1 = {32, 4, "ciao", -23}
print(set1)
set1.add(True)
print(set1)
set1.remove(-23)
print(set1)
print(33 in set1)
'''

# DICT
dict1 = {'a': 12, 'b': True, 'c': -2.5}
dict2 = {'d': 56, 'e': False}
'''
print(dict1)
print(dict1['c'])
dict1['b'] = "ciao"
dict1['d'] = 50
print(dict1)
del dict1['a']
print(dict1)

print("Coppie chiave-valore della lista:", list(dict1.items()))
print("Chiavi della lista:", list(dict1.keys()))
print("Valori della lista:", list(dict1.values()))
print(dict1.get('d'))
print(dict1.pop('c'))
print(dict1)
dict1.update(dict2)
print(dict1)
dictCopied = dict1.copy()
print(dictCopied)
dictCopied.clear()
print(dictCopied)
'''

# CICLO FOR
lista = [4, 3, 56]
# print(lista)
'''
k = 0
while k < len(lista):
    lista[k] = 0
    k = k + 1

for elementoLista in lista:
    elementoLista = 0

for indice, elementoLista in enumerate(lista):
    print(indice, "=>", elementoLista)
    lista[indice] = 0

for i in range(0, 21, 2):
    print(i)
print(lista)
'''
'''
stringa1 = "Hello-World-!"
print(stringa1.split("-"))

listaParole = ["Hello", "World", "Everyone"]
separatoreLista = " "
print(separatoreLista.join(listaParole))
'''
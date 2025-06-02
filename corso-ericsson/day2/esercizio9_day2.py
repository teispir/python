'''
Si chieda all’utente di inserire due valori reali (di tipo float) x e y,
stampando il valore (x + y) / (x - y).

Esempio:

>>> Inserire primo valore (reale): 2.4
>>> Inserire secondo valore (reale): 7.12
'''
x = float(input("Inserire primo valore (reale):"))
y = float(input("Inserire secondo valore (reale):"))

risultato = (x + y) / (x - y)

print("Risultato:", risultato)
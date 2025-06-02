'''
Numero di gatti = 44, Gatti per fila = 6
Output: Numero di file = 7, Gatti esclusi = 2
'''
gatti = 44
gatti_per_fila = 6

# Calcola il numero di file

num_file = gatti // gatti_per_fila

# calcola il resto
gatti_esclusi = gatti % gatti_per_fila

print("Numero di file = ", num_file)
print("Gatti esclusi = ", gatti_esclusi)
from math import pow

base = int(input("Inserire la base: "))
esponente = int(input("Inserire l'esponente: "))
potenza = pow(base, esponente)

print("b^e = " + str(potenza))
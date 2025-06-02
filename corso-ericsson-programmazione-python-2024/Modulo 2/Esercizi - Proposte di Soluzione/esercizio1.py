numero1 = int(input("Inserire il primo numero: "))
numero2 = int(input("Inserire il secondo numero: "))
numero3 = int(input("Inserire il terzo numero: "))

if numero1 >= numero2 and numero1 >= numero3:
    numeroMax = numero1
elif numero2 >= numero1 and numero2 >= numero3:
    numeroMax = numero2
else:
    numeroMax = numero3

if numero1 <= numero2 and numero1 <= numero3:
    numeroMin = numero1
elif numero2 <= numero1 and numero2 <= numero3:
    numeroMin = numero2
else:
    numeroMin = numero3

print("Numero maggiore: " + str(numeroMax))
print("Numero minore: " + str(numeroMin))

from math import sqrt

numeroInput = float(input("Inserire un numero intero (> 0): "))

if numeroInput % 1 == 0 and numeroInput > 0:
    radiceQuadrata = sqrt(numeroInput)
    print("Radice quadrata di " + str(numeroInput) + ": " + str(radiceQuadrata))
elif numeroInput % 1 != 0 and numeroInput > 0:
    print("Non è un intero!")
elif numeroInput % 1 == 0 and numeroInput <= 0:
    print("Non è maggiore di 0!")
else:
    print("Non è né un intero né maggiore di 0!")

numeroInput = int(input("Inserire un numero intero: "))

if numeroInput % 2 == 0:
    pariODispari = "pari"
else:
    pariODispari = "dispari"

print("Il numero " + str(numeroInput) + " è " + pariODispari)
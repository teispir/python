def massimo(a, b):
    if a >= b:
        return a
    else:
        return b


inputNum1 = int(input("Inserisci il primo numero: "))
inputNum2 = int(input("Inserisci il secondo numero: "))
massimoOutput = massimo(inputNum1, inputNum2)
print("Il massimo tra", inputNum1, "e", inputNum2, "è", massimoOutput)
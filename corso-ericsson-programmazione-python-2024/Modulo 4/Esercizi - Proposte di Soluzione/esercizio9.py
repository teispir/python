def is_distinct_int(listInt):
    listTemp = []
    for numInt in listInt:
        if numInt % 1 != 0:
            raise ValueError("Formato non corretto")
        if numInt in listTemp:
            return False
        else:
            listTemp.append(numInt)
    return True


listInput = []
for index in range(0, 5):
    listInput.append(float(input("Inserisci un numero intero: ")))

if is_distinct_int(listInput):
    print("La lista è composta da tutti numeri distinti")
else:
    print("La lista NON è composta da tutti numeri distinti")
a = int(input("Inserire un numero intero a: "))
b = int(input("Inserire un numero intero b: "))
countA = 0
countB = 0

while countB < b:
    lato = ""
    while countA < a:
        if (countB == 0) or (countB == b - 1):
            lato += "* "
        elif (countA == 0) or (countA == a - 1):
            lato += "* "
        else:
            lato += "  "
        countA += 1
    print(lato)
    countB += 1
    countA = 0

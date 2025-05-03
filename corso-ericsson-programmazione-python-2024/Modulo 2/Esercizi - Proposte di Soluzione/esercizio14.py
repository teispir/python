n = float(input("Inserire un numero intero n: "))

if n % 1 == 0 and n > 0:
    count = 0
    output = ""
    while count < n:
        output += "*"
        count += 1
    print(output)
    print("Finito!")
elif n % 1 != 0 and n > 0:
    print("Non è un intero!")
elif n % 1 == 0 and n <= 0:
    print("Non è maggiore di 0!")
else:
    print("Non è né un intero né maggiore di 0!")
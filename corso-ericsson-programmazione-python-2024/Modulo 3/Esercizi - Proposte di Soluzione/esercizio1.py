a = int(input('Inserire valore a: '))
b = int(input('Inserire valore b > a: '))

if b <= a:
    print('Il valore di b non è > a')
else:
    listaOutput = []
    counter = a
    while counter <= b:
        listaOutput.append(counter)
        counter += 1
    print(listaOutput)
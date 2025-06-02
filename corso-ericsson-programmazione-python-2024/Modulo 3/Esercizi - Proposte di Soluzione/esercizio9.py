checkCorretto = False

while not checkCorretto:
    # Prendo in input i valori min e max
    minimo = int(input('Inserisci valore minimo: '))
    massimo = int(input('Inserisci valore massimo: '))

    # Controllo condizione max > min
    if massimo <= minimo:
        print('Il valore massimo non è maggiore di minimo')
    else:
        checkCorretto = True

        # Ciclo su tutti i numeri interi tra minimo e massimo
        for valoreCorrente in range(minimo, massimo + 1):
            # Ciclo di controllo su tutti i valori da 2 a (valoreCorrente - 1)
            check = True
            for numeroCheckPrimo in range(2, valoreCorrente - 1):
                # Controllo se valoreCorrente è divisibile per numeroCheckPrimo
                if valoreCorrente % numeroCheckPrimo == 0:
                    print(valoreCorrente, 'NON è numero primo')
                    check = False
                    break

            if check:
                print(valoreCorrente, 'è numero primo')
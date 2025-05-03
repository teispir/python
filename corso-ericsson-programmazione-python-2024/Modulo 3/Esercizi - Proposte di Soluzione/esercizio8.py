for valoreCorrente in range(2, 101):
    # Ciclo di controllo su tutti i valori da 2 a 100
    check = True
    for numeroCheckPrimo in range(2, valoreCorrente - 1):
        # Controllo se valoreCorrente è divisibile per numeroCheckPrimo
        if valoreCorrente % numeroCheckPrimo == 0:
            print(valoreCorrente, 'NON è numero primo')
            check = False
            break

    if check:
        print(valoreCorrente, 'è numero primo')
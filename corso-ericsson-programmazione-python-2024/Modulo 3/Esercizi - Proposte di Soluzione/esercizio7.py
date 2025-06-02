listaStringhe = []

for iterazioneInput in range(5):
    listaStringhe.append(input('Inserisci stringa di testo: '))

for stringa in listaStringhe:
    print(stringa, '=> Lunghezza:', len(stringa), 'caratteri')
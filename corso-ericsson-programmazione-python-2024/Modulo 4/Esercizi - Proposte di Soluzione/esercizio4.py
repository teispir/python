from functions import stampa_controllo_alfanumerico

listaStringhe = []

for index in range(0, 5):
    stringaInput = input("Inserire una stringa: ")
    listaStringhe.append(stringaInput)

stampa_controllo_alfanumerico(listaStringhe)
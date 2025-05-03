stringaInput = input("Inserire una stringa: ")
dictFrequenza = {}

for carattere in stringaInput:
    if carattere in dictFrequenza:
        dictFrequenza[carattere] += 1
    else:
        dictFrequenza[carattere] = 1

print("Dizionario della frequenza di comparsa:", dictFrequenza)
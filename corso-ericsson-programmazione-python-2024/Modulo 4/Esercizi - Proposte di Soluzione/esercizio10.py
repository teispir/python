def get_distinct_string(listString):
    listStringDistinct = []
    for currentString in listString:
        if type(currentString) is not str:
            raise ValueError("Formato non corretto")
        if currentString not in listStringDistinct:
            listStringDistinct.append(currentString)
    return listStringDistinct


listInput = []
for index in range(0, 5):
    listInput.append(input("Inserisci una stringa: "))

print(get_distinct_string(listInput))

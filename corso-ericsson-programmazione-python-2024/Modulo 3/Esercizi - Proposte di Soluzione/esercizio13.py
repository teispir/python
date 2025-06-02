studenti = [
    {"nome": "Luca", "cognome": "Rossi", "classe": "3A", "voti": [6, 10, 8]},
    {"nome": "Mario", "cognome": "Bianchi", "classe": "3A", "voti": [7, 8, 9]},
    {"nome": "Anna", "cognome": "Verdi", "classe": "3B", "voti": [8, 9, 10]},
]

for studente in studenti:
    mediaVoto = 0
    for voto in studente["voti"]:
        mediaVoto += voto
    mediaVoto /= len(studente["voti"])
    print(studente["nome"] + " " + studente["cognome"] + " - Media voto: " + str(mediaVoto))
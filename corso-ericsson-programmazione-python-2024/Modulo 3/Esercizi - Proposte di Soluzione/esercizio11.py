pianeti = (
    ("Mercurio", "roccioso", 0),
    ("Venere", "roccioso", 0),
    ("Terra", "roccioso", 1),
    ("Marte", "roccioso", 2),
    ("Giove", "gassoso", 95),
    ("Saturno", "gassoso", 83),
    ("Urano", "gassoso", 27),
    ("Nettuno", "gassoso", 14)
)
totSatelliti = 0

for pianeta in pianeti:
    print(pianeta[0] + ": pianeta " + pianeta[1] + " con " + str(pianeta[2]) + " satelliti")
    totSatelliti += pianeta[2]

print("Numero di satelliti totali: " + str(totSatelliti))
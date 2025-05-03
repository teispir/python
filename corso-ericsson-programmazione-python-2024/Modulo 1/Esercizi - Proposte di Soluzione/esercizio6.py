secondiInput = 5430

ore = secondiInput // (60 * 60)  # ore = 3
minuti = (secondiInput - (ore * 60 * 60)) // 60  # 12560 - (3 * 3600) // 60 ==> minuti = 29
secondi = (secondiInput - (ore * 60 * 60) - (minuti * 60))  # secondi = 20

print("Secondi di partenza:", secondiInput)
print(ore, "ore,", minuti, "minuti e", secondi, "secondi")
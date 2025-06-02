'''
Secondi: 12560
Output: 3 ore, 29 minuti e 20 secondi.
'''
secondi = 12560

'''
ore = dif/3600; //un'ora sono 3600sec...
minuti = dif/60; //un minuto 60sec...
secondi = dif;//i secondi già li hai! :D
'''
ore = secondi // 3600
minuti = (secondi % 3600) // 60
secondi2 = (secondi % 3600) % 60
secondi = secondi % 60

print("Ore: ", ore)
print("Minuti: ", minuti)
print("Secondi: ", secondi2)
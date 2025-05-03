import matplotlib.pyplot as plt
import numpy as np

# Dati
values = [
    1207.75, 1210.25, 1213.32, 1208.32, 1212.32, 1212.32, 1214.52, 1216.72, 1227.38, 1236.98,
    1236.98, 1216.98, 1225.98, 1205.98, 1205.98, 1213.24, 1223.90, 1238.40, 1251.72, 1261.72,
    1274.02, 1282.90, 1262.90, 1271.90, 1251.90, 1262.56, 1242.56, 1253.16, 1233.16, 1213.16,
    1221.16, 1231.16, 1211.16, 1226.16, 1238.36, 1248.36, 1228.36, 1198.36, 1198.36, 1210.36,
    1180.36, 1195.36, 1213.36, 1213.36, 1231.66, 1249.96, 1263.16, 1263.16, 1279.06, 1279.06,
    1292.38, 1309.48, 1309.48, 1309.48, 1327.48, 1348.48, 1363.48, 1375.48, 1345.48, 1305.48,
    1328.28, 1352.68, 1372.68, 1395.48, 1415.48, 1375.48, 1399.88, 1359.88, 1384.28, 1384.28,
    1384.28, 1344.28, 1370.68, 1391.88, 1418.28, 1434.28, 1394.28, 1354.28, 1314.28, 1342.28,
    1362.28, 1382.28, 1402.28, 1419.88, 1379.88, 1397.48, 1347.48, 1297.48, 1325.98, 1350.98,
    1350.98, 1350.98, 1350.98, 1379.48, 1404.48, 1426.48, 1376.48, 1402.98, 1402.98, 1429.48,
    1454.48, 1454.48, 1454.48, 1482.98, 1432.98, 1467.98, 1467.98, 1497.98, 1519.98, 1546.48,
    1586.48, 1621.48, 1651.98, 1601.98, 1601.98, 1601.98, 1551.98, 1586.98, 1622.98, 1622.98,
    1572.98, 1601.48, 1601.48, 1634.48, 1634.48, 1584.48, 1620.48, 1645.48, 1670.48, 1670.48,
    1696.98, 1696.98, 1727.48, 1677.48, 1627.48, 1577.48, 1527.48, 1552.48, 1574.48, 1524.48,
    1524.48, 1474.48, 1499.48, 1449.48, 1479.48, 1479.48, 1504.48, 1354.48, 1354.48, 1354.48,
    1354.48, 1444.48, 1444.48, 1444.48, 1294.48, 1294.48, 1373.98, 1448.98, 1556.98, 1556.98,
    1648.48, 1498.48, 1348.48, 1348.48, 1348.48, 1348.48, 1447.48, 1297.48, 1376.98, 1442.98,
    1442.98, 1534.48, 1639.48, 1718.98, 1817.98, 1667.98, 1765.48, 1615.48, 1465.48, 1315.48,
    1165.48, 1250.98, 1100.98, 1166.98, 1256.98, 1331.98, 1181.98, 1181.98, 1031.98, 1031.98,
    881.98, 953.23, 1019.23, 869.23, 869.23, 869.23, 923.23, 923.23, 989.23, 1055.23, 905.23,
    980.23, 1070.23, 1136.23, 1136.23, 1202.23, 1262.23, 1112.23, 962.23
]

# Creazione dell'array degli indici
times = np.arange(len(values))

# Trova minimo, massimo e ultimo valore
min_index = np.argmin(values)
max_index = np.argmax(values)
current_index = len(values) - 1  # Ultimo valore

# Trova il primo indice in cui compare il valore 1354.48
investment_change_value = 1354.48
change_index = np.where(np.array(values) == investment_change_value)[0][0]

# Aggiungi una linea orizzontale rossa continua per il valore 1200
plt.axhline(y=1200, color='red', linestyle='-', linewidth=1.5, label='Soglia 1200')

# Creazione del grafico
plt.figure(figsize=(12, 6))
plt.fill_between(times, values, color="skyblue", alpha=0.4)
plt.plot(times, values, color="blue", alpha=0.6)

# Evidenzia minimo, massimo e ultimo valore
highlight_indices = [min_index, max_index, current_index]
highlight_values = [values[min_index], values[max_index], values[current_index]]
colors = ['red', 'green', 'purple']
labels = ['Min', 'Max', 'Current']

for i, (idx, val, color, label) in enumerate(zip(highlight_indices, highlight_values, colors, labels)):
    plt.scatter(idx, val, color=color, zorder=3, label=label)
    plt.text(idx, val, f'{label}: {val:.2f}', verticalalignment='bottom' if i == 0 else 'top', 
             horizontalalignment='right', fontsize=10, color=color)

# Aggiungi una linea verticale al punto di cambio investimento
plt.axvline(x=change_index, color='orange', linestyle='--', linewidth=1.5, label='Cambio Investimento')

# Titoli e label
plt.title("Fantasista 2023-2025")
plt.xlabel("Indice Temporale")
plt.ylabel("EUR")

# Impostiamo la griglia con passo di 100
plt.yticks(np.arange(min(values) - 100, max(values) + 200, 100))
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Mostra la legenda e il grafico
plt.legend()
plt.show()
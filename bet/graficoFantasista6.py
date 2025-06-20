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
    980.23, 1070.23, 1136.23, 1136.23, 1202.23, 1262.23, 1112.23, 962.23, 1016.23, 1082.23, 
    932.23, 1011.73, 1077.73, 1124.73, 1183.23, 1283.73, 1352.73, 1418.73, 1493.73, 1493.73, 
    1343.73, 1406.73, 1406.73, 1465.53, 1539.03, 1605.03, 1755.03, 1645.03, 1756.33
]

# Aggiungiamo la cedola
values.append(1256.33)

# Creazione dell'array degli indici
times = np.arange(len(values))

# Trova minimo, massimo e ultimo valore
min_index = np.argmin(values)
max_index = np.argmax(values)
current_index = len(values) - 1  # Ultimo valore

# Creazione del grafico
plt.figure(figsize=(12, 6))
plt.fill_between(times, values, color="skyblue", alpha=0.4)
plt.plot(times, values, color="blue", alpha=0.6)

# Evidenzia minimo, massimo e ultimo valore
highlight_indices = [min_index, max_index, current_index]
highlight_values = [values[min_index], values[max_index], values[current_index]]
colors = ['red', 'green', 'purple']
labels = ['Min', 'Max', 'Current']

for idx, val, color, label in zip(highlight_indices, highlight_values, colors, labels):
    plt.scatter(idx, val, color=color, zorder=3, label=label)
    plt.text(idx, val, f'{label}: {val:.2f}', verticalalignment='bottom' if idx == min_index else 'top',
             horizontalalignment='right', fontsize=10, color=color)

# Aggiunta annotazione cedola
plt.annotate('Cedola -500 EUR',
             xy=(current_index - 1, 1756.33), xycoords='data',
             xytext=(current_index - 10, 1600), textcoords='data',
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color='red'),
             fontsize=12, color='red')

# Linee, titoli, griglia, legenda
plt.title("Fantasista 2023-2025")
plt.xlabel("Indice Temporale")
plt.ylabel("EUR")
plt.yticks(np.arange(700, max(values) + 100, 100))
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend()
plt.show()

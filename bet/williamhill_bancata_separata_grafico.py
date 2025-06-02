# Script corretto + grafico per analizzare Super Quota con bancate separate

import matplotlib.pyplot as plt

# Parametri modificabili
stake_super_quota = 10  # Importo puntato sulla super quota
quota_super_quota = 7.92  # Quota della super quota (X primo tempo / 2 finale)

# Quote di banca sui mercati singoli
banca_x_primo_tempo = 3.75  # Quota di bancata su X primo tempo
banca_2_finale = 3.15      # Quota di bancata su 2 finale

# Commissione Exchange
commissione = 0.045  # 4.5%

# Calcoli

# Vincita potenziale Super Quota
vincita_super_quota = stake_super_quota * quota_super_quota

# Bancate
bancata_x = stake_super_quota
bancata_2 = stake_super_quota

# Responsabilità
responsabilita_x = (banca_x_primo_tempo - 1) * bancata_x
responsabilita_2 = (banca_2_finale - 1) * bancata_2

# Vincita netta da bancata
incasso_banca_x = bancata_x * (1 - commissione)
incasso_banca_2 = bancata_2 * (1 - commissione)

# Scenari

profitto_caso_super_quota = vincita_super_quota - responsabilita_x - responsabilita_2
perdita_totale = -(stake_super_quota + responsabilita_x + responsabilita_2)
profitto_vittoria_entrambi = incasso_banca_x + incasso_banca_2 - stake_super_quota
profitto_vinci_x = incasso_banca_x - stake_super_quota - responsabilita_2
profitto_vinci_2 = incasso_banca_2 - stake_super_quota - responsabilita_x

# Output testuale

print("=== Analisi Super Quota CORRETTA ===")
print(f"Importo puntato: {stake_super_quota}€")
print(f"Quota Super Quota (X/2): {quota_super_quota}")
print(f"Vincita potenziale Super Quota: {vincita_super_quota:.2f}€")
print()
print("=== Bancate Separate ===")
print(f"Banca su X primo tempo a quota: {banca_x_primo_tempo}")
print(f"Banca su 2 finale a quota: {banca_2_finale}")
print(f"Responsabilità X primo tempo: {responsabilita_x:.2f}€")
print(f"Responsabilità 2 finale: {responsabilita_2:.2f}€")
print()
print("=== Scenari ===")
print(f"✅ Se vince la Super Quota: profitto netto {profitto_caso_super_quota:.2f}€")
print(f"❌ Se perdi Super Quota e perdi entrambe le bancate: perdita totale {perdita_totale:.2f}€")
print(f"🔄 Se perdi Super Quota e vinci entrambe le bancate: profitto netto {profitto_vittoria_entrambi:.2f}€")
print(f"🔹 Se perdi Super Quota e vinci SOLO bancata X: profitto netto {profitto_vinci_x:.2f}€")
print(f"🔹 Se perdi Super Quota e vinci SOLO bancata 2: profitto netto {profitto_vinci_2:.2f}€")

# Preparazione dati per il grafico

scenari = [
    "Vince SuperQuota",
    "Perdi Tutto",
    "Vinci Entrambe Bancate",
    "Vinci Solo Bancata X",
    "Vinci Solo Bancata 2"
]

profitti = [
    profitto_caso_super_quota,
    perdita_totale,  # attenzione, perdita negativa
    profitto_vittoria_entrambi,
    profitto_vinci_x,
    profitto_vinci_2
]

# Creazione grafico

plt.figure(figsize=(10,6))
barlist = plt.bar(scenari, profitti, color="skyblue")
# Coloriamo diversamente i profitti negativi
for i, profitto in enumerate(profitti):
    if profitto < 0:
        barlist[i].set_color('tomato')

plt.axhline(0, color='black', linewidth=0.8)
plt.title("Analisi Scenari Super Quota")
plt.ylabel("Profitto (€)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()
import matplotlib.pyplot as plt

# === Parametri iniziali ===
stake_super_quota = 10
quota_super_quota = 7.70

banca_x_primo_tempo = 3.75
banca_2_finale = 3.15

commissione = 0.045  # 4.5%

# === Funzioni di utilità ===

def responsabilita(quota_banca, importo):
    return (quota_banca - 1) * importo

def vincita_netta_banca(importo, commissione):
    return importo * (1 - commissione)

# === Calcolo Equal Profit ===

peso_x = 1 / banca_x_primo_tempo
peso_2 = 1 / banca_2_finale
somma_pesi = peso_x + peso_2

bancata_x = stake_super_quota * (peso_x / somma_pesi)
bancata_2 = stake_super_quota * (peso_2 / somma_pesi)

vincita_super_quota = stake_super_quota * quota_super_quota
responsabilita_x = responsabilita(banca_x_primo_tempo, bancata_x)
responsabilita_2 = responsabilita(banca_2_finale, bancata_2)

incasso_x = vincita_netta_banca(bancata_x, commissione)
incasso_2 = vincita_netta_banca(bancata_2, commissione)

# === Scenari ===

profitto_super_quota = vincita_super_quota - responsabilita_x - responsabilita_2
perdita_totale = stake_super_quota + responsabilita_x + responsabilita_2
profitto_vittoria_x = incasso_x - stake_super_quota - responsabilita_2
profitto_vittoria_2 = incasso_2 - stake_super_quota - responsabilita_x
profitto_vittoria_entrambi = incasso_x + incasso_2 - stake_super_quota

# === Output ===

print("=== Strategia Equal Profit ===")
print(f"Banca X primo tempo: {bancata_x:.2f}€ a quota {banca_x_primo_tempo}")
print(f"Banca 2 finale:     {bancata_2:.2f}€ a quota {banca_2_finale}")
print(f"Responsabilità X:   {responsabilita_x:.2f}€")
print(f"Responsabilità 2:   {responsabilita_2:.2f}€")
print()

print("=== Scenari ===")
print(f"✅ Vince Super Quota (X/2):          profitto netto {profitto_super_quota:.2f}€")
print(f"🔄 Vince solo X primo tempo:         profitto netto {profitto_vittoria_x:.2f}€")
print(f"🔄 Vince solo 2 finale:              profitto netto {profitto_vittoria_2:.2f}€")
print(f"✅ Vince entrambe le bancate (no X/2): profitto netto {profitto_vittoria_entrambi:.2f}€")
print(f"❌ Perdi tutto:                      perdita totale {perdita_totale:.2f}€")

# === Grafico ===

scenari = [
    "Vince SuperQuota",
    "Vince solo X primo tempo",
    "Vince solo 2 finale",
    "Vince entrambe le bancate",
    "Perdi tutto"
]

profitti = [
    profitto_super_quota,
    profitto_vittoria_x,
    profitto_vittoria_2,
    profitto_vittoria_entrambi,
    -perdita_totale
]

plt.figure(figsize=(10,6))
barlist = plt.bar(scenari, profitti, color='lightblue')
for i, p in enumerate(profitti):
    if p < 0:
        barlist[i].set_color('tomato')

plt.axhline(0, color='black', linewidth=0.8)
plt.title("Strategia Equal Profit - Scenari")
plt.ylabel("Profitto (€)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

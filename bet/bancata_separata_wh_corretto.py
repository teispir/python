# Script corretto per analizzare una Super Quota con bancate separate

# Parametri modificabili
stake_super_quota = 10  # Importo puntato sulla super quota
quota_super_quota = 7.70  # Quota della super quota (X primo tempo / 2 finale)

# Quote di banca sui mercati singoli
banca_x_primo_tempo = 3.75  # Quota di bancata su X primo tempo
banca_2_finale = 3.15      # Quota di bancata su 2 finale

# Commissione Exchange
commissione = 0.045  # 4.5%

# Calcoli

# Vincita potenziale sulla super quota
vincita_super_quota = stake_super_quota * quota_super_quota

# Bancate
bancata_x = stake_super_quota  # Puoi personalizzare la divisione
bancata_2 = stake_super_quota  # Stesso stake per semplicità

# Responsabilità su bancate
responsabilita_x = (banca_x_primo_tempo - 1) * bancata_x
responsabilita_2 = (banca_2_finale - 1) * bancata_2

# Vincita netta su bancata se il risultato è favorevole
incasso_banca_x = bancata_x * (1 - commissione)
incasso_banca_2 = bancata_2 * (1 - commissione)

# === Scenari ===

# Caso 1: vince la Super Quota (X primo tempo + 2 finale)
# Vinci super quota ma perdi entrambe le bancate (paghi responsabilità)
profitto_caso_super_quota = vincita_super_quota - responsabilita_x - responsabilita_2

# Caso 2: perdi Super Quota e perdi entrambe le bancate
# Perdita totale = stake iniziale + responsabilità X + responsabilità 2
perdita_totale = stake_super_quota + responsabilita_x + responsabilita_2

# Caso 3: perdi Super Quota, ma vinci entrambe le bancate
# Vinci le due bancate -> incasso da entrambe - perdita stake
profitto_vittoria_entrambi = incasso_banca_x + incasso_banca_2 - stake_super_quota

# Caso 4: perdi Super Quota, vinci solo una bancata
# Possibili due sottocasi:
# - Vinci bancata X, perdi bancata 2
profitto_vinci_x = incasso_banca_x - stake_super_quota - responsabilita_2
# - Vinci bancata 2, perdi bancata X
profitto_vinci_2 = incasso_banca_2 - stake_super_quota - responsabilita_x

# Output

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

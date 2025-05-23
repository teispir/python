# Script di esempio per analizzare una Super Quota con copertura separata

# Parametri modificabili
stake_super_quota = 10  # Importo puntato sulla super quota
quota_super_quota = 7.70  # Quota della super quota (X primo tempo / 2 finale)

# Quote di banca sui mercati singoli
banca_x_primo_tempo = 3.75  # Quota di bancata su X primo tempo
banca_2_finale = 3.15      # Quota di bancata su 2 finale

# Commissione Exchange
commissione = 0.045  # 54.5%

# Calcoli

# Vincita potenziale se azzecchi la super quota
vincita_super_quota = stake_super_quota * quota_super_quota

# Calcolo delle responsabilità delle bancate
# Responsabilità = (Quota_banca - 1) * importo bancato

# Per una copertura "semplice" assumiamo che l'utente banca l'equivalente dello stake
bancata_x = stake_super_quota  # Puoi personalizzare la divisione
bancata_2 = stake_super_quota  # Uguale stake per semplicità

responsabilita_x = (banca_x_primo_tempo - 1) * bancata_x
responsabilita_2 = (banca_2_finale - 1) * bancata_2

# Guadagno o perdita in tutti i casi

# Caso 1: esce X primo tempo + 2 finale (vinci super quota, perdi le due bancate)
profitto_caso_super_quota = vincita_super_quota - responsabilita_x - responsabilita_2

# Caso 2: NON esce X/2
# Potresti perdere la super quota e vincere almeno una delle bancate (a seconda del caso)
# (semplifichiamo: il massimo rischio è perdere stake_super_quota e pagare le commissioni sulle vincite delle bancate)

# Incasso da bancata X (in caso X NON esca al primo tempo)
incasso_banca_x = bancata_x * (1 - commissione)

# Incasso da bancata 2 (in caso Real NON vinca il finale)
incasso_banca_2 = bancata_2 * (1 - commissione)

# Profitto in caso di bancata vincente (non perfetto perché dipende dall'esito esatto)
profitto_caso_bancate = incasso_banca_x + incasso_banca_2 - stake_super_quota

# Output

print("=== Analisi Super Quota ===")
print(f"Importo puntato: {stake_super_quota}€")
print(f"Quota Super Quota (X/2): {quota_super_quota}")
print(f"Vincita potenziale: {vincita_super_quota:.2f}€")
print()
print("=== Bancate Separate ===")
print(f"Banca X primo tempo a quota: {banca_x_primo_tempo}")
print(f"Banca 2 finale a quota: {banca_2_finale}")
print(f"Responsabilità X primo tempo: {responsabilita_x:.2f}€")
print(f"Responsabilità 2 finale: {responsabilita_2:.2f}€")
print()
print("=== Scenari ===")
print(f"Se vince la Super Quota: guadagni {profitto_caso_super_quota:.2f}€")
print(f"Se perdi la Super Quota ma vinci entrambe le bancate: guadagni {profitto_caso_bancate:.2f}€ (circa)")
print(f"Se perdi la Super Quota e perdi entrambe le bancate: perdi {stake_super_quota:.2f}€ + commissioni")
print(f"Se perdi la Super Quota e vinci una bancata: guadagni {incasso_banca_x:.2f}€ (circa)")
print(f"Se perdi la Super Quota e vinci l'altra bancata: guadagni {incasso_banca_2:.2f}€ (circa)")
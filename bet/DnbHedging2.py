def calcola_copertura_dnb(importo_dnb, quota_dnb, quota_nantes, quota_pareggio):
    # Perdita potenziale sulla DNB se Nantes vince
    perdita_dnb = importo_dnb
    
    # Stake sul Nantes per ridurre la perdita
    stake_nantes = (perdita_dnb * 0.8) / (quota_nantes - 1)  # 80% della perdita
    
    # Stake sul pareggio per ridurre ulteriormente la perdita
    stake_pareggio = (perdita_dnb * 0.2) / (quota_pareggio - 1)  # 20% della perdita
    
    return stake_nantes, stake_pareggio

# Esempio di utilizzo
importo_dnb = float(input("Inserisci l'importo giocato sulla DNB: "))
quota_dnb = float(input("Inserisci la quota della DNB: "))
quota_nantes = float(input("Inserisci la quota live del Nantes vincente: "))
quota_pareggio = float(input("Inserisci la quota live del pareggio: "))

stake_nantes, stake_pareggio = calcola_copertura_dnb(importo_dnb, quota_dnb, quota_nantes, quota_pareggio)

print(f"Dovresti puntare {stake_nantes:.2f}€ sul Nantes e {stake_pareggio:.2f}€ sul pareggio per minimizzare la perdita.")
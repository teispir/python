def calcola_stake_dnb(importo_dnb, quota_dnb, quota_pareggio_live):
    # Calcola il profitto in caso di vittoria della squadra (DNB vinto)
    profitto_dnb = (importo_dnb * quota_dnb) - importo_dnb
    print(f"profitto_dnb:", profitto_dnb)
    
    # Calcola lo stake ottimale per coprire il pareggio
    stake_pareggio = profitto_dnb / (quota_pareggio_live - 1)
    
    # Calcola il profitto finale garantito
    profitto_garantito = profitto_dnb - stake_pareggio
    
    return stake_pareggio, profitto_garantito

# Esempio di utilizzo
importo_dnb = 150  # Importo scommesso sul DNB
quota_dnb = 1.44    # Quota del DNB
quota_pareggio_live = 12.00  # Quota live sul pareggio

stake, profitto = calcola_stake_dnb(importo_dnb, quota_dnb, quota_pareggio_live)

print(f"Dovresti puntare {stake:.2f}€ sul pareggio.")
print(f"Il tuo profitto garantito sarà di {profitto:.2f}€ indipendentemente dal risultato.")
# matched_betting_equal_profit.py

# Parametri modificabili
quota_promo = 4.5           # Quota maggiorata
quota_reale = 2.65          # Quota reale (non usata direttamente qui)
quota_lay = 2.8             # Quota della bancata su Exchange
commissione_lay = 0.045      # Commissione dell'exchange (es. 5%)
bonus_gold_cap = 10         # Massimo Bonus Gold ottenibile

# Calcolo puntata ideale per ricevere 10€ di Bonus Gold
puntata = bonus_gold_cap / (quota_promo - quota_reale)

# Approssimazione: calcolo lay stake per Equal Profit
# Risolviamo: profitto_vittoria = profitto_sconfitta
# profitto_vittoria = puntata * quota_promo - responsabilita + bonus_gold
# profitto_sconfitta = lay_stake * (1 - commissione_lay) - puntata

# Poiché responsabilità = lay_stake * (quota_lay - 1)
# Sostituiamo tutto in una funzione da risolvere numericamente

def calcola_equal_profit_lay(puntata, quota_promo, quota_lay, commissione_lay, bonus_gold):
    # Trova lay_stake che pareggia i profitti nei due scenari
    from scipy.optimize import fsolve

    def equazione(lay_stake):
        responsabilita = lay_stake * (quota_lay - 1)
        profitto_vittoria = puntata * quota_promo - responsabilita + bonus_gold
        profitto_sconfitta = lay_stake * (1 - commissione_lay) - puntata
        return profitto_vittoria - profitto_sconfitta

    lay_iniziale = (puntata * quota_promo) / quota_lay  # punto iniziale
    lay_stake = fsolve(equazione, lay_iniziale)[0]
    return lay_stake

# Calcolo lay stake per equal profit
lay_stake = calcola_equal_profit_lay(puntata, quota_promo, quota_lay, commissione_lay, bonus_gold_cap)
responsabilita = lay_stake * (quota_lay - 1)

# Profitti in entrambi i casi
profitto_vittoria = puntata * quota_promo - responsabilita + bonus_gold_cap
profitto_sconfitta = lay_stake * (1 - commissione_lay) - puntata

# Output
print(f"--- STRATEGIA EQUAL PROFIT CON BONUS GOLD ---")
print(f"Quota maggiorata: {quota_promo}")
print(f"Quota bancata: {quota_lay} con commissione {commissione_lay*100:.0f}%")
print()
print(f"✅ Punta {puntata:.2f} € su SNAI per massimizzare Bonus Gold")
print(f"✅ Banca {lay_stake:.2f} € su Exchange (Responsabilità: {responsabilita:.2f} €)")
print()
print(f"💰 In caso di VITTORIA INTER → Profitto netto = {profitto_vittoria:.2f} € (incluso bonus)")
print(f"💰 In caso di SCONFITTA/PAREGGIO → Profitto netto = {profitto_sconfitta:.2f} €")

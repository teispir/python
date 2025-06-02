# matched_betting_bonus_gold_auto.py

# Parametri modificabili
quota_promo = 4.5           # Quota maggiorata
quota_reale = 2.65          # Quota reale del bookmaker
quota_lay = 2.8             # Quota della bancata su Exchange
commissione_lay = 0.05      # Commissione dell'exchange (es. 5% → 0.05)
bonus_gold_cap = 10         # Massimo Bonus Gold ottenibile

# Calcolo della puntata per ottenere esattamente il bonus_gold_cap
differenza_quote = quota_promo - quota_reale
puntata = bonus_gold_cap / differenza_quote

# Calcolo bancata Equal Profit
lay_stake = (puntata * quota_reale) / (quota_lay - commissione_lay)
responsabilita = lay_stake * (quota_lay - 1)

# Profitto se Inter NON vince (si vince su Exchange)
profitto_exchange = lay_stake * (1 - commissione_lay) - puntata

# Profitto se Inter vince (con bonus incluso)
guadagno_lordo = puntata * quota_promo
profitto_bookie = guadagno_lordo - responsabilita
profitto_bookie_con_bonus = profitto_bookie + bonus_gold_cap

# Output
print(f"--- STRATEGIA MATCHED BETTING AUTOMATICA ---")
print(f"Quota maggiorata: {quota_promo}")
print(f"Quota reale: {quota_reale}")
print(f"Quota lay (Exchange): {quota_lay} con commissione {commissione_lay*100:.0f}%")
print()
print(f"✅ Punta {puntata:.2f} € su SNAI per ottenere esattamente {bonus_gold_cap:.2f} € in Bonus Gold")
print(f"✅ Banca {lay_stake:.2f} € su Exchange (Responsabilità: {responsabilita:.2f} €)")
print()
print(f"💰 In caso di VITTORIA INTER → Profitto = {profitto_bookie:.2f} € + Bonus Gold = {bonus_gold_cap:.2f} € → Totale = {profitto_bookie_con_bonus:.2f} €")
print(f"💰 In caso di SCONFITTA o pareggio → Profitto netto = {profitto_exchange:.2f} €")

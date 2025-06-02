# matched_betting_bonus_gold.py

# Parametri modificabili
puntata = 5.41             # Puntata sulla quota maggiorata
quota_promo = 4.5
quota_reale = 2.65
quota_lay = 2.8
commissione_lay = 0.05     # 5%
bonus_gold_cap = 10        # Max bonus gold

# Calcolo del bonus previsto
bonus_gold = puntata * (quota_promo - quota_reale)
bonus_gold_effettivo = min(bonus_gold, bonus_gold_cap)

# Calcolo bancata equal profit
lay_stake = (puntata * quota_reale) / (quota_lay - commissione_lay)

# Responsabilità sull'exchange
responsabilita = lay_stake * (quota_lay - 1)

# Profitto se Inter NON vince (vittoria su Exchange)
profitto_exchange = lay_stake * (1 - commissione_lay) - puntata

# Profitto se Inter vince (bonus incluso)
guadagno_lordo = puntata * quota_promo
profitto_bookie = guadagno_lordo - responsabilita
profitto_bookie_con_bonus = profitto_bookie + bonus_gold_effettivo

# Output
print(f"--- STRATEGIA MATCHED BETTING ---")
print(f"Punta {puntata:.2f} € su SNAI a quota maggiorata {quota_promo}")
print(f"Banca {lay_stake:.2f} € su Exchange a quota {quota_lay} (commissione {commissione_lay*100:.0f}%)")
print(f"Responsabilità Exchange: {responsabilita:.2f} €")
print()
print(f"In caso di VITTORIA INTER → Profitto = {profitto_bookie:.2f} € + Bonus Gold = {bonus_gold_effettivo:.2f} € → Totale = {profitto_bookie_con_bonus:.2f} €")
print(f"In caso di SCONFITTA o pareggio → Profitto netto = {profitto_exchange:.2f} €")

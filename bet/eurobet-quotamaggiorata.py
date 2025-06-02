def calcola_bancate_equal_profit(puntata_book, quota_book, quote_banca, commissione=0.0):
    vincita_lorda = puntata_book * quota_book
    bancate = {}
    responsabilita_tot = 0

    # Calcolo stake bancate per equal profit
    # Formula: responsabilità su ciascun evento = vincita_combo / n_eventi_coperti
    responsabilita_target = vincita_lorda / len(quote_banca)

    for risultato, quota in quote_banca.items():
        responsabilita = responsabilita_target
        stake_banca = responsabilita / (quota - 1)
        perdita_combo_vinta = stake_banca * (quota - 1)
        perdita_banca = puntata_book
        profitto_se_combo_vince = vincita_lorda - perdita_combo_vinta
        profitto_se_combo_perde = stake_banca * (1 - commissione)
        bancate[risultato] = {
            'quota_banca': quota,
            'stake_banca': stake_banca,
            'responsabilita': responsabilita,
            'profitto_combo_vince': profitto_se_combo_vince,
            'profitto_combo_perde': profitto_se_combo_perde,
        }
        responsabilita_tot += responsabilita

    return bancate, vincita_lorda, responsabilita_tot


# ESEMPIO DI UTILIZZO
if __name__ == "__main__":
    puntata = 20.0
    quota_combo = 4.4
    quote_banca = {
        "1-1": 8.4,
        "2-2": 16.0,
        "3-3": 70.0
    }
    commissione = 0.0  # oppure 0.05 per 5%

    bancate, vincita_combo, responsabilita_tot = calcola_bancate_equal_profit(puntata, quota_combo, quote_banca, commissione)

    print(f"Puntata sulla combo: {puntata} € @ {quota_combo} → Vincita lorda: {vincita_combo:.2f} €")
    print(f"Responsabilità totale sulle bancate: {responsabilita_tot:.2f} €\n")

    for risultato, dati in bancate.items():
        print(f"📌 {risultato}")
        print(f"  - Quota banca: {dati['quota_banca']}")
        print(f"  - Stake banca: {dati['stake_banca']:.2f} €")
        print(f"  - Responsabilità: {dati['responsabilita']:.2f} €")
        print(f"  - Profitto se vince la combo (e questo è il risultato): {dati['profitto_combo_vince']:.2f} €")
        print(f"  - Profitto se la combo perde e questa bancata vince: {dati['profitto_combo_perde']:.2f} €\n")

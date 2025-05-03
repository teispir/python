def matched_betting_ottimizzato(
    book_odds=6.0,
    real_odds=4.1,
    lay_odds=4.6,
    commission=0.045,
    bonus_cap=10.0,
    stake_min=1.0,
    stake_max=10.0,
    stake_step=0.1
):
    best_result = {
        "stake_book": 0,
        "lay_stake": 0,
        "profit": -float("inf"),
        "book_profit": 0,
        "exchange_profit": 0,
        "bonus_gold": 0,
        "liability": 0
    }

    stake = stake_min
    while stake <= stake_max:
        theoretical_bonus = stake * (book_odds - real_odds)
        bonus_gold = min(theoretical_bonus, bonus_cap)

        best_diff = float("inf")
        best_local = {}

        lay_start = stake
        lay_end = stake * 3
        lay_step = 0.01

        lay = lay_start
        while lay <= lay_end:
            liability = lay * (lay_odds - 1)
            real_win = stake * real_odds
            book_profit = real_win - stake + bonus_gold - liability
            exchange_profit = lay * (1 - commission) - stake
            diff = abs(book_profit - exchange_profit)

            if diff < best_diff:
                best_diff = diff
                best_local = {
                    "lay_stake": lay,
                    "profit": (book_profit + exchange_profit) / 2,
                    "book_profit": book_profit,
                    "exchange_profit": exchange_profit,
                    "bonus_gold": bonus_gold,
                    "liability": liability
                }

            lay += lay_step

        if best_local["profit"] > best_result["profit"]:
            best_result.update({
                "stake_book": round(stake, 2),
                "lay_stake": round(best_local["lay_stake"], 2),
                "profit": round(best_local["profit"], 2),
                "book_profit": round(best_local["book_profit"], 2),
                "exchange_profit": round(best_local["exchange_profit"], 2),
                "bonus_gold": round(best_local["bonus_gold"], 2),
                "liability": round(best_local["liability"], 2)
            })

        stake = round(stake + stake_step, 2)

    print("\n📊 Analisi Matched Betting con Superquota")
    print("─────────────────────────────────────────────")
    print(f"▶ Puntata Bookmaker: {best_result['stake_book']} € a quota maggiorata {book_odds}")
    print(f"▶ Quota reale: {real_odds}, Quota Exchange (lay): {lay_odds}, Commissione: {commission * 100:.1f}%")
    print(f"▶ Bonus teorico: {round(best_result['stake_book'] * (book_odds - real_odds), 2)} €, Bonus riconosciuto (cap): {best_result['bonus_gold']} €")
    if best_result['bonus_gold'] < round(best_result['stake_book'] * (book_odds - real_odds), 2):
        print("⚠️  Parte del bonus è sprecata a causa del limite massimo.")

    print(f"\n✅ Lay Stake ottimale (equal profit): {best_result['lay_stake']} €")
    print(f"💥 Responsabilità su Exchange: {best_result['liability']} €")

    print("\n📈 Scenario 1: Vittoria sul Bookmaker")
    print(f"  • Vincita reale: {round(best_result['stake_book'] * real_odds - best_result['stake_book'], 2)} €")
    print(f"  • Bonus Gold: {best_result['bonus_gold']} €")
    print(f"  • Totale incasso: {round(best_result['stake_book'] * real_odds - best_result['stake_book'] + best_result['bonus_gold'], 2)} €")
    print(f"  • Meno responsabilità Exchange: -{best_result['liability']} €")
    print(f"  ⇒ Guadagno netto: {best_result['book_profit']} €")

    print("\n📉 Scenario 2: Vittoria su Exchange")
    print(f"  • Incasso Exchange: {round(best_result['lay_stake'] * (1 - commission), 2)} €")
    print(f"  • Meno puntata Bookmaker: -{best_result['stake_book']} €")
    print(f"  ⇒ Guadagno netto: {best_result['exchange_profit']} €")

    print(f"\n💰 Profitto netto stimato (Equal Profit): {best_result['profit']} €\n")

# Esegui la funzione principale
if __name__ == "__main__":
    matched_betting_ottimizzato()

def matched_betting_superquota(
    stake_book: float,
    book_odds: float,
    real_odds: float,
    lay_odds: float,
    commission: float,
    bonus_cap: float
):
    # Calcolo bonus teorico e applicazione cap
    theoretical_bonus = stake_book * (book_odds - real_odds)
    bonus_gold = min(theoretical_bonus, bonus_cap)

    # Lay stake ottimizzato per equal profit
    best_diff = float('inf')
    best_lay_stake = 0
    best_profit = None
    best_book_profit = 0
    best_exchange_profit = 0

    for lay_stake in [x / 100 for x in range(800, 2001)]:
        liability = lay_stake * (lay_odds - 1)

        # Scenario 1: Vince bookmaker
        book_return = stake_book * real_odds
        book_profit = book_return + bonus_gold - liability  # stake non incluso

        # Scenario 2: Vince exchange
        exchange_profit = lay_stake * (1 - commission) - stake_book

        diff = abs(book_profit - exchange_profit)

        if diff < best_diff:
            best_diff = diff
            best_lay_stake = lay_stake
            best_profit = (book_profit + exchange_profit) / 2
            best_book_profit = book_profit
            best_exchange_profit = exchange_profit

    # Output dettagliato
    print("\n📊 Analisi Matched Betting con Superquota")
    print("─────────────────────────────────────────────")
    print(f"▶ Puntata Bookmaker: {stake_book:.2f} € a quota maggiorata {book_odds}")
    print(f"▶ Quota reale: {real_odds}, Quota Exchange (lay): {lay_odds}, Commissione: {commission * 100:.1f}%")
    print(f"▶ Bonus teorico: {theoretical_bonus:.2f} €, Bonus riconosciuto (cap): {bonus_gold:.2f} €")
    if theoretical_bonus > bonus_cap:
        print("⚠️  Parte del bonus è sprecata a causa del limite massimo.")

    print(f"\n✅ Lay Stake ottimale (equal profit): {best_lay_stake:.2f} €")
    liability = best_lay_stake * (lay_odds - 1)
    print(f"💥 Responsabilità su Exchange: {liability:.2f} €")

    print("\n📈 Scenario 1: Vittoria sul Bookmaker")
    print(f"  • Vincita reale: {stake_book * real_odds:.2f} €")
    print(f"  • Bonus Gold: {bonus_gold:.2f} €")
    print(f"  • Totale incasso: {(stake_book * real_odds + bonus_gold):.2f} €")
    print(f"  • Meno responsabilità Exchange: -{liability:.2f} €")
    print(f"  ⇒ Guadagno netto: {best_book_profit:.2f} €")

    print("\n📉 Scenario 2: Vittoria su Exchange")
    exchange_return = best_lay_stake * (1 - commission)
    print(f"  • Incasso Exchange: {exchange_return:.2f} €")
    print(f"  • Meno puntata Bookmaker: -{stake_book:.2f} €")
    print(f"  ⇒ Guadagno netto: {best_exchange_profit:.2f} €")

    print("\n💰 Profitto netto stimato (Equal Profit): {:.2f} €\n".format(best_profit))


# ESEMPIO DI USO — dati dell'Inter-Barcellona
matched_betting_superquota(
    stake_book=5.5,
    book_odds=6.0,
    real_odds=4.10,
    lay_odds=4.6,
    commission=0.045,
    bonus_cap=10
)

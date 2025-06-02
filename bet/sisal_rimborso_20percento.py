def lay_stake_equal_profit(back_odds, lay_odds, back_stake, commission):
    return (back_odds * back_stake) / (lay_odds - commission)

def lay_liability(lay_stake, lay_odds):
    return lay_stake * (lay_odds - 1)

def calc_profit_equal(back_stake, back1, lay1, back2, lay2, commission, cashback_cap):
    # Rimborso massimo 20% fino a cap
    cashback = min(0.2 * back_stake, cashback_cap)

    # STEP 1 - Banca Evento 1
    lay1_stake = lay_stake_equal_profit(back1, lay1, back_stake, commission)
    lay1_liab = lay_liability(lay1_stake, lay1)

    # Se il primo evento perde ⇒ cashback + vincita da lay1
    profit_exchange_if_lose1 = lay1_stake * (1 - commission) - back_stake + cashback

    # Se il primo evento vince ⇒ si bancherà il secondo evento

    # STEP 2 - Banca Evento 2 (progressivo)
    total_odds = back1 * back2
    win_book_profit = (back_stake * total_odds) - back_stake

    # Dobbiamo trovare lay2_stake che bilancia perfettamente con lo scenario precedente

    # Uguagliamo profitto:
    # Profitto book - responsabilità 1 e 2 = profitto_exchange_if_lose1
    # ⇒ win_book_profit - lay1_liab - lay2_liab = profit_exchange_if_lose1
    target_profit = profit_exchange_if_lose1
    lay2_liab = win_book_profit - lay1_liab - target_profit
    lay2_stake = lay2_liab / (lay2 - 1)

    # Calcolo vincita se multipla perde dopo evento 2 (quindi entrambe le bancate vincenti)
    lay2_win = lay2_stake * (1 - commission)
    profit_exchange_if_lose2 = lay1_stake * (1 - commission) + lay2_win - back_stake + cashback

    # Profitto se multipla vince:
    profit_book = win_book_profit - lay1_liab - lay2_liab

    print(f"\n🎯 Stake multipla bookmaker: {back_stake:.2f} €")
    print(f"Quota multipla: {total_odds:.2f}")
    print(f"Rimborso in caso di perdita: {cashback:.2f} €")
    print("\n📌 Evento 1:")
    print(f"  Lay stake: {lay1_stake:.2f} €, Liability: {lay1_liab:.2f} €")
    print("\n📌 Evento 2 (solo se Evento 1 vinto):")
    print(f"  Lay stake: {lay2_stake:.2f} €, Liability: {lay2_liab:.2f} €")
    print("\n💰 PROFITTI NEI DUE SCENARI:")
    print(f"  ✔ Multipla vinta (bookmaker): {profit_book:.2f} €")
    print(f"  ✔ Multipla persa (exchange + cashback): {profit_exchange_if_lose2:.2f} €")

if __name__ == "__main__":
    # Quote esempio
    back1 = 1.48
    lay1 = 1.64
    back2 = 1.87
    lay2 = 1.98

    back_stake = 25.00
    commission = 0.05
    cashback_cap = 5.00

    calc_profit_equal(back_stake, back1, lay1, back2, lay2, commission, cashback_cap)

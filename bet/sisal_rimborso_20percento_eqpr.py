from scipy.optimize import minimize_scalar

def lay_stake_equal_profit(back_odds, lay_odds, back_stake, commission):
    return (back_odds * back_stake) / (lay_odds - commission)

def lay_liability(lay_stake, lay_odds):
    return lay_stake * (lay_odds - 1)

def profit_difference(book_stake, back1, lay1, back2, lay2, commission, cashback_cap):
    cashback = min(0.2 * book_stake, cashback_cap)

    lay1_stake = lay_stake_equal_profit(back1, lay1, book_stake, commission)
    lay1_liab = lay_liability(lay1_stake, lay1)
    profit_if_lose1 = lay1_stake * (1 - commission) - book_stake + cashback

    combined_odds = back1 * back2
    book_win_profit = combined_odds * book_stake - book_stake

    lay2_liab = book_win_profit - lay1_liab - profit_if_lose1
    lay2_stake = lay2_liab / (lay2 - 1)
    lay2_win = lay2_stake * (1 - commission)

    profit_bookwin = book_win_profit - lay1_liab - lay2_liab
    profit_exchange = lay1_stake * (1 - commission) + lay2_win - book_stake + cashback

    return abs(profit_bookwin - profit_exchange)

def main():
    # Quote e commissione
    back1 = 1.48  # Brommapojkarna - Djurgarden (GOL)
    lay1 = 1.64
    back2 = 1.87  # Cremonese - Spezia (GOL)
    lay2 = 1.98
    commission = 0.045
    cashback_cap = 5.00

    # Ottimizza lo stake sul bookmaker per equal profit
    result = minimize_scalar(
        profit_difference,
        bounds=(5, 25),
        method='bounded',
        args=(back1, lay1, back2, lay2, commission, cashback_cap)
    )

    stake = round(result.x, 2)
    cashback = min(0.2 * stake, cashback_cap)

    # Calcoli finali
    lay1_stake = lay_stake_equal_profit(back1, lay1, stake, commission)
    lay1_liab = lay_liability(lay1_stake, lay1)
    profit_if_lose1 = lay1_stake * (1 - commission) - stake + cashback

    combined_odds = back1 * back2
    book_win_profit = combined_odds * stake - stake

    lay2_liab = book_win_profit - lay1_liab - profit_if_lose1
    lay2_stake = lay2_liab / (lay2 - 1)
    lay2_win = lay2_stake * (1 - commission)

    profit_bookwin = book_win_profit - lay1_liab - lay2_liab
    profit_exchange = lay1_stake * (1 - commission) + lay2_win - stake + cashback

    # Output
    print("\n🎯 STRATEGIA MATCHED BETTING - SISAL Equal Profit (Progressiva)")
    print("-------------------------------------------------------------")
    print(f"✅ Stake sul bookmaker: {stake:.2f} €")
    print(f"✅ Cashback previsto: {cashback:.2f} € (20%)")
    print(f"✅ Quota multipla: {combined_odds:.2f}")
    print("\n📌 Evento 1 (lay subito):")
    print(f"  Lay stake: {lay1_stake:.2f} €")
    print(f"  Liability: {lay1_liab:.2f} €")
    print("\n📌 Evento 2 (lay solo se Evento 1 è vinto):")
    print(f"  Lay stake: {lay2_stake:.2f} €")
    print(f"  Liability: {lay2_liab:.2f} €")
    print("\n💰 PROFITTO FINALE NEI DUE SCENARI:")
    print(f"  ✔ Multipla vinta (bookmaker): {profit_bookwin:.2f} €")
    print(f"  ✔ Multipla persa (exchange + cashback): {profit_exchange:.2f} €")
    print("-------------------------------------------------------------")

if __name__ == "__main__":
    main()
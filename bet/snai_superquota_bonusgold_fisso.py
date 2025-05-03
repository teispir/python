import matplotlib.pyplot as plt

# Parametri fissi
back_stake = 10
book_odds = 6.00
real_odds = 4.10
commission = 0.045
bonus_cap = 10

lay_odds_range = [x / 100 for x in range(440, 501)]  # da 4.40 a 5.00
profits = []

# Calcolo del profitto equal per ogni quota exchange
for lay_odds in lay_odds_range:
    best_diff = float('inf')
    best_profit = 0

    for lay_stake in [x / 100 for x in range(800, 1500)]:
        liability = lay_stake * (lay_odds - 1)
        bonus = min(back_stake * (book_odds - real_odds), bonus_cap)

        book_profit = (back_stake * real_odds + bonus) - liability
        exchange_profit = lay_stake * (1 - commission) - back_stake
        diff = abs(book_profit - exchange_profit)

        if diff < best_diff:
            best_diff = diff
            best_profit = (book_profit + exchange_profit) / 2

    profits.append(best_profit)

# Grafico
plt.figure(figsize=(10, 6))
plt.plot(lay_odds_range, profits, marker='o', linestyle='-', color='royalblue')
plt.title("Matched Betting Profitto Equal vs Quota Exchange", fontsize=14)
plt.xlabel("Quota Exchange (lay)", fontsize=12)
plt.ylabel("Profitto Equal (€)", fontsize=12)
plt.grid(True)
plt.axhline(0, color='gray', linestyle='--')
plt.tight_layout()
plt.show()

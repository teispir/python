import numpy as np
import matplotlib.pyplot as plt

# Parametri noti
real_bonus = 20.58
profit_target = 15.38
max_loss = real_bonus - profit_target
min_odds_per_event = 1.50
commission = 0.05  # Commissione exchange del 5%

# Gamma di spread assoluti da testare (differenza tra quota book e quota exchange per evento)
spreads = np.linspace(0.01, 0.50, 100)
losses = []

for spread in spreads:
    # Quote bookmaker (tutte uguali a 1.50)
    book_odds = np.array([min_odds_per_event] * 3)
    # Quote exchange = quote book + spread
    lay_odds = book_odds + spread
    # Quota totale della multipla (bookmaker)
    combined_back_odds = np.prod(book_odds)
    # Quota totale della multipla (exchange)
    combined_lay_odds = np.prod(lay_odds)
    
    # Puntata = bonus
    stake = real_bonus
    # Calcolo responsabilità su exchange con commissione
    lay_stake = stake * combined_back_odds / (combined_lay_odds - commission * (combined_lay_odds - 1))
    liability = lay_stake * (combined_lay_odds - 1)
    
    # In caso vinca la multipla sul book: si vincono stake * quota multipla
    win_book = stake * combined_back_odds
    # In caso vinca la bancata: si incassa il lay stake meno la commissione
    win_exchange = lay_stake * (1 - commission)
    
    # Passivo peggiore (quello che ci interessa): quando vince la multipla e si perde la responsabilità
    worst_case_profit = win_book - liability - stake
    loss = -worst_case_profit
    losses.append(loss)

# Trova lo spread massimo che non supera la perdita consentita
max_allowed_spread = spreads[np.array(losses) <= max_loss].max()

# Grafico
plt.figure(figsize=(10, 6))
plt.plot(spreads, losses, label='Passivo finale (peggiore dei casi)')
plt.axhline(max_loss, color='red', linestyle='--', label=f'Limite massimo perdita = {max_loss:.2f} €')
plt.axvline(max_allowed_spread, color='green', linestyle='--', label=f'Spread massimo consentito ≈ {max_allowed_spread:.3f}')
plt.xlabel('Spread assoluto medio per evento (quota exchange - quota book)')
plt.ylabel('Perdita massima in caso di vittoria multipla')
plt.title('Perdita in funzione dello spread medio per evento (tripla quota 1.50)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

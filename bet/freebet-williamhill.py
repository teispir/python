def calcola_lay_snr_equal_profit(freebet, back_odds, lay_odds, commission_percent=5.0):
    commission = commission_percent / 100
    lay_stake = (freebet * (back_odds - 1)) / (lay_odds - lay_odds * commission)

    liability = lay_stake * (lay_odds - 1)
    profit_bookmaker = freebet * (back_odds - 1) - liability
    profit_exchange = lay_stake * (1 - commission)

    return lay_stake, profit_bookmaker, profit_exchange


def main():
    print("🎯 Calcolatore Freebet (SNR) - Equal Profit Corretta\n")

    try:
        freebet = float(input("Inserisci l'importo della freebet (€): "))
        back_odds = float(input("Inserisci la quota BACK (Bookmaker): "))
        lay_odds = float(input("Inserisci la quota LAY (Exchange): "))
        commission = float(input("Inserisci la commissione Exchange (%) [default 5]: ") or 5)

        lay_stake, profit_bookmaker, profit_exchange = calcola_lay_snr_equal_profit(
            freebet, back_odds, lay_odds, commission
        )

        print("\n📊 Risultati:")
        print(f"👉 Lay Stake per Equal Profit: {lay_stake:.2f} €")
        print(f"✅ Profitto se vince il Bookmaker: {profit_bookmaker:.2f} €")
        print(f"✅ Profitto se vince l'Exchange: {profit_exchange:.2f} €")
        print(f"💡 Equal Profit: {abs(profit_bookmaker - profit_exchange) < 0.05}")
        print(f"🔄 Percentuale di conversione: {min(profit_bookmaker, profit_exchange) / freebet * 100:.2f}%")

    except ValueError:
        print("❌ Errore: Inserisci solo numeri validi.")

if __name__ == "__main__":
    main()

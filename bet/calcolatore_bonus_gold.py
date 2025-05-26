
def calcola_profitto_netto(bonus, perdita_precedente, commissione):
    stake_lay = bonus
    profitto_exchange = stake_lay * (1 - commissione)
    responsabilita_minima = stake_lay * (1.01 - 1)  # lay minima ipotetica
    profitto_netto = profitto_exchange - perdita_precedente
    return profitto_netto, responsabilita_minima

def calcola_responsabilita(stake_lay, quota_lay):
    return stake_lay * (quota_lay - 1)

def main():
    print("=== Calcolatore Profitto Netto Bonus Gold ===")
    try:
        bonus = float(input("Inserisci l'importo del bonus (€): "))
        perdita = float(input("Inserisci il passivo exchange accumulato (€): "))
        commissione = float(input("Inserisci la commissione exchange (es. 0.05 per 5%): "))

        profitto, responsabilita_min = calcola_profitto_netto(bonus, perdita, commissione)

        print(f"\n💰 Profitto netto atteso (se perdi la multipla al primo evento): {profitto:.2f} €")
        print(f"📉 Responsabilità minima teorica (lay 1.01): {responsabilita_min:.2f} €")

        scelta = input("\nVuoi calcolare la responsabilità per una quota Lay specifica? (s/n): ").strip().lower()
        if scelta == 's':
            quota_lay = float(input("Inserisci la quota Lay dell'evento bancato: "))
            responsabilita = calcola_responsabilita(bonus, quota_lay)
            print(f"📌 Responsabilità per quota Lay {quota_lay}: {responsabilita:.2f} €")

    except ValueError:
        print("Errore: inserisci solo numeri validi.")

if __name__ == "__main__":
    main()

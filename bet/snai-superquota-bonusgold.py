def calcola_strategia_super_quota(
    quota_snai: float,
    quota_reale: float,
    max_bonus: float,
    quota_banca: float,
    commissione_exchange: float = 0.0
):
    # Calcolo puntata ideale su SNAI per ricevere il massimo bonus
    puntata_snai = max_bonus / (quota_snai - quota_reale)

    # Vincita cash (parte reale della quota)
    vincita_cash = puntata_snai * quota_reale

    # Bonus Gold
    bonus_gold = min(puntata_snai * (quota_snai - quota_reale), max_bonus)

    # Importo da bancare per coprire vincita cash
    importo_bancato = vincita_cash / (quota_banca - 1)
    responsabilita = importo_bancato * (quota_banca - 1)

    # Guadagno in caso di vittoria Inter (Bonus)
    profitto_vittoria = vincita_cash - responsabilita
    totale_bonus = bonus_gold

    # Guadagno in caso di NON vittoria Inter (cash)
    vincita_banca = importo_bancato * (1 - commissione_exchange)
    profitto_non_vittoria = vincita_banca - puntata_snai

    # Output
    print(f"\n--- STRATEGIA OTTIMALE ---")
    print(f"Punta su SNAI:         €{puntata_snai:.2f} @ quota {quota_snai}")
    print(f"Banca su Exchange:     €{importo_bancato:.2f} @ quota {quota_banca} (Responsabilità: €{responsabilita:.2f})")
    print(f"\n💰 In caso di VITTORIA Inter:")
    print(f"  +€{vincita_cash:.2f} cash su SNAI")
    print(f"  -€{responsabilita:.2f} responsabilità Exchange")
    print(f"  => Profitto netto: €{profitto_vittoria:.2f} cash + €{bonus_gold:.2f} Bonus Gold")

    print(f"\n💸 In caso di NON vittoria Inter:")
    print(f"  -€{puntata_snai:.2f} su SNAI")
    print(f"  +€{vincita_banca:.2f} su Exchange")
    print(f"  => Profitto netto: €{profitto_non_vittoria:.2f} cash")

# Esempio di utilizzo con i tuoi dati:
calcola_strategia_super_quota(
    quota_snai=7.00,
    quota_reale=3.80,
    max_bonus=10.00,
    quota_banca=4.20,
    commissione_exchange=0.045  # 4.5% tipica su Betfair
)
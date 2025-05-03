def calcolo_snai_bonus_gold(
    stake_snai,
    quota_snai,
    quota_lay,
    commissione_lay=0.05,
    valore_bonus_percent=0.7,
    prob_3gol=0.65,
):
    # Calcolo della responsabilità e del profitto
    lay_stake = (stake_snai * quota_snai) / (quota_lay - commissione_lay)
    responsabilità = lay_stake * (quota_lay - 1)

    # Scenario 1: Vinci su SNAI
    profit_snai = (stake_snai * quota_snai) - stake_snai
    perdita_exchange = -responsabilità
    netto1 = profit_snai + perdita_exchange

    # Scenario 2: Perdi su SNAI - meno di 3 gol
    vincita_exchange = lay_stake * (1 - commissione_lay)
    perdita_snai = -stake_snai
    netto2 = vincita_exchange + perdita_snai

    # Scenario 3: Perdi su SNAI - almeno 3 gol
    bonus_gold = stake_snai * 0.20
    bonus_convertito = bonus_gold * valore_bonus_percent
    netto3 = vincita_exchange + perdita_snai + bonus_convertito

    # Valore atteso
    ev = (1 - prob_3gol) * netto2 + prob_3gol * netto3

    # Output
    print("== RISULTATI ==")
    print(f"Scenario 1 (Vinci su SNAI): {netto1:.2f} €")
    print(f"Scenario 2 (Perdi senza bonus): {netto2:.2f} €")
    print(f"Scenario 3 (Perdi con bonus): {netto3:.2f} €")
    print(f"\nValore Atteso (EV): {ev:.2f} €")
    print(f"Responsabilità exchange: {responsabilità:.2f} €")


# ESEMPIO D'USO
calcolo_snai_bonus_gold(
    stake_snai=100,
    quota_snai=3.5,
    quota_lay=3.6,
    commissione_lay=0.045,
    valore_bonus_percent=0.7,
    prob_3gol=0.65  # probabilità stimata che ci siano almeno 3 gol
)

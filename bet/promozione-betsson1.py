def copertura_totale(eventi, stake, commissione):
    quota_combinata = 1
    print("\n📘 Copertura Totale:\n")
    for i, evento in enumerate(eventi):
        quota_combinata *= evento["quota_book"]
        vincita_potenziale = stake * quota_combinata
        lay_odds = evento["quota_exchange"]
        lay_stake = vincita_potenziale / (lay_odds - commissione)
        responsabilita = lay_stake * (lay_odds - 1)

        print(f"{i+1}. {evento['nome']}")
        print(f"   Quota combinata: {round(quota_combinata, 2)}")
        print(f"   Lay Stake: {round(lay_stake, 2)} €")
        print(f"   Responsabilità: {round(responsabilita, 2)} €\n")

def copertura_incrementale(eventi, stake, commissione):
    quota_parziale = 1
    print("\n📗 Copertura Incrementale / Equal Profit:\n")
    for i, evento in enumerate(eventi):
        back_odds = evento["quota_book"]
        lay_odds = evento["quota_exchange"]
        quota_parziale *= back_odds
        profitto = stake * (quota_parziale - 1)
        lay_stake = profitto / (lay_odds - commissione)
        responsabilita = lay_stake * (lay_odds - 1)

        print(f"{i+1}. {evento['nome']}")
        print(f"   Profitto incrementale da coprire: {round(profitto, 2)} €")
        print(f"   Lay Stake: {round(lay_stake, 2)} €")
        print(f"   Responsabilità: {round(responsabilita, 2)} €\n")

def copertura_bonus_netto(eventi, stake, commissione, bonus_totale):
    quota_combinata = 1
    print("\n🟩 Copertura finale considerando il Bonus previsto:\n")

    for i in range(len(eventi) - 1):
        quota_combinata *= eventi[i]["quota_book"]

    vincita_attesa = stake * quota_combinata * eventi[-1]["quota_book"]
    lay_odds = eventi[-1]["quota_exchange"]

    lay_stake = (vincita_attesa - bonus_totale) / (lay_odds - commissione)
    responsabilita = lay_stake * (lay_odds - 1)

    print(f"{len(eventi)}. {eventi[-1]['nome']} (finale, con bonus)")
    print(f"   Vincita attesa: {round(vincita_attesa, 2)} €")
    print(f"   Bonus previsto: {bonus_totale} €")
    print(f"   Lay Stake finale: {round(lay_stake, 2)} €")
    print(f"   Responsabilità: {round(responsabilita, 2)} €\n")


eventi = [
    {"nome": "Torino - Udinese GOAL", "quota_book": 2.00, "quota_exchange": 2.18},
    {"nome": "Cagliari - Fiorentina OVER 2.5", "quota_book": 2.10, "quota_exchange": 2.34},
    {"nome": "Genoa - Lazio OVER 2.5", "quota_book": 2.22, "quota_exchange": 2.52},
    {"nome": "Parma - Juventus UNDER 1.5", "quota_book": 3.20, "quota_exchange": 3.90}]

stake_iniziale = 10
commissione = 0.045  # 4.5%
bonus_per_goal = 2
goal_previsti = 5  # ad es. 5 goal totali nella multipla
bonus_totale = goal_previsti * bonus_per_goal

copertura_totale(eventi, stake_iniziale, commissione)
copertura_incrementale(eventi, stake_iniziale, commissione)
copertura_bonus_netto(eventi, stake_iniziale, commissione, bonus_totale)
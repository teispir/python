
import tkinter as tk
from tkinter import messagebox

def calcola_bonus_snai():
    try:
        stake_snai = float(entry_stake.get())
        quota_snai = float(entry_quota_snai.get())
        quota_lay = float(entry_quota_lay.get())
        commissione_lay = float(entry_commissione.get()) / 100
        valore_bonus_percent = float(entry_valore_bonus.get()) / 100
        prob_3gol = float(entry_prob_gol.get()) / 100

        lay_stake = (stake_snai * quota_snai) / (quota_lay - commissione_lay)
        responsabilita = lay_stake * (quota_lay - 1)

        profit_snai = (stake_snai * quota_snai) - stake_snai
        perdita_exchange = -responsabilita
        netto1 = profit_snai + perdita_exchange

        vincita_exchange = lay_stake * (1 - commissione_lay)
        perdita_snai = -stake_snai
        netto2 = vincita_exchange + perdita_snai

        bonus_gold = stake_snai * 0.20
        bonus_convertito = bonus_gold * valore_bonus_percent
        netto3 = vincita_exchange + perdita_snai + bonus_convertito

        ev = (1 - prob_3gol) * netto2 + prob_3gol * netto3

        risultato = (
            f"Scenario 1 (Vinci su SNAI): {netto1:.2f} €\n"
            f"Scenario 2 (Perdi senza bonus): {netto2:.2f} €\n"
            f"Scenario 3 (Perdi con bonus): {netto3:.2f} €\n\n"
            f"Valore Atteso (EV): {ev:.2f} €\n"
            f"Responsabilità exchange: {responsabilita:.2f} €"
        )

        messagebox.showinfo("Risultati", risultato)

    except ValueError:
        messagebox.showerror("Errore", "Inserisci solo numeri validi.")

# GUI Setup
app = tk.Tk()
app.title("Calcolatore Bonus SNAI - Match Betting")

tk.Label(app, text="Puntata su SNAI (€)").grid(row=0, column=0, sticky="w")
entry_stake = tk.Entry(app)
entry_stake.grid(row=0, column=1)

tk.Label(app, text="Quota su SNAI").grid(row=1, column=0, sticky="w")
entry_quota_snai = tk.Entry(app)
entry_quota_snai.grid(row=1, column=1)

tk.Label(app, text="Quota Lay sull'exchange").grid(row=2, column=0, sticky="w")
entry_quota_lay = tk.Entry(app)
entry_quota_lay.grid(row=2, column=1)

tk.Label(app, text="Commissione exchange (%)").grid(row=3, column=0, sticky="w")
entry_commissione = tk.Entry(app)
entry_commissione.insert(0, "5")
entry_commissione.grid(row=3, column=1)

tk.Label(app, text="Valore bonus convertito (%)").grid(row=4, column=0, sticky="w")
entry_valore_bonus = tk.Entry(app)
entry_valore_bonus.insert(0, "70")
entry_valore_bonus.grid(row=4, column=1)

tk.Label(app, text="Probabilità 3+ gol (%)").grid(row=5, column=0, sticky="w")
entry_prob_gol = tk.Entry(app)
entry_prob_gol.insert(0, "65")
entry_prob_gol.grid(row=5, column=1)

tk.Button(app, text="Calcola", command=calcola_bonus_snai).grid(row=6, column=0, columnspan=2, pady=10)

app.mainloop()

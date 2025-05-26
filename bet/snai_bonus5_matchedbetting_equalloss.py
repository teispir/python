import itertools
import csv
from scipy.optimize import minimize
import tkinter as tk
from tkinter import messagebox

# Parametri iniziali
def get_initial_data():
    return {
        "book_stake": 10,
        "book_odds": [1.61, 1.80, 1.80],
        "lay_odds": [1.69, 1.84, 1.89],
        "commission": 0,
        "bonus": 5
    }

def calculate_profit(scenario, lay_stakes, data):
    profit_exchange = 0
    for i in range(3):
        lay_odd = data["lay_odds"][i]
        lay_stake = lay_stakes[i]
        if scenario[i] == 1:  # persa su exchange
            liability = (lay_odd - 1) * lay_stake
            profit_exchange -= liability
        else:  # vinta su exchange
            profit_exchange += lay_stake * (1 - data["commission"])

    book_win = data["book_stake"] * data["book_odds"][0] * data["book_odds"][1] * data["book_odds"][2]
    profit_book = book_win if sum(scenario) == 3 else 0
    return profit_book + data["bonus"] - data["book_stake"] + profit_exchange

def variance_objective(lay_stakes, data):
    scenarios = list(itertools.product([0, 1], repeat=3))
    profits = [calculate_profit(s, lay_stakes, data) for s in scenarios]
    mean_profit = sum(profits) / len(profits)
    return sum((p - mean_profit) ** 2 for p in profits) / len(profits)

def optimize_lay_stakes(data):
    result = minimize(variance_objective, [10, 10, 10], args=(data,), bounds=[(0, 50)] * 3)
    return result.x

def save_to_csv(scenarios, profits):
    with open("risultati_equal_loss.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Scenario", "Profitto Netto (€)"])
        for s, p in zip(scenarios, profits):
            writer.writerow(["-".join(map(str, s)), f"{p:.2f}"])

def stampa_risultati(data, lay_stakes):
    scenarios = list(itertools.product([0, 1], repeat=3))
    profits = [calculate_profit(s, lay_stakes, data) for s in scenarios]
    mean_profit = sum(profits) / len(profits)

    print("\nLay stake ottimali:")
    for i, stake in enumerate(lay_stakes, 1):
        print(f"  Partita {i}: {stake:.2f} €")

    print("\nProfitti netti in ogni scenario (V=vinta sul Book):")
    for s, p in zip(scenarios, profits):
        print(f"  {s} → {p:.2f} €")

    print(f"\nProfitto medio atteso: {mean_profit:.2f} €")
    save_to_csv(scenarios, profits)
    print("\n✔️ Risultati salvati su 'risultati_equal_loss.csv'")

# Interfaccia grafica opzionale
class EqualLossGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Equal Loss Matched Betting")
        self.entries = {}
        fields = ["book_stake", "bonus", "commission"] + [f"book_odds_{i+1}" for i in range(3)] + [f"lay_odds_{i+1}" for i in range(3)]

        for i, field in enumerate(fields):
            tk.Label(root, text=field.replace("_", " ")).grid(row=i, column=0, sticky=tk.W)
            entry = tk.Entry(root)
            entry.grid(row=i, column=1)
            self.entries[field] = entry

        tk.Button(root, text="Calcola", command=self.calcola).grid(row=len(fields), column=0, columnspan=2)

    def calcola(self):
        try:
            data = {
                "book_stake": float(self.entries["book_stake"].get()),
                "bonus": float(self.entries["bonus"].get()),
                "commission": float(self.entries["commission"].get()),
                "book_odds": [float(self.entries[f"book_odds_{i+1}"].get()) for i in range(3)],
                "lay_odds": [float(self.entries[f"lay_odds_{i+1}"].get()) for i in range(3)]
            }
            lay_stakes = optimize_lay_stakes(data)
            stampa_risultati(data, lay_stakes)
            messagebox.showinfo("Successo", "Calcolo completato! Controlla il terminale e il file CSV.")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

# MAIN
if __name__ == "__main__":
    data = get_initial_data()
    lay_stakes = optimize_lay_stakes(data)
    stampa_risultati(data, lay_stakes)

    try:
        root = tk.Tk()
        app = EqualLossGUI(root)
        root.mainloop()
    except Exception:
        print("\nGUI non disponibile. Usa solo da terminale.")

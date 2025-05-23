import tkinter as tk
from tkinter import ttk, messagebox

def calcola_bancata_qualificante(puntata, quota_punta, quota_banca, commissione):
    bancata = (puntata * quota_punta) / (quota_banca - commissione)
    responsabilita = (quota_banca - 1) * bancata
    perdita = round(puntata - (bancata * (1 - commissione)), 2) if quota_punta < quota_banca else round((puntata * quota_punta) - responsabilita - puntata, 2)
    return round(bancata, 2), round(responsabilita, 2), perdita

def calcola_bancata_freebet(valore_freebet, quota_punta, quota_banca, commissione):
    bancata = (valore_freebet * (quota_punta - 1)) / (quota_banca - commissione)
    responsabilita = (quota_banca - 1) * bancata
    profitto_book = (valore_freebet * (quota_punta - 1)) - responsabilita
    profitto_exchange = bancata * (1 - commissione)
    return round(bancata, 2), round(responsabilita, 2), round(profitto_book, 2), round(profitto_exchange, 2)

def calcola():
    try:
        puntata = float(entry_puntata.get())
        quota_punta_q = float(entry_quota_punta_q.get())
        quota_banca_q = float(entry_quota_banca_q.get())
        valore_freebet = float(entry_valore_freebet.get())
        quota_punta_f = float(entry_quota_punta_f.get())
        quota_banca_f = float(entry_quota_banca_f.get())
        commissione = float(entry_commissione.get()) / 100

        bq, rq, perdita_q = calcola_bancata_qualificante(puntata, quota_punta_q, quota_banca_q, commissione)
        bf, rf, prof_fb_book, prof_fb_ex = calcola_bancata_freebet(valore_freebet, quota_punta_f, quota_banca_f, commissione)
        profitto_totale = round(min(prof_fb_book, prof_fb_ex) - perdita_q, 2)

        output = f"""--- QUALIFICANTE ---
Bancata: {bq} €
Responsabilità: {rq} €
Perdita: {perdita_q} €

--- FREEBET ---
Bancata: {bf} €
Responsabilità: {rf} €
Profitto se vince la punta: {prof_fb_book} €
Profitto se vince la bancata: {prof_fb_ex} €

--- PROFITTO NETTO ---
Minimo garantito: {profitto_totale} €
"""
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, output)
    except ValueError:
        messagebox.showerror("Errore", "Inserisci valori numerici validi.")

# GUI
root = tk.Tk()
root.title("Calcolatore Matched Betting - Freebet")

fields = [
    ("Puntata qualificante (€):", "10"),
    ("Quota punta qualificante:", "1.90"),
    ("Quota banca qualificante:", "2.12"),
    ("Valore Freebet (€):", "10"),
    ("Quota punta Freebet:", "5.0"),
    ("Quota banca Freebet:", "5.4"),
    ("Commissione Exchange (%):", "5")
]

entries = []
for label_text, default in fields:
    frame = ttk.Frame(root)
    frame.pack(fill='x', padx=5, pady=2)
    label = ttk.Label(frame, text=label_text, width=28)
    label.pack(side='left')
    entry = ttk.Entry(frame)
    entry.insert(0, default)
    entry.pack(side='left', expand=True, fill='x')
    entries.append(entry)

(entry_puntata, entry_quota_punta_q, entry_quota_banca_q,
 entry_valore_freebet, entry_quota_punta_f, entry_quota_banca_f,
 entry_commissione) = entries

ttk.Button(root, text="Calcola", command=calcola).pack(pady=5)

text_output = tk.Text(root, height=15, width=60)
text_output.pack(padx=5, pady=5)

root.mainloop()
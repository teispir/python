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

# --- ⚙️ Parametri iniziali modificabili ---
puntata_qualificante = 10
quota_punta_qualificante = 1.90
quota_banca_qualificante = 2.12

valore_freebet = 10
quota_punta_freebet = 5.0
quota_banca_freebet = 5.4

commissione_exchange_percento = 5
commissione = commissione_exchange_percento / 100

# --- Calcoli ---
bq, rq, perdita_q = calcola_bancata_qualificante(puntata_qualificante, quota_punta_qualificante, quota_banca_qualificante, commissione)
bf, rf, prof_fb_book, prof_fb_ex = calcola_bancata_freebet(valore_freebet, quota_punta_freebet, quota_banca_freebet, commissione)
profitto_netto = round(min(prof_fb_book, prof_fb_ex) - perdita_q, 2)

# --- Output ---
print(f"--- QUALIFICANTE ---")
print(f"Bancata: {bq} €")
print(f"Responsabilità: {rq} €")
print(f"Perdita: {perdita_q} €\n")

print(f"--- FREEBET ---")
print(f"Bancata: {bf} €")
print(f"Responsabilità: {rf} €")
print(f"Profitto se vince la punta: {prof_fb_book} €")
print(f"Profitto se vince la bancata: {prof_fb_ex} €\n")

print(f"--- PROFITTO NETTO ---")
print(f"Minimo garantito: {profitto_netto} €")

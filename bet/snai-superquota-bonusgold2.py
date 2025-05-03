import plotly.graph_objects as go

def analizza_strategie_bancate_interattivo(
    quota_snai: float,
    quota_reale: float,
    max_bonus: float,
    quote_bancata: list,
    commissione_exchange: float = 0.0
):
    puntata_snai = max_bonus / (quota_snai - quota_reale)
    vincita_cash = puntata_snai * quota_reale
    bonus_gold = min(puntata_snai * (quota_snai - quota_reale), max_bonus)

    results = []

    for q_banca in quote_bancata:
        importo_bancato = vincita_cash / (q_banca - 1)
        responsabilita = importo_bancato * (q_banca - 1)

        profitto_vittoria_cash = vincita_cash - responsabilita
        profitto_vittoria_totale = profitto_vittoria_cash + bonus_gold

        vincita_banca = importo_bancato * (1 - commissione_exchange)
        profitto_non_vittoria = vincita_banca - puntata_snai

        results.append({
            "quota_banca": q_banca,
            "importo_bancato": importo_bancato,
            "responsabilita": responsabilita,
            "profitto_vittoria": profitto_vittoria_totale,
            "profitto_non_vittoria": profitto_non_vittoria
        })

    best = max(results, key=lambda x: min(x["profitto_vittoria"], x["profitto_non_vittoria"]))

    # Dati per grafico
    x = [r["quota_banca"] for r in results]
    y_vittoria = [r["profitto_vittoria"] for r in results]
    y_non_vittoria = [r["profitto_non_vittoria"] for r in results]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x, y=y_vittoria, mode='lines+markers',
        name='Profitto se VINCE (cash + bonus)',
        line=dict(color='green'), marker=dict(size=10)
    ))

    fig.add_trace(go.Scatter(
        x=x, y=y_non_vittoria, mode='lines+markers',
        name='Profitto se NON VINCE',
        line=dict(color='red'), marker=dict(size=10)
    ))

    fig.add_trace(go.Scatter(
        x=[best["quota_banca"]], y=[best["profitto_vittoria"]],
        mode='markers+text',
        name='Strategia Ottimale',
        marker=dict(size=14, color='gold', symbol='star'),
        text=[f"⭐ {best['quota_banca']}"],
        textposition="top center"
    ))

    fig.update_layout(
        title="📈 Profitto netto in base alla quota bancata (interattivo)",
        xaxis_title="Quota Bancata Exchange",
        yaxis_title="Profitto Netto (€)",
        hovermode="x unified",
        template="plotly_white"
    )

    fig.show()

# Esempio di utilizzo
quote_bancata_test = [3.80, 4.00, 4.20, 4.40, 4.60]

analizza_strategie_bancate_interattivo(
    quota_snai=7.00,
    quota_reale=3.80,
    max_bonus=10.00,
    quote_bancata=quote_bancata_test,
    commissione_exchange=0.045
)
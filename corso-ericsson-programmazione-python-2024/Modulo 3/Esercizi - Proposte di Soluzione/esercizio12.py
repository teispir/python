sportSquadra = {"calcio", "basket", "volley", "hockey su ghiaccio", "rugby", "football", "curling"}
sportIndividuali = {"tennis", "golf", "pugilato", "atletica", "surf", "nuoto", "ciclismo", "judo"}

sportUtente = input("Inserisci il tuo sport preferito: ").lower()
if sportUtente in sportSquadra:
    print("Il tuo sport preferito è di squadra")
elif sportUtente in sportIndividuali:
    print("Il tuo sport preferito è individuale")
else:
    print("Sport non trovato")
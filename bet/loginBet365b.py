import requests
from requests.auth import HTTPBasicAuth

# URL della pagina protetta
protected_url = "https://www.bet365.it"

# Credenziali di accesso
username = "psalera365"
password = "Ma_07102001"

# Effettua una richiesta con autenticazione
response = requests.get(protected_url, auth=HTTPBasicAuth(username, password))

# Verifica la risposta
if response.status_code == 200:
    print("Accesso riuscito!")
    print(response.text)  # Mostra il contenuto della pagina
else:
    print(f"Errore nell'accesso: {response.status_code}")
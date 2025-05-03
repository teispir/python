import requests

# URL della pagina di login
login_url = "https://www.bet365.it/#/HO/"

# Credenziali di accesso
payload = {
    "username": "psalera365",
    "password": "Ma_07102001"
}

# Crea una sessione
session = requests.Session()

# Effettua il login
response = session.post(login_url, data=payload)

print(response)

# Verifica se il login è riuscito
if "Benvenuto" in response.text:
    print("Login effettuato con successo!")
else:
    print("Login fallito!")        
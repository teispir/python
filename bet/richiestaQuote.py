import requests
from bs4 import BeautifulSoup

url = "https://www.bet365.it/#/AC/B1/C1/D1002/G40/J99/I1/Q1/F^72/"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')

# Esempio: estrai le quote 1X2
quote_1 = soup.find("div", {"id": "quote1"}).text
quote_X = soup.find("div", {"id": "quoteX"}).text
quote_2 = soup.find("div", {"id": "quote2"}).text

print(f"Quote: 1: {quote_1}, X: {quote_X}, 2: {quote_2}")
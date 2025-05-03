import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Configura il driver del browser
driver = webdriver.Chrome()

# Apri l'URL protetto
url = "https://www.bet365.it/"
print("----------------1")
driver.get(url)
print("----------------2")

# Inserisci le credenziali nel pop-up
driver.switch_to.alert.send_keys("psalera365" + Keys.TAB + "Ma_07102001")
print("----------------3")
driver.switch_to.alert.accept()  # Conferma il pop-up
print("----------------4")

# Verifica se l'accesso è riuscito
if "Benvenuto" in driver.page_source:
    print("Accesso riuscito!")
else:
    print("Errore di accesso.")

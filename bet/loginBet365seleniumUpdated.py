import os
import selenium 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


username = os.getenv("BET365_USERNAME")
print("username:",username)
password = os.getenv("BET365_PASSWORD")
print("password:",password)

# Configura il driver del browser
driver = webdriver.Chrome()

# Apri il sito Bet365
url = "https://www.bet365.it/"
driver.get(url)

# Aspetta il caricamento della pagina
time.sleep(10)  # Aspetta un po' di tempo per il caricamento completo della pagina

# Trova i campi di input per username e password
username_input = driver.find_element(By.CSS_SELECTOR, ".lms-StandardLogin_InputsContainer.lms-StandardLogin_NoControl")  # Sostituisci con l'ID corretto
print("lms-StandardLogin_NoControl:",username_input)
# username_input = driver.find_element(By.ID, "lms-StandardLogin_Username")  # Sostituisci con l'ID corretto
# print("lms-StandardLogin_Username:",username_input)

password_input = driver.find_element(By.ID, "lms-StandardLogin_Password")  # Sostituisci con l'ID corretto
print("password_input:",password_input)

driver.save_screenshot("debug_page.png")

# Inserisci le credenziali
username_input.send_keys(username)
password_input.send_keys(password)

# Trova e clicca il pulsante di login
login_button = driver.find_element(By.ID, "bottone_login")  # Sostituisci con l'ID corretto
login_button.click()

# Aspetta il caricamento della pagina post-login
time.sleep(5)

# Verifica se l'accesso è riuscito
if "Benvenuto" in driver.page_source:
    print("Accesso riuscito!")
else:
    print("Errore di accesso.")

# Chiudi il browser
driver.quit()
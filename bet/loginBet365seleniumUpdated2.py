from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura il driver
driver = webdriver.Chrome()

# Vai alla pagina di login
driver.get("https://www.bet365.it/#/HO/")

try:
    # Attendi che il campo username sia visibile
    username_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "username"))  # Modifica con l'ID corretto
    )
    
    # Trova il campo password
    password_input = driver.find_element(By.ID, "password")  # Modifica con l'ID corretto

    # Inserisci credenziali
    username_input.send_keys("tuo_username")
    password_input.send_keys("tua_password")
    
    # Premi Invio o clicca sul pulsante di login
    password_input.send_keys(Keys.RETURN)

    print("Login effettuato!")

except Exception as e:
    print(f"Errore durante il login: {e}")

finally:
    driver.quit()

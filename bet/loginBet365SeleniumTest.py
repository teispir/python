from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura il driver (assicurati che il driver sia nel PATH)
driver = webdriver.Chrome()

# Vai alla pagina di login
driver.get("https://www.bet365.it/#/HO/")

# Accetta il banner dei cookie
try:
    cookie_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".cookie-banner-accept-button"))  # Modifica il selettore in base al sito
    )
    cookie_button.click()
    print("Banner dei cookie accettato.")
except Exception as e:
    print("Banner dei cookie non trovato o già gestito:", e)

try:
    # Attendi la presenza dell'elemento
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".lms-StandardLogin_InputsContainer.lms-StandardLogin_NoControl"))
    )
    print("Elemento trovato!")
except Exception as e:
    print(f"Errore: {e}")
finally:
    driver.quit()
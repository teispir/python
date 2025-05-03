import os
import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configura il driver
driver = webdriver.Chrome()

try:
    # Vai alla pagina
    driver.get("https://www.bet365.it/#/HO/")
    
    # Attendi il caricamento completo
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))  # Assicurati che il corpo della pagina sia caricato
    )
    
    # Salva il sorgente della pagina
    with open("page_source.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    print("Sorgente salvato.")

    # Salva uno screenshot
    driver.save_screenshot("debug_screenshot.png")
    print("Screenshot salvato.")

except Exception as e:
    print(f"Errore: {e}")
finally:
    driver.quit()

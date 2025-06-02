import os
import selenium 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configura il driver (assicurati che il driver sia nel PATH)
driver = webdriver.Chrome()

# Vai alla pagina di login
driver.get("https://www.bet365.it/#/HO/")

# Aspetta il caricamento della pagina
time.sleep(10)  # Aspetta un po' di tempo per il caricamento completo della pagina

print(driver.page_source)
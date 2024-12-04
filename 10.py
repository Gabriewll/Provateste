from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
navegador.get("https://the-internet.herokuapp.com/login")
time.sleep(3)

try:
    navegador.find_element(By.XPATH,'//*[@id="username"]').send_keys("tomsmith")
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys("SuperSecretPassword!")
    time.sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="login"]/button').click()
    time.sleep(3)

    #verificar se o login foi aceito
    aceito = navegador.find_element(By.ID, "flash").text
    if "You logged into a secure area!" in aceito:
        print("Login aceito")
    else:
        print("Falha no login")

except Exception as e:
     print(f"Erro: {e}")
finally:
    # Fechar o navegador
    navegador.quit()           
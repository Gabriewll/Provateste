from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time

#abrir navegador
navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
navegador.get("https://www.selenium.dev/")
time.sleep(3)

try:
    #entrar nos downloads
    navegador.find_element(By.LINK_TEXT, "Downloads").click()
    time.sleep(2)

    #imprimir cabeçalho
    header = navegador.find_element(By.TAG_NAME, "h2")  
    print("Texto H2 da pagina:", header.text)

finally:
    # fechar o navegador
    navegador.quit()
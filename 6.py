from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
navegador.get("https://www.google.com")
time.sleep(3)

#encontrar a barra de pesquisa
search_bar = navegador.find_element("name", "q")

#digitar "Python Selenium" e pressionar Enter
search_bar.send_keys("Python Selenium")
search_bar.send_keys(Keys.RETURN)

# Esperar um tempo para garantir que a página de resultados carregue
time.sleep(3)

#captura de tela da página de resultados
navegador.save_screenshot("resultado.png")

# Fechar o navegador
navegador.quit()

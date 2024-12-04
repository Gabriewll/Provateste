from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time

#abrir navegador
navegador = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
navegador.get("https://vivo.com.br/para-voce")
time.sleep(3)

#fechar pop de cookie
navegador.find_element(By.XPATH,'/html/body/div[4]/div[6]/div/div/div/button').click()
time.sleep(3)

#selecionar cidade
navegador.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div/div[2]/ul/li[5]/a/span').click()
time.sleep(2)

navegador.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Configurações do Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Para rodar em modo headless (sem abrir o navegador)

# Caminho para o ChromeDriver
service = Service('./chromedriver')  # Substitua com o caminho do seu ChromeDriver

# Inicializando o WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abrindo o site da Sephora no produto desejado
driver.get('https://www.sephora.com.br/creme-hidratante-shiseido-vital-perfection-uplifting-firming-cream-9090740945-9090740945.html')

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Pausa para garantir que a página carregue completamente
time.sleep(5)

# Encontrando e extraindo os reviews
marca = driver.find_element(By.XPATH, '//*[@id="product-content"]/div[1]/div/h2/a')
nome = driver.find_element(By.XPATH, '//*[@id="product-content"]/div[1]/div/div[3]/div/h1')
reviews = driver.find_elements(By.XPATH, '//*[@id="BVRRContainer"]/div/div/div/div/ol/li/div[2]/div[1]/div/div[2]/div/div/div[1]/p')

#printar o texto do review
print(marca.text)
print(nome.text)
for review in reviews:
    print(review.text)

# Adcionando os reviews em um arquivo CSV sem apagar os anteriores

import csv

with open('sephora_reviews.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    for review in reviews:
        writer.writerow([marca.text, nome.text, review.text])

# Fechando o WebDriver
driver.quit()

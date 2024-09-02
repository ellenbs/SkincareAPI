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
driver.get('https://www.sephora.com.br/tonico-rose-inc-skin-resolution-clarifying-toner-9090640948-9090640948.html')

# Pausa para garantir que a página carregue completamente
time.sleep(5)

# Encontrando e extraindo os reviews
marca = driver.find_element(By.XPATH, '//*[@id="product-content"]/div[1]/div/h2/a')
nome = driver.find_element(By.XPATH, '//*[@id="product-content"]/div[1]/div/div[3]/div/h1')
reviews_title = driver.find_elements(By.XPATH, '//*[@id="BVRRContainer"]/div/div/div/div/ol/li[1]/div[2]/div[1]/div/div[1]/div/div[2]/h3')
reviews_text = driver.find_elements(By.XPATH, '//*[@id="BVRRContainer"]/div/div/div/div/ol/li/div[2]/div[1]/div/div[2]/div/div/div[1]/p')

#printar o texto do review
print(marca.text)
print(nome.text)
for review_title in reviews_title:
    print(review_title.text)
for review_text in reviews_text:
    print(review_text.text)

# Adcionando os reviews em um arquivo CSV sem apagar os anteriores

import csv

with open('sephora_reviews.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    for review_title in reviews_title:
        writer.writerow([marca.text, nome.text, review_title.text])
    for review_text in reviews_text:
            writer.writerow([marca.text, nome.text, review_text.text])

# Fechando o WebDriver
driver.quit()

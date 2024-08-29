from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv

# Configurações do Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")  # Para rodar em modo headless (sem abrir o navegador)

# Caminho para o ChromeDriver
service = Service('./chromedriver')  # Substitua com o caminho do seu ChromeDriver

# Inicializando o WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Abrindo o site da Sephora no produto desejado
driver.get('https://www.sephora.com.br/skincare/')

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Pausa para garantir que a página carregue completamente
time.sleep(5)


# Abre o arquivo CSV para salvar os dados
with open('sephora_skincare_products.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Marca", "Nome", "Link", "Preço"])

    # Extrai produtos da página
    products = driver.find_elements(By.CSS_SELECTOR, 'div.tiles-container__product')

    for product in products:
        try:
            # Extrair marca
            brand = product.get_attribute('data-brand')

            # Extrair nome
            name = product.get_attribute('data-product-name')

            # Extrair link do produto
            link = product.find_element(By.CSS_SELECTOR, 'a.tiles-container__link').get_attribute('href')

            # Extrair preço
            try:
                price = product.find_element(By.CSS_SELECTOR, 'div.product-normal-price').text
            except:
                price = 'Não disponível'

            # Salvar os dados no CSV
            writer.writerow([brand, name, link, price])

            print(f"Marca: {brand}, Nome: {name}, Link: {link}, Preço: {price}")
        except Exception as e:
            print(f"Erro ao extrair dados de um produto: {e}")

# Fechar o navegador
driver.quit()
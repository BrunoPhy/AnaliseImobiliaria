from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

# Configuração do Selenium para usar o Chrome em modo headless
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# URL que será acessada
url = "https://www.niponimoveis.com.br/index.asp?sec=home"
driver.get(url)
time.sleep(3)  # Espera para garantir que a página foi carregada

# Captura o conteúdo da página
html = driver.page_source
driver.quit()

# Faz a análise do HTML com BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Encontra os elementos de imóveis
imoveis = soup.find_all("div", class_="caixa")

dados_imoveis = []

# Loop para extrair os dados de cada imóvel
for imovel in imoveis:
    # Tenta extrair cada dado, se a tag não for encontrada, retorna uma string vazia
    titulo = imovel.find("div", id="Titulo").text.strip() if imovel.find("div", id="Titulo") else ""
    preco = imovel.find("div", id="Preco").text.strip() if imovel.find("div", id="Preco") else ""
    localizacao = imovel.find("div", id="flag-localizacao").text.strip() if imovel.find("div", id="flag-localizacao") else ""

    # Adiciona os dados extraídos a lista
    dados_imoveis.append({
        "Título": titulo,
        "Preço": preco,
        "Localização": localizacao,
    })

# Exibe os dados extraídos no terminal
for item in dados_imoveis:
    print(item)

# Salvando os dados em um arquivo CSV
# O código para salvar deve estar fora do loop que imprime os dados
with open('imoveis.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Título", "Preço", "Localização"])
    writer.writeheader()  # Escreve o cabeçalho do CSV
    for imovel in dados_imoveis:
        writer.writerow(imovel)

print("Dados exportados para imoveis.csv")

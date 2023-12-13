from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date
import urllib.request
import urllib.error
import pdfplumber
import os
import re


data = date.today()
day = str(data.day).zfill(2) if data.day < 10 else str(data.day)
month, year = str(data.month), str(data.year)

cidade = None
cidades = ['Curitiba', 'Maringá', 'Londrina', 'Cascavel', 'Foz do Iguaçu']
ceasa_url = None
patterns = None
html_cities = {
    'Curitiba': None,
    'Maringá': None,
    'Londrina': None,
    'Cascavel': None,
    'Foz do Iguaçu': None}
links_cities = {
    'Curitiba': None,
    'Maringá': None,
    'Londrina': None,
    'Cascavel': None,
    'Foz do Iguaçu': None}
today_links = {
    'Curitiba': None,
    'Maringá': None,
    'Londrina': None,
    'Cascavel': None,
    'Foz do Iguaçu': None}
pdf_cities = {
    'Curitiba': None,
    'Maringá': None,
    'Londrina': None,
    'Cascavel': None,
    'Foz do Iguaçu': None}
#
class Explorer:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument("--no-exit")
        self.driver = None
        self.actions = None
        self.html = None

    def open(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.options)
        self.actions = webdriver.ActionChains(self.driver)
    
    def loadPage(self, url):
        try:
            self.driver.get(url)
            print("Navegador carregado")
        except Exception as e:
            print(f"Ocorreu um erro ao carregar a página: {str(e)}")

    def extractHTML(self):
        self.html = self.driver.page_source
        self.soup = BeautifulSoup(self.html, "html.parser")
        return self.soup

#Variáveis dinâmicas



#Variáveis estruturais - torná-las funções mais simples

def extractHtmlCidades():
    
    html_divs = soup.find_all('div', class_='spoiler')
    
    for chave in html_cities:
        for spoiler in html_divs:
            if chave in str(spoiler):
                html_cities[chave] = spoiler

def extractLinks():
    for cidade in html_cities:
        for html in html_cities[cidade]:
            links = html_cities[cidade].find_all(
                'a', 
                href=lambda href: href and 
                href.startswith('https://www.ceasa.pr.gov.br/sites/ceasa/arquivos_restritos/files/'))
            links_cities[cidade] = [link.get('href') for link in links]

def getPatterns(dia, mes, ano):
    padroes = []
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    mes_extenso = meses[int(mes) - 1]

    regex_patterns = [
        rf'{dia.zfill(2)}{mes.zfill(2)}{ano}',               # ddmmAAAA = 01012023
        rf'{dia.zfill(2)}_{mes_extenso.lower()[:3]}_{ano}', # dd_mês(3 char)_AAAA = 01_jan_2023 
        rf'{dia.zfill(2)}_{mes_extenso.lower()}_{ano}',     # dd_mês_AAAA = 01_janeiro_2023
        rf'{dia.zfill(2)}{mes_extenso.lower()}{ano}'        # ddmesaaaa = 01janeiro2023
    ]

    # Iteração para imprimir os padrões de regex
    for pattern in regex_patterns:
        padroes.append(pattern)

    return padroes

def getLinkCities(padroes):
    for padrao in padroes:
        for cidade in today_links:
            for link in links_cities[cidade]:
                if padrao in link:
                    today_links[cidade] = link

def rascunho_lista(algo):
    with open('rascunho.txt', 'w', encoding='utf-8') as file:
        for elemento in algo:
            file.write(str(elemento) + '\n')
            file.write('FIM FIM FIM FIM FIM\n')

def rascunho(algo):
    with open('rascunho.txt', 'w', encoding='utf-8') as file:
        file.write(str(algo))




#main

explorer = Explorer()
explorer.open()
explorer.loadPage(f"https://www.ceasa.pr.gov.br/Pagina/Cotacao-Diaria-de-Precos-{year}")
soup = explorer.extractHTML()
extractHtmlCidades()
extractLinks()
padroes = getPatterns(day, month, year)
getLinkCities(padroes)

padrao = r'^\b[A-Z]+\b .*' #Padrão dos subgrupos dos produtos


for cidade in cidades: #solicita ao navegador o download das cotações e adiciona em today_links
    url = today_links.get(cidade)  # Obtendo o link da cidade a partir do dicionário
    if url:
        local_file = f"{cidade}.pdf"  # Nome do arquivo local, você pode ajustar conforme necessário
        try:
            with urllib.request.urlopen(url) as response, open(local_file, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Arquivo baixado com sucesso como '{local_file}' para a cidade {cidade}")
        except urllib.error.URLError as e:
            print(f"Erro ao solicitar o arquivo para a cidade {cidade}: {e}")
    else:
        print(f"Link para a cidade {cidade} não encontrado.")

for cidade in pdf_cities:
    url = today_links.get(cidade)  # Obtendo o link da cidade a partir do dicionário
    if url:
        local_directory = f"{cidade}.pdf"  # Nome do arquivo local, ajustado conforme necessário
        if os.path.exists(local_directory):  # Verifica se o arquivo existe localmente
            with pdfplumber.open(local_directory) as pdf:
                all_text = ''
                for page in pdf.pages:
                    text = page.extract_text()
                    all_text += text + '\n'  # Adiciona o texto da página atual ao texto acumulado
                pdf_cities[cidade] = all_text  # Atualiza o dicionário com o texto extraído
                print(f"Texto extraído do PDF '{local_directory}' para a cidade {cidade}:\n{all_text}")
        else:
            print(f"Arquivo para a cidade {cidade} não encontrado localmente.")
    else:
        print(f"Link para a cidade {cidade} não encontrado.")


# Encontrar todas as linhas correspondentes ao padrão
linhas_produtos = re.findall(padrao, pdf_cities['Curitiba'], re.MULTILINE)



from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import date
import re

day = None
month = None
year = None
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
actual_links = {
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
def actualDateFormmat():
    data = date.today()
    day = str(data.day).zfill(2) if data.day < 10 else str(data.day)
    month, year = str(data.month), str(data.year)

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
        for cidade in actual_links:
            for link in links_cities[cidade]:
                if padrao in link:
                    actual_links[cidade] = link

def rascunho_lista(algo):
    with open('rascunho.txt', 'w', encoding='utf-8') as file:
        for elemento in algo:
            file.write(str(elemento) + '\n')
            file.write('FIM FIM FIM FIM FIM\n')

def rascunho(algo):
    with open('rascunho.txt', 'w', encoding='utf-8') as file:
        file.write(str(algo))




#main

day, month, year = actualDateFormmat()
explorer = Explorer()
explorer.open()
explorer.loadPage(f"https://www.ceasa.pr.gov.br/Pagina/Cotacao-Diaria-de-Precos-{year}")
soup = explorer.extractHTML()
extractHtmlCidades()
extractLinks()
padroes = getPatterns(day, month, year)
getLinkCities(padroes)



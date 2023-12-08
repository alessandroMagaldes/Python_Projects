from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from tkinter import Tk, Button, Label, Entry, filedialog

class Navegador:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        #self.options.add_experimental_option("detach", True)
        #self.options.add_argument("--no-exit")
        self.driver = None
        self.actions = None

    def abre(self):
        self.driver = webdriver.Chrome(options=self.options)
        self.actions = ActionChains(self.driver)

    def fecha(self):
        self.driver.quit()

    def carrega_pagina(self, url):
        self.driver.get(url)
        print("Navegador carregado")

    def seleciona_pagina(self,pagina_numero):
        self.driver.switch_to.window(self.driver.window_handles[pagina_numero])

    def fecha_pagina(self):
        pass

    def extrair_pagina(self):
        self.html = self.driver.page_source
        self.soup = BeautifulSoup(self.html, "html.parser")
        return self.soup

    def extrair_elementos(self, elemento, classe):
        elementos = self.extrai_pagina().find_all(elemento, classe)
        return elementos

    def salva_arquivo_lista(self, lista):
        self.lista = lista
        self.caminho = filedialog.asksaveasfilename(
            title="Salvar o arquivo como",
            filetypes=(("Arquivos de texto", "*.txt"), ("Texto CSV", "*.csv"))
        )
        with open(self.caminho, 'w') as file:
            file.write('Descrição;Embalagem;Preço\n')
            for linha in lista:
                for i in linha:
                    file.write(i)
                    file.write(';')
                file.write('\n')

class Ifood(Navegador):
    def __init__(self):
        super().__init__()
        self.mercados = []
        self.corredores = []
        self.produtos = []


        self.html_produtos_promo = []
        self.produtos_pagina = []
        self.vitrine_links = []
        self.produtos_promo = {}
        self.produtos_promo_peso = {}
        self.lista_produtos_promo = []
        self.lista_produtos_promo_peso = []
        self.indices_produtos_promo_peso = []

    def atualiza_produtos_promo(self):
        self.html_produtos_promo = self.extrai_elementos("a", "dish-card dish-card--horizontal dish-card--has-image")

    def atualiza_produtos(self):
        self.produtos_pagina = self.navegador.extrai_elementos("span", "product-card__details")
        contagem = 0

        while contagem < len(self.produtos_pagina):
            print(len(self.produtos_pagina))
            contagem = len(self.produtos_pagina)
            body_element = self.navegador.driver.find_element(By.TAG_NAME, 'body')
            body_element.send_keys(Keys.END)
            time.sleep(2)
            self.navegador.extrai_pagina()
            self.produtos_pagina = self.navegador.extrai_elementos("span", "product-card__details")

    def links_vitrine(self):
        print("Função carrosel iniciada")
        lista_vitrine = self.navegador.extrai_pagina().find_all("li", class_="aisle-menu__item")
        self.vitrine_links = []

        for lista in lista_vitrine:
            if lista['class'] == ['aisle-menu__item']:
                elemento_a = lista.find('a', attrs={'class': 'aisle-menu__item__link'})
                link = elemento_a['href']
                self.vitrine_links.append(link)

    def carrosel_links(self):
        self.html_produtos = []
        self.links_vitrine()

        print("Função atualiza_produtos_pagina executada")
        for link in self.vitrine_links:
            link_url = "https://www.ifood.com.br" + link
            self.navegador.driver.get(link_url)
            time.sleep(1)
            self.atualiza_produtos()
            self.html_produtos.append(self.produtos_pagina)

'''
class Produtos:
    def __init__(self):
        self.produtos_promo = {}
        self.produtos_promo_peso = {}
        self.lista_produtos_promo = []
        self.lista_produtos_promo_peso = []
        self.indices_produtos_promo_peso = []
        self.id = 1

    def extrai_produtos_promo(self, driver):
        self.atualiza_produtos_promo(driver)

        for i in range(len(self.html_produtos_promo)):
            elemento_descricao = self.html_produtos_promo[i].find("h3", attrs={"class": "dish-card__description"})
            descricao = elemento_descricao.get_text()
            elemento_embalagem = self.html_produtos_promo[i].find("span", attrs={"class": "dish-card__details"})
            embalagem = elemento_embalagem.get_text()
            if embalagem == "Compra por peso":
                self.indices_produtos_promo_peso.append(i)
            else:
                elemento_preco = self.html_produtos_promo[i].find("span", attrs={"class": "dish-card__price"})
                preco = elemento_preco.text.replace(elemento_preco.find('span', class_='dish-card__price--original').text, '') if elemento_preco.find('span', class_='dish-card__price--original') else elemento_preco.text

                self.produtos_promo[self.id] = (descricao, embalagem, preco)
                self.id += 1

        for i in self.produtos_promo:
            self.lista_produtos_promo.append(self.produtos_promo[i])

        for i in range(len(self.lista_produtos_promo)):
            produto = list(self.lista_produtos_promo[i])
            produto[2] = produto[2].replace("R$ ", "")
            self.lista_produtos_promo[i] = tuple(produto)

        elementos_a = driver.find_elements('css selector', 'a.dish-card.dish-card--horizontal.dish-card--has-image')

        for i in self.indices_produtos_promo_peso:
            elemento_descricao = self.html_produtos_promo[i].find("h3", attrs={"class": "dish-card__description"})
            descricao = elemento_descricao.get_text()
            embalagem = "KG"
            elementos_a[i].click()
            time.sleep(0)
            self.extrai_pagina()
            preco = driver.find_element('css selector', 'span.product-detail__weighable--value').text
            ActionChains(driver).move_by_offset(xoffset=1, yoffset=1).click().perform()
            self.produtos_promo_peso[self.id] = (descricao, embalagem, preco)
            self.id += 1

        for i in self.produtos_promo_peso:
            self.lista_produtos_promo_peso.append(self.produtos_promo_peso[i])

        for i in range(len(self.lista_produtos_promo_peso)):
            produto = list(self.lista_produtos_promo_peso[i])
            produto[2] = produto[2].replace("R$ ", "")
            self.lista_produtos_promo_peso[i] = tuple(produto)


class Tela:
    def __init__(self):
        self.app = Tk()
        self.app.title('Script')
        self.app.resizable(width=False, height=False)

        self.navegador = Navegador()
        self.produtos = Produtos()
        self.ifood = Ifood(self.navegador)

        self.botao_abre_navegador = Button(self.app, text='Abrir navegador', command=self.abre_navegador)
        self.botao_abre_navegador.grid(column=0, row=0)

        self.label_abre_pagina = Label(self.app, text='Copie a url do site de promoção do mercado abaixo antes de abrir a página')
        self.label_abre_pagina.grid(column=0, row=1)

        self.label_exemplo = Label(self.app, text='Ex: https://www.ifood.com.br/delivery/londrina-pr/viscardi---ouro-verde-coliseu/732229d2-6720-4b9b-af0a-29d5b154268a?originArea=aisleMenu&corredor=promo')
        self.label_exemplo.grid(column=0, row=2)

        self.url_pagina = Entry(self.app)
        self.url_pagina.grid(column=0,row=3)

        self.botao_abre_pagina = Button(self.app, text='Abrir página', command=self.inicia_navegador)
        self.botao_abre_pagina.grid(column=0,row=4)

        self.botao_fecha_navegador = Button(self.app, text='Fecha navegador', command=self.fecha_navegador)
        self.botao_fecha_navegador.grid(column=0, row=10)

        self.botao_extrai_produtos = Button(self.app, text='Extrai produtos', command=self.extrai_produtos_promo)
        self.botao_extrai_produtos.grid(column=0, row=5)

        self.app.mainloop()

    def abre_navegador(self):
        self.navegador.abre_navegador()

    def fecha_navegador(self):
        self.navegador.fecha_navegador()

    def inicia_navegador(self):
        url = self.url_pagina.get()
        self.navegador.inicia_navegador(url)
        print("Navegador carregado")

    def extrai_produtos_promo(self):
        self.produtos.extrai_produtos_promo(self.navegador.driver)

tela = Tela()'''


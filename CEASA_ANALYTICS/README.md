# Ceasa - Cotação Diária de Preços

# RADAR

1. Coletar todo o histórico de cotações do CEASA

    1.a - Coletar links da página e filtrar pelos links que sejam de PDF
        Beatifulsoup - html
        find_all('a', href=lambda href: href and href.startswith("https://www.ceasa.pr.gov.br/sites/ceasa/arquivos_restritos/files/documento"))

2. Criar localizador de links PDF de cotações através de um algoritmo que simule os padrões e gere o link
    2.a - Padrões: 
            cotacaopdf02022023.pdf = ddmmaaaa
            maagosto10082023.pdf = ddmmaaaa
            fevereiro27022023.pdf ddmmaaaa
            abril03042023.pdf = ddmmaaaa
            cotacao_01_fev_2023.pdf = dd_mês(3 caracteres)_aaaa
            cotacao_01_agosto_2023.pdf = dd_mês_aaaa
            imprensa_17_janeiro_2023.pdf = dd_mês_aaaa
            cotacao_diaria_10_maio_2023.pdf = dd_mês_aaaa
            cotacaodiariacascavel03outubro2023.pdf = ddmêsaaaa

    2.b - Comuns:
            ddmmaaaa
            dd_mês(3 char)_aaaa
            dd_mês_aaaa

    3.b - Algoritmos
    



b. Salvar todo o histórico do CEASA em um banco
c. Criar aplicativo para visualização dos dados e estatísticas

# LOG

# APLICAÇÕES FUTURAS




# Resultado do TDD - TESTES
'''
Tentar outra abordagem para coletar o link de uma página

modelos
junho05072023.pdf
abril03042023.pdf
cotacao_06_julho_2023.pdf
cotacaodiaria_18_maio_2023_0.pdf
cotacaodiariacascavel23outubro2023.pdf
cotacaopdf06112023.pdf
imprensa_17_janeiro_2023.pdf

O que há e comum é que todos indicam a data completa no link, sendo os formatos:
1. ddmmaaaa
2. dd_mês_aaaa
3. ddmêsaaaa

Ou seja, usando as três possibilidades abaixo, consigo procurar pelos valores do link:
elemento = a
atributo = href

'''


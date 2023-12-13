# Automação de Extração de Dados da CEASA Paraná

Este repositório contém um script Python desenvolvido para automatizar a extração de informações de preços diários da CEASA (Centrais de Abastecimento do Estado do Paraná) para diferentes cidades.

## Descrição

O código Python disponibilizado faz uso das seguintes bibliotecas:
- `webdriver_manager` para gerenciamento do driver do navegador Chrome.
- `selenium` para automação do navegador web.
- `bs4` (BeautifulSoup) para analisar o HTML das páginas web.
- `datetime` para manipulação de datas.
- `re` para expressões regulares.

### Funcionalidades Principais

1. **Classe Explorer:**
   - Inicialização de um navegador Chrome utilizando o `webdriver_manager` e `selenium`.
   - Carregamento de páginas web.
   - Extração do HTML das páginas visitadas.

2. **Funções de Extração de Dados:**
   - `actualDateFormmat()`: Formata a data atual.
   - `extractHtmlCidades()`: Extrai o HTML relacionado às cidades de interesse.
   - `extractLinks()`: Extrai os links das páginas relevantes.
   - `getPatterns()`: Gera padrões de busca para datas.
   - `getLinkCities()`: Obtém os links das cidades conforme os padrões estabelecidos.

### Variáveis

O código utiliza variáveis para armazenar informações como a data atual, URLs, padrões de busca e links relevantes para as cidades de Curitiba, Maringá, Londrina, Cascavel e Foz do Iguaçu.

### Execução do Código

TO - DO

## Utilização

TO - DO

## Contribuição

Se deseja contribuir com melhorias, correções ou novas funcionalidades, sinta-se à vontade para abrir uma issue ou enviar um pull request.
---
Este código foi desenvolvido como parte de um projeto para facilitar a obtenção de informações de preços da CEASA Paraná de forma automatizada. Qualquer contribuição ou sugestão para aprimoramento é bem-vinda!

#Lista de atividades 1 - Python para Zumbis
#Link - https://www.dropbox.com/sh/m9wio7ock77yowd/AAAR3ogXRJqhd5Uw3NthvS0Ia?dl=0&preview=Lista+de+Exerc%C3%ADcios+I+Python+para+Zumbis.pdf

import sys

#Função input com parâmetro para texto
def cmd(mensagem):
    entrada = int(input(mensagem))
    return entrada

#Aumenta limite de caracteres no sistema
sys.set_int_max_str_digits(999999999)

while True:

    print('ATENÇÃO!\n\nOS NÚMEROS DECIMAIS DEVERÃO SER DESCRITOS COM PONTOS, E NÃO VIRGULAS.')
    
    #Exercício 1
    print('Exercício 1.\nFaça um programa que peça dois números inteiros e imprima a soma desses dois números.\n')
    inteiros = []
    inteiros.append(cmd('Digite o primeiro número inteiro:  '))
    inteiros.append(cmd('Digite o segundo número inteiro: '))
    print(f'A soma dos dois números é {sum(inteiros)}.\n')

    #Exercício 2
    print('Exercício 2.\nEscreva um programa que leia um valor em metros e o exiba convertido em milímetros.\n')
    metros = cmd('Digite o valor em metros: ')
    milimetros = metros * 1000
    print(f'Este valor convertido para milímetros é igual a {milimetros}.\n')

    #Exercício 3
    print('Exercício 3.\nEscreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.\n')
    dias = cmd('Digite a quantidade de dias: ')
    horas = cmd('Digite a quantidade de horas: ')
    minutos = cmd('Digite a quantidade de minutos: ')
    segundos = cmd('Digite a quantidade de segundos: ')
    total = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
    print(f'Total em segundos: {total}.\n')

    #Exercício 4
    print('Exercício 4.\nFaça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.\n')
    valor_salario = float(cmd('Digite o valor do salário atual em R$: '))
    perc_aumento = float(cmd('Digite a porcentagem de aumento: '))
    aumento_salarial = float(valor_salario * (1 + (perc_aumento/100)))
    print(f'O aumento salarial é de: R${aumento_salarial:.2f} reais.\n')

    #Exercício 5
    print('Exercício 5.\nSolicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.\n')
    preco_mercadoria = float(cmd('Digite o preço atual da mercadoria em R$: '))
    perc_desconto = float(cmd('Digite a porcentagem de desconto: '))
    valor_desconto = float(preco_mercadoria * (perc_desconto / 100))
    preco_mercadoria_atual = float(preco_mercadoria - valor_desconto)
    print(f'O valor de desconto é R${valor_desconto} e o preço atualizado do produto é R${preco_mercadoria_atual}.\n')

    #Exercício 6
    print('Exercício 6.\nCalcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.')
    distancia = cmd('Digite a distância do percurso em Km: ')
    velocidade_media = cmd('Digie a velocidade média em Km/h: ')
    tempo_viagem = distancia / velocidade_media
    print(f'O tempo de viagem é igual a {int(tempo_viagem)} horas e {(tempo_viagem - int(tempo_viagem))*60:.0f} minutos.\n')

    #Exercício 7
    print('Exercício 7.\nConverta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C /5 + 32.\n')
    Celsius = cmd('Digite a temperatura em Celsius: ')
    Fahrenheit = (9 * Celsius/5) + 32
    print(f'A temperatura de {Celsius:.1f}º Celsius é igual a {Fahrenheit:.1f}º Fahrenheit.\n')

    #Exercício 8
    print('Exercício 8.\nFaça agora o contrário, de Fahrenheit para Celsius.\n')
    Fahrenheit = cmd('Digite a temperatura em Fahrenheit: ')
    Celsius = 5/9 * (Fahrenheit - 32)
    print(f'A temperatura de {Fahrenheit:.1f}º Fahrenheit é igual a {Celsius:.1f}º Celsius.\n')

    #Exercício 9
    print('Exercício 9.\nEscreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.\n')
    km_rodados = cmd('Digite a quantidade de Km percorridos: ')
    dias_alugado = cmd('Digite a quantidade de dias que o carro foi alugado: ')
    taxa_km = 0.15
    taxa_dia = 60
    total_aluguel = (taxa_dia * dias_alugado) + (taxa_km * km_rodados)
    print(f'O preço do aluguel do carro alugado ficou em R$ {total_aluguel:.0f}.\n')

    #Exercício 10
    print('Exercício 10.\nEscreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 1 0 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.\n')
    qtde_cigarros_dia = cmd('Digite a quantidade de cigarros fumados por dia: ')
    anos_fumou = cmd('Digite a quantidade de anos que a pessoa fumou: ')
    reducao_vida = (((qtde_cigarros_dia * 10) * (anos_fumou * 365)) / 1440)
    print(f'O total do tempo de vida reduzido equivale a {int(reducao_vida)} dias.\n')

    #Exercício 11
    print('Exercício 11.\nSabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.')
    print(f'Há {len(str(2**1000000))} digitos.\n')

    break






    

#Lista de atividades 2 - Python para Zumbis
#Link - https://www.dropbox.com/sh/m9wio7ock77yowd/AAAR3ogXRJqhd5Uw3NthvS0Ia?dl=0&preview=Lista+de+Exerc%C3%ADcios+II+Python+para+Zumbis.pdf

import calendar

#Função input com parâmetro para texto
def inputer(mensagem):
    entrada = int(input(mensagem))
    return entrada


#Loop para exercícios
while True:

    #Exercício 1
    print('Exercício 1. \nFaça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.\n')
    lado1 = inputer('Digite o valor do lado 1 do triângulo: ')
    lado2 = inputer('Digite o valor do lado 2 do triângulo: ')
    lado3 = inputer('Digite o valor do lado 2 do triângulo: ')
    
    #Equilátero
    if lado1 == lado2 == lado3:
        print("É um triângulo equilátero.")
    #Isósceles
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("É um triângulo isósceles.")
    #Escaleno
    else:
        print("É um triângulo escaleno.")

    #Exercício 2
    print('\nExercício 2.\nDetermine se um ano é bissexto.\n')
    ano = inputer('Digite o ano para saber se é ou não bissexto: ')

    if calendar.isleap(ano):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

    #Exercício 3
    print('\nExercício 3.\nJoão Papo - de - Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Pa ulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.\n ')
    regula_pesca = 50
    peso_peixes = inputer('Digite o peso dos peixes: ')
    excesso = peso_peixes - regula_pesca if peso_peixes > regula_pesca else 0
    multa = excesso * 4

    if multa > 0:
        print(f'Você pescou além do regulamento e foi multado em R${multa:.2f} reais')
    else:
        print('Você está dentro do regulamento de pesca. Boa pescaria!')

    #Exercício 4
    print('\nExercício 4.\nFaça um Programa que leia três números e mostre o maior deles.\n')
    n1 = inputer('Digite o valor do número 1: ')
    n2 = inputer('Digite o valor do número 2: ')
    n3 = inputer('Digite o valor do número 3: ')
    max = 0

    for i in n1, n2, n3:
        if i > max:
            max = i
    print(max)


   #Exercício 5
    print('\nExercício 5.\nFaça um Programa que leia três números e mostre o menor deles.\n')
    n1 = inputer('Digite o valor do número 1: ')
    n2 = inputer('Digite o valor do número 2: ')
    n3 = inputer('Digite o valor do número 3: ')
    min = 0

    for i in n1, n2, n3:
        if i < min:
            min = i
    print(min)
    

    #Exercício 6
    print('\nExercício 6.\nFaça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo - se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, q uanto pagou ao INSS, quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os descontos e o salário líquido, conforme a tabela abaixo: \na. + Salário Bruto : R$ \nb. - IR (11%) : R$ \nc. - INSS (8%) : R$ \nd. - Sindica to ( 5%) : R$ \ne. = Salário Liquido : R$')
    ganhos_hora = inputer('Digite o valor da sua hora: R$ ')
    horas_trabalhadas = inputer('Digite quantas horas você trabalha por mês: ')
    salario_bruto = ganhos_hora * horas_trabalhadas
    IR = salario_bruto * 0.11
    INSS = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - IR - INSS - sindicato

    print(f'a. + Salário Bruto : R$ {salario_bruto:.2f} \nb. - IR (11%) : R$ {IR:.2f} \nc. - INSS (8%) : R$ {INSS:.2f} \nd. - Sindica to ( 5%) : R$ {sindicato:.2f}\ne. = Salário Liquido : R$ {salario_liquido:.2f}')

    #Exercício 7
    print('\nExercício 7.\nFaça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.\n')
    area_pintada = inputer('Digite o tamanho da área a ser pintada em metros quadrados: ')
    tinta_pinta = 3
    tinta_volume = 18
    tinta_lata_cobre = tinta_pinta * tinta_volume
    tinta_preco = 80
    latas = area_pintada // tinta_lata_cobre if (area_pintada // tinta_lata_cobre) > 0 else 1
    latas_preco = latas * tinta_preco
    
    print(f'\nSerá necessário {latas} lata(s) de tinta que custarão R$ {latas_preco:.2f} reais.')

    break
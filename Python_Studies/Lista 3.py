#Lista de atividades 3 - Python para Zumbis
#Link - https://www.dropbox.com/sh/m9wio7ock77yowd/AAAR3ogXRJqhd5Uw3NthvS0Ia?dl=0&preview=Lista+de+Exerc%C3%ADcios+III+Python+para+Zumbis.pdf


#Função input com parâmetro para texto
def cmd(mensagem):
    entrada = input(mensagem)
    return entrada

while True:

    #Exercício 1
    print('Exercício 1.\nFaça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.\n')
    while True:
        nota = int(cmd('Digite uma nota entre zero e dez: '))
        
        if 0 <= nota <= 10:
            print('Passou!')
            break
        else:
            print('Valor inválido! O número digitado deve estar entre zero e dez.')

    #Exercício 2
    print('\nExercício 2.\nFaça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.\n')
    login = cmd('Digite o nome do seu usuário: ')
    while True:
        senha = cmd('Digite sua senha: ')
        if senha == login:
            cmd('A senha não pode ser igual ao login! Digite novamente.')
        else:
            cmd('Usuário criado com sucesso!')
            break
    
    #Exercício 3
    print('\nExercício 3.\nSupondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a po pulação de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.\n')
    pop_pais_A = 80000
    pop_pais_B = 200000
    crescimento_anual_A = 3
    crescimento_anual_B = 1.5
    anos = 0
    while pop_pais_A < pop_pais_B:
        anos += 1
        pop_pais_A += pop_pais_A * (crescimento_anual_A/100)
        pop_pais_B += pop_pais_B * (crescimento_anual_B/100)
    print(f'A quantidade em anos para que a população do país A ultrasse o país B é de {anos} anos.')

    #Exercício 4
    print('\nExercício 4.\nA seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. F 1 = 1, F 2 = 1, F 3 = 2, etc.\n')
    while True:
        n = int(cmd('Digite um número que deseja descobrir a sua sequência de Fibonacci: '))
        if n > 2:
            seq = [1, 1]
            for i in range(2,n):
                fib = seq[i-1] + seq[i-2]
                seq.append(fib)
            cmd(f'A sequência de Fibonnaci para o número digitado é: \n{seq[:n]}')
            break
        else:
            cmd("A sequência de Fibonacci começa com '1, 1', então insira um número maior que 2 para gerar a sequência.")
    
    #Exercício 5
    print('\nExercício 5.\nDados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.\n')
    while True:
        a = int(cmd('Digite o primeiro número: '))
        b = int(cmd('Digite o segundo número: '))
        if a <= 0 or b <= 0:
            print('Os números precisam ser maiores que zero!')
        else:
            break
    x, y = a, b          
    def mdc(x, y): 
        while y != 0:
            x, y = y, x % y #quando b > a, a divisão não será possível, portanto b assumirá o valor de a, invertendo os termos
        print(f'O MDC entre {a} e {b} é {x}')
    mdc(a,b)




    


    
    
    break
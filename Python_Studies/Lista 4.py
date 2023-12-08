#Lista de atividades 4 - Python para Zumbis
#Link - https://www.dropbox.com/sh/m9wio7ock77yowd/AAAR3ogXRJqhd5Uw3NthvS0Ia?dl=0&preview=Lista+de+Exerc%C3%ADcios+IV+Python+para+Zumbis.pdf

import random

#Função input com parâmetro para texto
def cmd(mensagem):
    entrada = int(input(mensagem))
    return entrada


while True:

    #Exercício 1
    print('Exercício 1.\nSorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.\n')
    lista = [random.randint(0,100) for i in range(10)]
    max, min = 0, 100
    for i in lista:
        if i > max:
            max = i
        if i < min:
            min = i
    print(f'A lista de número é {lista}')
    print(f'O maior número da lísta é igual {max} e o menor número é igual a {min}.')

    #Exercício 2
    print('\nExercício 2.\nSorteie 20 inteiros entre 1 e 100 num a lista . Armazene os números pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três lista s')
    lista = [random.randint(0,100) for i in range(20)]
    lista_pares = [n for n in lista if n % 2 == 0]
    lista_impares = [n for n in lista if n % 2 != 0]
    print(f'Lista inicial.\n{lista}\nLista de pares.\n{lista_pares}\nLista de ímpares.\n{lista_impares}')

    #Exercício 3
    print('\nExercício 3.\nFaça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100 . Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. Imprima os três vetores.\n')
    vetor1 = [random.randint(0,100) for i in range(10)]
    vetor2 = [random.randint(0,100) for i in range(20)]
    vetor3 = [(x, y) for x, y in zip(vetor1, vetor2)]
    print(f'Vetor 1.\n{vetor1}\nVetor 2.\n{vetor2}')
    print(f'O terceiro vetor criado corresponde a listagem.\n{vetor3}')

    #Exercício 4
    print('\nExercício 4.\nSeja o statement sobre diversidade : “ The Python Software Foundation and the global Python community welcome and encou rage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.” . Gere uma lista de palavras deste texto com split () , a seguir crie uma lista com as palavras que começam ou terminam com uma das letras “ python ” . Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.\n')
    frase = '''The Python Software Foundation and the global Python community welcome and encou rage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''
    palavras_frase = frase.lower().replace(',','').split()
    #método 1
    lista = []
    for i in 'python':
        for p in palavras_frase:
            if i in p[0] or i in p[-1]:
                if p not in lista:
                    lista.append(p)
    #método 2 
    lista2 = list(set(p for p in palavras_frase if any(i in p[0] or i in p[-1] for i in 'python')))
    print(f'Lista resultante:\n{lista}')

    #Exercício 5
    print('\nSeja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais.\n')
    lista3 = list(set(p for p in palavras_frase if 4 >= len(p) and any(i in p for i in 'python')))
    print(lista3)


    break

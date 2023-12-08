'''import time
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

#root = tk.Tk()
#root.title("Leitor de CNAB")
#root.withdraw() # esconde a janela principal


file_path = filedialog.askopenfilename(
title="Selecione o arquivo",
filetypes=(("Arquivos de texto", "*.txt"),("Todos os arquivos", "*.*")))'''




#------------------------------- MAPA DE REGISTROS DE CADA SEGMENTO ------------------------------------------

posHeader = [('Banco',0,3), ('Lote',3,7), ('Registro',7,8), ('CNAB',8,17), ('Tipo de inscrição',17,18), ('Número da inscrição',18,32), ('Convênio',32,52),
('Agência-DV',52,58), ("Conta-DV",58,71), ('DV',71,72), ('Nome da Empresa',72,102), ('Nome do banco',102,132), ('CNAB',132,142),('Código da remessa',142,143),
('Data de Geração',143,151), ('Hora da Geração',151,157), ('Sequência NSA',157,163), ('Versão do layout do arquivo',163,166), ('Densidade',166,171),
('Reservado Banco',171,191), ('Reservado Empresa',191,211), ('CNAB',211,240)]

posLote = [('Banco',0,3), ('Lote',3,7), ('Registro',7,8), ('Operação',8,9), ('Serviço',9,11),('CNAB',11,13), ('Versão do layout do lote',13,16),
('CNAB',16,17), ('Tipo de inscrição',17,18), ('Número da inscrição',18,33), ('Convênio',33,53), ('Agência-DV',53,59), ('Conta-DV',59,72),('DV',72,73),
('Nome da Empresa',73,103), ('Mensagem 1',103,143), ('Mensagem 2',143,183), ('Número de Retorno',183,191), ('Data de gravação',191,199), ('Data do crédito',199,207),
('CNAB',207,240)]

posSegP = [('Banco',0, 3), ('Lote',3,7), ('Registro',7,8), ('Nº do Registro',8,13), ('Segmento',13,14), ('CNAB',14,15), ('Código de Movimento Remessa',15,17),
('Agência-DV',17,23), ('Conta-DV',23,35), ('DV_AG/Conta',36,37 ), ('Nosso número', 37,57), ('Carteira',57,58), ('Cadastramento',58,59), ('Documento',59,60),
('Emissão Boleto',60,61), ('Distrib. Boleto',61,62), ('Nº do Documento',62,77), ('Vencimento',77,85), ('Valor do Título',85,100), ('Ag. Cobradora-DV',100,106),
('Espécie do Título',106,108), ('Aceite',108,109), ('Data Emissão do Título',109,117), ('Cod. Juros Mora',117,118), ('Data Juros Mora',118,126),
('Juros Mora',126,141), ('Cód. Desc. 1',141,142), ('Data Desc. 1',142,150), ('Desconto 1',150,165), ('Vlr IOF',165,180), ('Vlr Abatimento',180,195),
('Uso Empresa Beneficiário', 195,220), ('Código p/ Protesto',220,221), ('Prazo p/ Protesto',221,223), ('Código p/ Baixa/Devolução',223,224),
('Prazo p/ Baixa/Devolução',224,227), ('Código da Moeda',227,229), ('Número do Contrato', 229,239), ('CNAB',239,240)]

posSegQ = [('Código do banco',0,3), ('Lote de serviço',3,7), ('Tipo de Registro',7,8), ('Nº Seq. do Reg. no Lote',8,13), ('Cód. Seg. do Registro Detalhe',13,14),
('FEBRABAN/CNAB',14,15), ('Código de Movimento Remessa',15,17), ('Tipo de Inscrição',17,18), ('Número da Inscrição',18,33), ('Nome',33,73),('Endereço',73,113),
('Bairro',113,128), ('CEP',128,133), ('Sufixo do CEP',133,136), ('Cidade',136,151), ('UF',151,153), ('Sac./Aval.',153,154),('Número da Inscrição',154,169),
('Nome do Sacador/Avalista',169,209), ('Cód. Bco. Corresp. na Compensação', 209,212), ('Nosso Nº no Banco Correspondente',212,232), ('CNAB',232,240)]

posSegR = [('Banco',0, 3), ('Lote',3,7), ('Registro',7,8), ('Nº do Registro',8,13), ('Segmento',13,14), ('CNAB',14,15), ('Código de Movimento Remessa',15,17),
('Código do desconto 2',17,18), ('Data do desconto 2',18,26), ('Desconto percentual 2',26,41), ('Código do desconto 3',41,43), ('Data do desconto 3',42,50),
('Desconto percentual 3',50,65), ('Código da multa',65,66), ('Data da multa',66,74), ('Valor percentual da multa',74,89), ('Informação ao pagador',89,99),
('Mensagem 3',99,139), ('Mensagem 4',139,179), ('CNAB',179,199), ('Data limite de pagamento',199,207), ('Débito:Banco',207,210), ('Débito:Agência',211,215),
('Débito:CC-DV',216,229), ('DV',229,230), ('Aviso para débito automático',230,231), ('CNAB',231,240)]

posSegS = [('Banco',0, 3), ('Lote',3,7), ('Registro',7,8), ('Nº do Registro',8,13), ('Segmento',13,14), ('CNAB',14,15), ('Código de Movimento Remessa',15,17),
('Agência-DV',17,23), ('Conta-DV',23,35), ('DV_AG/Conta',36,37 ), ('Nosso número', 37,57), ('Carteira',57,58), ('Cadastramento',58,59), ('Documento',59,60),
('Emissão Boleto',60,61), ('Distrib. Boleto',61,62), ('Nº do Documento',62,77), ('Vencimento',77,85), ('Valor do Título',85,100), ('Ag. Cobradora-DV',100,106),
('Espécie do Título',106,108), ('Aceite',108,109), ('Data Emissão do Título',109,117), ('Cod. Juros Mora',117,118), ('Data Juros Mora',118,126),
('Juros Mora',126,141), ('Cód. Desc. 1',141,142), ('Data Desc. 1',142,150), ('Desconto 1',150,165), ('Vlr IOF',165,180), ('Vlr Abatimento',180,195),
('Uso Empresa Beneficiário', 195,220), ('Código p/ Protesto',220,221), ('Prazo p/ Protesto',221,223), ('Código p/ Baixa/Devolução',223,224),
('Prazo p/ Baixa/Devolução',224,227), ('Código da Moeda',227,229), ('Número do Contrato', 229,239), ('CNAB',239,240)]

posSegT = [('Banco',0, 3), ('Lote',3,7), ('Registro',7,8), ('Nº do Registro',8,13), ('Segmento',13,14), ('CNAB',14,15), ('Código de Movimento Retorno',15,17),
('Agência-DV',17,23), ('Conta-DV',23,35), ('DV_AG/Conta',36,37 ), ('Nosso número', 37,57), ('Carteira',57,58), ('Nº do Documento',58,73),
('Vencimento',73,81), ('Valor do Título',81,96), ('Banco Cobr/Receb.',96,99),('Ag.Cobradora-DV',99,105), ('Identificação do título na empresa',105,130),
('Código da Moeda',130,132), ('Tipo de inscrição',132,133), ('Número da inscrição',133,148), ('Nome do pagador',148,188), ('Número do contrato',188,198),
('Valor da tar/custas',198,213), ('Motivo da Ocorrência',213,223), ('CNAB',223,240)]

posSegU = [('Banco',0,3), ('Lote',3,7), ('Registro',7,8), ('Nº do Registro',8,13), ('Segmento',13,14), ('CNAB',14,15), ('Código de Movimento Retorno',15,17), ('Acréscimos',17,32),
('Desconto',32,47), ('Abatimento',47,62), ('IOF',62,77), ('Valor Pago',77,92), ('Valor Líquido',92,107), ('Outras Despesas',107,122),
('Outros Créditos',122,137), ('Data da Ocorrência',137,145), ('Data do Crédito', 145,153), ('Código', 153,157), ('Data Ocorrência',157,165),
('Valor Ocorrência',165,180), ('Compl. da Ocorrência',180,210), ('Código do Banco Correspondente',210,213), ('Nº do Banco Correspondente',213,233), ('CNAB',233,240)]

#------------------------------- FINAL DAS POSIÇÕES DOS REGISTROS DO ITAU ------------------------------------------


#função lê arquivo e salva em remessa ou retorno
def identificaArquivo():

    global REM, RET, tipoArquivo
    
    tipoArquivo = int(input('Digite 1 para Remessa ou 2 para Retorno: '))
    with open(file_path, 'r') as arquivoLido:
            REM = RET = arquivoLido.read().split('\n')
#função que adiciona cada registro no seu respectivo tipo de segmento
def arranjaSeg():
    for linha in REM:
        if linha[13:14] == "P":
            segmentoP.append(linha)
        if linha[13:14] == "Q":
            segmentoQ.append(linha)
        if linha[13:14] == "R":
            segmentoR.append(linha)
        if linha[13:14] == "T":
            segmentoT.append(linha)
        if linha[13:14] == "U":
            segmentoU.append(linha)
            
#salva todos os registros de cada segmentos em um arquivo separado nomeado com o tipo de segmento
def salvaSeg():
    try:
        folder_selected = filedialog.askdirectory()
        if tipoArquivo == 1:
            with open(folder_selected + '/segmentoP.txt', 'w+') as arquivo:
                for campo in posSegP:
                    arquivo.write(campo[0])
                    arquivo.write(';')
                for linha in segmentoP:
                    arquivo.write('\n')
                    for campo, posini, posf in posSegP:
                        regSegP = linha[posini:posf]
                        arquivo.write(regSegP)
                        arquivo.write(';')
            with open(folder_selected + '/segmentoQ.txt', 'w+') as arquivo:
                for campo in posSegQ:
                    arquivo.write(campo[0])
                    arquivo.write(';')
                for linha in segmentoQ:
                    arquivo.write('\n')
                    for campo, posini, posf in posSegQ:
                        regSegQ = linha[posini:posf]
                        arquivo.write(regSegQ)
                        arquivo.write(';')
            with open(folder_selected + '/segmentoR.txt', 'w+') as arquivo:
                for campo in posSegR:
                    arquivo.write(campo[0])
                    arquivo.write(';')
                for linha in segmentoR:
                    arquivo.write('\n')
                    for campo, posini, posf in posSegR:
                        regSegR = linha[posini:posf]
                        arquivo.write(regSegR)
                        arquivo.write(';')
        else:
            with open(folder_selected + '/segmentoT.txt', 'w+') as arquivo:
                for campo in posSegT:
                    arquivo.write(campo[0])
                    arquivo.write(';')
                for linha in segmentoT:
                    arquivo.write('\n')
                    for campo, posini, posf in posSegT:
                        regSegT = linha[posini:posf]
                        arquivo.write(regSegT)
                        arquivo.write(';')
            with open(folder_selected + '/segmentoU.txt', 'w+') as arquivo:
                for campo in posSegU:
                    arquivo.write(campo[0])
                    arquivo.write(';')
                for linha in segmentoU:
                    arquivo.write('\n')
                    for campo, posini, posf in posSegU:
                        regSegU = linha[posini:posf]
                        arquivo.write(regSegU)
                        arquivo.write(';')
    except Exception as e:
        print(f"Erro: {str(e)}")

def procuraDoc():
    documento = input('Digite o número do documento: ')
    segmento = input('Qual segmento do documento que deseja buscar (P,Q,R,T,U): ')
    match segmento:
        case "P": segmento, posSeg = segmentoP, posSegP
        case "Q": segmento, posSeg = segmentoQ, posSegQ
        case "R": segmento, posSeg = segmentoR, posSegR
        case "T": segmento, posSeg = segmentoT, posSegT
        case "U": segmento, posSeg = segmentoU, posSegU
        
    for linha in segmento:
        if tipoArquivo == 1:
            doc = linha[62:71]
            if documento == doc:
                for campo, posini, posf in posSeg:
                    regSeg = linha[posini:posf]
                    print(campo, ':', regSeg)
        elif tipoArquivo == 2:
            doc = linha[58:66]
            print(doc)
            if documento == doc:
                for campo, posini, posf in posSeg:
                    regSeg = linha[posini:posf]
                    print(campo, ':', regSeg)

class Arquivo()

class Arquivo_cabecalho:
    def __init__(self):
        self.codBanco = codBanco
        self.loteServico = loteServico
        self.tipoRegistro = tipoRegistro
        self.CNAB1 = CNAB1
        self.tipoInscricao = tipoInscricao
        self.numeroInscricao = numeroInscricao
        self.codConvBanco = codConvBanco
        self.agConta = agConta
        self.agDV = agDV
        self.numeroConta = numeroConta
        self.contaDV = contaDV
        self.agContaDV = agContaDV
        self.nomeEmpresa = nomeEmpresa
        self.nomeBanco = nomeBanco
        self.CNAB2 = CNAB2
        self.codArquivo = codArquivo
        self.dataArquivo = dataArquivo
        self.horaArquivo = horaArquivo
        self.numeroSequencial = numeroSequencial
        self.versaoLayout = versaoLayout
        self.densidadeGravacao = densidadeGravacao
        self.reservadoBanco = reservadoBanco
        self.reservadoEmpresa = reservadoEmpresa
        self.CNAB3 = CNAB3

    posicoes = {
        "codBanco": [0, 3],
        "loteServico": [3, 7],
        "tipoRegistro": [7, 8],
        "CNAB1": [8, 17],
        "tipoInscricao": [17, 18],
        "numeroInscricao": [18, 32],
        "codConvBanco": [32, 52],
        "agConta": [52, 57],
        "agDV": [57, 58],
        "numeroConta": [58, 70],
        "contaDV": [70, 71],
        "agContaDV": [71, 73],
        "nomeEmpresa": [73, 103],
        "nomeBanco": [103, 133],
        "CNAB2": [133, 393],
        "codArquivo": [393, 394],
        "dataArquivo": [394, 400],
        "horaArquivo": [400, 406],
        "numeroSequencial": [406, 413],
        "versaoLayout": [413, 416],
        "densidadeGravacao": [416, 419],
        "reservadoBanco": [419, 424],
        "reservadoEmpresa": [424, 484],
        "CNAB3": [484, 999]
    }

    
            
            






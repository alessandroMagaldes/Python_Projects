from tkinter import *
from tkinter import ttk


def exibir_arvore():
    app_arvore = Tk()
    app_arvore.title("Visualizador do segmento X")
    
    arvore = ttk.Treeview(app_arvore)
    arvore["columns"] = tuple(f"coluna{i+1}" for i in range(10))
    
    for coluna in arvore["columns"]:arvore.heading(coluna, text=coluna)
    for coluna in arvore["columns"]: arvore.column(coluna,width=50)

    for i in range(30):
        valores = tuple(f"dado {i+1}" for j in range(len(arvore["columns"])))
        arvore.insert("", END, text=f"Linha {i+1}", values=valores)

    arvore.pack()
    # Restante do código da janela arvore...

app = Tk()
app.title("CNAB")
app.resizable(width=False, height=False)
app.geometry("210x160")


botao_arquivo = Button(app, text="Selecione o arquivo") #Comando seleciona arquivo
botao_arquivo.grid(column=0, row=0, pady=10)

arquivo_selecionado = Label(app, text="")
arquivo_selecionado.grid(column=0, row=1)

opcao_orientacao = Label(app, text="Selecione o segmento a ser visualizado")
opcao_orientacao.grid(column=0, row=2)

segmentos = [""]
opcao_segmentos = ttk.OptionMenu(app, StringVar(), *segmentos)
opcao_segmentos.grid(column=0,row=3)

botao_visualizar = Button(app, text="Visualizar", command=exibir_arvore) #Comando gera tela
botao_visualizar.grid(column=0, row=4, pady=10)

app.mainloop()




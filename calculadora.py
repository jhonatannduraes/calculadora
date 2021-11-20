from tkinter import *


janela = Tk()
janela.title("Calculadora")
janela.geometry("185x180")
visor = Entry(janela)


def clique_botao(numero):
    atual = visor.get()
    visor.delete(0, END)
    visor.insert(END, str(atual) + str(numero))

def clique_virgula():
    conteudo = visor.get().split(".")
    if(visor.get() == ""):
        return
    if(len(conteudo) == 1):
        visor.insert(END, ".")  

def limpar():
    visor.delete(0, END)

def clique_adicao():
    conteudo = visor.get()
    global primeiro_numero
    global operacao
    primeiro_numero = float(conteudo)
    operacao = "adicao"
    limpar()

def clique_subtracao():
    conteudo = visor.get()
    global primeiro_numero
    global operacao
    primeiro_numero = float(conteudo)
    operacao = "subtracao"
    limpar()

def clique_divisao():
    conteudo = visor.get()
    global primeiro_numero
    global operacao
    primeiro_numero = float(conteudo)
    operacao = "divisao"
    limpar()

def clique_multiplicacao():
    conteudo = visor.get()
    global primeiro_numero
    global operacao
    primeiro_numero = float(conteudo)
    operacao = "multiplicacao"
    limpar()

def igual():
    conteudo = visor.get()
    segundo_numero = float(conteudo)
    limpar()
    if(operacao == "adicao"):
        visor.insert(END, primeiro_numero + segundo_numero)

    elif(operacao == "subtracao"):
        visor.insert(END, primeiro_numero - segundo_numero)

    elif(operacao == "divisao"):
        visor.insert(END, primeiro_numero / segundo_numero)

    elif(operacao == "multiplicacao"):
        visor.insert(END, primeiro_numero * segundo_numero)

#Botões:

botao1 = Button(janela, text = "1", command=lambda: clique_botao(1))
botao2 = Button(janela, text = "2", command=lambda: clique_botao(2))
botao3 = Button(janela, text = "3", command=lambda: clique_botao(3))
botao4 = Button(janela, text = "4", command=lambda: clique_botao(4))
botao5 = Button(janela, text = "5", command=lambda: clique_botao(5))
botao6 = Button(janela, text = "6", command=lambda: clique_botao(6))
botao7 = Button(janela, text = "7", command=lambda: clique_botao(7))
botao8 = Button(janela, text = "8", command=lambda: clique_botao(8))
botao9 = Button(janela, text = "9", command=lambda: clique_botao(9))
botao0 = Button(janela, text = "0", command=lambda: clique_botao(0))

botao_limpar = Button(janela, text = "C", command=limpar)
botao_virgula = Button(janela, text = ",", command=clique_virgula)
botao_divisao = Button(janela, text = "/", command=clique_divisao)
botao_multiplicacao = Button(janela, text = "X", command=clique_multiplicacao)
botao_subtracao = Button(janela, text = "-", command=clique_subtracao)
botao_adicao = Button(janela, text = "+", command=clique_adicao)
botao_igual = Button(janela, text= "=", command=igual)

#Posicionamento:

botao_divisao.grid(column=3, row=1)
botao1.grid(column=0, row=1)
botao2.grid(column=1, row=1)
botao3.grid(column=2, row=1)
botao_multiplicacao.grid(column=3, row=2)
botao4.grid(column=0, row=2)
botao5.grid(column=1, row=2)
botao6.grid(column=2, row=2)
botao_subtracao.grid(column=3, row=3)
botao7.grid(column=0, row=3)
botao8.grid(column=1, row=3)
botao9.grid(column=2, row=3)
botao_adicao.grid(column=3, row=4)
botao0.grid(column=1, row=4)
botao_limpar.grid(column=0, row=4)
botao_virgula.grid(column=2, row=4)
botao_igual.grid(column=0, row=5)

visor.grid(column=0, row=0, columnspan=4)

janela.mainloop()
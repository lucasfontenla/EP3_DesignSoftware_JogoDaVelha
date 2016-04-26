# -*- coding: utf-8 -*-
"""
Lucas Fontenla & Victor Hugo - Engenharia 1B
EP3_JogoDaVelha
"""
import tkinter as tk
import tkinter.messagebox as tkm
from Jogo_da_Velha import Jogo

class Tabuleiro:
    def __init__(self):
        self.meu_jogo = Jogo() #criação do objeto jogo

        #window
        self.window = tk.Tk()
        self.window.title("Jogo da Velha")
        self.window.geometry("450x520")
        self.window.resizable(False,False) #o usuário fica impossibilitado de mexer no tamanho da tela
        for k in range(0, 3): #gera as linhas e colunas números 0, 1 e 2
            self.window.rowconfigure(k, minsize=150)
            self.window.columnconfigure(k, minsize=150)
        self.window.rowconfigure(3, minsize=40) #linha para display das jogadas

        #buttons
        global botoes #todas as funçãoes tem acesso aos botões
        botoes = [[[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]] #lista que armazena os botões
        for i in range(0, 3): #gera os botões --> aqui gera as linhas
            for j in range(0, 3): #--> aqui gera as colunas
                botoes[i][j] = tk.Button(self.window) #cria os botões
                botoes[i][j].configure(height=10, width=10, command=lambda botao=(i,j): self.command_botao(botao))
                                                     #a função lambda é usada pra retornar a posição do clique
                botoes[i][j].grid(row=i, column=j, sticky="NSEW") #posiciona cada botão em seu lugar
        
        #labels
        global label1 #todas as funções tem acesso à label
        label1 = tk.Label(self.window) #cria a label de infos
        label1.configure(width=60, height=1)
        label1.grid(row=3, column=0, columnspan=3, sticky="W")
        self.gera_label("Primeira Jogada: {0}".format(self.meu_jogo.jogada))
    
    #função reponsável por adicionar a letra no botão e desabilitá-lo, para não haver jogada repetida        
    def gera_botoes(self, posicao_tupla, limpar_botoes): #quando chamada a função limpar tela, ela usa a função gera botoes para resetar os botões
        conteudo_botao = tk.StringVar()
        if limpar_botoes == False:
            conteudo_botao.set(self.meu_jogo.jogada) #se não foi chamada a função limpar tela, ele continua adicionando X/O
        else:
            conteudo_botao.set("") #se foi chamada a função limpa tela, todos os botões são resetados

        global botoes
        botoes[posicao_tupla[0]][posicao_tupla[1]].config(textvariable=conteudo_botao,\
                state="disabled") #após escrever, o botão é desabilitado
        self.gera_label("Próxima Jogada: {0}".format(self.meu_jogo.proxima_jogada))

    #função responsável por adicionar texto na label 
    def gera_label(self, display): 
        conteudo_label = tk.StringVar()
        conteudo_label.set(display)
        global label1
        label1.configure(textvariable=conteudo_label, anchor="w")
    
    #função que retorna para a classe jogo a posição do clique
    def command_botao(self, posicao_tupla): 
        self.gera_botoes(posicao_tupla, False)
        self.meu_jogo.recebe_jogada(posicao_tupla)

        resultado = self.meu_jogo.verifica_ganhador()

        if resultado == -1:
            pass
        elif resultado == 0:
            self.mostra_vencedor_reset("Empate")
        elif resultado == 1:
            global listaX
            ap_listaX(self)
            self.mostra_vencedor_reset("Vitória do X")
        elif resultado == 2:
            global listaO
            ap_listaO(self)
            self.mostra_vencedor_reset("Vitória do O")

    #função mostra um pop-up com o vencedor. 
    #A função tem dois botões para isso: Novo Jogo --> reseta a tela e reinicia o jogo; Sair --> fecha todas as telas
    def mostra_vencedor_reset(self, resultado):
        self.janela_resultado = tkm.askquestion("Resultado", "{0}\nNovo Jogo?".format(resultado)) #criaçaão da tela pop up
        
        self.meu_jogo.limpa_jogadas()
        self.limpa_tela()

        if self.janela_resultado == "no": #caso o clique seja não, o jogo fecha
            self.window.destroy()

    def limpa_tela(self): #reseta a tela
        for i in range(0,3):
            for j in range(0,3):
                self.gera_botoes((i,j), True) #True para resetar os botoes em gera_botoes
                botoes[i][j].config(state="normal") #todos os botões são reabilitados 
        self.gera_label("Primeira Jogada: {0}".format(self.meu_jogo.jogada)) #reseta a label para a primeira jogada

    def iniciar(self): #função que inicia o jogo
        self.window.mainloop()

class Placar:
    def __init__(self):
        self.meu_jogo = Jogo() #criação do objeto jogo

        self.placar = tk.Tk()
        
        # Design do placar
        self.placar.title("Resultado Final")
        self.placar.geometry("250x300")
        self.placar.resizable(False,False)

        #Label
        global label_placar
        label_placar = tk.Label(self.placar, fg = "red")
        label_placar.configure(width = 200, height = 250)
        self.placar.rowconfigure(0, minsize=150, weight=1)
        self.placar.columnconfigure(0, minsize=150, weight=1)
        label_placar.grid()

    def conteudo_Label(self, a, b):
        conteudoLabel = tk.StringVar()
        conteudoLabel.set("Pontos do jogador X: {0} \nPontos do jogador O: {1}".format(a, b))
        global label_placar
        label_placar.config(textvariable = conteudoLabel)
    
    def iniciar(self):
        self.conteudo_Label(len(listaX),len(listaO))
        self.placar.mainloop()

class Pergunta_Jogador:
    def __init__(self):
        
        self.pergunta = tk.Tk() # Criação da janela pergunta
        
        # Interfase do placar
        self.pergunta.title("Resultado Final")
        self.pergunta.geometry("350x210")
        self.pergunta.resizable(False,False)
        self.pergunta.rowconfigure(0, minsize=70, weight=1)
        self.pergunta.rowconfigure(1,minsize=70, weight=1)
        self.pergunta.rowconfigure(2,minsize=70, weight=1)
        self.pergunta.columnconfigure(0, minsize=175, weight=1)
        self.pergunta.columnconfigure(1, minsize=175, weight=1)
        
        # Propriedades dos Label's
        label_jogX = tk.Label(self.pergunta)
        label_jogX.configure(width = 10, height = 10)
        label_jogX.configure(text= "Jogador X:", fg= "Red")
        label_jogX.grid(row=0, column=0, sticky="NSEW")

        label_jogO = tk.Label(self.pergunta)
        label_jogO.configure(width = 10, height = 10)
        label_jogO.configure(text= "Jogador O:", fg= "Red")
        label_jogO.grid(row=0, column=1, sticky="NSEW")


        # Caixas de texto
        self.conteudo_ctX = tk.StringVar()
        caixa_textoX = tk.Entry(self.pergunta)
        caixa_textoX.configure(textvariable= self.conteudo_ctX)
        caixa_textoX.grid(row=1, column=0, padx=20, sticky="ew")
        
        self.conteudo_ctO = tk.StringVar()
        caixa_textoO = tk.Entry(self.pergunta)
        caixa_textoO.configure(textvariable=self.conteudo_ctO)
        caixa_textoO.grid(row=1, column=1, padx=20, sticky="ew")

        # Botão
        botão = tk.Button(self.pergunta)
        botão.configure(text="Enter")
        botão.configure(command= self.apertou_botao)
        botão.grid(row=2, column=0, columnspan=2)
        botão.configure(width=10, height=3)
        
    def apertou_botao(self):
        print("Oi")
        self.pergunta.destroy()

    def iniciar_pr(self):
        self.pergunta.mainloop()

listaX = []
listaO = []

def ap_listaX(self):
    listaX.append("Resp")

def ap_listaO(self):
    listaO.append("Resp")

pr = Pergunta_Jogador()
pr.iniciar_pr()
tela = Tabuleiro()
tela.iniciar()
p = Placar()
p.iniciar()

# -*- coding: utf-8 -*-
"""
Lucas Fontenla & Victor Hugo - Engenharia 1B
EP3_JogoDaVelha
"""
import tkinter as tk
import tkinter.messagebox as tkm #para gerar a mensagem pop-up
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
        self.botoes = [[[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]] #lista que armazena os botões
        for i in range(0, 3): #gera os botões --> aqui gera as linhas
            for j in range(0, 3): #--> aqui gera as colunas
                self.botoes[i][j] = tk.Button(self.window) #cria os botões
                self.botoes[i][j].configure(height=10, width=10, command=lambda botao=(i,j): self.command_botao(botao))
                                                     #a função lambda é usada pra retornar a posição do clique
                self.botoes[i][j].grid(row=i, column=j, sticky="NSEW") #posiciona cada botão em seu lugar
        #labels
        self.label1 = tk.Label(self.window) #cria a label de infos
        self.label1.configure(width=60, height=1)
        self.label1.grid(row=3, column=0, columnspan=3, sticky="W")
        self.gera_label("Primeira Jogada: {0}".format(self.meu_jogo.jogada))
    
    #função reponsável por adicionar a letra no botão e desabilitá-lo, para não haver jogada repetida        
    def gera_botoes(self, posicao_tupla, limpar_botoes): #quando chamada a função limpar tela, ela usa a função gera botoes para resetar os botões
        conteudo_botao = tk.StringVar()
        if limpar_botoes == False:
            conteudo_botao.set(self.meu_jogo.jogada) #se não foi chamada a função limpar tela, ele continua adicionando X/O
        else:
            conteudo_botao.set("") #se foi chamada a função limpa tela, todos os botões são resetados

        self.botoes[posicao_tupla[0]][posicao_tupla[1]].config(textvariable=conteudo_botao,\
                state="disabled") #após escrever, o botão é desabilitado
        self.gera_label("Próxima Jogada: {0}".format(self.meu_jogo.proxima_jogada))

    #função responsável por adicionar texto na label 
    def gera_label(self, display): #função responsável por mostrar de uqem será a próxima jogada
        conteudo_label = tk.StringVar()
        conteudo_label.set(display)
        self.label1.configure(textvariable=conteudo_label, anchor="w")
    
    #função que retorna para a classe jogo a posição do clique
    def command_botao(self, posicao_tupla): 
        self.gera_botoes(posicao_tupla, False)
        self.meu_jogo.recebe_jogada(posicao_tupla) #função que irá registrar a jogada

        resultado = self.meu_jogo.verifica_ganhador()

        if resultado == -1: #o jogo continua
            pass
        elif resultado == 0:
            self.mostra_vencedor_reset("Empate")
        elif resultado == 1:
            self.mostra_vencedor_reset("Vitória do X")
        elif resultado == 2:
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
                self.botoes[i][j].config(state="normal") #todos os botões são reabilitados 
        self.gera_label("Primeira Jogada: {0}".format(self.meu_jogo.jogada)) #reseta a label para a primeira jogada

    def iniciar(self): #função que inicia o jogo
        self.window.mainloop()

tela = Tabuleiro()
tela.iniciar()


# -*- coding: utf-8 -*-
"""
Lucas Fontenla & Victor Hugo - Engenharia 1B
EP3_JogoDaVelha
"""
import tkinter as tk
import tkinter.messagebox as tkm
from Jogo_da_Velha_extra_por_Lucas_Fontenla import Jogo

class Tabuleiro:
    def __init__(self):
        self.meu_jogo = Jogo() #criação do objeto jogo
        self.tela_inicial()

    #função responsável por gerar a tela inicial --> entrada dos nomes + escolha do modo
    def tela_inicial(self):
        self.win_inicial = tk.Tk()
        self.win_inicial.title("Jogo da Velha")
        self.win_inicial.geometry("450x520")
        self.win_inicial.resizable(False,False) #o usuário não pode redimensionar a tela

        self.win_inicial.columnconfigure(0, minsize=450)
        self.win_inicial.rowconfigure(0, minsize=80) #primeira linha --> título (maior)
        for n in range(1,9):
            self.win_inicial.rowconfigure(n, minsize=55) #gera 8 linhas para adicionar conteúdo

        title = tk.Label(self.win_inicial) #gera o título da página
        title.configure(text="# JOGO DA VELHA #", bg="black")
        title.configure(font=("Courier", 30, "bold"), fg="white")
        title.grid(row=0, column=0, sticky="NSEW")

        label_jogadorx = tk.Label(self.win_inicial) #info ao usuário
        label_jogadorx.configure(text="Nome Jogador X", font="Courier 12 bold")
        label_jogadorx.grid(row=1, column=0, sticky="W")

        self.entry_jogadorx = tk.Entry(self.win_inicial) #entrada do nome do jogador que joga com "X"
        self.entry_jogadorx.configure(font="Courier 10 italic")
        self.entry_jogadorx.grid(row=2, column=0, sticky="NSEW")
        
        label_jogadory = tk.Label(self.win_inicial) #info ao usuário
        label_jogadory.configure(text="Nome Jogador Y", font="Courier 12 bold")
        label_jogadory.grid(row=3, column=0, sticky="W")

        self.entry_jogadory = tk.Entry(self.win_inicial) #entrada do nome do jogador que joga com "O"
        self.entry_jogadory.configure(font="Courier 10 italic")
        self.entry_jogadory.grid(row=4, column=0, sticky="NSEW")

        modos = tk.Label(self.win_inicial) #info ao usuário
        modos.configure(text="Modo de Jogo", font="Courier 12 bold", bg="black", fg="white")
        modos.grid(row=5, column=0, sticky="NSEW")

        label_dados_finais = tk.Label(self.win_inicial) #info extras --> criação final
        label_dados_finais.configure(text="© Lucas Fontenla | Engenharia Insper", font="Courier 10", bg="black", fg="white", anchor="w")
        label_dados_finais.grid(row=8, column=0, sticky="NSEW")

        botoes_win_iniciar = list() #gera os botões da tela principal
        for i in range(0,2):
            botoes_win_iniciar.append(tk.Button(self.win_inicial))
            botoes_win_iniciar[i].configure(command=lambda bot=i: self.escolha_modo(bot), width=20, height=1, font="Courier 10")
            botoes_win_iniciar[i].grid(row=(6+i), column=0)

        nomes = ["Modo Livre", "Melhor de 3"] #lista que dará nome aos botões
        for name in nomes:
            botoes_win_iniciar[nomes.index(name)].configure(text=name)

    #função resposável por enviar os nomes entrados na tela inicial, registrar o modo de jogo e iniciar a tela de jogo
    def escolha_modo(self, bot):
        if self.entry_jogadorx.get() == "" or self.entry_jogadory.get() == "": #se não inserir um nome, o jogo pede para inserir
            self.aviso_nome = tkm.showerror("Nomes", "Inserir nome(s)")
        else:
            self.meu_jogo.recebe_jogadores(self.entry_jogadorx.get(), self.entry_jogadory.get()) #recebe o nome dos jogadores
            self.meu_jogo.registra_modo(bot) #regitra o modo de jogo escolhido
            self.win_inicial.destroy() #fecha a janela inicial
            self.tela_jogo() #inicia o tabuleiro

    #função responsável por gerar a tela de jogo
    def tela_jogo(self):
        self.window = tk.Tk() #window
        self.window.title("Jogo da Velha")
        self.window.geometry("450x500")
        self.window.configure(bg="black")
        self.window.resizable(False,False) #o usuário fica impossibilitado de mexer no tamanho da tela
        for k in range(0, 3): #gera as linhas e colunas números 0, 1 e 2
            self.window.rowconfigure(k, minsize=150)
            self.window.columnconfigure(k, minsize=150)
        for j in range(3, 6):
            self.window.rowconfigure(j, minsize=40) #linha para display das jogadas

        #buttons
        self.botoes = [[[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]] #lista que armazena os botões
        for i in range(0, 3): #gera os botões --> aqui gera as linhas
            for j in range(0, 3): #--> aqui gera as colunas
                self.botoes[i][j] = tk.Button(self.window) #cria os botões
                self.botoes[i][j].configure(command=lambda botao=(i,j): self.command_botao(botao), font="Courier 60")
                                                     #a função lambda é usada pra retornar a posição do clique
                self.botoes[i][j].grid(row=i, column=j, sticky="NSEW") #posiciona cada botão em seu lugar
        
        #labels
        self.label1 = tk.Label(self.window) #cria a label de infos
        self.label1.configure(width=60, height=1, bg="black", fg="white", font="Courier 9 bold")
        self.label1.grid(row=3, column=0, columnspan=3, sticky="W")
        self.gera_label("Primeira Jogada: X - {0}".format(self.meu_jogo.jogador1))

    #função reponsável por adicionar a letra no botão e desabilitá-lo, para não haver jogada repetida        
    def gera_botoes(self, posicao_tupla, limpar_botoes): #quando chamada a função limpar tela, ela usa a função gera botoes para resetar os botões
        conteudo_botao = tk.StringVar()
        if limpar_botoes == False:
            conteudo_botao.set(self.meu_jogo.jogada) #se não foi chamada a função limpar tela, ele continua adicionando X/O
        else:
            conteudo_botao.set("") #se foi chamada a função limpa tela, todos os botões são resetados

        self.botoes[posicao_tupla[0]][posicao_tupla[1]].config(textvariable=conteudo_botao,\
                state="disabled") #após escrever, o botão é desabilitado

        if self.meu_jogo.proxima_jogada == "X": #usado para mostrar o nome do próximo jogado
            string = "X - {0}".format(self.meu_jogo.jogador1) 
        else:
            string = "O - {0}".format(self.meu_jogo.jogador2)

        self.gera_label("Próxima Jogada: {0}".format(string))

    #função responsável por adicionar texto na label 
    def gera_label(self, display): 
        conteudo_label = tk.StringVar()
        conteudo_label.set(display)
        self.label1.configure(textvariable=conteudo_label, anchor="w")
    
    #função que retorna para a classe jogo a posição do clique
    def command_botao(self, posicao_tupla): 
        self.gera_botoes(posicao_tupla, False)
        self.meu_jogo.recebe_jogada(posicao_tupla)

        resultado = self.meu_jogo.verifica_ganhador()

        if resultado == -1:
            pass
        elif resultado == 0:
            self.mostra_vencedor_reset()
        elif resultado == 1:
            self.mostra_vencedor_reset()
        elif resultado == 2:
            self.mostra_vencedor_reset()

    #função mostra um pop-up com o vencedor. 
    #A função tem dois botões para isso: Novo Jogo --> reseta a tela e reinicia o jogo; Sair --> fecha todas as telas
    def mostra_vencedor_reset(self):
        modo = self.meu_jogo.verifica_modo()

        if self.meu_jogo.vencedor == "X":
            resultado = "Vencedor(a): {0}".format(self.meu_jogo.jogador1)
        elif self.meu_jogo.vencedor == "O":
            resultado = "Vencedor(a): {0}".format(self.meu_jogo.jogador2)
        else:
            resultado = "Empate"

        if modo == 0:
            self.janela_resultado = tkm.askquestion("Resultado modo livre", "{0}\n{1}:{2} x {3}:{4}\nNovo Jogo?".format(resultado, self.meu_jogo.jogador1, \
            self.meu_jogo.vitorias_jogador1, self.meu_jogo.jogador2, self.meu_jogo.vitorias_jogador2), icon="info") #criaçaão da tela pop up, que mostra o resultado + placar

            if self.janela_resultado == "no": #caso o clique seja não, o jogo fecha
                self.meu_jogo.vitorias_jogador1 = self.meu_jogo.vitorias_jogador2 = 0
                self.meu_jogo.limpa_jogadas()
                self.limpa_tela() 
                self.meu_jogo.contador = 0
                self.tela_inicial()
                self.window.destroy()

            else: 
                self.meu_jogo.limpa_jogadas()
                self.limpa_tela() 

        elif modo == 1:
            self.janela_resultado = tkm.showinfo("Resultado parcial", "{0}\n{1}:{2} x {3}:{4}".format(resultado, self.meu_jogo.jogador1, \
            self.meu_jogo.vitorias_jogador1, self.meu_jogo.jogador2, self.meu_jogo.vitorias_jogador2), type="ok", icon="info") #criaçaão da tela pop up que mostra o resultado + placar

            self.meu_jogo.limpa_jogadas()
            self.limpa_tela() 

        elif modo == -1:
            self.janela_resultado = tkm.askquestion("Resultado melhor de 3", "{0}\nNovo Jogo?".format(self.meu_jogo.vencedor_melhor3), icon="info") #criaçaão da tela pop up

            if self.janela_resultado == "no": #caso o clique seja não, o jogo fecha
                self.meu_jogo.vitorias_jogador1 = self.meu_jogo.vitorias_jogador2 = 0
                self.meu_jogo.limpa_jogadas()
                self.limpa_tela() 
                self.meu_jogo.contador = 0
                self.tela_inicial()
                self.window.destroy()

            else: 
                self.meu_jogo.limpa_jogadas()
                self.limpa_tela() 
                self.meu_jogo.contador = 0

    def limpa_tela(self): #reseta a tela
        if self.meu_jogo.jogada == "X":
            string = "X - {0}".format(self.meu_jogo.jogador1) 
        else:
            string = "O - {0}".format(self.meu_jogo.jogador2)
        for i in range(0,3):
            for j in range(0,3):
                self.gera_botoes((i,j), True) #True para resetar os botoes em gera_botoes
                self.botoes[i][j].config(state="normal") #todos os botões são reabilitados 
        self.gera_label("Primeira Jogada: {0}".format(string)) #reseta a label para a primeira jogada

    def iniciar(self): #função que inicia o jogo
        self.win_inicial.mainloop()

tela = Tabuleiro()
tela.iniciar()
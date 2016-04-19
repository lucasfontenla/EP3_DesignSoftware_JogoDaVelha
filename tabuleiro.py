# -*- coding: utf-8 -*-
"""
Lucas Fontenla & Victor Hugo - Engenharia 1B
EP3_JogoDaVelha
"""
import tkinter as tk

class Tabuleiro:
    def __init__(self):
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
    
    #função reponsável por adicionar a letra no botão e desabilitá-lo, para não haver jogada repetida        
    def gera_botoes(self, posicao_tupla, letra):
        conteudo_botao = tk.StringVar()
        conteudo_botao.set(letra)
        global botoes
        botoes[posicao_tupla[0]][posicao_tupla[1]].config(textvariable=conteudo_botao,\
                state="disabled") #após escrever, o botão é desabilitado
    
    #função responsável por adicionar texto na label 
    def gera_label(self, display): 
        conteudo_label = tk.StringVar()
        conteudo_label.set(display)
        global label1
        label1.configure(textvariable=conteudo_label, anchor="w")
    
    #função que retorna para a classe jogo a posição do clique
    def command_botao(object, i):
        object.jogada = i 

    #função mostra um pop-up com o vencedor. 
    #A função tem dois botões para isso: Novo Jogo --> reseta a tela e reinicia o jogo; Sair --> fecha todas as telas
    def mostra_vencedor_reset(self, resultado):
        self.janela_vencedor = tk.Toplevel()
        self.janela_vencedor.resizable(False,False) #o pop up não pode ser redimensionado
        self.janela_vencedor.title("Resultado")
        self.janela_vencedor.geometry("200x180")
        #define o grid da janela
        self.janela_vencedor.rowconfigure(0, minsize="100")
        self.janela_vencedor.rowconfigure(1, minsize="30")
        self.janela_vencedor.rowconfigure(2, minsize="30")
        self.janela_vencedor.columnconfigure(0, minsize="200")
        #display do resultado como mensagem ao usuário
        display_vencedor = tk.Message(self.janela_vencedor, text=resultado, font="Verdana 10", justify="center")
        display_vencedor.grid(row=0, column=0, sticky="nsew")
        #gera o botão novo jogo: se apertado, reseta a tela e reinicia o jogo
        self.botao_novo_jogo = tk.Button(self.janela_vencedor, text="Novo Jogo", width=10, command=self.limpa_tela)
        self.botao_novo_jogo.grid(row=1, column=0)
        #gera o botão sair: se apertado, fecha tudo
        botao_sair = tk.Button(self.janela_vencedor, text="Sair", width=10, command=self.window.destroy)
        botao_sair.grid(row=2, column=0)

        # Coloca X no botão ao passar o mouse, e volta ao normal ao tirar o mouse        
        botoes[0][0].bind("<Motion>", self.muda_para_letra)
        botoes[0][0].bind("<Leave>", self.volta_normal)        
        
    def limpa_tela(self): #reseta a tela
        self.janela_vencedor.destroy() #fecha a tela pop-up
        for i in range(0,3):
            for j in range(0,3):
                tela.gera_botoes((i, j), "")
                botoes[i][j].config(state="normal") #todos os botões são reabilitados  

    def iniciar(self): #função que inicia o jogo
        self.window.mainloop()
    
    def muda_para_letra(self, event): # função que coloca o X
        botoes[0][0].configure(text = "X")
    
    def volta_normal(self, event): # função que volta ao normal
        tela.gera_botoes((0,0), "")
        botoes[0][0].config(state="normal")

#teste das funções --> tirar o "#" para executar testes        
tela = Tabuleiro()
tela.gera_botoes((0,1), "X")
tela.gera_label("Legenda Teste")
tela.mostra_vencedor_reset("X")
tela.iniciar()

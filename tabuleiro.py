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
        self.window.geometry("450x520")
        for k in range(0, 3): #gera as linhas e colunas números 0, 1 e 2
            self.window.rowconfigure(k, minsize=150)
            self.window.columnconfigure(k, minsize=150)
        self.window.rowconfigure(3, minsize=40) #linha para display das jogadas
        
        #buttons
        global botoes
        botoes = [[[0],[0],[0]],[[0],[0],[0]],[[0],[0],[0]]]
        for i in range(0, 3):
            for j in range(0, 3):
                botoes[i][j] = tk.Button(self.window)
                botoes[i][j].configure(height=10, width=10, command=lambda botao=(i,j): self.command_botao(botao))
                botoes[i][j].grid(row=i, column=j, sticky="NSEW")
        
        #labels
        global label1 
        label1 = tk.Label(self.window)
        label1.configure(width=60, height=1)
        label1.grid(row=3, column=0, columnspan=3, sticky="W")
                
    def gera_botoes(self, posicao_tupla, letra):
        conteudo_botao = tk.StringVar()
        conteudo_botao.set(letra)
        global botoes
        botoes[posicao_tupla[0]][posicao_tupla[1]].config(textvariable=conteudo_botao)
     
    def gera_label(self, display): 
        conteudo_label = tk.StringVar()
        conteudo_label.set(display)
        global label1
        label1.configure(textvariable=conteudo_label)
    
    def command_botao(self, i):
        print("Click", i)
        
    def iniciar(self):
        self.window.mainloop()
        
tela = Tabuleiro()
tela.gera_label("Legenda Teste")
tela.gera_botoes((0,1), "X")
tela.iniciar()

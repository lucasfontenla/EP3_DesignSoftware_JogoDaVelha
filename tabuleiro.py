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
        self.window.geometry("450x530")
        
        for k in range(0, 3): #gera as linhas e colunas
            self.window.rowconfigure(k, minsize=150)
            self.window.columnconfigure(k, minsize=150)
        self.window.rowconfigure(3, minsize=50) #linha para display das jogadas
         
        global label1 
        label1 = tk.Label(self.window)
        label1.configure(width=450, height=40)
        #label1.grid(row=3, column=0, columnspan=3)
        
    def gera_botoes(self): #lista com lista de linhas
        self.botoes = [[0]*3]*3
       
        for i in range(0, 3):
            for j in range(0, 3):
                self.botoes[i][j] = tk.Button(self.window)
                self.botoes[i][j].configure(height=10, width=10)
                self.botoes[i][j].grid(row=i, column=j, sticky="NSEW")
                
    def gera_label(self, display): 
        conteudo_label = tk.StringVar()
        conteudo_label.set(display)
        global label1
        label1.configure(textvariable=conteudo_label)
        
    def iniciar(self):
        self.window.mainloop()
        
tela = Tabuleiro()
tela.gera_botoes()
tela.gera_label("Legenda Teste")
tela.iniciar()

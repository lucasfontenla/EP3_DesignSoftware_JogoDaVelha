# -*- coding: utf-8 -*-
"""
Lucas Fontenla & Victor Hugo - Engenharia 1B
EP3_JogoDaVelha
"""
import tkinter as tk

class Tabuleiro:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("450x530")
        self.window.rowconfigure(0, minsize=150)
        self.window.rowconfigure(1, minsize=150)
        self.window.rowconfigure(2, minsize=150)
        self.window.columnconfigure(0, minsize=150)
        self.window.columnconfigure(1, minsize=150)
        self.window.columnconfigure(2, minsize=150)
        self.window.columnconfigure(3, minsize=80) #linha para display das jogadas
                
    def gera_botoes(self): #lista com lista de linhas
        self.botoes = [[0]*3]*3
       
        for i in range(0, 3):
            for j in range(0, 3):
                self.botoes[i][j] = tk.Button(self.window)
                self.botoes[i][j].configure(height=10, width=10)
                self.botoes[i][j].grid(row=i, column=j, sticky="NSEW")
        
    def iniciar(self):
        self.window.mainloop()
        
tela = Tabuleiro()
tela.gera_botoes()
tela.iniciar()

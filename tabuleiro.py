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
        self.window.resizable(0,0)
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
        botoes[posicao_tupla[0]][posicao_tupla[1]].config(textvariable=conteudo_botao,\
                state="disabled") #após escrever, o botão é desabilitado
     
    def gera_label(self, display): 
        conteudo_label = tk.StringVar()
        conteudo_label.set(display)
        global label1
        label1.configure(textvariable=conteudo_label, anchor="w")
    
    def command_botao(self, i):
        print("Click", i)
        tela.gera_botoes(i, "X") #testar se o botão funciona

    def mostra_vencedor_reset(self, resultado): #display dos resultados + reset dos botões
        self.janela_vencedor = tk.Toplevel()
        self.janela_vencedor.resizable(0,0)
        self.janela_vencedor.title("Vencedor")
        self.janela_vencedor.geometry("200x180")

        self.janela_vencedor.rowconfigure(0, minsize="100")
        self.janela_vencedor.rowconfigure(1, minsize="30")
        self.janela_vencedor.rowconfigure(2, minsize="30")
        self.janela_vencedor.columnconfigure(0, minsize="200")

        display_vencedor = tk.Message(self.janela_vencedor, text=resultado, font="Verdana 10", justify="center")
        display_vencedor.grid(row=0, column=0, sticky="nsew")

        self.botao_novo_jogo = tk.Button(self.janela_vencedor, text="Novo Jogo", width=10, command=self.limpa_tela)
        self.botao_novo_jogo.grid(row=1, column=0)

        botao_sair = tk.Button(self.janela_vencedor, text="Sair", width=10, command=self.window.destroy)
        botao_sair.grid(row=2, column=0)

    def limpa_tela(self): 
        self.janela_vencedor.destroy()
        for i in range(0,3):
            for j in range(0,3):
                tela.gera_botoes((i, j), "")
                botoes[i][j].config(state="normal")    

    def iniciar(self):
        self.window.mainloop()

#teste das funções        
tela = Tabuleiro()
tela.gera_botoes((0,1), "X")
tela.gera_label("Legenda Teste")
tela.mostra_vencedor_reset("X")
tela.iniciar()

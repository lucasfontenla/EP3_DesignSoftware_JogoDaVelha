# -*- coding: utf-8 -*-
"""
Lucas Fontenla & Victor Hugo - Engenharia 1B
EP3_JogoDaVelha
"""
#NOTAS
#começa com X
import numpy as np #importa numpy para gerar a matrizes

class Jogo:
	def __init__(self):
		global contador #contador de número de jogadas
		contador = 0

		global tabuleiro_virtual
		tabuleiro_virtual = np.zeros([3,3]) #gera o tabuleiro como uma matriz 3x3 de zeros

		self.jogada = "X" #define a primeira jogada como "X"
		self.proxima_jogada = "O"
		self.ganhador = -1 #O valor -1 sempre prossegue o jogo até que haja um ganhador 

	def recebe_jogada(self, posicao_jogada_tupla): #função que recebe a jogada do tabuleiro
		
		self.registra_jogada(posicao_jogada_tupla) #chama a função registra jogada para ser registrada na matriz

		global contador
		contador += 1 #adc 1 cada vez que há uma jogada

		if self.jogada == "X": #sempre que o númeoro for par, escreve "X"
			self.proxima_jogada = "O"

		elif self.jogada == "O":
			self.proxima_jogada = "X"

	def registra_jogada(self, posicao_jogada_tupla): #função responsável por registrar a jogada na matriz
		if self.jogada == "X":
			valor = 1
		elif self.jogada == "O":
			valor = 2

		tabuleiro_virtual[posicao_jogada_tupla[0]][posicao_jogada_tupla[1]] = valor

		self.jogada = self.proxima_jogada

		global contador

	def verifica_ganhador(self): #SOMENTE PARA TESTE DAS FUÇÕES AIDANTE --> AINDA A CRIAR VERIFICAÇÃO FINAL DE GANHADOR
		valores_resultados = list()

		global vencedor
		vencedor = 0

		add_valor_diagonal1 = 1
		add_valor_diagonal2 = 1

		for i in range(0, 3):
			add_valor_linhas = 1
			add_valor_colunas = 1

			for j in range(0, 3):
				add_valor_linhas *= tabuleiro_virtual[i][j]
				add_valor_colunas *= tabuleiro_virtual[j][i]
				
			add_valor_diagonal1 *= tabuleiro_virtual[i][i]
			add_valor_diagonal2 *= tabuleiro_virtual[i][(i*(-1)-1)]

			valores_resultados.append(add_valor_linhas)
			valores_resultados.append(add_valor_colunas)

		valores_resultados.append(add_valor_diagonal1)
		valores_resultados.append(add_valor_diagonal2)

		if valores_resultados.count(1) > 0:
			vencedor = "X"
			return 1
		elif valores_resultados.count(8) > 0:
			vencedor = "O"
			return 2	
		elif valores_resultados.count(0) > 0:
			return -1
		else:
			vencedor = 0
			return 0

	def limpa_jogadas(self): #Função que reseta todo o tabuleiro
		global contador
		global vencedor

		if vencedor == "X":
			self.jogada = "X"

		elif vencedor == "O":
			self.jogada = "O"

		elif vencedor == -1: 
			self.jogada = self.proxima_jogada

		for i in range(0,3):
			for j in range(0,3):
				tabuleiro_virtual[i][j] = 0


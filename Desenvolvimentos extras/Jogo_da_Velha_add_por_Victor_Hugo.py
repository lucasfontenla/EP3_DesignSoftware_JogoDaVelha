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
		self.tabuleiro_virtual = np.zeros([3,3]) #gera o tabuleiro como uma matriz 3x3 de zeros

		self.jogada = "X" #define a primeira jogada como "X"
		self.proxima_jogada = "O"
		self.ganhador = -1 #O valor -1 sempre prossegue o jogo até que haja um ganhador 
		
	def recebe_jogada(self, posicao_jogada_tupla): #função que recebe a jogada do tabuleiro
		self.registra_jogada(posicao_jogada_tupla) #chama a função registra jogada para ser registrada na matriz
		if self.jogada == "X":
			self.proxima_jogada = "O"

		elif self.jogada == "O":
			self.proxima_jogada = "X"

	def registra_jogada(self, posicao_jogada_tupla): #função responsável por registrar a jogada na matriz
		if self.jogada == "X":
			valor = 1
		elif self.jogada == "O":
			valor = 2

		self.tabuleiro_virtual[posicao_jogada_tupla[0]][posicao_jogada_tupla[1]] = valor

		self.jogada = self.proxima_jogada
		
	def verifica_ganhador(self): #SOMENTE PARA TESTE DAS FUÇÕES AIDANTE --> AINDA A CRIAR VERIFICAÇÃO FINAL DE GANHADOR
		valores_resultados = list()
		self.vencedor = 0

		add_valor_diagonal1 = 1
		add_valor_diagonal2 = 1

		for i in range(0, 3):
			add_valor_linhas = 1
			add_valor_colunas = 1
			for j in range(0, 3):
				add_valor_linhas *= self.tabuleiro_virtual[i][j]
				add_valor_colunas *= self.tabuleiro_virtual[j][i]
			add_valor_diagonal1 *= self.tabuleiro_virtual[i][i]
			add_valor_diagonal2 *= self.tabuleiro_virtual[i][(i*(-1)-1)]

			valores_resultados.append(add_valor_linhas)
			valores_resultados.append(add_valor_colunas)

		valores_resultados.append(add_valor_diagonal1)
		valores_resultados.append(add_valor_diagonal2)

		if valores_resultados.count(1) > 0:
			self.vencedor = "X"
			return 1
		elif valores_resultados.count(8) > 0:
			self.vencedor = "O"
			return 2	
		elif valores_resultados.count(0) > 0:
			return -1
		else:
			self.vencedor = 0
			return 0

	def limpa_jogadas(self): #Função que reseta todo o tabuleiro
		if self.vencedor == "X":
			self.jogada = "X"
			self.proxima_jogada = "O"

		elif self.vencedor == "O":
			self.jogada = "O"
			self.proxima_jogada = "X"

		elif self.vencedor == -1: 
			self.jogada = self.proxima_jogada
			if self.jogada == "X":
				self.proxima_jogada = "O"
			else:
				self.proxima_jogada = "X"
		self.tabuleiro_virtual = np.zeros([3,3])


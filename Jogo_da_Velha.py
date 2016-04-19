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

		self.proxima_jogada = "X" #define a primeira jogada como "X"
		self.ganhador = -1 #O valor -1 sempre prossegue o jogo até que haja um ganhador 

	def recebe_jogada(self, posicao_jogada_tupla): #função que recebe a jogada do tabuleiro
		
		self.registra_jogada(posicao_jogada_tupla) #chama a função registra jogada para ser registrada na matriz

		global contador
		contador += 1 #adc 1 cada vez que há uma jogada

		if contador % 2 == 0: #sempre que o númeoro for par, escreve "X"
			self.proxima_jogada = "X"
		else:
			self.proxima_jogada = "O"

	def registra_jogada(self, posicao_jogada_tupla): #função responsável por registrar a jogada na matriz
		if self.proxima_jogada == "X":
			valor = 1
		else:
			valor = 2

		tabuleiro_virtual[posicao_jogada_tupla[0]][posicao_jogada_tupla[1]] = valor

		global contador

		print(tabuleiro_virtual)
		if contador > 4: #só começa a avaliar o resultado se a número de jogadas for maior que 4, já que ninguém ganha o jogo com menos de 4 rodadas
			self.verifica_ganhador() #chama a função que verifica ganhador

	def verifica_ganhador(self): #SOMENTE PARA TESTE DAS FUÇÕES AIDANTE --> AINDA A CRIAR VERIFICAÇÃO FINAL DE GANHADOR
		lista_de_zeros = list()
		for i in tabuleiro_virtual:
			for j in i:
				if j == 0:
					lista_de_zeros.append(j)
				else:
					pass

		if lista_de_zeros.count(0) == 0:
			self.limpa_jogadas()
			self.ganhador = 1

		else:
			self.ganhador = -1

	def limpa_jogadas(self): #Função que reseta todo o tabuleiro
		for i in range(0,3):
			for j in range(0,3):
				tabuleiro_virtual[i][j] = 0


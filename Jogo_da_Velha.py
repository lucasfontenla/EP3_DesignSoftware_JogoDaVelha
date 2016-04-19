# -*- coding: utf-8 -*-
"""
Lucas Fontenla & Victor Hugo - Engenharia 1B
EP3_JogoDaVelha
"""
#NOTAS
#começa com X
import numpy as np

class Jogo:
	def __init__(self):
		global contador
		contador = 0

		global tabuleiro_virtual
		tabuleiro_virtual = np.zeros([3,3])

		self.proxima_jogada = "X"
		self.ganhador = -1

	def recebe_jogada(self, posicao_jogada_tupla):
		
		self.registra_jogada(posicao_jogada_tupla)

		global contador
		contador += 1

		if contador % 2 == 0:
			self.proxima_jogada = "X"
		else:
			self.proxima_jogada = "O"

	def registra_jogada(self, posicao_jogada_tupla):
		if self.proxima_jogada == "X":
			valor = 1
		else:
			valor = 2

		tabuleiro_virtual[posicao_jogada_tupla[0]][posicao_jogada_tupla[1]] = valor

		global contador

		print(tabuleiro_virtual)
		if contador > 4:
			self.verifica_ganhador()

	def verifica_ganhador(self): #SOMENTE PARA TESTE DAS FUÇÕES AIDANTE DESSA
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

	def limpa_jogadas(self):
		for i in range(0,3):
			for j in range(0,3):
				tabuleiro_virtual[i][j] = 0


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

	def recebe_jogada(self, posicao_jogada_tupla):
		
		self.registra_jogada(posicao_jogada_tupla)

		global contador
		contador += 1

		if contador % 2 == 0:
			self.proxima_jogada = "X"
		else:
			self.proxima_jogada = "O"

		print(posicao_jogada_tupla, contador, self.proxima_jogada)

	def registra_jogada(self, posicao_jogada_tupla):
		if self.proxima_jogada == "X":
			valor = 1
		else:
			valor = 2

		tabuleiro_virtual[posicao_jogada_tupla[0]][posicao_jogada_tupla[1]] = valor
		print(tabuleiro_virtual)

	def limpa_jogadas(self):
		tabuleiro_virtual = np.zeros([3,3])
		


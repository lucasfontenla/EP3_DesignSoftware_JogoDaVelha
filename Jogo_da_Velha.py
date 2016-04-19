# -*- coding: utf-8 -*-
"""
Lucas Fontenla & Victor Hugo - Engenharia 1B
EP3_JogoDaVelha
"""
#NOTAS
#começa com X

class Jogo:
	def __init__(self):
		global contador
		contador = 0

	def recebe_jogada(self, i):
		self.proxima_jogada = str()

		global contador
		contador += 1

		if contador % 2 == 0:
			self.proxima_jogada = "X"
		else:
			self.proxima_jogada = "O"

		print(i, contador, self.proxima_jogada)


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
		#jogadores
		self.jogador1 = str()
		self.vitorias_jogador1 = int()
		self.jogador2 = str()
		self.vitorias_jogador2 = int()
		#contador de número de partidas
		self.contador = int()
		self.contador_max = int()
		#mostra vencedor dos dois modos
		self.vencedor = str()
		self.vencedor_melhor3 = str()

		self.modo_jogo = int()

		self.tabuleiro_virtual = np.zeros([3,3]) #gera o tabuleiro como uma matriz 3x3 de zeros

		self.jogada = "X" #define a primeira jogada como "X"
		self.proxima_jogada = "O"

	def recebe_jogadores(self, jogador1, jogador2):
		self.jogador1 = "{0}".format(jogador1) #X
		self.jogador2 = "{0}".format(jogador2) #O

	def registra_modo(self, modo):
		self.modo_jogo = modo

	def recebe_jogada(self, posicao_jogada_tupla): #função que recebe a jogada do tabuleiro
		
		self.registra_jogada(posicao_jogada_tupla) #chama a função registra jogada para ser registrada na matriz

		if self.jogada == "X": #sempre que o númeoro for par, escreve "X"
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

	#função que verifica se há ganhador	
	#a função multiplica os valores das linhas, colunas e diagonais. Como X = 1, se "X" ganhar, a multiplicação da linha é 1
	#o mesmo para "O", só que como seu valor é 2, a multiplicação será 8. Espaços vazios são 0, desse modo qualquer multiplicação
	#com resultado 0 significa que o jogo ainda não acabou pois há espaço livre. Se nem 0, nem 1, nem 8 for encontrado, houve empate.
	def verifica_ganhador(self):
		valores_resultados = list()

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
			self.contador += 1
			self.vencedor = "X"
			self.vitorias_jogador1 += 1
			return 1
		elif valores_resultados.count(8) > 0:
			self.contador += 1
			self.vencedor = "O"
			self.vitorias_jogador2 += 1
			return 2	
		elif valores_resultados.count(0) > 0:
			return -1
		else:
			self.vencedor = 0
			self.contador += 1
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

	def verifica_modo(self):
		contador_max = 3

		if self.vitorias_jogador1 > self.vitorias_jogador2:
			self.vencedor_melhor3 = "Vencedor(a) {0}".format(self.jogador1)
		elif self.vitorias_jogador1 < self.vitorias_jogador2:
			self.vencedor_melhor3 = "Vencedor(a) {0}".format(self.jogador2)
		else:
			self.vencedor_melhor3 = "Empate"

		if self.modo_jogo == 1:
			if self.vitorias_jogador1 == 2 or self.vitorias_jogador2 == 2 and self.contador == 2:
				self.contador = 0
				self.vitorias_jogador1 = self.vitorias_jogador2 = 0
				return -1
			elif self.contador == contador_max:
				self.contador = 0
				self.vitorias_jogador1 = self.vitorias_jogador2 = 0
				return -1
			else:
				return 1

		return 0
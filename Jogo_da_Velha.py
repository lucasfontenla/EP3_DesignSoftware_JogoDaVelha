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
		if self.jogada == "X": #se a jogada foi "X", registra como próxima jogada o "O"
			self.proxima_jogada = "O"

		elif self.jogada == "O": #se a jogada foi "O", registra a próxima jogada como "X"
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
		valores_resultados = list() #lista que armazena as 8 multiplicações possíveis (3-colunas, 3-linhas, 2-diagonais)
		self.vencedor = 0 #armazena qual o vencedor

		add_valor_diagonal1 = 1 #o valor inicial é 1, porque qualquer número multiplicado por 1 é ele mesmo
		add_valor_diagonal2 = 1

		for i in range(0, 3): #laço for para pegar as 3 linhas e 3 colunas, mais os 3 valores de cada diagonal
			add_valor_linhas = add_valor_colunas = 1 #reseta o valor que vai ser adicionado à multiplicação

			for j in range(0, 3): #laço para pegar os três valores de cada linha e cada coluna
				add_valor_linhas *= self.tabuleiro_virtual[i][j] #o valor pego é multiplicado pelo add_valor
				add_valor_colunas *= self.tabuleiro_virtual[j][i] 

			add_valor_diagonal1 *= self.tabuleiro_virtual[i][i]
			add_valor_diagonal2 *= self.tabuleiro_virtual[i][(i*(-1)-1)]

			valores_resultados.append(add_valor_linhas) #o valor é adicionado `lista com todos os resultados
			valores_resultados.append(add_valor_colunas)

		valores_resultados.append(add_valor_diagonal1)
		valores_resultados.append(add_valor_diagonal2)

		if valores_resultados.count(1) > 0: #se encontrou um resultado 1, o "X" ganhou
			self.vencedor = "X"
			return 1
		elif valores_resultados.count(8) > 0:
			self.vencedor = "O"
			return 2	
		elif valores_resultados.count(0) > 0: #se ainda existe algum valor 0, significa que ainda há espaços vazios e ninguém venceu
			return -1
		else:
			self.vencedor = 0 #se não foi adicionado nenhum valor ao vencedor (ninguém ganhou) e não há espaços livres, retorna 0
			return 0

	def limpa_jogadas(self): #Função que reseta todo o tabuleiro
		if self.vencedor == "X": #quem ganha começa o jogo
			self.jogada = "X"
			self.proxima_jogada = "O"

		elif self.vencedor == "O":
			self.jogada = "O"
			self.proxima_jogada = "X"

		elif self.vencedor == -1: #caso haja empate, quem começa é o próximo jogador
			self.jogada = self.proxima_jogada
			if self.jogada == "X":
				self.proxima_jogada = "O"
			else:
				self.proxima_jogada = "X"

		self.tabuleiro_virtual = np.zeros([3,3]) #reseta o tabuleiro virtual, todos as casas ficam vazias


'''
Classe Empregado Mensalista
'''
from Empregado import Empregado


class EmpregadoMensalista(Empregado):
	'''
	Empregado Mensalista
	'''

	def __init__(self, primeiro_nome, ultimo_nome, salario, valorFalta):
		super().__init__(primeiro_nome, ultimo_nome, salario)
		self.__valor_falta = valorFalta
		self.__faltas = 0


	def calcular_pagamento(self):
		'''
		Calcula o Pagamento do Mensalista
		'''
		return self.salario - (self.__valor_falta * self.__faltas)


	def adicionar_faltas(self, faltas):
		'''
		Adiciona Faltas
		'''
		self.__faltas = self.__faltas + faltas

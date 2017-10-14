'''
Classe Empregado Horista
'''
from Empregado import Empregado


class EmpregadoHorista(Empregado):
	'''
	Empregado Horista
	'''
	def __init__(self, primeiro_nome, ultimo_nome, salario):
		super().__init__(primeiro_nome, ultimo_nome, salario)
		self.__horas = 0


	def calcular_pagamento(self):
		'''
		Calcula o Pagamento do Horista
		'''
		return self.__horas * self.salario


	def adicionar_horas(self, horas):
		'''
		Adicionar Horas
		'''
		self.__horas = self.__horas + horas

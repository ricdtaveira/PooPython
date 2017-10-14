'''
Classe Empregado Comissionado
'''

from Empregado import Empregado


class EmpregadoComissionado(Empregado):
	'''
	Empregado Comissionado
	'''
	def __init__(self, primeiro_nome, ultimo_nome, salario, comissao):
		super().__init__(primeiro_nome, ultimo_nome, salario)
		self.__comissao = comissao
		self.__unidades = 0


	def calcular_pagamento(self):
		''' Calcula o pagamento comissionado '''
		return self.salario + (self.comissao * self.unidades)


	@property
	def comissao(self):
		''' Retorna comissao '''
		return self.__comissao


	@property
	def unidades(self):
		''' Retorna unidades vendidas '''
		return self.__unidades


	def adicionar_vendas(self, unidades):
		'''
		Adiciona Vendas
		'''
		self.__unidades = self.__unidades + unidades

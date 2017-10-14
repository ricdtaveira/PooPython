'''
Classe Empregado
'''

class Empregado():
	'''
	Atributos: primeiro_nome, ultimo_nome, salario.
	Metodos: gets para cada atributo, e imprimirCheckPagamento.
	'''
	def __init__(self, primeiro_nome, ultimo_nome, salario):
		self.__primeiro_nome = primeiro_nome
		self.__ultimo_nome = ultimo_nome
		self.__salario = salario


	@property
	def primeiro_nome(self):
		''' Retorna o valor do primeiro nome '''
		return self.__primeiro_nome


	@property
	def ultimo_nome(self):
		''' Retorna o valor do ultimo nome '''
		return self.__ultimo_nome


	@property
	def salario(self):
		''' Retorna o valor do salario '''
		return self.__salario



	def calcular_pagamento(self):
		''' Metódo definido por herança '''
		pass


	def nome_completo(self):
		''' Retorna o nome completo '''
		return self.__ultimo_nome + ", " + self.__primeiro_nome


	def imprimir_check_pagamento(self):
		''' Imprime o pagamento em um determinado formato '''
		return "Pagamento: {0} R$ {1}".format(self.nome_completo(), self.calcular_pagamento())

'''
Classe Produto
'''


class Produto():
    '''
    Produto
    '''
    def __init__(self, descricao, unidade, valor):
        self.__descricao = descricao
        self.__unidade = unidade
        self.__valor = valor


    @property
    def descricao(self):
        '''
        Retorna descricao
        '''
        return self.__descricao


    @descricao.setter
    def descricao(self, descricao):
        '''
        Atribui um novo valor a descricao
        '''
        self.__descricao = descricao


    @property
    def unidade(self):
        '''
        Retorna unidade
        '''
        return self.__unidade


    @unidade.setter
    def unidade(self, unidade):
        '''
        Atribui um novo valor a unidade
        '''
        self.__unidade = unidade


    @property
    def valor(self):
        '''
        Retorna valor
        '''
        return self.__valor


    @valor.setter
    def valor(self, valor):
        '''
        Atribui um novo valor
        '''
        self.__valor = valor

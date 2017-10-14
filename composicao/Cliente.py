'''
Classe Cliente
'''


class Cliente():
    '''
    Cliente
    '''
    def __init__(self, nome):
        self.__nome = nome


    @property
    def nome(self):
        '''
        Retorna nome
        '''
        return self.__nome


    @nome.setter
    def nome(self, nome):
        '''
        Atribui um novo valor a nome
        '''
        self.__nome = nome

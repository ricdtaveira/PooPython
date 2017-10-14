'''
Classe ItemNotaFiscal
'''


class ItemNotaFiscal():
    '''
    Item Nota Fiscal
    '''
    def __init__(self, sequencial, quantidade, produto):
        self.__sequencial = sequencial
        self.__quantidade = quantidade
        self.__produto = produto


    @property
    def produto(self):
        '''
        Retorna produto
        '''
        return self.__produto


    @produto.setter
    def produto(self, produto):
        '''
        Atribui um novo valor a produto
        '''
        self.__produto = produto


    @property
    def quantidade(self):
        '''
        Retorna quanntidade
        '''
        return self.__quantidade


    @quantidade.setter
    def quantidade(self, quantidade):
        '''
        Atribui um novo valor a quantidade
        '''
        self.__quantidade = quantidade


    @property
    def sequencial(self):
        '''
        Retorna sequencial
        '''
        return self.__sequencial


    @sequencial.setter
    def sequencial(self, sequencial):
        '''
        Atribui um novo valor a sequencial
        '''
        self.__sequencial = sequencial

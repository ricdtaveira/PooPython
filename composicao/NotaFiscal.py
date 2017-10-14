'''
Classe Nota Fiscal
'''


class NotaFiscal():
    '''
    Nota Fiscal
    '''
    def __init__(self, numero, data_emissao, items, cliente):
        self.__numero = numero
        self.__data_emissao = data_emissao
        self.__items = [] if items is None or items == [] else items
        self.__cliente = cliente


    @property
    def numero(self):
        '''
        Retorna numero
        '''
        return self.__numero


    @numero.setter
    def numero(self, numero):
        '''
        Atribui um novo valor a numero
        '''
        self.__numero = numero


    @property
    def data_emissao(self):
        '''
        Retorna data_emissao
        '''
        return self.__data_emissao


    @data_emissao.setter
    def data_emissao(self, data_emissao):
        '''
        Atribui um novo valor a data_emissao
        '''
        self.__data_emissao = data_emissao


    @property
    def items(self):
        '''
        Retorna items
        '''
        return self.__items


    @items.setter
    def items(self, items):
        '''
        Atribui um novo valor a items
        '''
        self.__items = items


    @property
    def cliente(self):
        '''
        Retorna Cliente
        '''
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente


    def inserir_item_nota_fiscal(self, item):
        '''
        Inseri um novo item
        '''
        self.__items.append(item)


    def calcular_nota_fiscal(self):
        '''
        Calcula o valor da nota fiscal
        '''
        sum_nota_fiscal = lambda func, x: 0 if x == [] else func(x[:1][0]) + sum_nota_fiscal(func, x[1:])
        item_valor = lambda x: x.quantidade * x.produto.valor
        return sum_nota_fiscal(item_valor, self.__items)

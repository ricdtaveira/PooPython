'''
Classe Aviao
'''

from Veiculo import Veiculo

class Aviao(Veiculo):
    '''
    Aviao
    '''
    def freia(self):
        '''
        freia
        '''
        print("Aviao freia")


    def acelera(self):
        '''
        acelera
        '''
        print("Aviao acelera")


    def vira(self, direcao):
        '''
        vira
        '''
        print("Aviao vira para {0}".format(direcao))

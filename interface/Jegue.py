'''
Classe Jegue
'''

from Veiculo import Veiculo

class Jegue(Veiculo):
    '''
    Jegue
    '''
    def freia(self):
        '''
        freia
        '''
        print("Jegue freia")


    def acelera(self):
        '''
        acelera
        '''
        print("Jegue acelera")


    def vira(self, direcao):
        '''
        vira
        '''
        print("Jegue vira para {0}".format(direcao))

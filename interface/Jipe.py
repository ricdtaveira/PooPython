'''
Classe Jipe
'''

from Veiculo import Veiculo

class Jipe(Veiculo):
    '''
    Jipe
    '''
    def freia(self):
        '''
        freia
        '''
        print("Jipe freia")


    def acelera(self):
        '''
        acelera
        '''
        print("Jipe acelera")


    def vira(self, direcao):
        '''
        vira
        '''
        print("Jipe vira para {0}".format(direcao))

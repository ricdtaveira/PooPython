'''
Classe Onibus
'''

from Veiculo import Veiculo

class Onibus(Veiculo):
    '''
    Onibus
    '''
    def freia(self):
        '''
        freia
        '''
        print("Onibus freia")


    def acelera(self):
        '''
        acelera
        '''
        print("Onibus acelera")


    def vira(self, direcao):
        '''
        vira
        '''
        print("Onibus vira para {0}".format(direcao))

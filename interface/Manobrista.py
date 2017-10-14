'''
Classe Manobrista
'''


class Manobrista():
    '''
    Manobrista
    '''
    def estaciona(self, veiculo):
        '''
        Estaciona
        '''
        veiculo.vira("Direita")
        veiculo.vira("Esquerda")
        veiculo.freia()

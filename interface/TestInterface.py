'''
Teste Interface
'''

from Jipe import Jipe
from Jegue import Jegue
from Manobrista import Manobrista


if __name__ == "__main__":
    V1 = Jipe()
    V2 = Jegue()
    MANO = Manobrista()


    MANO.estaciona(V1)
    MANO.estaciona(V2)

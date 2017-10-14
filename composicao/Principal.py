'''
Principal
'''


from datetime import datetime
from Produto import Produto
from Cliente import Cliente
from ItemNotaFiscal import ItemNotaFiscal
from NotaFiscal import NotaFiscal


if __name__ == "__main__":

    C1 = Cliente("Jose Maria")

    P1 = Produto("Farinha", "KG", 1.00)
    P2 = Produto("Feijao", "KG", 5)
    P3 = Produto("Macarrao", "PC", 3.5)

    NF1 = NotaFiscal(None, None, None, None)

    NF1.cliente = C1

    NF1.data_emissao = str(datetime.now())


    ITNF1 = ItemNotaFiscal(1, 10, P1)
    ITNF2 = ItemNotaFiscal(2, 5, P2)
    ITNF3 = ItemNotaFiscal(3, 6, P3)


    NF1.inserir_item_nota_fiscal(ITNF1)
    NF1.inserir_item_nota_fiscal(ITNF2)
    NF1.inserir_item_nota_fiscal(ITNF3)

    print

    print("O valor da Nota Fiscal= {0}".format(NF1.calcular_nota_fiscal()))

''' Exemplos de Uso '''

from EmpregadoMensalista import EmpregadoMensalista
from EmpregadoHorista import EmpregadoHorista
from EmpregadoComissionado import EmpregadoComissionado

if __name__ == "__main__":

	C_EMP = EmpregadoComissionado("Jose", "Sales", 25000.00, 1000.00)
	H_EMP = EmpregadoHorista("Carlos", "Sousa", 6.50)
	M_EMP = EmpregadoMensalista("Joao", "Moura", 2000.00, 20.00)

	C_EMP.adicionar_vendas(5)
	H_EMP.adicionar_horas(40)
	M_EMP.adicionar_faltas(5)

	print("Pagamento Comisssionado: R$ " + str(C_EMP.calcular_pagamento()))
	print("Pagamento Horista      : R$ " + str(H_EMP.calcular_pagamento()))
	print("Pagamento Mensalista   : R$ " + str(M_EMP.calcular_pagamento()))

	print()
	print()

	print(C_EMP.imprimir_check_pagamento())
	print(H_EMP.imprimir_check_pagamento())
	print(M_EMP.imprimir_check_pagamento())

import data
from conta import Conta

conta = Conta(1234,'João',900.00,1000)
conta2 = Conta(569,'Pedro',500,1000)

conta2.transferir(15.55,conta)

#conta.imprimir()
# conta.depositar(157.58)
# conta.sacar(1000)

conta.imprimir()
conta2.imprimir()

dia = data.Data()
dia.datanow()
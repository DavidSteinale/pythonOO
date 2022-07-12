class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        print("Objeto criado com sucesso..")

    def imprimir(self):
        print()
        print('INFORMAÇÂO DA CONTA:')
        print('Número da conta:', self.numero)
        print('Titular da conta:', self.titular)
        print('Saldo da conta {} é {:.2f}'.format(self.numero,self.saldo))
        print('Limite:{:.2f}'.format(self.limite))
        print()

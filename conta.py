class Conta:

    def __init__(self, numero, titular, saldo, limite): #METODO CONSTRUTOR
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        print("Objeto criado com sucesso..")

    def depositar(self,deposito):
        self.saldo += deposito
        print('Saldo realizado com sucesso, valor atual é de {:.2f}'.format(self.saldo))

    def sacar(self,sacar):
        total = self.saldo+self.limite
        if(sacar<total):
            self.saldo -= sacar
            print('Saque realizado com sucesso, valor atual é de {:.2f}'.format(self.saldo))
        else:
            print('Valor do saque maior que saldo+limite, total de {}'.format(total))


    def imprimir(self):
        print()
        print('INFORMAÇÂO DA CONTA:')
        print('Número da conta:', self.numero)
        print('Titular da conta:', self.titular)
        print('Saldo da conta {} é {:.2f}'.format(self.numero,self.saldo))
        print('Limite:{:.2f}'.format(self.limite))
        print()
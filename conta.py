class Conta:

    def __init__(self, numero, titular, saldo, limite): #METODO CONSTRUTOR
        self.__numero = numero ## o "__" indica que o atributo é privado
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self,deposito):
        self.__saldo += deposito
        print('Saldo realizado com sucesso, valor atual é de {:.2f}'.format(self.__saldo))

    def sacar(self,sacar):
        __total = self.__saldo+self.__limite
        if(sacar<__total):
            self.__saldo -= sacar
            print('Saque realizado com sucesso, valor atual é de {:.2f}'.format(self.__saldo))
        else:
            print('Valor do saque maior que saldo+limite, total de {}'.format(__total))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def imprimir(self):
        print()
        print('INFORMAÇÂO DA CONTA:')
        print('Número da conta:', self.__numero)
        print('Titular da conta:', self.__titular)
        print('Saldo da conta {} é {:.2f}'.format(self.__numero,self.__saldo))
        print('Limite:{:.2f}'.format(self.__limite))
        print()

    def get_saldo(self):
        return self.__saldo

    def set_limiti(self,limite):
        self.__limite = limite
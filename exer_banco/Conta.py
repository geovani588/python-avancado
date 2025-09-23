import abc

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abc.abstractmethod
    def sacar(self, valor: float) -> float:
        ...
    
    def depositar(self, valor)-> float:
        self.saldo += valor
        self.detalhes(f'Deposito de {valor}')
        return self.saldo
        
    def detalhes(self, msg: str ='') -> None:
        print(f'O seu saldo é {self.saldo:.2f} {msg}')

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'Saque de {valor}')
            return self.saldo
        
        print('Não foi possivel sacar o valor desejado')
        self.detalhes(f'Saque negado {valor}')
        return self.saldo


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta:int, saldo: int=0, limite: int=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo

        print('Não foi possível sacar o valor desejado')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')
        return self.saldo


        
if __name__ == '__main__':
    cp = ContaPoupanca(111,111,0)
    cp.sacar(1)
    cp.depositar(1)
    cp.sacar(1)
    cp.sacar(1)
    print('\n')

    cc1 = ContaCorrente(111, 222, 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)
    cc1.sacar(1)
        
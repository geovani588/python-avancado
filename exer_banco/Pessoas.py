import Conta

class Pessoas:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        
    @property
    def nome(self: str):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome 
        
    @property
    def idade(self: int):
        return self._idade   
    
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'
        
class Cliente(Pessoas):
    def __init__(self, nome: str, idade: int)-> None:
        super().__init__(nome, idade)
        self.conta = None
        
   
        
if __name__ == '__main__':
    c1 = Cliente('Ana', 25)
    print(c1)
    c1.conta = Conta.ContaCorrente(111, 222, 0, 0)
    print(c1.conta)
    
    c2 = Cliente('mario', 25)
    print(c2)
    c2.conta = Conta.ContaPoupanca(111, 333, 0)
    print(c2.conta)
    
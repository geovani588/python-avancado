import Conta
import Pessoas

class Banco:
    def __init__(self, 
                 agencia: list[int] | None = None,
                 clientes: list[Pessoas.Cliente] | None = None,
                 contas: list[Conta.Conta] | None = None,
    ):
        self.agencia = agencia or []
        self.clientes = clientes or []
        self.contas = contas or []
    
    
    def _checar_agencia(self,conta):
        if conta.agencia in self.agencia:
            print('Agência válida')
            return True
        return False
        
    def _checar_agencia(self,cliente): 
        if cliente in self.clientes:
            print('cliente válida')
            return True 
        return False  


    def _checar_agencia(self,conta):    
        if conta in self.contas:
            print('conta válida')
            return True 
        return False    
        
    def autenticar(self, cliente, conta):
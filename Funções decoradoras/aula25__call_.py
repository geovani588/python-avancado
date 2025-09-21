# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

class CallMe:
    def __init__(self,phone):
        self.phone = phone
        
    def __call__(self, *args, **kwds):
        print(f'Ligando para {self.phone}...')


call1 = CallMe('1234-5678')
call1()
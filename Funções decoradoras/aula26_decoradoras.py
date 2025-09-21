# Classes decoradoreas (Decorator classes)

class Multiplicar:
    def __init__(self, func):
        self.func = func
        self._multiplicadora = 10
        
    
    def __call__(self, *args, **kwargs):
        resultado = self.func(*args, **kwargs)
        return resultado * self._multiplicadora

@Multiplicar # classe decoradora
def soma(x,y):
    return x + y

@Multiplicar
def menos(x,y):
    return x - y


dois_mais_quatro = soma(2,4)
print(dois_mais_quatro)

cinco_menos_um = menos(5,1)
print(cinco_menos_um)

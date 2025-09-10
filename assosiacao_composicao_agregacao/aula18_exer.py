# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela
#ctrl + d para selecionar
class Carro:

    
    def __init__(self,nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
    
    @property    
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,valor):
        self._motor = valor
    
    
    @property    
    def fabricante(self):
        return self._fabricante
        
    @fabricante.setter
    def fabricante(self,valor):
        self._fabricante = valor
    
class Motor:
        def __init__(self,nome):
            self.nome = nome
   
    
class Fabricante:
        def __init__(self,nome):
            self.nome = nome
            
ferrari = Carro('Ferrari S.p.A')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')

ferrari.fabricante = volkswagen
ferrari.motor = motor_1_0
print(ferrari.nome, ferrari.fabricante.nome, ferrari.motor.nome)


ferrari = Carro("Ferrari 812 Superfast")
volkswagen = Fabricante("Volkswagen")
motor_v12 = Motor("V12 6.5L")

ferrari.fabricante = volkswagen
ferrari.motor = motor_v12

print(ferrari.nome, ferrari.fabricante.nome, ferrari.motor.nome)


fusca = Carro("fusca")
volkswagen = Fabricante("Volkswagen")
motor_1_0 = Motor("1.0")

fusca.fabricante = volkswagen
fusca.motor = motor_1_0

print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)
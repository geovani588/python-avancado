# Metodo em instancancias de classes Python
# Hard coded - e algo que foi escrito diretamente no códico
class Carro:
    def __init__(self,nome):
        # self.nome = 'fusca', # hard coded
        self.nome = nome,
        
    def acelerar(efc):
        print(f'{efc.nome} esta acelerando...')

string = 'geovani'
print(string.upper())# centralizar nome


fusca = Carro('Fusca') # dados carros
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
        



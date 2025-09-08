# Escopo da classe e de métodos da classe

class Animal:
    def __init__(self,nome):
        self.nome = nome          # escopo da instância (atributo), acessível em toda a classe
        variavel = 'valor'        # escopo local do __init__, só existe dentro deste método
        print(variavel)           # pode usar aqui porque está dentro do mesmo escopo (__init__)

    def comendo(self, alimento):
        return f'{self.nome} está comando {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    
leao = Animal(nome='Leão')
# print(leao.nome)
print(leao.executar('maçã'))
    
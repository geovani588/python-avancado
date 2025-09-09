# Metodos de classe + factories(fabricas)
# São metodos onde "self" sera "cls", ou seja,
# ao inves de recever a instância no primeiro
# parâmetro, receveremos a propria class.

class Pessoa:
    ano = 2025 # atributo de classe
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def metodo_de_classe(cls):
        print('Hey')
        
    @classmethod
    def metodo_com_50_anos(cls,nome):
        return cls(nome,50)
    
    @classmethod
    def criar_sem_nome(cls,idade):
        return cls('Anonima', idade)
        
p1 = Pessoa('joão', 34)
p2 = Pessoa.metodo_com_50_anos('Helena')
p3 = Pessoa('Anonima', 23)
p4 = Pessoa.criar_sem_nome(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)

# print(Pessoa.ano)
# Pessoa.metodo_de_classe()
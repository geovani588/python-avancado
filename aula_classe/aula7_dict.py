# __dict__ e vars para atributos de instancia


class Pessoa:
    ano_atual = 2025
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa('joao', 35)
# p1.nome = 'EITA'
# print(p1.idade)
print(p1.__dict__) # Ele vai pegar todos valores {'nome': 'EITA', 'idade': 35}
print(vars(p1))# igaul dict
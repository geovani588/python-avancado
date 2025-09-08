class Pessoa: # e para criar o molde da classe
    def __init__(self, nome, sobrenome):# primeiro coisa self, segundo o nome do atributo
        self.nome = nome
        self.sobrenome = sobrenome

# Criando as instâncias
p1 = Pessoa('geovani', 'oliveira')
p2 = Pessoa('Maria', 'Joana')

# Imprimindo os atributos
print(p1.nome)
print(p1.sobrenome+'\n')

print(p2.nome)
print(p2.sobrenome)


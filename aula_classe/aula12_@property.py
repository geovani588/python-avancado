# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

class Caneta:
    def __init__(self, cores_tinta,):
        self.cores_tinta = cores_tinta   # lista com várias cores
        self._cor_atual = cores_tinta[0] # começa na primeira cor

    @property
    def cor(self):
        print('PROPERTY cor_tinta')
        return self._cor_atual

   

    def mudar_cor(self, nova_cor):
        if nova_cor in self.cores_tinta:
            self._cor_atual = nova_cor
        else:
            print(f"A cor {nova_cor} não existe nessa caneta.")


caneta = Caneta(["Azul", "Vermelha", "Preta"])

print(caneta.cor)    
caneta.mudar_cor("Vermelha")
print(caneta.cor)     
caneta.mudar_cor("Preta")
print(caneta.cor)    



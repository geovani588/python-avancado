class Motor:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Motor: {self.nome}"


class Fabricante:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f"Fabricante: {self.nome}"


class Carro:
    def __init__(self, nome, motor, fabricante):
        self.nome = nome
        self.motor = motor       
        self.fabricante = fabricante  

    def __str__(self):
        return (f"Carro: {self.nome}\n"
                f"{self.motor}\n"
                f"{self.fabricante}")


motor1 = Motor("V8 5.0")
fabricante1 = Fabricante("Ford")
carro1 = Carro("Mustang", motor1, fabricante1)

print(carro1)

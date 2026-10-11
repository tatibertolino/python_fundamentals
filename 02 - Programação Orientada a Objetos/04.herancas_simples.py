class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass # não precisa definir nada, puxa tudo da classe pai

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas) # estende as características da classe pai
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("preta", "ABC-1234", 2)
# moto.ligar_motor()

carro = Carro("branco", "XYZ-9900", 4)
# carro.ligar_motor()

caminhao = Caminhao("Roxo", "GJS-5646", 8, False) #tem q ir dando os comportamentos da pai e da filho
# caminhao.ligar_motor()
# caminhao.esta_carregado()

print(carro)
print(moto)
print(caminhao)




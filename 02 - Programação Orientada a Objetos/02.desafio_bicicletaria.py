# João tem uma bicletaria e precisa cadastrar as vendas
# crie um programa que informa: cor, modelo, ano e valor das bicicletas
# os comportamentos são: buzinar, parar e correr

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # métodos são funções dentro de uma classe
    def buzinar(self):
        print("Plim plim")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada")

    def correr(self):
        print("Vruuuuuum ...")

    # desse jeito não é usual, pq atributos são acessíveis
    # não pode definir o método(funções) do mesmo nome dos atributos
    def get_cor(self):
        return self.cor
    #tem q definir a classe e depois ir colocando as funções.
    # depois embaixo dá os comportamentos e chama as funções
    
    # def __str__(self):
    #     return f'Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}' <-complicado

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

# quando definir um método, tem que colocar pelo menos um atributo, que é o self       

# init é um construtor
# o self é a referência ao próprio objeto, é referência explícita
# this é referência implícita
# ele representa a instância do objeto. Boas práticas pede o self.

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
b2.buzinar() # = Bicicleta.buzinar(b2)
# quando define um atributo, fica assim, mas pode usar print(b2.cor), fica mais fácil
print(b2.get_cor())

# para exibir as instâncias, só dar print nelas -- print(b2)
print(b2) # <__main__.Bicicleta object at 0x000001519CA082D0>
# não é intuitivo
# então faz um def __str__(self) (método) que aceita valores string

# erro comuns: não colocar argumento nos métodos
# colocar outro argumento que não self, o python interpreta como o self, mesmo q não tenho o mesmo nome

# sempre é executado quando a instância da classe é criado
# __init__
# esses __ são métodos especiais, só usa quando sabe o que faz
# ele faz alocação de memória

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo instância da classe") #mensagem pra mostrar funcionando
        # ele só limpa no final
    
    def falar(self):
        print("auau")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)

c = Cachorro("Chappie", "amarelo")
c.falar()

del c #para forçar a limpeza antes)

criar_cachorro()
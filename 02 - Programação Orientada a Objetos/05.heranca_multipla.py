class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
            return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw): # precisa ter chave e valor na parte de parâmetros
        self.cor_pelo = cor_pelo
        super().__init__(**kw) # passa o kwargs pra classe pai

    def __str__(self):
        # return self.__class__.__name__ # retorna o nome da instância da classe
        return "Mamífero"
    
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

    def __str__(self):
        return "Ave" #se isso existir, ele não chega até a classe de cima, pq já encontrou nessa classe

# class Cachorro(Mamifero):
#     pass

class Gato(Mamifero):
    pass

class FalarMixin:
    def falar(self):
        return "Oi, estou falando"

# class Leao(Mamifero):
#     pass

class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_pelo, cor_bico, nro_patas):
        # print(Ornitorrinco.__mro__) só pra saber a ordem de leitura
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)

    def __str__(self):
        return "Ornitorrinco" #se tem esse, é o primeiro que pega

gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato) # pega a str da classe mamíferos, pq não tem str

ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo="Marrom", cor_bico = "Laranja")
print(ornitorrinco) # pega a str da classe ornitorrinco pq tem str
print(ornitorrinco.falar())

# começa a ficar complexo o código
# usar com parcimônia
# mro = method resolution order

#mixin é uma implementação
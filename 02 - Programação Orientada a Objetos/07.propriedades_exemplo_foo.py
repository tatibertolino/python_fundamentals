# property() criar atributos gerenciados
# atributos gerenciados (propriedades) para modificar implementação interna sem mudar a API pública da classe

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property # pega um método e transforma em propriedade
    # permite acesso com sintaxe de variável
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value
        # errado: return self._x + value <- só atribui o valor e guarda. tem q trabalhar como se fosse atributo. não confundir pq tem sintaxe igual a método

    @x.deleter
    def x(self):
#        self._x = -1 # difícil usar mas quando vc não quer deletar direto na propriedades:
        # del self._x 
        self._x = 0 # ao invés de deletar, atribui zero e deixa lá

foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)



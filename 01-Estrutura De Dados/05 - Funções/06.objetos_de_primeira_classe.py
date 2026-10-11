# tudo no python é objeto. Funções tb são.
# objeto de primeira classe possuem os mesmo "direito" que tipos básicos
# podem ser atribuídos a variáveis, armazenados em estruturas de dados,
# ser argumento em outra função, ser retornado como resultado de outra função

# função inicial, diz o q tem q fazer no return
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def test(a, b):
    return a*2 + b*3

# segunda função, recebe 3 parâmetros: os dois da primeira e a própria função
def exibir_resultado(a, b, funcao):
    # a variável resultado chama a segunda função, que ativa a primeira
    resultado = funcao(a, b)
    print(f"O resultado da operação é {resultado}")

# assim dá pra manter a mesma função secundária, só mudando os argumentos dela

exibir_resultado(10, 10, somar)  # O resultado da operação é 20
exibir_resultado(10, 10, subtrair)  # O resultado da operação é 0
exibir_resultado(10, 10, test)  # O resultado da operação é 50
def dividir(c, d):
    return c / d

def faz_conta(c, d, conta):
    resultado2 = int(conta(c, d))
    print(f"a conta {c} dividido por {d} dá {resultado2}")

faz_conta(100, 5, dividir)

# para diminuir tudo, mas fica só o resultado
op = somar

print(op(1,23))

op2 = faz_conta

print(op2(200,25, dividir)) # printa coisa a mais =/
print(op2(200,25)) # não funciona sem o terceiro argumento
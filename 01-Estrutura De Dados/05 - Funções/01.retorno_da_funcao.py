# palavra reservada é return
# por padrão devolve None, se não tem valor pra retornar

def calcular_total(numeros):
    return sum(numeros)

# pode retornar mais de um valor
# retorna em forma de tupla

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

# não tem argumento, vai retornar none
def func_3():
    print("hello world")

# é a mesma coisa que 
def func_4():
    return None

print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)
print(func_3())
print(func_4())
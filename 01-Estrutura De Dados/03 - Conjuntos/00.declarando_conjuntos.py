# é uma coleção com elementos únicos, sem repetição
# serve pra eliminar elementos duplicados

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

# é mais raro, mas pode ter essa sintaxe

linguagens = {"python", "java", "python"}
print(linguagens)
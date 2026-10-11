# as listas conseguem armazenar outras listas: lista aninhada
# usado para representação de matriz

matriz = [
    [1, "a", 2], # lembrar da vírgula separando os elementos da lista principal
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0]) # [1, "a", 2]
print(matriz[0][0]) # 1 -> usa 2 índices para um elemento
print(matriz[0][-1]) # 2
print(matriz[-1][-1]) # "C"


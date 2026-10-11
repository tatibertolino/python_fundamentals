# prima da lista, é uma estrutura imutável. não pode ser alterada após a criação.
# não dá pra trocar valores declarando de novo.
# ao contrário de listas, os valores são entre parênteses ou nomeado por "tuple"
# para que o python não confunda tupla com precedência, boas práticas diz para terminar em , 

frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)
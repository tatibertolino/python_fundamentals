# cjtos em python não aceitam indexação. Tem q transformar em lista primeiro

numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])
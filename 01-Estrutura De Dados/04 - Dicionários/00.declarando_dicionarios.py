# conjunto não ordenado de par chave/valor
# a chave tem que ser objeto imutável
# a chave recupera o valor "chave": "valor"


pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"} <- coloca novas chaves, ele adiciona
print(pessoa)

pessoa["nome"] = "Maria" #se atribuir novo valor à chave, ele sobrescreve
print(pessoa)
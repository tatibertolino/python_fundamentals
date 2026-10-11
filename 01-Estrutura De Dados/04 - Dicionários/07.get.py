# segunda forma de acessar os dados

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

# usa o get pra saber se a chave existe

resultado = contatos.get("chave")  # None
print(resultado)

# pede pra retornar um dicionário vazio caso não encontre

resultado = contatos.get("chave", {})  # {}
print(resultado)

# aqui ele encontrou, então retorna o que está no dicionário

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)
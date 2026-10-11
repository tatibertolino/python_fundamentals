# retira valores, um a um. no caso de dicionários, deleta o valor todo dele

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

# pode dar valor padrão de resposta, caso não tenha nada pra dar pop - pode ser símbolo, string, etc

resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)
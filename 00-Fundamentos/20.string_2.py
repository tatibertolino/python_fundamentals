nome = "Tatiana"
idade = 47
profissão = "bióloga"
linguagem = "python"
saldo = 45.435

dados = {"nome": "Tatiana", "idade": 47}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1}".format(idade, nome)) #dá pra chamar várias vezes

print("Nome: {nome} Idade: {idade}".format(idade=idade, nome=nome))
print("Nome: {name} Idade: {age} {name} {name}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")
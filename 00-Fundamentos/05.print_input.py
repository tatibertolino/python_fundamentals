nome = input('Informe seu nome: ')
idade = input('Informe a sua idade: ')

print(nome, idade)
print(nome, idade, end="... \n")
print(nome, idade, sep="#")

#por padrão, o final sempre é \n (por isso q precisa colocar no end)
#por padrão o sep sempre é espaço

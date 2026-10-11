# se tem uma função e passa a lista, se alguém mudar na cópia, muda na original
# usa a copy para fazer mais uma instância, aí não muda

lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

print(id(l2), id(lista))

l2[0] = 2

print(lista)
print(l2)

#copy garante cópia com mesmos valores, mas não modifica a original
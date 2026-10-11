# para acrescentar novo elementos, ao contrário do append (de 1 em 1), usa extend
# junta novas listas
# ele não elimina elementos duplicados

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

linguagens.extend(["c", "java"])

print(linguagens)
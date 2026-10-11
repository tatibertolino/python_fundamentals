# ordena a lista, alfabeticamente, é a padrão

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)



linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

# ordena espalhada, de trás pra frente - reverse

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"]
print(linguagens)

# ordena por tamanho das palavras - len(x) <-- onde o x é cada um dos elementos da lista

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"]
print(linguagens)

# além de ordenar por tamanho, reverte a ordem - len + reverse
# quando tem mais de um elemento com mesmo tamanho, ele ordena por quem aparece primeiro, por isso python em posições diferentes
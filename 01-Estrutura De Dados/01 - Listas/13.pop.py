# lista já vem com sistema de pilha. Sempre pega o "prato" que tá em cima.
# sempre python vai colocar de o primeiro elemento "embaixo"
# pra tirar, ele pega o último elemento adicionado
# se dar pop, ele sempre tira o último elemento
# se der o índice, ele tira o correspondente

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python
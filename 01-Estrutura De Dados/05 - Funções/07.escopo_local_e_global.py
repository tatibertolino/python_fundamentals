# dentro do bloco da função, o escopo é local
# ou seja, acabou a função, acabou a variável (deixa de ser imutável)
# se colocar global, avisa pro interpretador q a variável não é local
# para usar variável q não está sendo declarada localmente, mas está no global
# NÃO é uma boa prática. Zoa debug e manutenção

salario = 2000 # <- fora da função, está na raíz do programa


def salario_bonus(bonus, lista):
    global salario # <- indica q a variável está fora da função
    
    lista_aux = lista.copy() # <- se não fizer cópia, e usar a lista de fora, ele vai herdar lá fora
    lista_aux.append(2) # modifica apenas localmente.
    print(f"lista aux = {lista_aux}")

    salario += bonus
    return salario


lista = [1] # a lista de fora continua intacta
salario_com_bonus = salario_bonus(500, lista)  # 2500
print(salario_com_bonus)
print(lista)

# em resumo: quem tá fora não entra, mas quem tá dentro vaza
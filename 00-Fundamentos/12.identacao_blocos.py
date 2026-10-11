def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


sacar(1000)
sacar(100)

"""def depositar(valor):
saldo = 500  #se deixar assim, dá erro
saldo += valor"""

def depositar(valor):
    saldo = 500  
    saldo += valor
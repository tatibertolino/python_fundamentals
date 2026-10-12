# encapsulamento impôe restrições ao acesso direto a variáveis e métodos
# ajuda a evitar alterações acidentais, só altera variável por método desse objeto
# dá pra fazer métodos diferentes pra coisas diferentes

# usa um _ pra definir atributo privado

# público: pode ser acessado de fora da classe
# dá pra mudar a variável no meio do programa
# _privado: só pode ser acessado pela classe
# o programador acessa o valor, e pode reatribuir valor
# não pode ser acessado ou lido
# métodos não podem ser chamados fora da classe

# o _variável e _método não garante a proteção do recurso

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia


    def depositar(self, valor):
        # ... <- códigos que garantem que as regras foram implementadas vão aqui
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo
    

conta = Conta("0001", 100)
# conta._saldo += 100 - não deve ser feito pq reatribui diretamente valor, dribla encapsulamento
conta.depositar(100)
# print(conta._saldo) não faz
print(conta.nro_agencia) #só o atributo, não tem ()
print(conta.mostrar_saldo()) # método, precisa do ()

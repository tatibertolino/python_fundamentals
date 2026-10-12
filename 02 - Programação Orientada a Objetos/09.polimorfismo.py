# mesmo nome de função (assinaturas diferentes) usado para tipos diferentes

# se passa número, é um comportamento, se é string é outro

len("python") # conta o número de caracteres da variável tipo string
len([10, 20, 30]) # conta o número de elementos da variável tipo lista

# na herança, classe filha herda métodos da classe pai
# pode moficiar um método herdado
# útil quando o método da classe pai não encaixa perfeitamente na classe filha

class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        print("Pardal pode voar")
    
class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")

def plano_voo(obj):
    obj.voar() #todo objeto daqui é filho de pássaro, então tem q ter o método voar

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
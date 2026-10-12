class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self._ano_nascimento = ano_nascimento

    # @property
    # def nome(self):
    #     return self._nome
    # não precisa pq o nome pode ser alterado direto na classe

    def nome(self):
        return self.nome

    @property
    def idade(self):
        _ano_atual = 2026
        return _ano_atual - self._ano_nascimento

    # @nome.setter
    # def nome(self, value):
    #     #lógica para modificar o nome
    #     pass

    # def get_nome(self):
    #     return self._nome

    # def get_idade(self):
    #     return 2026 - self._ano_nascimento 
    # funciona mas é de outras linguagens, fica comprido demais

pessoa = Pessoa("Tatiana", 1978)
print(f'Nome: {pessoa.nome} \tIdade: {pessoa.idade}')
# print(f'Nome: {pessoa.get_nome()} \tIdade: {pessoa.get_idade()}') 

# \t insere tabulação
# \n insere nova linha
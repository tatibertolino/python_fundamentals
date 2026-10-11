# def função(posição_1, pos2, /, pos_or_Keyword, *, kwd1, kwd2):
#           *positional only*   *pos or keyword*  *keyword only*
# quando aparece a /, muda pra escolha, nomeado ou posicional
# Quando aparece o *, obriga a ser nomeado

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina") #vai funcionar pq tem escolha
# não vai funcionar pq nomeou os posicionais (antes da /)
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
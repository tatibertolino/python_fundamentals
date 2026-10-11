# pode passar usando o conjunto chave/valor

def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# argumentos posicionados: parece vantajoso, mas tem q saber a ordem das chaves, continua funcionando se alguém muda as chaves
salvar_carro("Fiat", "Palio", 1999, "ABC-1234") 
# argumentos nomeados: diminui a chance de ter argumentos trocados, mas para de funcionar se mexer nas chaves
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
# os ** significa que vc vai passar um dicionário {}
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
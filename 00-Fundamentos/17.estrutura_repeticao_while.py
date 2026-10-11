opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n:"))

    if opcao == 1:
        print("sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
else: #de novo, não é muito usado, mas para saber q existe
    print("Obrigado por usar nossos serviços!")


opcao = ""

while opcao != "2":
    print("1. Mostrar saudação")
    print("2. Sair do programa")

    opcao = int(input("Escolha uma opçcão:"))
    if opcao == 1:
        print("Ola seja muito bem vindo(a)!")
    elif opcao == 2:
        print("Saindo do programa...Até logo!")
    else:
        print("Opção invalida! Tente novamente.")
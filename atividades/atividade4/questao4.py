saldo_atual = float(input("Digite o saldo atual: "))
valor_saque = int(input("Digite o valor do saque:"))

if saldo_atual <= valor_saque:
    saldo_total = saldo_atual - valor_saque
    print("Saque realizado com sucesso! saldo atual R$:")
else:
    print("Saldo insuficiente para realizar esta operação.")
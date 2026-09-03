valor = float(input("Digite o valor da comanda R$: "))
pessoas = int(input("Digite a quantidade de pessoas: "))

total = valor / pessoas

print(f"O valor total foi de R$ {valor:.2f}, e cada pessoa deve pagar R$ {total:.2f}.")
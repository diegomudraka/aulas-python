soma = 0

numero = int(input("Digite um numero inteiro (0 para sair: "))
while numero != 0:
    soma += numero
    numero = int(input("Digite outro numero inteiro (0 para sair: "))
print(f"A soma dos numeros digitados é: {soma}")
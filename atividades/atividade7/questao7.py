funcionarios = []

print("Cadastro de funcionarios:(Digite'sair' para encerrar) ")
while True:
    nome = input("Digite o nome do funcionario:(ou 'sair' para encerrar) ")
    if nome.lower () == 'sair':
        break
    funcionarios.append(nome)

print("\nLista de funcionarios cadastrados:")
for i in range(len(funcionarios)):
    print(f"{i} - {funcionarios [i]}")

indices_aumento = [0, 2]
indices_demissão = [1, 3]

aumento = []
demitidos = []

for i in range (len(funcionarios)):
    if i in indices_aumento:
        aumento.append(funcionarios [i])
    elif i in indices_demissão:
        demitidos.append(funcionarios[i])

print("\nFuncionarios que recebrao aumento: ")
for nome in aumento:
    print(f" - {nome}")
print("n\Funcionarios que serao demitidos: ")
for nome in demitidos:
    print(f" - {nome}")


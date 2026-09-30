usuario = input('Digite o nome de usuario: ')
carrinho = []
total = 0

while True:
    produto = input(f"Digite o nome do produto(ou 'fim' para finalizar): ")
    if produto.lower() == "fim":
        break

    preco = float(input(f"Digite o valor do '{produto}': R$ "))
    total += preco


    carrinho.append((produto, preco))

with open("mercadinho.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(f"Usuário: {usuario}\n")
    arquivo.write("-" * 30 + "\n")
    arquivo.write("PRODUTOS COMPRADOS:\n")

    for nome_produto, preco_produto in carrinho:
        arquivo.write(f"- {nome_produto}: R$ {preco_produto:.2f}\n")

    arquivo.write("-" * 30 + "\n")
    arquivo.write(f"TOTAL: R$ {total:.2f}\n")

print("\nCompra finalizada e salva em 'mercadinho.txt'!")







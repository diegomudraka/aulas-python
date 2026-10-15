import json

loja = {
    "nome": "TechStore",
    "produtos": [
        {"nome": "Teclado", "preco": 150.00, "quantidade": 25},
        {"nome": "Mouse", "preco": 80.00, "quantidade": 40},
        {"nome": "Monitor", "preco": 900.00, "quantidade": 10},
    ],
}

with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(loja, arquivo, indent=4, ensure_ascii=False)

print("Arquivo estoque.json criado com sucesso!\n")

with open("estoque.json", "r", encoding="utf-8") as arquivo:
    dados_lidos = json.load(arquivo)

print(f"Produtos da loja {dados_lidos['nome']}:")
for produto in dados_lidos["produtos"]:
    print(f"O produto {produto['nome']} custa R$ {produto['preco']:.2f}")

novo_produto = {"nome": "Headset", "preco": 250.00, "quantidade": 15}
dados_lidos["produtos"].append(novo_produto)

for produto in dados_lidos["produtos"]:
    if produto["nome"] == "Monitor":
        produto["preco"] = round(produto["preco"] * 0.90, 2)
        print(f"\nDesconto de 10% aplicado no {produto['nome']}! "f"Novo preço: R$ {produto['preco']:.2f}")

with open("estoque.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_lidos, arquivo, indent=4, ensure_ascii=False)

print("\nEstoque atualizado e salvo com sucesso!")

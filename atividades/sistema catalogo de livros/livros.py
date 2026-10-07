import json

dicionario_txt = "biblioteca.txt"

catalogo_livros = []

with open(dicionario_txt, "r", encoding="utf-8") as arquivo_txt:
    for linha in arquivo_txt:
        linha_limpa = linha.strip()
        if not linha_limpa:
            continue
        dados = linha_limpa.split(";")

    livro = {
        "id": int(dados[0]),
        "nome": dados[1],
        "descricao": dados[2],
        "preco": dados[3],
        "em estoque": dados[4],
    }

    catalogo_livros.append(livro)
print(f"Etapa 1 concluida: {len(catalogo_livros)} livros lidos do arquivo TXT.")

dicionario_json = "biblioteca.json"
with open(dicionario_json, "w", encoding = "utf-8") as arquivo_json:
    json.dump(catalogo_livros, arquivo_json, indent=4, ensure_ascii=False)
print("Etapa 2 Concluida: Arquivo 'catalogo.json' criado com sucesso")

novo_catalogo = [
    {
        "id": 31,
        "nome": "O Silmarilion",
        "descricao": "Mitos e lendas da criação da Terra Media",
        "preco": 69.90,
        "em estoque": 12,
    },
    {
        "id": 32,
        "nome": "Fundação",
        "descrição": "Classico da ficção cientifica de Issac Asimov",
        "preco": 49.90,
        "em estoque": 8,
    },
    {
        "id": 33,
        "nome": "O Sol é para todos",
        "descrição": "Romance sobre igualdade e intuição moral",
        "preco": 41.50,
        "em estoque": 14,
    },
    {
        "id": 34,
        "nome": "Frankstein",
        "descrição": "Classico do terror e ficção cientifica",
        "preco": 45.90,
        "em estoque": 12,
    },
    {
        "id": 35,
        "nome": "O Apfabeiro de Auschwitz",
        "descrição": "Historia real sobre amor e sobreviviencia",
        "preco": 45.90,
        "em estoque": 6,
    },


]

catalogo_livros.extend(novo_catalogo)

with open(dicionario_json, "w", encoding = "utf-8") as arquivo_json:
    json.dump(catalogo_livros, arquivo_json, indent=4, ensure_ascii=False)

    print(f"Etapa 3 Concluida: Arquivo 'catalogo.json' criado com sucesso")

print("\n" + "=" * 50)
print("RELATORIO DE ESTOQUE")
print("=" * 50)

with open(dicionario_json, "r", encoding = "utf-8") as arquivo_json:
    novo_catalogo = json.load(arquivo_json)

print("\n--- Livros com menos de 15 unidades em estoque ---")
livros_baixo_estoque = []
for livro in novo_catalogo:
    if int(livro["em estoque"]) < 15:
        livros_baixo_estoque.append(livro)

print("\n--- Livros com menos de 15 unidades em estoque ---")
if livros_baixo_estoque:
    for livro in livros_baixo_estoque:
        print(f". {livro['nome']} (Estoque: {livro['em estoque']} un.)")
else:
    print("Nenhum livro com estoque baixo.")
valor_total_estoque = 0.0
for livro in livros_baixo_estoque:
    valor_total_estoque += livro["preco"] * livro["em estoque"]

print("\n--- Resumo Financeiro ---")
print(f"Valor Total do estoque: R$ {valor_total_estoque:.2f}")
print("=" * 50)





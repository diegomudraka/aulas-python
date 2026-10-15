import json

with open("base1.json", "r", encoding="utf-8") as arquivo:
    dados1 = json.load(arquivo)

with open("base2.json", "r", encoding="utf-8") as arquivo:
    dados2 = json.load(arquivo)

with open("base3.json", "r", encoding="utf-8") as arquivo:
    dados3 = json.load(arquivo)


lista_aniversariantes = []

for funcionario in dados1:
    lista_aniversariantes.append({
        "nome": funcionario["nome"],
        "aniversario": funcionario["aniversario"],
    })
for funcionario in dados2:
    lista_aniversariantes.append({
        "nome": funcionario["nome"],
        "aniversario": funcionario["aniversario"],
    })
for funcionario in dados3:
    lista_aniversariantes.append({
        "nome": funcionario["nome"],
        "aniversario": funcionario["aniversario"],
    })

lista_aniversariantes.sort(key=lambda pessoa: pessoa["nome"].lower())

with open("aniversariantes.json", "w", encoding="utf-8") as arquivo:
    json.dump(lista_aniversariantes, arquivo, indent=4, ensure_ascii=False)

print(f"Processamento concluido! {len(lista_aniversariantes)} registros processados com sucesso.")


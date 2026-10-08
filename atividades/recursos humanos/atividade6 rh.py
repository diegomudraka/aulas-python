import json

with open("base1.json", "r", encoding="utf-8") as json_file:
    dados1 = json.load(json_file)

with open("base2.json", "r", encoding="utf-8") as json_file:
    dados2 = json.load(json_file)

with open("base3.json", "r", encoding="utf-8") as json_file:
    dados3 = json.load(json_file)



    lista_aniversariantes  = []
    bases = [dados1, dados2, dados3]
    for base in bases:
        for funcionario in base:
            dados_filtrados = {
                "nome": funcionario["nome"],
                "aniversario": funcionario["aniversario"],

            }
        lista_aniversariantes.append(dados_filtrados)





import random
import pandas as pd

ARQ_FUNC = "funcionarios.csv"
ARQ_ALTOS = "cargos_altos.csv"

df = pd.read_csv(ARQ_FUNC, sep=";", encoding="utf-8-sig")
df[df["salario"] > 6000] . to_csv(ARQ_ALTOS, index=False, sep=";", encoding="utf-8-sig")

proximo_id = int(df["id"].max()) + 1
candidatos = [
    ("Renata Barbosa", 5200.00, "Analista Juridico"),
    ("Ricardo Alves", 8300.00, "Diretor de Tecnologia"),
    ("Juliana Costa", 9500.00, "Gerente Financeiro"),
    ("Paulo Mendes", 4300.00, "Arquiteto de Soluções"),
    ("Camila Rocha", 6700.00, "Scrum Master"),
]
cargos_existentes = set(df["cargo"])
novos = []
for nome, salario, cargo in candidatos:
    if cargo not in cargos_existentes:
        novos.append({"id": proximo_id, "nome": nome, "salario": salario, "cargo": cargo})
        cargos_existentes.add(cargo)
        proximo_id += 1
df = pd.concat([df, pd.DataFrame(novos)], ignore_index=True)

df = df.drop(index=[0, 1]). reset_index(drop=True)

random.seed(42)
df["tempo_empresa"] = [random.randint(3, 120) for _ in range(len(df))]
df["tempo_empresa"] = df["tempo_empresa"]. astype(int)

estagiario = {
    "id": int(df["id"].max()) + 1,
    "nome": "Lucas Ferreira",
    "salario": 1800.00,
    "cargo": "Estagiario",
    "tempo_empresa": 4,
}
df = pd.concat([df, pd.DataFrame([estagiario])], ignore_index=True)
df["tempo_empresa"] = df["tempo_empresa"]. astype(int)

df.to_csv(ARQ_FUNC, index=False, sep=";", encoding="utf-8-sig")
df[df["salario"] > 6000]. to_csv(ARQ_ALTOS, index=False, sep=";", encoding="utf-8-sig")

print("=== funcionarios.csv (releitura) ===")
check = pd.read_csv(ARQ_FUNC, sep=";", encoding="utf-8-sig")
print(check)
print("\nTipos:\n", check.dtypes)
print("\nIds 0 e 1 originais removidos? Primeiro índice agora:", check.iloc[0]["id"])
print("Estagiário presente:", (check["cargo"] == "Estagiário").any())

print("\n=== cargos_altos.csv (releitura) ===")
altos = pd.read_csv(ARQ_ALTOS, sep=";", encoding="utf-8-sig")
print(altos)
print("Todos com salário > 6000:", (altos["salario"] > 6000).all())
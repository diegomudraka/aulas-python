import pandas as pd

df = pd.read_csv("dados_despadronizados.csv", dtype=str, keep_default_na=False)

df["cpf"] = df["cpf"].str.replace(r"\D", "", regex=True)

df["cpf_formatado"] = (
    df["cpf"].str[0:3] + "." + df["cpf"].str[3:6] + "." +
    df["cpf"].str[6:9] + "-" + df["cpf"].str[9:11]
)

def cpf_valido(cpf):
    """11 digitos, não repetidos, e digitos verificadores corretos."""
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in (9, 10):
        soma = sum(int(cpf[j]) * (i + 1 - j) for j in range(1))
        digito = (soma * 10 % 11) % 10
        if digito != int(cpf[i]):
            return False
        return True

df["cpf_valido"] = df["cpf"].apply(cpf_valido)

df["numero"] = df["numero"].str.replace(r"\D", "", regex=True)
df["numero"] = df["numero"].str.replace(r"^55(?=\d{11}$)", "", regex=True)

df["numero_formatado"] = (
    "(" + df["numero"].str[0:2] + ") " +
    df["numero"].str[2:7] + "-" + df["numero"].str[7:11]
)

df["numero_valido"] = df["numero"].str.match(r"^[1-9][1-9]9\d{8}$")

df["salario"] = df["salario"].str.replace("R$", "", regex=False).str.replace(" ", "", regex=False)

tem_virgula = df["salario"].str.contains(",")
df.loc[tem_virgula, "salario"] = (
    df.loc[tem_virgula, "salario"]
    .str.replace(".", "", regex=False)
    .str.replace(",", ".", regex=False)
)
df["salario"] = df["salario"].astype(float)



df["salario_formatado"] = (
    "R$ " + df["salario"].map("{:,.2f}".format)
    .str.replace(",", "X", regex=False)
    .str.replace(".", ",", regex=False)
    .str.replace("X", ".", regex=False)
)
df["salario_anual"] = df["salario"] * 12

colunas = ["nome", "cpf", "cpf_formatado", "cpf_valido",
           "numero", "numero_formatado", "numero_valido",
           "salario", "salario_formatado", "salario_anual"]
df[colunas].to_csv("dados_padronizados.csv", index=False, encoding="utf-8")
print(df[colunas].to_string())



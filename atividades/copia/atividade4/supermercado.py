import pandas as pd

# 1. Carregamento dos dados
df = pd.read_csv("estoque_supermercado.csv")

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

HOJE = pd.Timestamp("2026-10-27")

# ------------------------------------------------------------ 2. LIMPEZAS
# --- preco: tira "R$" e espaços, vírgula -> ponto, vira float ("dez reais" -> NaN)
df["preco"] = (
    df["preco"].astype(str)
    .str.replace("R$", "", regex=False)
    .str.replace(" ", "", regex=False)
    .str.replace(",", ".", regex=False)
)
df["preco"] = pd.to_numeric(df["preco"], errors="coerce")
df["preco"] = df["preco"].fillna(df["preco"].mean())  # nulos -> média da base

# --- quantidade: textos ("vinte", "cem") -> NaN -> 0 -> int
df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce")
df["quantidade"] = df["quantidade"].fillna(0).astype(int)

# --- setor: sem espaços nas pontas, tudo minúsculo, vazio -> "sem setor"
df["setor"] = df["setor"].astype(str).str.strip().str.lower()
df["setor"] = df["setor"].replace(["", "nan"], pd.NA).fillna("sem setor")

# --- datas: máscara dia/mês/ano (vazio -> NaT)
df["data_compra"] = pd.to_datetime(df["data_compra"], format="%d/%m/%Y", errors="coerce")
df["data_vencimento"] = pd.to_datetime(df["data_vencimento"], format="%d/%m/%Y", errors="coerce")

# --- valor patrimonial de cada produto
df["valor_total_estoque"] = df["quantidade"] * df["preco"]

# ------------------------------------------------ 3. DATAFRAME LIMPO
print("\n--- BASE DE DADOS LIMPA ---")
print(df.head())
print()
print(df.dtypes)

# ------------------------------------------------ 4. ANÁLISES
# 1) Alerta de vencimento: 27/10/2026 a 03/11/2026
print("\n--- PRODUTOS VENCENDO ESTA SEMANA ---")
fim_semana = pd.Timestamp("2026-11-03")
vencendo = df[(df["data_vencimento"] >= HOJE) & (df["data_vencimento"] <= fim_semana)]
print(vencendo[["nome", "quantidade", "setor", "data_vencimento"]]
      .sort_values("data_vencimento").to_string(index=False))

# 2) Maior quantidade entre os que vencem esta semana
print("\n--- MAIOR QUANTIDADE A VENCER ---")
maior_qtd = vencendo[vencendo["quantidade"] == vencendo["quantidade"].max()]
print(maior_qtd[["nome", "quantidade", "data_vencimento"]].to_string(index=False))

# 3) Compras recentes: 24/10/2026 a 27/10/2026
print("\n--- COMPRAS DOS ÚLTIMOS 3 DIAS ---")
recentes = df[(df["data_compra"] >= pd.Timestamp("2026-10-24")) & (df["data_compra"] <= HOJE)]
print(recentes[["nome", "quantidade", "data_compra"]].to_string(index=False))

# 4) Produtos sem data de vencimento (conferência física)
print("\n--- PRODUTOS SEM DATA DE VENCIMENTO ---")
print(df[df["data_vencimento"].isna()][["nome", "setor", "data_compra"]].to_string(index=False))

# 5) Setor com maior valor financeiro parado
print("\n--- MAIOR VALOR PATRIMONIAL POR SETOR ---")
por_setor = df.groupby("setor")["valor_total_estoque"].sum().sort_values(ascending=False)
print(por_setor.round(2))
print(f"\nSetor com maior valor parado: {por_setor.idxmax()} (R$ {por_setor.max():,.2f})")

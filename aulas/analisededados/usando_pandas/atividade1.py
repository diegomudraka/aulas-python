import pandas as pd

print("Filtrando dados!")

df = pd.read_csv("funcionarios.csv", sep=";")


filtro_salarios = df[(df["salario"] < 3000) | (df['salario'] > 5000)| (df['salario']== 3100)]



cargos = ['Analista de Dados', 'Analista de Sistemas', 'Desenvolvedor Java','Cientista de Dados']
filtro_cargos = df[df['cargo'].isin (cargos)]
print(filtro_cargos)

filtro_nome_cargo = df.loc[df['salario']> 6000, ["nome", "cargo"]]


filtro_id_par = df[df['id']% 2 == 0]

divisor = "=" * 60

print(divisor)
print("1) Salarios < 3000, > 5000 ou == 3100")
print(divisor)
print(filtro_salarios.to_string(index=False))

print("\n" + divisor)
print("2) Cargos: Analista de Dados, Analista de Sistemas,\n Desenvolvedor Java e Cientista de Dados")
print(divisor)
print(filtro_cargos.to_string(index=False))

print("\n" + divisor)
print("3) Nome e cargo de quem tem salario > 6000")
print(divisor)
print(filtro_nome_cargo.to_string(index=False))

print("\n" + divisor)
print("4) Funcionarios com id par")
print(divisor)
print(filtro_id_par.to_string(index=False))














import pandas as pd

df = pd.read_csv("funcionarios.csv", sep=";")
print("BASE DE DADOS")
print(df.columns.tolist())

filtroSalario = df[
    (df['salario'] < 3000) |
    (df['salario'] > 5000) |
    (df['salario'] == 3100)
]

print("\nFILTRO POR SALARIOS")
print(filtroSalario)


filtroCargo = df[
    (df['cargo'] == "Analista de Dados") |
    (df['cargo'] == "Analista de Sistemas") |
    (df['cargo'] == "Desenvolvedor Java") |
    (df['cargo'] == "Cientista de Dados") 
]

print("\nFILTRO POR CARGOS")
print(filtroCargo)

filtroSalarioCargo = df[
    (df['salario'] < 6000)
]

print("FILTRO POR CARGOS E SALARIO")
print(filtroSalarioCargo[
    ['nome', 'cargo']
])

filtroID = df[
    (df['id'] % 2 == 0)
]

print("FILTRO POR ID")
print(filtroID)

filtroSalarioCargo.to_csv("filtro_salario_cargo.csv", index=False, encoding='utf-8', sep='|')
arquivoFiltrado = pd.read_csv("filtro_salario_cargo.csv", sep="|")
print(arquivoFiltrado)
import pandas as pd

df = pd.read_csv('funcionarios.csv', sep=';')
filtroSalarioAlto = df[
    (df['salario']> 6000)
]

filtroSalarioAlto.to_csv("cargos_altos.csv", index=False, encoding='utf-8', sep="|")
print(filtroSalarioAlto)

novo_funcionario = [{
    "id": 100,
    "nome": "Fulano da Silva",
    "salario": 10000,
    "cargo": "cargoTeste"
},
{
    "id": 101,
    "nome": "Bla bla bla",
    "salario": 9000,
    "cargo": "cargoTeste"
}
]
dfFuncionarioNovo = pd.DataFrame(novo_funcionario)
dfFiltrado = pd.concat([filtroSalarioAlto, dfFuncionarioNovo], ignore_index=True)

dfFiltrado['tempo_empresa'] = [12, 4, 2, 8, 12, 3, 10]
print(dfFiltrado)


dfFiltrado['tempo_empresa'] = [12, 1, 2, 6, 12, 9, 999]
print(dfFiltrado)

dfFiltrado = dfFiltrado.drop(index=0)
dfFiltrado = dfFiltrado.drop(index=1)

novoFuncionario = [{
    "id": 200,
    "nome": "Estagiario de Souza",
    "salario": 1500,
    "cargo": "Estagiário",
    "tempo_empresa": 3
}]

dfNovoFuncionario = pd.DataFrame(novo_funcionario)
dfFiltrado = pd.concat([dfFiltrado, dfNovoFuncionario], ignore_index=True)
print(dfFiltrado)


dfFiltrado.to_csv("cargos_altos.csv", index=False, sep=";")
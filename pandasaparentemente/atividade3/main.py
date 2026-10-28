import pandas as pd

dadosDespadronizados = pd.read_csv("dados_despadronizados.csv", 
                                    dtype={"cpf" : str, 
                                        "salario": "string", 
                                        "telefone" : "string"})

dadosDespadronizados.insert(2, "cpf_formatado", dadosDespadronizados["cpf"].str.replace(r"\D", "", regex=True))
dadosDespadronizados.insert(3, "cpf_validado", dadosDespadronizados["cpf_formatado"].str.fullmatch(r"\d{11}"))

salarioFormatado = (dadosDespadronizados["salario"]
                                        .str.replace(r"[^\d,.\-]", "", regex=True)
                                        .str.replace(r"\.(?=\d{3}(?:\.|,|$))", "", regex=True)
                                        .str.replace(r",",".", regex=False))
salarioFormatado = pd.to_numeric(salarioFormatado, errors="coerce")

dadosDespadronizados.insert(5,"salario_formatado",salarioFormatado)


numeroFormatado = (dadosDespadronizados["numero"].str.replace(r"\D", "", regex=True))

dadosDespadronizados.insert(7, "numero_formatado", numeroFormatado)

dadosDespadronizados["numero_validado"] = (dadosDespadronizados['numero_formatado'].str.fullmatch(r"\d{10,13}"))

print(dadosDespadronizados)

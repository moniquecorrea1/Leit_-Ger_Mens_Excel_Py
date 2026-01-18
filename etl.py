import pandas as pd

# EXTRAÇÃO


arquivo_entrada = "base_etl_clientes.xlsx"
df = pd.read_excel(arquivo_entrada, sheet_name="Base_Dados")


# TRANSFORMAÇÃO

def gerar_mensagem(row):
    return (
        f"Olá {row['Nome']}, identificamos movimentações na conta "
        f"{row['Conta']}. Caso não reconheça, entre em contato com o banco."
    )

df["Mensagem"] = df.apply(gerar_mensagem, axis=1)


# CARGA

arquivo_saida = "mensagens_clientes.xlsx"
df.to_excel(arquivo_saida, index=False)

print("ETL finalizado com sucesso!")
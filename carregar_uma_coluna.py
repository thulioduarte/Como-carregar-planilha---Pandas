# Carrega apenas a coluna 'NomeDaColuna' da aba específica
df_coluna = pd.read_excel('arquivo.xlsx', sheet_name='NomeDaAba', usecols=['NomeDaColuna'])

# Exibe as primeiras linhas do DataFrame
print(df_coluna.head())

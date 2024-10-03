# Carrega as colunas 'Coluna1' e 'Coluna2' da aba específica
df_varias_colunas = pd.read_excel('arquivo.xlsx', sheet_name='NomeDaAba', usecols=['Coluna1', 'Coluna2'])

# Exibe as primeiras linhas do DataFrame
print(df_varias_colunas.head())

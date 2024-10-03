# Carrega uma aba específica, selecionando colunas e pulando linhas
df = pd.read_excel('caminho/para/seu_arquivo.xlsx', sheet_name='NomeDaAba', usecols='A:C', skiprows=2)

# Exibe as primeiras linhas
print(df.head())

# Carrega várias colunas de várias abas
abas_varias_colunas = pd.read_excel('arquivo.xlsx', sheet_name=['Aba1', 'Aba2'], usecols=['Coluna1', 'Coluna2'])

# Exibe as primeiras linhas de cada aba carregada
for nome_aba, df_aba in abas_varias_colunas.items():
    print(f'Aba: {nome_aba}')
    print(df_aba.head())

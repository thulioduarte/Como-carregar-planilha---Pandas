# Carrega várias abas
abas = pd.read_excel('arquivo.xlsx', sheet_name=['Aba1', 'Aba2'])

# Exibe as primeiras linhas de cada aba carregada
for nome_aba, df_aba in abas.items():
    print(f'Aba: {nome_aba}')
    print(df_aba.head())

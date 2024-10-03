import pandas as pd

# Carregando as planilhas
vendas_2023 = pd.read_excel('vendas_2023.xlsx')
vendas_2024 = pd.read_excel('vendas_2024.xlsx')

# Calculando a diferença de vendas
diferenca_vendas = total_vendas_2024 - total_vendas_2023

# Adicionando essa diferença ao DataFrame de 2024 para visualização
vendas_2024['Diferença em relação a 2023'] = diferenca_vendas

# Mostrando o resultado
print("\nComparação de Vendas:")
print(vendas_2024[['Total de Vendas', 'Diferença em relação a 2023']])

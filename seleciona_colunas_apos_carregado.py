import pandas as pd

# Carregando as planilhas
vendas_2023 = pd.read_excel('vendas_2023.xlsx')
vendas_2024 = pd.read_excel('vendas_2024.xlsx')

# Selecionando a coluna "Total de Vendas"
total_vendas_2023 = vendas_2023['Total de Vendas']
total_vendas_2024 = vendas_2024['Total de Vendas']

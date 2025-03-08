import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Exemplo de dados financeiros
data = {
    'Ano': [2021, 2022, 2023],
    'Receitas': [100000, 120000, 130000],
    'Despesas': [60000, 70000, 80000]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Calcular fluxo de caixa
df['Fluxo de Caixa'] = df['Receitas'] - df['Despesas']

# Calcular indicadores financeiros
df['Margem Bruta'] = df['Receitas'] / df['Despesas']
df['Retorno sobre Investimento (ROI)'] = df['Fluxo de Caixa'] / df['Despesas']

# Plotar gráficos
plt.figure(figsize=(12, 6))

# Gráfico de barras das Receitas e Despesas
plt.subplot(1, 2, 1)
sns.barplot(x='Ano', y='value', hue='variable', data=pd.melt(df, ['Ano'], value_vars=['Receitas', 'Despesas']))
plt.title('Receitas e Despesas por Ano')
plt.xlabel('Ano')
plt.ylabel('Valor')

# Gráfico de linha do Fluxo de Caixa
plt.subplot(1, 2, 2)
sns.lineplot(x='Ano', y='Fluxo de Caixa', data=df, marker='o')
plt.title('Fluxo de Caixa por Ano')
plt.xlabel('Ano')
plt.ylabel('Fluxo de Caixa')

plt.tight_layout()
plt.show()

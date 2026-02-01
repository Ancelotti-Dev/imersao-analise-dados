import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
print(df.head(10)) #Para mostrar os 10 primeiros dados
print(df.info()) #Para obter infomações de cada categoria, quais saõ floats, quais estão nulos
print(df.describe()) #Para ver as estatisticas 
print(df.shape)

linhas = df.shape[0]

colunas =  df.shape[1]

# print(f"colunas: {colunas} ,linhas: {linhas}")

# print(df.columns) # Para mostrar as colunas que exitem no Dataframe

df.rename(columns={ # PAra traduzir as colunas
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'tipo_contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda_original',
    'salary_in_usd': 'salario_usd',
    'employee_residence': 'residencia_funcionario',
    'remote_ratio': 'remoto',
    'company_location': 'localizacao_empresa',
    'company_size': 'tamanho_empresa'
}, inplace=True)

# print(df.columns)

# print(df['senioridade'].value_counts())

# print(df['remoto'].value_counts(0))

#print(df['cargo'].unique)

# Criando o dicionário de tradução
traducao_senioridade = {
    'EN': 'Júnior',
    'MI': 'Pleno',
    'SE': 'Sênior',
    'EX': 'Executivo'
}

# Aplicando na coluna (ajuste o nome da coluna se for diferente de 'serionidade')
df['senioridade'] = df['senioridade'].map(traducao_senioridade)

# print(df.head())
# print(df.describe(include="object"))

print(df.isnull())
print(df["ano"].unique())

df_salarios = pd.DataFrame ({
    "nome": ["Pedro","Athur","Marcela","Nayane","Luan"],
    "salarios": [4432, np.nan, 2534, np.nan, 12344]
})
#Calcula Media Salarial e substitui oos valores null pela media e arredonda os avalores
df_salarios['salarios_media'] = df_salarios['salarios'].fillna(df_salarios['salarios'].mean().round(2))

df_salarios['salarios_mediana'] = df_salarios['salarios'].fillna(df_salarios['salarios'].median())

print(df_salarios)

df_limpo = df.dropna()
df_limpo = df_limpo.assign(ano = df_limpo["ano"].astype('Int64'))

print(df_limpo.head())

print(df_limpo['senioridade'].value_counts().plot(kind='bar', title="Distribução da senioridade"))
plt.show()

# sns.barplot(data=df_limpo,x='senioridade', y='salario_usd')
# plt.show()

plt.figure(figsize=(9,7))
sns.barplot(data=df_limpo,x='senioridade', y='salario_usd')
plt.title("Salario medio por nivel de senirioridade")
plt.xlabel("Nivel de senioridade")
plt.ylabel("Salario Médio USD Anual")
plt.show()

print(df_limpo.groupby('senioridade')['salario_usd'].mean().sort_values(ascending=False))

ordem = df_limpo.groupby('senioridade')['salario_usd'].mean().sort_values(ascending=False).index #PARA CONTER A ORDEM USAMOS INDEX

print(ordem)

plt.figure(figsize=(9,7))
sns.barplot(data=df_limpo,x='senioridade', y='salario_usd',order=ordem)
plt.title("Salario medio por nivel de senirioridade")
plt.xlabel("Nivel de senioridade")
plt.ylabel("Salario Médio USD Anual")
plt.show()



plt.figure(figsize=(11,9))
sns.histplot(df_limpo['salario_usd'], bins=50, kde=True)
plt.title("Salario medio por senirioridade")
plt.xlabel("frequencia desses valores")
plt.ylabel("Salario Médio USD Anual")
plt.show()

plt.figure(figsize=(8,5))
sns.boxenplot(x=df_limpo['salario_usd'])
plt.title("Salario medio por senirioridade")
plt.xlabel("Box Plot do salario em USD")
plt.show()


senioridade_media_salarial = df_limpo.groupby('senioridade')['salario_usd'].mean().sort_values(ascending=False).reset_index()

# fig = px.bar(senioridade_media_salarial,
#             x='senioridade',
#             y='salario_usd',
#             title="Media Salarial por Senioridade",
#             labels={"senioridade": 'Nivel de Senioridade', 'salario_usd': 'Salario USD Anual'})
# fig.show()


remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho','quantidade']

fig = px.pie(remoto_contagem,
            names = 'tipo_trabalho',
            values='quantidade', 
            title="Proporção do tipos de trabalho",
            hole=0.5)
fig.update_traces(textinfo='percent+label')
fig.show()








# DIA 1: Palavra secreta PANDAS
# DIA 2: Palavra secreta PRINT
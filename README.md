# 📊 Dashboard de Análise de Salários na Área de Dados

## 🎯 Sobre o Projeto

Este é um projeto educacional desenvolvido durante a **Imersão em Dados da EBAC** que analisa e visualiza dados salariais de profissionais na área de tecnologia e ciência de dados.

O projeto foi deployado e está disponível em: **[https://dados-ancelotti.streamlit.app](https://dados-ancelotti.streamlit.app)**

---

## 📚 O que foi Aprendido

Durante o desenvolvimento deste projeto, foram estudados e aplicados os seguintes conceitos:

### Data Science & Python
- ✅ **Pandas**: Manipulação, limpeza e transformação de dados
- ✅ **NumPy**: Operações numéricas e tratamento de valores ausentes
- ✅ **Estatística Descritiva**: Média, mediana, distribuição de dados

### Visualização de Dados
- ✅ **Matplotlib**: Gráficos estáticos (histogramas, box plots, gráficos de barras)
- ✅ **Seaborn**: Visualizações estatísticas avançadas
- ✅ **Plotly**: Gráficos interativos e mapas coropletos

### Web Development
- ✅ **Streamlit**: Criação de dashboards interativos sem necessidade de HTML/CSS/JavaScript
- ✅ **Deployment**: Publicação da aplicação na plataforma Streamlit Cloud

### Processamento de Dados
- ✅ Tratamento de valores nulos (fillna, dropna)
- ✅ Renomeação de colunas e tradução de dados
- ✅ Mapeamento de valores (dicionários de tradução)
- ✅ Filtros interativos
- ✅ Agregação e agrupamento de dados (groupby)

---

## 🚀 Como Usar

### Pré-requisitos
- Python 3.8+
- pip

### Instalação Local

1. Clone ou baixe este repositório

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o aplicativo Streamlit:
```bash
streamlit run app.py
```

4. A aplicação será aberta automaticamente no seu navegador em `http://localhost:8501`

---

## 📁 Estrutura do Projeto

```
imersão_dados/
├── app.py              # Dashboard Streamlit (Aplicação Principal)
├── dados.py            # Exploração e processamento de dados
├── requirements.txt    # Dependências do projeto
└── README.md          # Este arquivo
```

### Arquivos Principais

#### `app.py`
Dashboard interativo com:
- 🔍 **Filtros avançados** (Ano, Senioridade, Tipo de Contrato, Tamanho da Empresa)
- 📈 **KPIs principais** (Salário médio, máximo, total de registros, cargo mais frequente)
- 📊 **Gráficos interativos**:
  - Top 10 cargos por salário médio
  - Distribuição de salários
  - Proporção de tipos de trabalho (remoto/presencial/híbrido)
  - Mapa com salários por país

#### `dados.py`
Script exploratório com:
- Carregamento e limpeza de dados
- Análise exploratória (head, info, describe)
- Tradução de colunas
- Tratamento de valores ausentes
- Visualizações estáticas

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Propósito |
|-----------|--------|----------|
| **Pandas** | 2.2.3 | Manipulação de dados |
| **Streamlit** | 1.44.1 | Dashboard web interativo |
| **Plotly** | 5.24.1 | Gráficos interativos |
| **Matplotlib** | - | Visualizações estáticas |
| **Seaborn** | - | Gráficos estatísticos |
| **NumPy** | - | Operações numéricas |

---

## 📊 Funcionalidades do Dashboard

### Filtros Interativos
- Filtrar por **Ano** (2020-2024)
- Filtrar por **Nível de Senioridade** (Júnior, Pleno, Sênior, Executivo)
- Filtrar por **Tipo de Contrato** (Full-time, Part-time, Freelance, etc.)
- Filtrar por **Tamanho da Empresa** (Pequena, Média, Grande)

### Visualizações
- **Gráfico de Barras Horizontal**: Top 10 cargos mais bem remunerados
- **Histograma**: Distribuição de salários com KDE
- **Gráfico de Pizza**: Proporção de trabalho remoto vs presencial
- **Mapa Coropleto**: Salários por país para Cientistas de Dados
- **Tabela Detalhada**: Visualização completa dos dados filtrados

---

## 🌐 Deploy no Streamlit Cloud

A aplicação foi deployada com sucesso no **Streamlit Cloud** e está disponível em:

### 🔗 [https://dados-ancelotti.streamlit.app](https://dados-ancelotti.streamlit.app)

**Como foi feito:**
1. Publicação do repositório no GitHub
2. Conexão da conta GitHub com Streamlit Cloud
3. Deployment automático do branch main
4. A aplicação é atualizada automaticamente a cada push

---

## 📈 Dados Utilizados

- **Fonte**: [GitHub - guilhermeonrails/data-jobs](https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv)
- **Colunas principais**: Ano, Senioridade, Cargo, Salário (USD), Tipo de Contrato, Regime de Trabalho, Localização da Empresa
- **Período**: 2020-2024
- **Total de Registros**: ~2000+ profissionais

---

## 💡 Insights Principais

Através da análise, é possível observar:
- 📍 Variação significativa de salários por país e nível de experiência
- 🏢 Influência do tamanho da empresa na remuneração
- 💻 Tendência de crescimento do trabalho remoto
- 📊 Diferenças salariais entre diferentes cargos na área de dados

---

## 🎓 Conceitos-Chave Aplicados

- **Limpeza de Dados**: Tratamento de missing values e duplicatas
- **Análise Exploratória**: EDA com Pandas e Matplotlib
- **Visualização Eficaz**: Escolha de gráficos apropriados para cada tipo de dado
- **Interatividade**: Uso de widgets Streamlit para filtros dinâmicos
- **Deploy**: Publicação de aplicação web sem frontend complexo

---

## 📝 Palavras-chave do Projeto

- DIA 1: **PANDAS** 🐼
- DIA 2: **PRINT** 🖨️
- DIA 3: **MATPLOTLIB** 📊
- DIA 4: **ALURA** 🎓

---

## 👨‍💻 Autor

Desenvolvido como projeto educacional na **Imersão em Dados - EBAC**

---

## 📞 Contato e Links

- 📊 Dashboard ao vivo: [https://dados-ancelotti.streamlit.app](https://dados-ancelotti.streamlit.app)

---

## 📜 Licença

Projeto educacional - Livre para uso e aprendizado.

---

**Última atualização**: Fevereiro de 2026

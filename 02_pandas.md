# PANDAS

### CONCAT, JOIN e MERGE
#### CONCAT
A biblioteca pandas oferece várias ferramentas para trabalhar com *DataFrames*, incluindo a capacidade de combinar, juntar e mesclá-los. Essas operações são úteis para combinar dados de diferentes fontes em um único *DataFrame*. Existem três principais métodos de união de *DataFrames* em `pandas`: `concat`, `join` e `merge`.  
A concatenação é um método simples para combinar DataFrames, no qual suas colunas e índices são mantidos e os valores são simplesmente concatenados uns sobre os outros. O método `concat()` permite que você concatene DataFrames verticalmente (um acima do outro) ou horizontalmente (lado a lado).  
```python
pd.concat([dataframe1, dataframe2, ...], axis=0/1)
```
No qual, axis é o eixo do qual a concatenação vai acontecer. Se axis=0, a concatenação ocorre ao longo do eixo vertical (empilhamento). Se axis=1, a concatenação ocorre ao longo do eixo horizontal (lado a lado).

#### JOIN
O método join é usado para unir dois DataFrames com base em suas colunas de índice ou uma coluna de nome especificada. Ele pode ser usado para unir DataFrames com as mesmas colunas ou com colunas diferentes.

Os dois DataFrames precisam ter uma coluna com nome em comum ou possuírem os índices contendo o mesmo tipo de informação, caso a união ocorra pelo índice e não usando alguma coluna. A sintaxe básica para usar o método join é a seguinte:

```python
dataframe1.join(dataframe2, on='nome_coluna', how='left')
```

No qual on é o nome da coluna em comum entre os dois DataFrames usada como chave de junção. Caso não seja utilizado nenhum valor, a união será feita com base nos índices dos DataFrames. O parâmetro how é o tipo de junção a ser realizada, podendo ser 'left', 'right', 'inner', 'outer'.

#### MERGE

O método merge é o método mais completo para unir dois DataFrames com base em seus índices ou em colunas de ligação. A sintaxe básica para usar o método merge é a seguinte:
```python
dataframe1.merge(dataframe2, on=None, how='inner', left_on='nome_coluna_dataframe1', right_on='nome_coluna_dataframe2')
```
Nela, o `on` é o nome da coluna nos dois DataFrames, caso seja o mesmo nome. O parâmetro `how` é o tipo de junção a ser realizada, podendo ser `'left'`, `'right'`, `'inner'`, `'outer'` e `'cross'`. Os parâmetros `left_on` e `right_on` são respectivamente os nomes das colunas do *DataFrame 1* e *DataFrame 2*, caso tenham nomes diferentes.

### GROUPBY
Trabalhando com *MultiIndex*(índice hierárquico)

#### Criando um *DataFrame* com *MultiIndex*
Para criar um *MultiIndex*, você não necessariamente precisa agrupar os níveis em uma tupla diretamente no groupby. A criação de um *MultiIndex* geralmente ocorre em etapas separadas, e o groupby pode ser aplicado a um DataFrame que já possui um *MultiIndex*.  

Existem algumas maneiras comuns de criar um *MultiIndex*:  
1. Usando `pd.*MultiIndex*.from_tuples()` ou `pd.*MultiIndex*.from_arrays()`:   
Você pode criar um *MultiIndex* a partir de uma lista de tuplas ou de arrays, respectivamente. Isso é útil quando você já tem os dados organizados dessa forma.
2. Usando `set_index()`:   
Você pode transformar colunas existentes em um *MultiIndex* usando o método `set_index()` do *DataFrame*. É aqui que você especifica quais colunas devem se tornar os níveis do índice.
No contexto da aula, o *MultiIndex* já foi criado antes de aplicar o groupby. Provavelmente, foi utilizado o `set_index()` para transformar as colunas `"Gás" e "Nível 1 - Setor"` em um *MultiIndex*.  
```python
import pandas as pd

# Criando um DataFrame de exemplo
data = {'Gás': ['CO2', 'CO2', 'CH4', 'CH4'],
        'Setor': ['Energia', 'Indústria', 'Agropecuária', 'Residencial'],
        'Emissão': [100, 150, 200, 50]}
df = pd.DataFrame(data)

# Criando um MultiIndex a partir das colunas 'Gás' e 'Setor'
df = df.set_index(['Gás', 'Setor'])

# Agora, df.index é um MultiIndex
print(df)
```
Neste exemplo, `df.set_index(['Gás', 'Setor'])` transforma as colunas `'Gás' e 'Setor'` em um *MultiIndex*. Após essa transformação, você pode usar `groupby(level=0)` para agrupar por **"Gás"** ou `groupby(level=1)` para agrupar por **"Setor"**, como demonstrado na aula.
#### Vantagens
**Vantagens de usar Índices:**

1. Acesso e Seleção de Dados Mais Eficientes:  
Com um índice, você pode selecionar dados de forma mais rápida e intuitiva, especialmente com `loc[]`. Em um *MultiIndex*, você pode selecionar subconjuntos de dados com base em combinações de níveis, o que seria mais complexo com colunas.
2. Alinhamento de Dados Simplificado:  
Índices facilitam o alinhamento de dados em operações como `join` e `merge`. Se você tem *DataFrames* com índices correspondentes, o Pandas pode alinhar os dados automaticamente com base nesses índices.
3. Estrutura Hierárquica Clara:  
MultiÍndices fornecem uma estrutura hierárquica para seus dados, o que pode ser útil para organizar e entender conjuntos de dados complexos.
4. Facilidade em Agrupamentos e Cálculos:  
Como vimos na aula, `groupby(level=...)` permite agrupar dados facilmente com base nos níveis do índice. Isso simplifica cálculos e agregações em dados hierárquicos.
5. Melhor Desempenho em Algumas Operações:  
Em certos casos, operações em *DataFrames* com índices podem ser mais rápidas do que operações em *DataFrames* sem índices, especialmente para grandes conjuntos de dados.
**Exemplo Prático:**

Imagine que você está analisando dados de vendas de uma loja online. Você tem as seguintes informações:

Data: Dia da venda.  
Produto: Nome do produto vendido.  
Região: Região onde a venda foi realizada.  
Vendas: Quantidade de vendas.  
Se você definir um *MultiIndex* com "Região" e "Data", poderá facilmente responder a perguntas como:

* "Quais foram as vendas totais em todas as regiões em um determinado dia?"
* "Quais foram as vendas de um produto específico em uma determinada região ao longo do tempo?"  
Código de Exemplo:
```python
import pandas as pd

# Dados de exemplo
data = {'Data': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
        'Produto': ['A', 'B', 'A', 'B'],
        'Região': ['Norte', 'Sul', 'Norte', 'Sul'],
        'Vendas': [10, 15, 12, 18]}
df = pd.DataFrame(data)

# Definindo *MultiIndex*
df = df.set_index(['Região', 'Data'])

# Agrupando por região e somando as vendas
vendas_por_regiao = df.groupby(level='Região')['Vendas'].sum()
print(vendas_por_regiao)

# Selecionando vendas na região Norte em 2023-01-01
vendas_norte_20230101 = df.loc[('Norte', '2023-01-01')]
print(vendas_norte_20230101)
```
Neste exemplo, o *MultiIndex* facilita a agregação de vendas por região e a seleção de vendas em uma região e data específicas. Fazer isso com colunas seria mais complicado e menos eficiente.

* Diferença entre criar o *multiIndex* e usar uma tupla no `groupby`:  
```python
df.set_index(['Gás', 'Setor']).groupby(level=[0, 1]): 
```
Aqui, você está primeiro transformando as colunas `"Gás" e "Setor"` em um *MultiIndex* e, em seguida, agrupando por esses níveis do índice.
```python
df.groupby(['Gás', 'Setor']):
``` 
Aqui, você está agrupando diretamente pelas colunas `"Gás" e "Setor"`, sem modificar a estrutura do índice.

### BUILTIN FUNCTIONS
#### CONTAINS
Este método é usado com string Series para verificar se uma substring específica ou um padrão de expressão regular está presente em cada elemento de string.

1. Diferenças com `isin()`:
* `isin()` verifica correspondências exatas de elementos dentro de uma coleção de valores.
* `str.contains()` verifica a presença de uma substring ou padrão dentro de elementos de string.  

### ASSIGN
O `assign()` permite adicionar novas colunas a um *DataFrame* existente, sem modificar o *DataFrame* original (a menos que você atribua o resultado a ele). Ele retorna um novo *DataFrame* com as colunas adicionadas.
#### Como funciona?

Você passa para o `assign()` os nomes das novas colunas como argumentos de palavra-chave, e os valores dessas colunas podem ser:

* **Valores únicos**: Um valor único que será atribuído a todas as linhas da nova coluna.
* **Listas ou arrays**: Uma lista ou array com o mesmo número de linhas do DataFrame, onde cada elemento será o valor da coluna para a respectiva linha.
* **Series**: Uma Series do Pandas com o mesmo índice do DataFrame, onde os valores da Series serão os valores da nova coluna.
* **Funções**: Uma função que recebe o DataFrame como argumento e retorna uma Series, lista ou array com os valores da nova coluna. Essa é a parte mais poderosa, pois permite criar colunas com base em outras colunas, inclusive as recém-criadas no mesmo `assign()`!

```python
import pandas as pd

data = {'Produto': ['A', 'B', 'C', 'D'],
        'Preço': [10, 20, 15, 25],
        'Quantidade': [5, 10, 7, 3]}
df = pd.DataFrame(data)
print(df)
```
Você pode usar o `assign()` para criar novas colunas:
```python
df = df.assign(
    Imposto = lambda x: x['Preço'] * 0.1,  # Imposto de 10% sobre o preço
    Total = lambda x: x['Preço'] * x['Quantidade'] + x['Preço'] * 0.1 # Calcula o total com imposto
)
print(df)
```
#### Analogia:

Imagine que você tem uma planilha com dados, e quer adicionar novas colunas com cálculos baseados nas colunas existentes. O `assign()` é como se você estivesse criando essas novas colunas na planilha, usando fórmulas que se referem às colunas originais.

#### Em resumo:

O `assign()` é uma ferramenta flexível e poderosa para criar novas colunas em *DataFrames* do Pandas, permitindo cálculos complexos e a criação de colunas dependentes umas das outras. Ele torna o código mais legível e conciso, facilitando a manipulação e análise de dados.

### JSON_NORMALIZE
O método `json_normalize()` do *Pandas* é uma ferramenta poderosa para transformar dados semiestruturados, como *JSONs* aninhados, em um formato tabular mais fácil de manipular e analisar. Imagine que você tem dados organizados em estruturas complexas, como dicionários dentro de dicionários, e precisa transformar isso em uma tabela onde cada chave se torna uma coluna. É aí que o `json_normalize()` entra em ação! Os parâmetros mais importantes do método `json_normalize()` são:

* **data**: o objeto *JSON* a ser normalizado.
* **record_path**: um caminho para acessar o array de registros dentro do objeto *JSON*.
* **meta**: uma lista de colunas adicionais a serem incluídas no *DataFrame*, além das colunas normalizadas.
* **errors**: como lidar com erros de normalização. Os valores possíveis são "raise" (lançar um erro), "ignore" (ignorar o erro).
* **sep**: separador de colunas usado para concatenar as chaves do objeto *JSON* aninhado. O padrão é ".".

#### Como funciona:

* **Entrada**: O método recebe como entrada uma coluna do seu DataFrame que contém os dados em formato *JSON* ou dicionário.
* **Normalização**: Ele "achata" a estrutura *JSON*, transformando cada chave em uma coluna separada. Se houver chaves aninhadas, ele as combina usando um separador (por padrão, um ponto ".") para criar nomes de colunas únicos.
* **Saída**: O resultado é um novo DataFrame onde cada linha representa um registro dos dados originais, e cada coluna representa um campo específico extraído do *JSON*.

#### Exemplo:
```python
import pandas as pd
data = [
  {
    "contrato": "mes a mes",
    "faturamento_eletronico": "sim",
    "metodo_pagamento": "cheque eletronico",
    "cobranca": {
      "mensal": 73.9,
      "Total": 280.85
    }
  },
  {
    "contrato": "anual",
    "faturamento_eletronico": "nao",
    "metodo_pagamento": "boleto",
    "cobranca": {
      "mensal": 50.0,
      "Total": 600.0
    }
  }
]
# Ao aplicar o json_normalize() nessa coluna:

data
df = pd.DataFrame(data)

df_normalizado = pd.json_normalize(df)
print(df_normalizado)
```
```cs
  contrato faturamento_eletronico   metodo_pagamento  cobranca.mensal  cobranca.Total
0  mes a mes                    sim  cheque eletronico            73.90          280.85
1      anual                    nao              boleto            50.00          600.00
```
#### Vantagens

* **Simplicidade**: Transforma estruturas complexas em tabelas com poucas linhas de código.
* **Flexibilidade**: Permite lidar com diferentes níveis de aninhamento e formatos de *JSON*.
* **Integração**: Facilmente integrado com outras funcionalidades do *Pandas* para análise e manipulação de dados.

### DUPLICATED e DROP_DUPLICATED()
O `duplicated()` serve para identificar as duplicatas, enquanto o `drop_duplicates()` serve para remover as duplicatas identificadas. Ambos são essenciais para garantir a qualidade e a eficiência do seu trabalho com dados.
1. **duplicated()**

* **Função**: Identifica e marca as linhas duplicadas em um *DataFrame*.
* **Retorno**: Uma Series booleana, onde **True** indica que a linha é duplicada (ou seja, já apareceu antes) e **False** indica que é a primeira ocorrência daquela linha.
* **Importância**: Permite identificar a existência e a quantidade de dados duplicados em seu conjunto de dados, o que é crucial para a limpeza e a qualidade dos dados.

2. **drop_duplicates()**

* **Função**: Remove as linhas duplicadas de um *DataFrame*.
* **Parâmetro inplace=True**: Modifica o *DataFrame* original, removendo as duplicatas diretamente, sem criar uma cópia.
* **Importância**: Elimina dados redundantes que podem distorcer análises, enviesar modelos de machine learning e aumentar o tempo de processamento.
```python
import pandas as pd

# Criando um DataFrame com dados duplicados
data = {'col1': ['A', 'B', 'C', 'A', 'B'],
        'col2': [1, 2, 3, 1, 2]}
df = pd.DataFrame(data)

print("DataFrame original:\n", df)

# Identificando as linhas duplicadas
duplicatas = df.duplicated()
print("\nLinhas duplicadas:\n", duplicatas)

# Removendo as linhas duplicadas
df.drop_duplicates(inplace=True)
print("\nDataFrame após remover duplicatas:\n", df)
```

Para descobrir a quantidade de dados duplicados você pode usar o método `sum()`, assim ele somará a quantidade de valores que são **True**

### DADOS NULOS
O tratamento de *dados nulos* é fundamental para garantir que um modelo de machine learning tenha uma precisão elevada e uma capacidade de generalização adequada. O uso de técnicas adequadas de tratamento de dados nulos é um passo importante no processo de preparação de dados para qualquer análise ou modelo de machine learning. No mercado de trabalho, *a exclusão de dados sempre deve ser a última opção*.  
Métodos `isna()`, `fillna()`, `dropna()` e `notnull()`
#### fillna()
* `df.fillna(valor)`: Preenche os valores nulos com um valor específico. 
* `df.fillna(df.mean())`: Preenche os valores nulos com a média das colunas. 
* `df.fillna(df.median())`: Preenche os valores nulos com a mediana das colunas. 
* `df.fillna(df.mean(numeric_only=True))`: Preenche os valores nulos com a média das colunas numéricas, ignorando outras colunas. 
* `df.interpolate(method = )`: Preenche os valores nulos usando interpolação, como `"linear"`, `"polinomial"`, etc. 
* `df.fillna(method='bfill')`: Preenche os valores nulos com o próximo valor válido (backward fill). 
* `df.fillna(method='ffill')`: Preenche os valores nulos com o valor anterior válido (forward fill).

#### dropna()
Remove linhas(axis = 0) ou colunas(axis = 1) que contêm valores nulos. É útil quando os dados faltantes são irrelevantes ou em pequena quantidade, e sua remoção não prejudica a análise.
* `df.dropna(subset=['coluna1', 'coluna2'])`: Remove linhas que contenham valores nulos em colunas específicas. 

#### isna() ou isnull()
Retorna um *DataFrame* de valores booleanos, indicando onde estão os valores nulos (True para nulo, False para não nulo). Essencial para identificar a presença e a localização de dados faltantes.

#### notna() ou notnull()
Retorna um *DataFrame* de valores booleanos, indicando onde não estão os valores nulos (True para não nulo, False para nulo). Similar ao isna(), mas com a lógica inversa, útil para selecionar dados válidos.

#### Outras funções úteis
* `df.describe()`: Fornece estatísticas descritivas, incluindo contagem de valores não nulos por coluna. 
* `df.info()`: Fornece informações sobre o *DataFrame*, incluindo o número de valores não nulos por coluna. 
* `df.isnull().sum()`: Retorna a soma de valores nulos por coluna. 
* `df.replace({valor_antigo: valor_novo})`: Substitui valores específicos, como `NaN`, por novos valores. 
*  **Imputação de Dados Nulos**: onde os valores são estimados com base em outras informações disponíveis no conjunto de dados. Isso é particularmente útil quando a quantidade de dados nulos é grande
* * **Imputação com Média e Mediana**
```python
from sklearn.impute import SimpleImputer

# Criar um objeto imputador com a estratégia da média
imputador_media = SimpleImputer(strategy='mean')

# Imputar os valores nulos da coluna 'Idade' com a média da coluna
df_imputado_media = pd.DataFrame(imputador_media.fit_transform(df[['Idade']]), columns=['Idade'])
```
* * **Imputação com Modelos de Aprendizado de Máquina**
```python
from sklearn.impute import KNNImputer

# Criar um objeto imputador usando KNeighborsRegressor
imputador_knn = KNNImputer(n_neighbors=2)

# Imputar os valores nulos das colunas 'Idade' e 'Salario' usando KNN
df_imputado_knn = pd.DataFrame(imputador_knn.fit_transform(df[['Idade', 'Salario']]), columns=['Idade', 'Salario'])
```

* * **Imputação com aprendizado de máquina manual**: *Onde você utiliza os próprios dados para treinar a máquina e definir as colunas ou linhas nulas com `target` e fazer isso para cada linha ou coluna*

#### Considerações
Aqui estão algumas considerações finais importantes:

* Sempre analise o contexto dos dados e avalie o impacto das diferentes estratégias de tratamento de dados nulos em suas análises e resultados.
* A remoção de dados nulos pode levar à perda de informações valiosas, portanto, use-a com cautela.
* O preenchimento com estatísticas descritivas, como média e mediana, é uma abordagem simples, mas pode introduzir distorções em alguns casos.
* A interpolação é útil quando os dados seguem uma tendência ou padrão.
* A imputação com modelos de aprendizado de máquina pode ser mais precisa, mas requer mais complexidade e cuidado na escolha do modelo.
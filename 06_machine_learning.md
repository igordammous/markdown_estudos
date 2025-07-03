# *Machine Learning*

## Ponderação
No momento de realizar o treinamento de modelos de *machine learning*, nos deparamos com um grande problema ao lidar com **variáveis categóricas**. As categorias não podem ser utilizadas em forma de texto, uma vez que os algoritmos compreendem apenas valores numéricos. Também não podemos simplesmente atribuir um valor numérico para cada categoria, uma vez que esse processo, conhecido como **ponderação arbitrária**, pode criar uma ordenação e pesos para as categorias que *não* refletem a realidade.

O processo correto de transformação das variáveis categóricas é feito a partir da criação de novas colunas a partir das categorias. Cada uma delas se torna uma nova coluna e o valor na linha correspondente será 1, caso tenha a presença da característica. Do contrário, será 0. Esse processo é conhecido como codificação "one-hot".

Considerando:

| Variável Categ.|
|----------------|
|Característica 1|
|Característica 2|
|Característica 3|

Aplicando o procedimento de `one-hot`, teremos:
|Característica 1|Característica 2|Característica 3|
|----------------|----------------|----------------|
|       1        |       0        |       0        |
|       0        |       1        |       0        |
|       0        |       0        |       1        |

### Get-Dummies
O método `get_dummies()` é da biblioteca [Pandas](https://github.com/igordammous/markdown_estudos/blob/main/02_pandas.md) e é simples de utilizar e faz a transformação de forma direta das variáveis categóricas. Importante dizer que a partir do *Pandas 2.0* os valores retornados serão em `bool(True / False)` ao inves de como é agora `(1 / 0)`. 
```python
import pandas as pd
dados = pd.DataFrame({'variavel':['caracteristica 1', 'caracteristica 2', 'caracteristica 3']})
pd.get_dummies(dados, columns = ['variavel'])
```
* Pandas 1.0+ ou `get_dummies(dtype = int)`

|variavel_caracteristica1|variavel_caracteristica2|variavel_caracteristica3|
|------------------------|------------------------|------------------------|
|       1                |       0                |       0                |
|       0                |       1                |       0                |
|       0                |       0                |       1                |

* Pandas 2.0+ ou `get_dummies(dtype = bool)`

|variavel_caracteristica1|variavel_caracteristica2|variavel_caracteristica3|
|------------------------|------------------------|------------------------|
|       True             |       False            |       False            |
|       False            |       True             |       False            |
|       False            |       False            |       True             |

Esses dados podem ser passados como dados de entrada de um modelo de *machine learning* para realizar uma previsão. Porém, imagine que precisamos aplicar o processo para dados novos, contendo uma **característica 2**, já conhecida, e uma **característica 4**, que não foi utilizada na construção do modelo. O método `get_dummies()` não conseguirá gerar todas as colunas necessárias para a previsão. Ele vai considerar como válida uma **característica** não vista anteriormente e que não será entendida pelo modelo treinado.
```python
dados_novos = pd.DataFrame({'variavel':['caracteristica 2', 'caracteristica 4']})
pd.get_dummies(dados_novos, columns = ['variavel'])
```
|    |variavel_caracteristica2|variavel_caracteristica4|
|----|------------------------|------------------------|
|  0 |       1                |       0                |
|  1 |       0                |       1                |

#### Parametros
O método `get_dummies()` da biblioteca Pandas é utilizado para transformar variáveis categóricas em variáveis binárias. Abaixo estão os parâmetros do método:

* `data`: parâmetro obrigatório que representa o conjunto de dados e contém as variáveis categóricas a serem transformadas em variáveis binárias.
* `prefix`: é um parâmetro opcional utilizado para adicionar um prefixo às colunas binárias geradas pelo método `get_dummies()`. Por exemplo, se você definir o prefixo como "cat_", as colunas binárias geradas terão nomes como "cat_1", "cat_2", etc.
* `prefix_sep`: parâmetro opcional utilizado para definir o separador entre o prefixo e o nome original da coluna categórica. O valor padrão é "_".
* `columns`: parâmetro opcional utilizado para selecionar as colunas específicas do conjunto de dados que devem ser transformadas em variáveis binárias. Se não for especificado, todas as colunas categóricas serão transformadas.
* `drop_first`: é um parâmetro opcional utilizado para remover a primeira coluna binária gerada pelo método `get_dummies()`. Isso é feito para evitar a multicolinearidade, que é uma situação em que duas ou mais variáveis independentes estão altamente correlacionadas entre si.
* `dtype`: parâmetro opcional utilizado para definir o tipo de dado das colunas binárias geradas pelo método `get_dummies()`. O valor padrão é "bool".

```python
import pandas as pd

# Criando um DataFrame de exemplo
df = pd.DataFrame({'cor': ['vermelho', 'azul', 'verde', 'vermelho'],
                   'tamanho': ['pequeno', 'médio', 'grande', 'médio'],
                   'formato': ['quadrado', 'redondo', 'redondo', 'quadrado']})

# Transformando as colunas categóricas em variáveis numéricas binárias
df_dummies = pd.get_dummies(df, columns=['cor', 'tamanho'], prefix=['cor', 'tam'], prefix_sep='-', drop_first=True)

# Exibindo o DataFrame resultante
df_dummies
```
Saída:
|   |formato |cor-verde|cor-vermelho|tam-médio|tam-pequeno|
|---|--------|---------|------------|---------|-----------|
| 0 |quadrado|    0    |     1      |    0    |     1     |
| 1 |redondo |    0    |     0      |    1    |     0     |
| 2 |redondo |    1    |     0      |    0    |     0     |
| 3 |quadrado|    0    |     1      |    1    |     0     |

Neste exemplo, o parâmetro data é o DataFrame df que contém as colunas categóricas a serem transformadas. O parâmetro columns é uma lista que contém os nomes das colunas categóricas a serem transformadas em variáveis binárias. O parâmetro prefix é uma lista que contém os prefixos a serem adicionados às colunas binárias geradas. Aqui, estamos adicionando o prefixo `"cor_"` às colunas binárias geradas a partir da coluna "cor" e o prefixo `"tam_"` às colunas binárias geradas a partir da coluna "tamanho".

Adicionamos também os parâmetros `prefix_sep='-'` para definir o separador entre o prefixo e o nome original da coluna categórica como um hífen `(-)`. Também adicionamos o parâmetro `drop_first=True` para remover a primeira coluna binária gerada pelo método `get_dummies()`. Isso é feito para evitar a multicolinearidade, que é uma situação em que duas ou mais variáveis independentes estão altamente correlacionadas entre si.

O resultado será um novo DataFrame chamado `df_dummies`, que contém as colunas originais do DataFrame df, bem como as novas colunas binárias geradas pelo método `get_dummies()` com um hífen `(-)` como separador de prefixo e a primeira coluna binária removida.

### OneHot
O método `OneHotEncoding()` é da biblioteca [sklearn](https://scikit-learn.org). E ao contrário do `get_dummies()`, o método `OneHotEncoder()` funciona como outros modelos disponíveis na biblioteca Sklearn. Nele, é necessário instanciar um objeto e depois ajustar aos dados com um método `fit()`. Dessa forma, esse objeto armazena os passos necessários para realizar a transformação dos dados.
```python
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
colunas_categoricas = ['variavel']
one_hot_enc = make_column_transformer(
    (OneHotEncoder(handle_unknown = 'ignore'),
    colunas_categoricas),
    remainder='passthrough')
dados = one_hot_enc.fit_transform(dados)
dados = pd.DataFrame(dados, columns=one_hot_enc.get_feature_names_out())
dados
```
|   |onehotencoder_variavel_caracteristica1|onehotencoder_variavel_caracteristica2|onehotencoder_variavel_caracteristica3|
|---|--------------------------------------|--------------------------------------|--------------------------------------|
| 0 |       1                              |                   0                  |                  0                   |
| 1 |       0                              |                   1                  |                  0                   |
| 2 |       0                              |                   0                  |                  1                   |

Ao aplicar em novos dados, o método `OneHotEncoder()` irá construir todas as colunas que foram geradas no treinamento atribuindo valor 0 ou 1, dependendo da presença ou ausência da característica, respectivamente. Logo, esse método é ideal para utilizar em modelos de *machine learning*.
```python
dados_novos = pd.DataFrame({'variavel':['caracteristica 2', 'caracteristica 4']})
dados_novos = one_hot_enc.transform(dados_novos)
dados_novos = pd.DataFrame(dados_novos, columns=one_hot_enc.get_feature_names_out())
dados_novos
```
|   |onehotencoder_variavel_caracteristica1|onehotencoder_variavel_caracteristica2|onehotencoder_variavel_caracteristica3|
|---|--------------------------------------|--------------------------------------|--------------------------------------|
| 0 |       0                              |                   1                  |                  0                   |
| 1 |       0                              |                   0                  |                  0                   |

Assim, a característica 4 contida nos novos dados não se torna uma nova coluna, apenas são atribuídos os valores 0 para cada uma das características utilizadas no momento do treinamento do modelo.

## Pickle
o processamento que foi criado pelo `OneHotEncoder()` pode ser armazenado em arquivos pickle, assim como outros modelos de *machine learning*, para ser utilizado fora do ambiente onde foi criado, permitindo o uso em outros projetos.
```python
import pickle
with open('modelo_onehotenc.pkl', 'wb') as file:
    pickle.dump(one_hot_enc, file)
```
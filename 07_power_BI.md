# Power BI

## Linguagens
No Power BI, há duas linguagens fundamentais para manipulação e transformação de dados são o [M](https://learn.microsoft.com/pt-br/powerquery-m/) e o [DAX](https://learn.microsoft.com/pt-br/dax/dax-overview).

Ambas as linguagens, M e DAX, desempenham papéis complementares no Power BI. O M é utilizado principalmente na fase de preparação dos dados, enquanto o DAX é utilizado para realizar cálculos e análises com base nos dados já carregados no modelo de dados. Combinar o uso dessas duas linguagens permite uma transformação completa dos dados, desde a extração inicial até a análise final.

Para aprofundar seus conhecimentos sobre as linguagens M e DAX no Power BI, recomendo a leitura do artigo [Power BI: M e DAX](https://www.alura.com.br/artigos/power-bi-linguagens-m-dax). Ele apresenta uma visão detalhada sobre as características e funcionalidades dessas linguagens, fornecendo insights valiosos para aprimorar suas habilidades no Power BI.

## Qualidade de Coluna
O recurso de Qualidade da Coluna no Power BI rotula os valores em linhas em cinco categorias, fornecendo informações sobre a qualidade dos dados em cada coluna:

* **Válido (verde):** indica que os valores na coluna estão corretos e dentro dos critérios definidos.
* **Erro (vermelho)**: sinaliza a presença de erros na coluna, indicando que os valores não estão de acordo com as regras ou critérios estabelecidos.
* **Vazio (cinza escuro)**: representa valores ausentes ou nulos na coluna, indicando que não há dados presentes.
* **Desconhecido (verde pontilhado)**: indica a presença de erros em uma coluna, resultando em uma qualidade de dados desconhecida para os demais valores.
* **Erro inesperado (vermelho pontilhado)**: identifica a ocorrência de erros inesperados na coluna, que não se enquadram nas categorias anteriores.

Essa funcionalidade de Qualidade da Coluna no Power BI proporciona uma visão rápida e clara sobre a qualidade dos dados em cada coluna. Entretanto, devemos estar atentos a um quesito muito importante quando se trata do Power BI, que é o fato de se tratar de uma ferramenta que tem como padrão resumir os dados, principalmente por questão de performance.

Pensando nisso, o Power BI oferece a opção de filtrar os dados das tabelas, por meio de duas opções: *criação de perfil da coluna com base nas primeiras 1000 linhas*, que é a opção padrão; e *criação de perfil da coluna com base em todo o conjunto de dados*. Essa opção de filtragem por todo o conjunto pode ser especialmente importante para garantir uma análise mais precisa e abrangente dos seus dados.

Ao ativar a opção de criação de perfil da coluna com base em todo o conjunto de dados, o Power BI analisará todas as linhas do conjunto de dados, permitindo identificar padrões, distribuições e problemas de qualidade que podem não ser detectados apenas com uma amostra limitada de linhas.

## Medidas
No Power BI, medidas são elementos essenciais para realizar cálculos e análises sobre os dados. Elas podem ser classificadas em **medidas implícitas** e **medidas explícitas**.
### Medidas Implícitas
O que são: Medidas implícitas são criadas automaticamente pelo Power BI quando você interage com os dados em um visual. Por exemplo, se você arrastar a coluna "Quantidade" de uma tabela para um cartão, o Power BI automaticamente soma os valores dessa coluna, ou seja, são medidas que você não sabe como foram desenvolvidas.
Como funcionam: O Power BI geralmente faz uma soma automática, mas oferece outras opções de agregação (como média, mínimo, contagem, etc.) ao campo que você adiciona ao visual. A agregação padrão pode variar dependendo do tipo de dado do campo.
#### Vantagens:
* **Simplicidade:** São fáceis de usar, pois não exigem que você escreva nenhuma fórmula.
* **Rapidez**: Permitem criar análises rápidas e explorar os dados de forma intuitiva.
#### Desvantagens:
* **Limitações**: As opções de cálculo são limitadas às agregações padrão oferecidas pelo Power BI.
* **Pouca flexibilidade**: Não permitem criar cálculos personalizados ou complexos.
### Medidas Explícitas
O que são: Medidas explícitas são cálculos que você define manualmente usando a linguagem DAX (Data Analysis Expressions). Você escreve a fórmula para calcular algo específico, como o "Faturamento Total" (que é a soma da coluna "Faturamento" da tabela "Vendas").
Como funcionam: Você cria uma nova medida e escreve uma fórmula DAX que define o cálculo desejado. Essa fórmula pode envolver funções, operadores, referências a outras colunas e medidas, etc.
#### Vantagens:
* **Flexibilidade**: Permitem criar cálculos personalizados e complexos para atender às suas necessidades específicas de análise.
* **Controle**: Você tem total controle sobre a lógica do cálculo e pode ajustá-la conforme necessário.
* **Reutilização**: Uma vez criada, a medida pode ser reutilizada em vários visuais e relatórios.

#### Desvantagens:
* **Complexidade**: Exigem conhecimento da linguagem DAX, que pode ter uma curva de aprendizado.
* **Tempo**: Criar medidas explícitas pode levar mais tempo do que usar medidas implícitas, especialmente para cálculos complexos.

### Quando usar cada tipo de medida:
* **Medidas Implícitas**: Use quando precisar de cálculos rápidos e simples, como somar valores ou calcular médias.
* **Medidas Explícitas**: Use quando precisar de cálculos personalizados, complexos ou que não podem ser feitos com as agregações padrão do Power BI.

Como boa prática, opte por medidas explícitas pois, além dos benefícios apresentados, você tem o poder de desenvolver cálculos mais complexos utilizando filtros e relacionamentos.

## Hierarquia
Os rótulos de hierarquia no Power BI são uma poderosa ferramenta que permite organizar e apresentar dados de forma estruturada e hierárquica. Com eles, é possível criar visualizações mais intuitivas e explorar a relação entre diferentes níveis de informações.
* **Seta apontada para cima (drill up)**: este botão aumenta um nível na hierarquia, mas para cima. Por exemplo, se estamos filtrando os dados por *Mês* e clicamos nele, os dados serão filtrados em Trimestre. Caso cliquemos de novo, serão filtrados por *Ano*, e assim por diante.
* **Seta apontada para baixo (drill down)**: esse botão serve para detalhar os campos. Por exemplo, se filtramos os dados por Trimestre, e clicamos no *mês* de janeiro, que faz parte do primeiro trimestre, todos os meses pertencentes ao primeiro trimestre serão detalhados.
* **Seta dupla apontada para baixo (próximo nível da hierarquia)**: essa opção faz o caminho inverso do Drill up, ou seja, quando clicamos nela os dados são filtrados pela hierarquia que vem abaixo. Por exemplo, se os dados estão filtrados por *Mês* e clicamos nessa seta, os dados passarão a ser filtrados por *Dia*.
* **Seta dupla em formato de garfo (expandir todo o campo um nível na hierarquia)**: essa opção só funciona quando estamos na hierarquia do topo, no caso do nosso exemplo, a hierarquia *Ano*. Como a seta dupla apontada para baixo, a seta dupla em formato de garfo também aciona as hierarquias abaixo da selecionada. Mas, ao invés de descer um nível todo, ela expande o nível com o próximo abaixo, de modo a incluir a filtragem do nível atual e a filtragem do nível abaixo. Por exemplo, quando estamos em *Ano* e clicamos nessa seta, os dados serão filtrados por *Ano* e *Trimestre*. Se clicarmos outra vez, serão filtrados por *Ano*, *Trimestre* e *Mês*, e assim por diante.

Em resumo, os rótulos de hierarquia no Power BI são uma excelente ferramenta para organizar e apresentar dados hierárquicos de forma clara e interativa. Eles permitem que você crie visualizações mais poderosas e flexíveis, oferecendo aos usuários a capacidade de explorar os dados em diferentes níveis de detalhe.
# SQL - Structured Query Language

Uma linguagem que foi construída para interagir com um banco de dados através de SGBD (Sistemas Gerenciadores de Banco de Dados), como Oracle, MySQL, MariaDB, PostgreSQL, Microsoft SQL Server e outros.

### DDL (Data Definition Language)
Os comandos DDL são usados para definir a estrutura do banco de dados:

* CREATE: cria objetos de banco de dados, como tabelas, índices, visões e procedimentos armazenados.
* ALTER: modifica a estrutura de objetos de banco de dados existentes, como adicionar ou remover colunas de tabelas.
* DROP: exclui objetos de banco de dados, como tabelas, índices ou visões.
* TRUNCATE: Remove todos os registros de uma tabela, mas mantém sua estrutura.

### DQL – Data Query Language
É um grupo de comandos dentro do SQL. Os comandos DQL são usados para **CONSULTAS**:
* **SELECT**: recupera dados de uma ou mais tabelas do banco de dados. É o comando principal para consultas.

Aqui temos a forma que é feita a seleção tanto geral *, ou com parametros. Numa tabela chamada clientes, com 5 colunas (id, nome, telefone, gênero e data_cadastro) qualquer uma dessas colunas pode ser consultada. Com 5 linhas (cabeçalho, 1, 2, 3, 4) que também podem ser consultadas a qualquer momento.

```
    SELECT campos FROM nome_da_tabela
```
```
    SELECT * FROM clientes -> dessa forma consulta todos os campos
    
    SELECT nome, telefone FROM clientes -> dessa forma seleciona o campo nome e telefone
```
A forma com * não é muito utilizada pois em grandes quantidades de dados, exige muito da máquina e há maneiras melhores.

#### Select com WHERE e operadores lógicos
```
    SELECT * FROM clientes WHERE genero = “F” AND nome LIKE “R%”
```
Nesse exemplo a seleção será com clientes do gênero feminino com o nome iniciando com R
Há também além do operador igual (=), os operadores IN e BETWEEN. O **IN** é usado a filtragem a partir de uma lista de buscas. Enquanto o **BETWEEN** é utilizado para fazer buscas entre intervalos. É mais utilizado para filtrar intervalos de datas.
```
    SELECT * FROM clientes WHERE genero IN id (1, 2, 3)
```
Neste comando, todos os clientes com id 1, 2 e 3 serão retornados.
```
    SELECT * FROM clientes WHERE data_cadastro BETWEEN ‘10-12-2019’ AND ‘20-10-2019’
```
Neste comando, todos os clientes que foram cadastrados entre essas datas serão retornados.

* **LIKE**: É utilizado para buscar strings(texto) dentro de uma coluna com valores textuais. Podemos buscar as linhas que o nome inicia com uma determinada palavra, como vimos acima ou contém um certo texto.
    * string: são retornadas todas as linhas que tem na coluna buscada exatamente a "string" informada no filtro. É a mesma coisa de usar o operador de igual.

    * %string%: são retornadas as linhas que tem na coluna buscada a "string" informada. Podemos buscar os nomes que tem "Jesus", ou que tem alguma sílaba ou letra específica. A linha com o nome "Roberta de Jesus", contém o termo "da", então atenderia ao filtro '%de%'.

    * %string: são retornadas as linhas que a coluna filtrada termina com a "string" informada. O % indica que pode ter qualquer valor no começo do campo, desde que ele termine com a “string". A linha com nome "Roberta de Jesus" atenderia ao filtro '%Jesus'.

    * string%: são retornadas as linhas que o coluna filtrada começa com a “string" informada. O % indica que depois da “string” pode ter qualquer valor. A linha com nome "Roberta de Jesus", atenderia ao filtro 'Roberta%'.

* **ORDER BY**: O ORDER BY é utilizado para ordenação. Podemos ordenar em ordem crescente (ASC) ou em ordem decrescente (DESC).
```
    SELECT * FROM clientes ORDER BY nome ASC
```
Neste comando, serão retornados todos os clientes ordenados pelo nome em ordem crescente.

### DML – Data Manipulation Language 
Essa manutenção se dá por meio do SGBD, que nos permite realizar vários processos nos bancos de dados, como consultar, inserir, alterar e excluir dados das tabelas. Para alterar e excluir dados de uma tabela, utilizamos duas cláusulas bem importantes da linguagem SQL: a cláusula **UPDATE** que é responsável por alterar os dados armazenados e a cláusula **DELETE** que é responsável por remover os dados. Serão os comandos DML usados para manipular os dados:
* INSERT: adiciona novos registros a uma tabela.
* UPDATE: modifica registros existentes em uma tabela.
* DELETE: remove registros de uma tabela.

* **UPDATE**: Utilizada para realizar alterações nos dados armazenados em uma tabela do banco de dados. A sintaxe básica do comando utilizado por todos os bancos de dados relacionais é:
```
    UPDATE nome_da_tabela
    SET coluna = valor, 
    WHERE condição;
```
Na cláusula UPDATE, informamos o nome da tabela que queremos atualizar, utilizamos o **SET** para indicar os campos da tabela que serão atualizados e no **WHERE** expressamos a condição para a atualização, ou seja, especificamos quais registros devem ser atualizados na tabela.

* **DELETE**: Utilizada para realizar a exclusão de dados de uma ou mais tabelas de um banco de dados. A sintaxe básica do comando utilizado por todos os bancos de dados relacionais é:
```
    DELETE
    FROM nome_da_tabela, 
    WHERE condição;
```
Onde na cláusula **FROM**, informamos o nome da tabela que queremos excluir os dados, e no WHERE informamos a condição que especifica quais registros devem ser excluídos da tabela.
* **Riscos e Cuidados ao executar os comandos**: Ao executar os comandos para realizar a atualização ou exclusão de dados de uma tabela de um banco de dados, precisamos tomar alguns cuidados.
Um ponto de atenção é sempre informar uma condição ao realizar uma atualização ou exclusão de dados de uma tabela. Quando não informamos essa condição, corremos o risco de que todos os dados da tabela sejam atualizados, ou até mesmo excluídos, ocorrendo assim a perda de dados importantes.

#### TABELAS QUE SERÃO USADAS NOS EXEMPLOS
|ID	|CPF	        |NOME	                |ENDEREÇO	            |BAIRRO	    |CIDADE	        |ESTADO	|CEP        |
|:-:|:-------------:|:---------------------:|:---------------------:|:---------:|:-------------:|:-----:|:---------:|
|01	|01471156710    |Érica Carvalho	        |R. Iriquitia	        |Jardins	|São Paulo	    |SP	    |80012212   |
|02	|19290992743	|Fernando Cavalcante	|R. Dois de Fevereiro   |Agua Santa	|Rio de Janeiro	|RJ	    |22000000   |
|03	|02600586709    |César Teixeira	        |Rua Conde de Bonfim    |Tijuca	    |Rio de Janeiro	|RJ	    |22020001   |
|04	|00492472718    |Eduardo Jorge	        |R. Volta Grande	    |Tijuca	    |Rio de Janeiro	|RJ	    |22012002   |
|05	|50534475787	|Abel Silva	            |Rua Humaitá	        |Humaitá	|Rio de Janeiro	|RJ	    |22000212   |
|06	|05576228758    |Petra Oliveira	        |R. Benício de Abreu	|Lapa	    |São Paulo	    |SP	    |88192029   |
|07	|05840119709    |Gabriel Araujo	        |R. Manuel de Oliveira	|Santo Amaro|São Paulo	    |SP	    |80010221   |


|MATRÍCULA  |NOME	            |BAIRRO	    |COMISSÃO   |DATA ADMISSÃO|
|:---------:|:-----------------:|:---------:|:---------:|:-----------:|
|235        |Márcio Almeida	    |Tijuca	    |0.08       |2014-08-15   |
|236	    |Cláudia Morais	    |Jardins	|0.08	    |2013-09-17   |
|237	    |Roberta Martins	|Copacabana	|0.11	    |2017-03-18   |
|238	    |Péricles Alves	    |Santo Amaro|0.11	    |2016-08-21   |

```
    UPDATE CLIENTES
    SET nome = 'Érica Silvia'
    WHERE CPF = '01471156710';
```
Nesse exemplo atualizará o cadastro da Érica, usando o CPF como condição
|ID	|CPF	        |NOME	                |ENDEREÇO	            |BAIRRO	    |CIDADE	        |ESTADO	|CEP        |
|:-:|:-------------:|:---------------------:|:---------------------:|:---------:|:-------------:|:-----:|:---------:|
|01	|01471156710    |**Érica Silvia**       |R. Iriquitia	        |Jardins	|São Paulo	    |SP	    |80012212   |

```
    UPDATE CLIENTES
    SET NOME = 'Fernando Sousa',CEP = '80012212'
    WHERE CPF = '19290992743';
```
Nesse caso, ao usar _vírgula_, você consegue alterar mais de um dado de uma vez
|ID	|CPF	        |NOME	                |ENDEREÇO	            |BAIRRO	    |CIDADE	        |ESTADO	|CEP        |
|:-:|:-------------:|:---------------------:|:---------------------:|:---------:|:-------------:|:-----:|:---------:|
|01	|01471156710    |Érica Silvia	        |R. Iriquitia	        |Jardins	|São Paulo	    |SP	    |80012212   |
|02	|19290992743	|Fernando Sousa     	|R. Dois de Fevereiro   |Agua Santa	|Rio de Janeiro	|RJ	    |80012212   |

Caso fosse um caso onde os estados tivessem errados, dá pra usar o *UPDATE* sem a condição *WHERE* e alterar o estado de todo mundo

```
    UPDATE Clientes
    SET ESTADO = 'SP';
```

|ID	|CPF	        |NOME	                |ENDEREÇO	            |BAIRRO	    |CIDADE	        |ESTADO	|CEP        |
|:-:|:-------------:|:---------------------:|:---------------------:|:---------:|:-------------:|:-----:|:---------:|
|01	|01471156710    |Érica Carvalho	        |R. Iriquitia	        |Jardins	|São Paulo	    |SP	    |80012212   |
|02	|19290992743	|Fernando Sousa     	|R. Dois de Fevereiro   |Agua Santa	|Rio de Janeiro	|SP	    |80012212   |
|03	|02600586709    |César Teixeira	        |Rua Conde de Bonfim    |Tijuca	    |Rio de Janeiro	|SP	    |22020001   |
|04	|00492472718    |Eduardo Jorge	        |R. Volta Grande	    |Tijuca	    |Rio de Janeiro	|SP	    |22012002   |
|05	|50534475787	|Abel Silva	            |Rua Humaitá	        |Humaitá	|Rio de Janeiro	|SP	    |22000212   |
|06	|05576228758    |Petra Oliveira	        |R. Benício de Abreu	|Lapa	    |São Paulo	    |SP	    |88192029   |
|07	|05840119709    |Gabriel Araujo	        |R. Manuel de Oliveira	|Santo Amaro|São Paulo	    |SP	    |80010221   |

E no caso de *DELETE*: Dois casos, um para deletar um cliente do bando de dados e outro para deletar todo o banco de dado e manter a formatação da tabela
```
DELETE
FROM Clientes
WHERE CPF = '05840119709';
```
|ID	|CPF	        |NOME	                |ENDEREÇO	            |BAIRRO	    |CIDADE	        |ESTADO	|CEP        |
|:-:|:-------------:|:---------------------:|:---------------------:|:---------:|:-------------:|:-----:|:---------:|
|01	|01471156710    |Érica Carvalho	        |R. Iriquitia	        |Jardins	|São Paulo	    |SP	    |80012212   |
|02	|19290992743	|Fernando Sousa     	|R. Dois de Fevereiro   |Agua Santa	|Rio de Janeiro	|SP	    |80012212   |
|03	|02600586709    |César Teixeira	        |Rua Conde de Bonfim    |Tijuca	    |Rio de Janeiro	|SP	    |22020001   |
|04	|00492472718    |Eduardo Jorge	        |R. Volta Grande	    |Tijuca	    |Rio de Janeiro	|SP	    |22012002   |
|05	|50534475787	|Abel Silva	            |Rua Humaitá	        |Humaitá	|Rio de Janeiro	|SP	    |22000212   |
|06	|05576228758    |Petra Oliveira	        |R. Benício de Abreu	|Lapa	    |São Paulo	    |SP	    |88192029   |

```
DELETE
FROM Clientes;
```

E por fim, o *UPDATE* com interação de duas tabelas, podemos informar na cláusula *WHERE* como condição para realizar atualização ou exclusão dos dados, outra consulta, que pode ser utilizada para buscar informações armazenadas na própria tabela ou em outras tabelas:

```
UPDATE VENDEDORES
SET COMISSÃO  = COMISSÃO + 0.03
WHERE COMISSÃO = (SELECT min(COMISSÃO) FROM VENDEDORES)
```

O *SELECT* passado na cláusula *WHERE*, retornará apenas o valor da menor comissão armazenada na tabela. Dessa forma, apenas os vendedores que possuem o valor da comissão igual ao valor retornado neste SELECT terão os seus dados alterados e o valor da sua comissão aumentará:

|MATRÍCULA  |NOME	            |BAIRRO	    |COMISSÃO   |DATA ADMISSÃO|
|:---------:|:-----------------:|:---------:|:---------:|:-----------:|
|235        |Márcio Almeida	    |Tijuca	    |**0.11**   |2014-08-15   |
|236	    |Cláudia Morais	    |Jardins	|**0.11**   |2013-09-17   |
|237	    |Roberta Martins	|Copacabana	|0.11	    |2017-03-18   |
|238	    |Péricles Alves	    |Santo Amaro|0.11	    |2016-08-21   |

```
INSERT INTO VENDEDORES (Matricula, Nome, Bairro, Comissão, Data Admissão) VALUES (239, 'João Krelin', 'Tijuca', 0.10, 2018-02-05);
```

|MATRÍCULA  |NOME	            |BAIRRO	    |COMISSÃO   |DATA ADMISSÃO|
|:---------:|:-----------------:|:---------:|:---------:|:-----------:|
|235        |Márcio Almeida	    |Tijuca	    |**0.11**   |2014-08-15   |
|236	    |Cláudia Morais	    |Jardins	|**0.11**   |2013-09-17   |
|237	    |Roberta Martins	|Copacabana	|0.11	    |2017-03-18   |
|238	    |Péricles Alves	    |Santo Amaro|0.11	    |2016-08-21   |
|239	    |João Krelin	    |Tijuca     |0.10	    |2018-02-05   |

Uma outra forma de garantir que apenas os dados desejados sofram alterações é a criação de uma chave primária na tabela. A chave primária, ou Primary key (PK) é o dado que pode ser utilizado como um identificador único de um registro em uma tabela no banco de dados. Se definirmos que o campo CPF será a chave primária da tabela de clientes, estamos definindo que este campo receberá apenas valores únicos. Ao utilizarmos este campo como uma condição no momento de executar uma consulta com as cláusulas DELETE ou UPDATE, garantimos que apenas o registro que possui aquele dado será alterado.

### DCL (Data Control Language)
Os comandos DCL controlam permissões de acesso e os comandos:

* GRANT: Concede permissões a usuários ou funções para acessar objetos de banco de dados.
* REVOKE: Remove permissões previamente concedidas a usuários.
### TCL (Transaction Control Language)
Os comandos TCL gerenciam transações:

* COMMIT: Confirma uma transação, tornando as alterações permanentes no banco de dados.
* ROLLBACK: Desfaz uma transação e restaura o banco de dados ao estado anterior.
* SAVEPOINT: Define um ponto de salvamento em uma transação, permitindo o rollback parcial.
* SET TRANSACTION: Define características de transação, como isolamento e nível de isolamento.

### SQL versus NoSQL
Artigo mais completo da [diferença](https://www.alura.com.br/artigos/sql-nosql-bancos-relacionais-nao-relacionais) entre os dois.
#### SQL (Bancos de Dados Relacionais):
* Modelo de Dados Relacional: Seguem o modelo relacional, onde os dados são organizados em tabelas com colunas que têm tipos de dados definidos.
* Esquema Fixo: Possuem um esquema rígido, o que significa que a estrutura das tabelas e a definição de colunas devem ser especificadas antecipadamente.
* ACID Transactions: Conhecidos por garantir transações ACID (Atomicidade, Consistência, Isolamento e Durabilidade), o que garante a integridade dos dados, mas pode impactar o desempenho em determinados casos.
* Flexibilidade Limitada: Mudanças no esquema, como adicionar ou remover colunas, podem ser complexas e demoradas.
* Consultas Complexas: Oferecem suporte a consultas complexas usando SQL, o que é ideal para análises e relatórios sofisticados.

#### Quando utilizar um banco de dados relacional?
O uso de um [banco de dados relacional](https://www.alura.com.br/artigos/o-que-e-sql) é recomendado em várias situações, principalmente quando temos um cenário que exige uma estrutura organizada e consistente. E a linguagem SQL tem um papel fundamental para a manipulação e gerenciamento desses bancos. Algumas situações onde o banco de dados relacional costuma ser adequado são:

* *Estrutura de dados definida:* Um banco de dados relacional é adequado quando os dados possuem uma estrutura definida e há relações claras entre as entidades.
* *Integridade dos dados críticos*: É recomendado utilizar um banco de dados relacional quando a integridade dos dados é crucial, especialmente em áreas como finanças, estoque ou registros de pacientes.
* *Consultas complexas e agregações*: Se você precisa realizar consultas complexas, como junções de tabelas, filtragem avançada, agrupamento e cálculos agregados, um banco de dados relacional é uma escolha adequada.
* *Conformidade e segurança*: Se a conformidade com normas de segurança e regulamentações é fundamental, um banco de dados relacional fornece recursos avançados de segurança, como controle de acesso e criptografia.

#### NoSQL (Bancos de Dados Não Relacionais):
* Modelo de Dados Flexível: Suportam diversos modelos de dados, como documentos, chave-valor, família de colunas e gráficos. Isso oferece flexibilidade na estrutura dos dados.
* Esquema Dinâmico: Geralmente têm esquemas dinâmicos, permitindo adicionar campos sem a necessidade de uma estrutura rígida.
* BASE Transactions: Frequentemente seguem o modelo BASE (Basically Available, Soft state, Eventually consistent), que sacrifica um pouco da consistência em favor da disponibilidade e desempenho.
* Escalabilidade Horizontal: São altamente escaláveis e podem ser dimensionados horizontalmente para lidar com grandes volumes de dados e tráfego.
* Simplicidade em Grande Escala Eles são frequentemente mais simples de usar em cenários de alto tráfego e grande volume de dados, como mídias sociais e aplicativos da web.

Dentro do [NoSQL](https://cursos.alura.com.br/extra/alura-mais/o-que-e-nosql--c1142) tem uma variedade de modelos e cada um possui características distintas por isso uma adequação de uso diferente pra cada um.
* *Modelo Colunar*: Também conhecido como armazenamento de colunas, é uma abordagem em que os dados são armazenados como colunas em vez de linhas. Esse modelo é ideal para situações que envolvem grande quantidade de dados e exigem alta performance, pois permite que apenas as colunas relevantes sejam buscadas e lidas, economizando recursos de processamento. Uma das empresas que utilizam esse modelo é a Netflix, que utiliza o Cassandra para gravações de volume muito alto com baixa latência.

* *Orientado a Documentos*: Nesse modelo, os dados são armazenados em documentos no formato JSON. Cada documento é identificado por uma chave única e pode conter diversas informações, como atributos e subdocumentos. Esse modelo é interessante para aplicações que exigem flexibilidade na estrutura dos dados e que lidam com grande volume de informações. Na Expedia, a empresa utiliza o modelo flexível do MongoDB que facilita o armazenamento de qualquer combinação de cidades, datas e destinos.

* *Chave-valor*: Os dados são armazenados em pares de chave-valor, o que significa que cada dado é identificado por uma chave única. Esse modelo é ideal para aplicações que exigem alta performance em leitura e gravação de dados, como em aplicações de cache ou armazenamento de sessões de usuários. Este modelo usado pelo Twitter, que utiliza o Redis para implementar recursos em tempo real como contadores de retweets, curtidas e seguidores.

* *Modelo de Grafos*: Neste modelo os dados são usados para armazenar dados interconectados, como em redes sociais ou sistemas de recomendação. Com o modelo de grafos, é possível fazer buscas detalhadas nas relações entre os dados, mesmo em bancos com centenas de milhares de relacionamentos. O Medium, por exemplo, utiliza o Neo4j para criar grafos que representam as conexões entre usuários e artigos, permitindo a montagem de um sistema de recomendação.

#### Quando utilizar bancos de dados não relacionais?
Os bancos não relacionais oferecem uma flexibilidade e escalabilidade muito vantajosa, principalmente quando se trata de grandes conjuntos de dados. Mas como as operações dos bancos NoSQL dependem do tipo de modelo escolhido, para utilizá-lo, precisamos entender a necessidade de nosso negócio, como:

* *Aplicações que trabalham com cache*: Em cenários onde o desempenho de leitura e gravação é fundamental, como em um sistema que precise de armazenar dados frequentemente acessados de forma rápida (sistema de cache) em tempo real, os modelos chave-valor dos bancos NoSQL, como o Redis, são frequentemente utilizados devido à sua alta velocidade de acesso e recuperação.

* *Sistemas de catálogos ou estruturas flexíveis*: Se a aplicação requer flexibilidade na estrutura e na consulta de dados, o modelo orientado a documentos, como MongoDB, pode ser uma boa escolha pela sua capacidade de conter informações de um objeto em um único documento.

É possivel o uso de sistema híbrido. Por exemplo, um sistema de comércio eletrônico pode usar um banco de dados SQL para gerenciar pedidos e um banco de dados NoSQL para rastrear eventos de registro de atividade do usuário, conforme está ilustrado na imagem a seguir.

E por fim tem uma [Apostila](https://www.alura.com.br/apostila-sql-e-modelagem-com-banco-de-dados) feita pela Alura a respeito de SQL e Modelagem de Dados.

### Tipos de Dados
Os bancos de dados armazenam uma variedade de tipos de dados para atender às necessidades de diferentes tipos de informações e aplicativos. A escolha dos tipos de dados a serem usados em um banco de dados depende da natureza dos dados que serão armazenados e processados. Aqui estão alguns dos tipos de dados mais comuns em um banco de dados:

#### Texto (String):

* CHAR: Armazena strings de tamanho fixo. Usado quando os valores têm um comprimento constante.
* VARCHAR: Armazena strings de tamanho variável. Apropriado para valores com comprimentos variáveis.
* TEXTO (TEXT): Armazena strings muito longas, como documentos ou descrições.

#### Numérico:

* INTEGER (INT): Armazena números inteiros.
* FLOAT: Armazena números de ponto flutuante, geralmente usados para valores com casas decimais.
* NUMERIC (DECIMAL): Armazena números com uma precisão específica, geralmente usados em aplicações financeiras.

#### Data e Hora:

* DATE: Armazena datas sem informações de horário.
* TIME: Armazena informações de horário.
* TIMESTAMP: Combina data e horário em um único tipo.

#### Booleano:

* BOOLEAN (BOOL): Armazena valores verdadeiros ou falsos.

#### Binário:

* BLOB (Binary Large Object): Armazena dados binários, como imagens, vídeos ou arquivos.
* BIT: Armazena valores binários, como 0 ou 1.

### Primary Key
A Primary Key é um campo ou conjunto de campos em uma tabela de banco de dados que serve para identificar de forma exclusiva cada registro nessa tabela.

#### Características da Primary Key:

* Unicidade: Cada valor na coluna de chave primária deve ser único em relação a todos os outros valores na mesma coluna. Isso garante que nenhum registro duplicado seja inserido na tabela.
* Não nulo: A chave primária não pode conter valores nulos. Cada registro deve ter um valor na coluna da chave primária.
* Eficiência de pesquisa: A chave primária é usada para acelerar a pesquisa de registros no banco de dados. Os SGBDs criam índices automaticamente nas colunas de chave primária para otimizar a recuperação de dados.

#### Por que a Primary Key é importante?

A chave primária é fundamental para manter a integridade dos dados e garantir que as operações de consulta e atualização sejam eficientes. Veja:

* Identificação única: Ela permite identificar cada registro de forma única, o que é essencial em muitos cenários de negócios. Por exemplo, em um banco de dados de clientes, a chave primária pode ser o número de identificação de cada cliente.
* Integridade referencial: A chave primária é usada em relacionamentos entre tabelas para garantir a integridade referencial. Isso significa que os registros relacionados em tabelas diferentes podem ser conectados de maneira confiável.
* Eficiência: Como mencionado anteriormente, as chaves primárias são indexadas automaticamente pelos SGBDs, tornando as consultas mais rápidas e eficientes.

Exemplos de Primary Key:

* Em uma tabela de "Funcionários", o número de identificação de cada funcionário pode ser a chave primária.

### Foreign Key

A Chave estrangeira é feita para cruzar informações, por exemplo usar uma chave primária de uma tabela em outra.

### ALIAS -> Apelidos para colunas
Usado principalmente em casos onde o nome das colunas não é muito claro em relação ao dado que ela representa.

Por exemplo, numa coluna chamada de *informacoes_de_contato* de um tabela chamada *tabelaclientes*, onde a unica informação que tem é o email, você pode dar uma apelido para quem se referenciar a essa coluna, use esse apelido e o código fique mais claro.

```
SELECT informacoes_de_contato AS email_cliente FROM tabelaclientes
```
E sempre que você quiser usar esse ou qualquer outro apelido, você tem que referenciar esse código pois você não está mudando o nome da coluna e sim dando um apelido para deixar ela mais clara.

Outro exemplo: suponha que estamos unindo as tabelas "Pedidos" e "Clientes," e queremos evitar ambiguidades nos nomes das colunas "ID" de ambas as tabelas:
```
SELECT P.ID AS IDPedido, C.ID AS IDCliente
FROM Pedidos AS P
JOIN Clientes AS C ON P.ClienteID = C.ID;
```
Neste caso, usamos ALIAS para renomear as tabelas "Pedidos" e "Clientes" como "P" e "C," respectivamente.

#### DELETE CASCADE
A exclusão em cascata é uma técnica poderosa para manter a integridade referencial e manter a consistência dos dados em um banco de dados. Quando você define uma restrição de chave estrangeira com a opção ON DELETE CASCADE, 
você garante que, se um registro na tabela "pai" for excluído, todos os registros relacionados nas tabelas "filhas" serão automaticamente excluídos, evitando referências a registros ausentes.

Suponha que você tenha duas tabelas, "Clientes" e "Pedidos," onde a tabela "Pedidos" possui uma chave estrangeira que faz referência ao "ID" do cliente na tabela "Clientes." 
Se você configurar a relação com ON DELETE CASCADE, quando um registro de cliente for excluído na tabela "Clientes," todos os registros de pedidos relacionados a esse cliente também serão excluídos automaticamente, 
evitando registros de pedidos órfãos sem um cliente associado.

Exemplo de definição da chave estrangeira com DELETE CASCADE:

```
CREATE TABLE Clientes (
    ID INT PRIMARY KEY,
    Nome VARCHAR(50)
);

CREATE TABLE Pedidos (
    PedidoID INT PRIMARY KEY,
    ClienteID INT,
    Descricao VARCHAR(100),
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ID) ON DELETE CASCADE
);
```

## SQLite ONLINE: executando consultas SQL
#### MAX, MIN, SUM, AVG, COUNT
```
SELECT mes, max(faturamento_bruto) FROM faturamento;
SELECT mes, min(faturamento_bruto) FROM faturamento;

SELECT sum(numero_novos_clientes) AS ‘Novos Clientes 2023’ FROM faturamento
WHERE mes like %2023;
```
Nesse código a função max, min e sum pede a coluna que será feita a função, para isso coloca-se entre parênteses.
Novamente o código **AS** dá um apelido para a somatória, enquanto o **WHERE mes LIKE %2023** filtra todos os meses que terminam com o ano de 2023.
```
SELECT AVG(despesas) AS 'Média Despesas', AVG(lucro_liquido) AS 'Média Lucro Líquido' FROM faturamento;
```
Nesse exemplo cria duas colunas, uma com a média (average) das despesas já com apelido e a média do lucro líquido também com apelido.
```
SELECT COUNT(*) FROM HistoricoEmprego
WHERE datatermino NOTNULL;
```
Aqui está contando quantas pessoas estão desempregadas na base de dados da empresa utilizada no exemplo.

```
SELECT COUNT(*) FROM Licencas
WHERE tipolicenca = 'férias';

SELECT parentesco, COUNT(*) FROM Dependentes
GROUP BY parentesco;

SELECT instituicao, COUNT(*) FROM Treinamento
GROUP BY instituicao
HAVING COUNT(curso) > 1;
```
No primeiro código seleciona e conta quantas pessoas entraram de férias. No segundo, seleciona quais são o parentesco das pessoas cadastradas sob dependentes e conta a quantidade de cada um e por fim agrupa eles por parentesco. 
No terceiro é feito a mesma coisa, porém ao usar o “GROUP BY” o “WHERE” não funciona para filtrar mais, para isso usa-se o “HAVING”.

```
SELECT ('O(A) colaborador(a) ' || nome || ' de CPF ' || cpf || ' possui o seguinte endereço: ' || endereco) AS texto FROM Colaboradores;
```
```
Saída:
O(A) colaborador(a) Dr. Cauê da Conceição de CPF 24657139061 possui o seguinte endereço: Recanto Isadora Nunes, Lagoa, 69660278 Jesus / MS
```
Nesse exemplo acima foi usada a barra dupla vertical || -> ela é usada para concatenar um texto(string)
Ainda é possivel assim como no python, usar o **UPPER**, **LOWER**, no caso são usados após o *SELECT* e antes do parenteses

#### Função TRIM, INSTR, REPLACE, SUBSTR
**TRIM**
* Funcionalidade: A função TRIM remove espaços (ou outro conjunto especificado de caracteres) do início e do fim de uma string.
* Sintaxe Básica: TRIM(string, [caractere_para_trimar])
* Exemplo de Uso: Para remover espaços do início e do fim da coluna nome:
Ao trabalhar com TRIM, se nenhum caractere específico for fornecido para remoção, ele removerá espaços por padrão.

**INSTR**
* Funcionalidade: INSTR retorna a posição de uma substring dentro de uma string. Equivalente ao CHARINDEX em alguns outros sistemas.
* Sintaxe Básica: INSTR(string, substring)
* Exemplo de Uso: Para encontrar a posição da substring 'abc' dentro da coluna descricao:
A função INSTR é particularmente útil para localizar substrings e pode ser usada em operações mais complexas, como extrações condicionais ou verificação de presença de padrões.

**REPLACE**
* Funcionalidade: REPLACE substitui todas as ocorrências de uma substring específica por outra substring dentro de uma string.
* Sintaxe Básica: REPLACE(string, substring_a_substituir, substring_para_substituir)
* Exemplo de Uso: Para substituir 'hello' por 'hi' na coluna saudacao:
REPLACE é uma ferramenta poderosa para limpeza e formatação de dados, sendo capaz de alterar padrões específicos em uma grande quantidade de texto.

**SUBSTR** OU *SUBSTRING*
* Funcionalidade: SUBSTR extrai uma parte de uma string com base em um ponto de início e um comprimento especificados.
* Sintaxe Básica: SUBSTR(string, inicio[, comprimento])
* Exemplo de Uso: Para extrair os primeiros 5 caracteres da coluna comentario:
Se comprimento não for especificado, SUBSTR retornará todos os caracteres a partir da posição inicio até o final da string.
*SUBSTR* é amplamente utilizada para cortar e analisar partes de strings, especialmente quando combinada com outras funções como *INSTR*.

#### TRABALHANDO COM DATA
Assim como outras linguagens usa-se o strptime e strftime, por exemplo
´´´
SELECT id_colaborador, STRFTIME('%Y/%m', datainicio) FROM Licencas;
´´´
No caso do SQLite, existe a função já pronta para calculos matemáticos simples com data, chamada de **JULIANDAY()**
´´´
SELECT id_colaborador, JULIANDAY( datatermino) - JULIANDAY (datacontratacao) data FROM HistoricoEmprego
WHERE datatermino IS NOT NULL
ORDER BY data ASC;
´´´
No exemplo acima está querendo saber da tabela HistoricoEmprego a quantidade de dias que as pessoas ficaram no emprego da empresa do exemplo, o filtro *WHERE* é para tirar pessoas que ainda estão empregadas.
E foi dado um apelido *data* para a subtração para que fosse possivel ordernar de maneira crescente, para saber qual colaborador ficou menos dias empregado na empresa.

#### FUNÇÕES DATE, TIME, DATETIME
**Função DATE**
* Funcionalidade: A função DATE é usada para extrair a data de um valor de data e hora ou para obter a data atual. Ela retorna a data no formato 'YYYY-MM-DD'.
* Sintaxe Básica: DATE('now', '[modificador]')
* Exemplo de Uso: Para obter a data atual:
```
SELECT DATE('now');
SELECT DATE('now', '-10 days');
```
No primeiro exemplo retorna a data atual e no segundo retorna 10 dias antes da data atual.

**Função TIME**
* Funcionalidade: A função TIME é usada para extrair a hora de um valor de data e hora ou para obter a hora atual. Ela retorna a hora no formato 'HH:MM:SS'.
* Sintaxe Básica: TIME('now', '[modificador]')
* Exemplo de Uso: Para obter a hora atual:


**Função DATETIME**
* Funcionalidade: DATETIME é uma função mais abrangente que retorna tanto a data quanto a hora no formato 'YYYY-MM-DD HH:MM:SS'. Pode ser usada para obter o momento atual ou converter/modificar valores de data e hora existentes.
* Sintaxe Básica: DATETIME('now', '[modificador]')
* Exemplo de Uso: Para obter a data e hora atuais:

```
SELECT DATETIME('now', '+1 year');
```
Assim como na função *DATE*, esse exemplo retorna data e hora do dia atual + um ano.

**Função CURRENT_TIMESTAMP**
* Funcionalidade: CURRENT_TIMESTAMP é uma função de conveniência que retorna a data e hora atuais no formato 'YYYY-MM-DD HH:MM:SS'. É equivalente a usar DATETIME('now').
* Sintaxe Básica: CURRENT_TIMESTAMP
* Exemplo de Uso: Para obter o timestamp atual:

#### FUNÇÕES FLOOR, CEIL, ROUND
A função *FLOOR* arrendo o número inteiro para baixo, a função *CEIL* é o oposto. E o *ROUND* arrendo o número de casas que o usuário decidir.

#### FUNÇÕES MATEMÁTICAS
**Função POWER**
* Funcionalidade: POWER é usada para elevar um número a uma potência específica.
* Sintaxe Básica: POWER(base, expoente)
* Exemplo de Uso: Para elevar 2 à 3ª potência, RETORNA 8:

**Função SQRT**
* Funcionalidade: SQRT retorna a raiz quadrada de um número.
* Sintaxe Básica: SQRT(numero)
* Exemplo de Uso: Para encontrar a raiz quadrada de 16, RETORNA 4:

**Função RANDOM**
* Funcionalidade: RANDOM gera um número inteiro aleatório entre -9223372036854775808 e +9223372036854775807.
* Sintaxe Básica: RANDOM()
* Exemplo de Uso: Para gerar um número aleatório:

**Função ABS**
* Funcionalidade: ABS retorna o valor absoluto de um número, que é o número sem seu sinal.
* Sintaxe Básica: ABS(numero)
* Exemplo de Uso: Para obter o valor absoluto de -5, RETORNA 5:

**Função HEX**
* Funcionalidade: HEX converte um número ou uma string para a sua forma hexadecimal.
* Sintaxe Básica: HEX(string)
* Exemplo de Uso: Para converter 255 para hexadecimal, RETORNA 'FF':

```
SELECT HEX('hello');
```
RETORNA '68656C6C6F'

**Considerações Importantes**
POWER e SQRT são particularmente úteis para cálculos científicos e financeiros.
RANDOM é útil para situações onde você precisa de dados aleatórios, como na criação de amostras ou em simulações.
ABS é frequentemente usado em análises matemáticas e estatísticas para garantir que apenas a magnitude de um número seja considerada.
HEX é útil para trabalhos com sistemas que usam representações hexadecimais, como trabalhos com cores na web ou com dados binários.

#### FUNÇÕES DE CONVERSÃO
1. **CAST**
* Funcionalidade: Converte um tipo de dados de uma expressão para outro tipo especificado.
* SGBDs Compatíveis: Quase todos os SGBDs principais, incluindo MySQL, PostgreSQL, SQL Server, SQLite e Oracle. Única função de conversão disponível no SQLite online.
* Sintaxe: CAST(expressao AS tipo)

2. **CONVERT**
* Funcionalidade: Semelhante ao CAST, mas com uma sintaxe ligeiramente diferente e, em alguns SGBDs, recursos adicionais.
* SGBDs Compatíveis: Principalmente SQL Server e MySQL. A função CONVERT no MySQL é usada mais comumente para conversão de codificação de caracteres, não tipos de dados.
* Sintaxe (SQL Server): CONVERT(tipo, expressao [, estilo])

3. **TO_NUMBER, TO_CHAR, TO_DATE** *(Funções específicas do Oracle)*
* Funcionalidade: Converte strings para números (TO_NUMBER), números ou datas para strings (TO_CHAR), e strings para datas (TO_DATE).
* SGBDs Compatíveis: Oracle.
* Sintaxe: TO_NUMBER(string [, formato [, 'nlsparam']]), TO_CHAR(valor [, formato [, 'nlsparam']]), TO_DATE(string [, formato [, 'nlsparam']])

4. **PARSE, TRY_PARSE, TRY_CONVERT** *(SQL Server)*
* Funcionalidade: PARSE tenta converter uma string para um tipo de dados numérico ou de data/hora com um estilo de cultura opcional. TRY_PARSE e TRY_CONVERT são versões mais seguras que retornam NULL em vez de um erro se a conversão falhar.
* SGBDs Compatíveis: SQL Server.
* Sintaxe: PARSE(string AS tipo USING cultura), TRY_PARSE(string AS tipo USING cultura), TRY_CONVERT(tipo, expressao [, estilo])

5. **STR_TO_DATE** *(MySQL)*
* Funcionalidade: Converte uma string em um formato de data especificado para uma data.
* SGBDs Compatíveis: MySQL.
* Sintaxe: STR_TO_DATE(string, formato)

6. **TO_NUMBER, TO_CHAR** *(PostgreSQL)*
* Funcionalidade: TO_NUMBER converte uma string para um número, e TO_CHAR converte um número ou data para uma string, ambos com base em um formato especificado.
* SGBDs Compatíveis: PostgreSQL.
* Sintaxe: TO_NUMBER(string, formato), TO_CHAR(valor, formato)

**Considerações Importantes:**
Compatibilidade: Sempre verifique a documentação específica do seu SGBD para entender a disponibilidade e o uso exato de cada função, pois pode haver pequenas variações na sintaxe e no comportamento.
Uso Cuidadoso: A conversão de tipos de dados deve ser feita com cuidado, especialmente ao converter entre numéricos e strings ou ao lidar com datas, para evitar erros ou resultados inesperados.
Dependência da Versão: Alguns SGBDs podem adicionar, modificar ou depreciar funções em diferentes versões, então é importante considerar a versão específica que você está usando.

### Aplicando mais comandos
#### EXPRESSÃO *CASE*
Possui duas formas, a simples e a pesquisada, o exemplo abaixo se trata da forma pesquisada, onde você passa uma condição e depois retorna um texto.
```
SELECT id_colaborador, cargo, salario, CASE
WHEN salario < 3000 THEN 'Baixo'
WHEN salario BETWEEN 3000 AND 6000 THEN 'Médio'
ELSE 'Alto'
END AS categoria_salario FROM HistoricoEmprego
```
A cláusula CASE em SQL é uma expressão condicional, semelhante às instruções "if-else" em linguagens de programação. Ela permite que você execute diferentes cálculos ou operações em seus dados com base em condições específicas. Essa funcionalidade é extremamente útil para transformar dados, realizar cálculos condicionais e categorizar informações dentro de suas consultas SQL.
E abaixo temos a forma simples.
```
CASE expressao
    WHEN valor1 THEN resultado1
    WHEN valor2 THEN resultado2
    ...
    ELSE resultado_padrao
END
```

**Considerações Importantes**
Performance: O uso excessivo de instruções CASE pode afetar a performance da consulta, especialmente em grandes conjuntos de dados.
Legibilidade: Embora a cláusula CASE seja poderosa, consultas muito complexas podem se tornar difíceis de ler e manter.
Compatibilidade: A cláusula CASE é amplamente suportada pela maioria dos SGBDs, tornando-a uma ferramenta versátil para análise de dados.

#### BOAS PRÁTICAS
1. **Clareza e Descritividade:**
* **Nomes Significativos**: Escolha nomes que reflitam claramente o conteúdo e a função da tabela ou coluna. Por exemplo, uma tabela que armazena informações sobre clientes pode ser chamada de Clientes ou InformacoesClientes.
* **Evite Abreviações Obscuras**: Abreviações podem tornar os nomes mais curtos, mas devem ser evitadas a menos que sejam amplamente compreendidas e consistentes em todo o banco de dados.

2. **Consistência:**
* **Convenção de Nomenclatura**: Escolha uma convenção de nomenclatura e seja fiel a ela em todo o banco de dados. Por exemplo, se você usar nomes no singular para tabelas (Cliente), use isso consistentemente. O mesmo vale para a capitalização; escolha entre PascalCase, camelCase ou snake_case e seja consistente.
* **Padrões de Nomenclatura de Coluna**: Mantenha um padrão para nomes de colunas semelhantes em diferentes tabelas. Por exemplo, se uma coluna que se refere a um identificador único é nomeada IdCliente em uma tabela, não a nomeie ClienteID em outra.

3. **Evitar Palavras Reservadas:**
Palavras do SQL: Evite usar palavras reservadas do SQL como nomes de tabelas ou colunas, como SELECT, DATE, TABLE, etc. Isso pode causar conflitos e erros em consultas.

4. **Precisão e Escopo:**
Especificidade: Nomes de colunas devem ser precisos. Por exemplo, em vez de chamar uma coluna de Data, nomeie-a como DataNascimento ou DataContratacao, dependendo do contexto.
Qualificação de Nomes: Em um banco de dados com muitas tabelas relacionadas, pode ser útil incluir uma referência à tabela pai no nome de uma coluna de chave estrangeira. Por exemplo, IdCliente em uma tabela de pedidos.

5. **Simplicidade e Tamanho:**
Nomes Curtos, Mas Descritivos: Enquanto a descritividade é importante, nomes excessivamente longos podem ser problemáticos para digitar e podem não ser totalmente suportados por todos os sistemas de banco de dados.

6. **Utilizar Sublinhados para Espaços:**
Sem Espaços: Não use espaços em nomes de tabelas ou colunas. Use sublinhados (_) se necessário para separar palavras.

7. **Documentação:**
Mantenha Documentação: Documente as convenções de nomenclatura e as decisões específicas de nomes para facilitar a compreensão e manutenção por outros usuários e desenvolvedores.

8. **Idioma:**
Considere o Idioma Padrão: Use um idioma consistente (geralmente inglês) para nomes de tabelas e colunas, a menos que haja uma razão específica para não fazê-lo.
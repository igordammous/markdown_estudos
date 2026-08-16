# Banco de Dados

## 1 - O que são *Banco de Dados*

Um *banco de dados* (BD) é uma coleção organizada e estruturada de dados persistentes, relacionados entre si, que representa aspectos do mundo real (o chamado mini-mundo ou universo de discurso). Ele é projetado, construído e povoado com dados para atender a um propósito específico (Elmasri & Navathe).

Além dos dados em si, um *banco de dados* inclui:

* **Metadados**: informações sobre a estrutura dos dados (dicionário de dados ou catálogo).
* **Restrições de integridade**: regras que garantem a validade e consistência dos dados.
* **Operações**: formas de consultar e modificar os dados (geralmente via SGBD).

### 1.1 - Analogia: Biblioteca organizada

Imagine uma **biblioteca antiga**, onde os livros eram armazenados sem nenhum critério. Encontrar um livro era uma tarefa de horas, e perder um exemplar era comum.

Agora imagine uma **biblioteca moderna**:

* Cada livro tem uma catalogação (título, autor, assunto, ISBN).
* Há prateleiras organizadas por categorias e ordem alfabética.
* Existe um catálogo (fichário ou sistema digital) que referencia cada livro.
* Há regras de empréstimo, devolução e reserva.

O *banco de dados* é exatamente essa biblioteca: dados organizados, com catálogo (metadados), regras (integridade) e operações definidas (consultar, inserir, remover).

### 1.2 - ALCOA++

Embora a **ALCOA++** não seja um tópico central nas bibliografias clássicas de banco de dados (*Elmasri, Silberschatz, Date*), ela é **fundamental na gestão de dados regulados**, especialmente nas indústrias *farmacêutica, química e alimentícia*, dentro do contexto de qualidade, integridade e governança de dados. **ALCOA++** é um conjunto de princípios que garante a integridade dos dados em ambientes regulados. Ele surgiu a partir de diretrizes de boas práticas de fabricação (GMP), boas práticas de laboratório (GLP) e boas práticas clínicas (GCP), sendo amplamente adotado por agências reguladoras como **FDA (EUA), EMA (Europa) e ANVISA (Brasil)**.

> O objetivo é assegurar que os dados sejam **confiáveis, rastreáveis e defensáveis** ao longo de todo o ciclo de vida — desde a geração até o arquivamento.

#### 1.2.1 Por que isso importa para bancos de dados?

Quando falamos de banco de dados, normalmente pensamos em eficiência, consistência e segurança. A **ALCOA++** acrescenta uma camada de conformidade regulatória, exigindo que os sistemas de banco de dados em indústrias reguladas sejam capazes de auditar cada alteração, rastrear cada acesso e preservar cada registro.

<img src="https://a3analitica.com.br/wp-content/uploads/2024/04/26.02.2023-1-Captura-de-tela-2024-01-16-163652.png" width="">

#### 1.2.2 - Atributos

##### 1.2.2.1 - Atribuível (Attributable) [A]

Cada dado deve estar associado à pessoa ou sistema que o gerou, modificou ou excluiu. Exemplo em banco de dados:

* Registro de `created_by`, `updated_by`, `deleted_by` em tabelas de auditoria.
* Login único por usuário (sem contas compartilhadas).

##### 1.2.2.2 -  Legível (Legible) [L]

Os dados devem ser legíveis e permanentes, sem possibilidade de rasuras ou alterações que comprometam a leitura. Exemplo:

* Uso de `INSERT` e `UPDATE` com auditoria imutável (tabela de histórico).
* Não usar `DELETE` em dados críticos; usar flag de "inativado" ou `soft delete`.

##### 1.2.2.3 - Contemporâneo (Contemporaneus) [C]

Os dados devem ser registrados no momento em que a atividade ocorre, não depois. Exemplo:

* Captura automática de data e hora (`timestamp`) no momento da gravação.
* Triggers ou eventos de banco que gravam automaticamente o horário real do evento.

##### 1.2.2.4 - Original (Original) [O]

O dado deve ser a primeira versão registrada, não uma cópia ou recriação. Exemplo:

* Armazenar o dado bruto original antes de qualquer transformação.
* Versionamento de registros (ex.: tabelas `historico_*` ou colunas `versao`).

##### 1.2.2.5 - Preciso (Accurate) [A]

Os dados devem estar corretos e refletir fielmente a realidade. Exemplo:

* Validação de dados na entrada (constraints, triggers).
* Uso de tipos de dados adequados (não armazenar data como string, por exemplo).

##### 1.2.2.6 - Completo (Complete) [++]

Todos os dados relevantes devem ser registrados, incluindo falhas, erros e correções. Exemplo:

* Auditoria de tentativas de login, alterações de configuração, exclusões lógicas.
* Logs completos de transações, mesmo as que falharam.

##### 1.2.2.7 - Consistente (Consistent) [++]

Os dados devem seguir uma ordem lógica e coerente ao longo do tempo. Exemplo:

* Sequência de `timestamps` coerente (sem datas no futuro, sem horários impossíveis).
* Regras de normalização e integridade referencial para evitar contradições.

##### 1.2.2.8 - Duradouro (Enduring) [++]

Os dados devem ser armazenados em mídia durável e legível por todo o período de retenção exigido. Exemplo:

* Políticas de backup e retenção.
* Migração de mídia legada sem perda de legibilidade.

##### 1.2.2.9 - Disponível (Available) [++]

Os dados devem estar disponíveis para revisão, auditoria ou inspeção quando necessário. Exemplo:

* Índices e estruturas que permitam consulta rápida de históricos.
* Replicação e alta disponibilidade do banco de dados.

### 1.3 - Componentes Essenciais

|Componente|Descrição|Analogia com biblioteca|
|----------|---------|-----------------------|
|Dados|Informações armazenadas|Livros|
|Metadados|Descrição da estrutura|Fichas catalográficas|
|Regras de integridade|Consistência e validade|Regras de empréstimo|
|Operações|Consulta, inserção, atualização, remoção|Emprestar, devolver, catalogar|
|Usuários|Pessoas ou sistemas que acessam|Leitores, bibliotecários|

### 1.4 - Importância dos Bancos de Dados

Os bancos de dados são a espinha dorsal de praticamente todas as aplicações modernas. Sem eles, a gestão da informação seria caótica, redundante e insegura.

#### 1.4.1 - Vantagens principais (segundo Elmasri & Navathe e Silberschatz)

* **Controle de redundância**: cada dado é armazenado uma única vez, evitando inconsistências.
* **Compartilhamento de dados**: múltiplos usuários e aplicações acessam os mesmos dados simultaneamente.
* **Restrições de integridade**: regras garantem que os dados sejam válidos e coerentes.
* **Segurança**: controle de acesso, autorização e auditoria.
* **Independência de dados**: mudanças na estrutura física não afetam as aplicações.
* **Acesso eficiente**: consultas otimizadas por meio de índices e heurísticas.
* **Recuperação de falhas**: transações e backups protegem contra perda de dados.
* **Concorrência**: múltiplos usuários acessam sem conflitos (controle de transações).

#### 1.4.2 - Analogia: Conta bancária

Imagine um banco sem banco de dados:

* Cada agência teria seu próprio cadastro de clientes.
* Um cliente poderia sacar mais do que tem em outra agência.
* As transações não seriam registradas de forma segura.
* Não haveria como garantir que o saldo está correto.

Com um banco de dados:

* O saldo é único e consistente.
* As transações são registradas e protegidas (ACID).
* Há controle de acesso para funcionários e clientes.
* Há recuperação de falhas em caso de queda de energia.

### 1.5 - Evolução

<img src="https://i.imgur.com/2oQCntd.png" width="1000">

### 1.6 - SGBD (Sistema Gerenciador de Banco de Dados)

O **SGBD** é o software que gerencia o banco de dados. Ele atua como intermediário entre os usuários e os dados, garantindo consistência, segurança e eficiência.

#### 1.6.1 Funções principais

* Definição de estrutura (DDL – Data Definition Language).
* Manipulação de dados (DML – Data Manipulation Language).
* Controle de acesso e concorrência.
* Otimização de consultas.
* Recuperação de falhas.

#### 1.6.2 Analogia: Maquinário do banco

Se o banco de dados é o cofre com dinheiro, o **SGBD** é o caixa eletrônico:

* Ele autentica o usuário.
* Valida a operação.
* Atualiza o saldo.
* Registra a transação.
* Recupera o sistema em caso de falha.

## 2 - Modelos de Banco de Dados

Um modelo de banco de dados é um conjunto de conceitos e regras usados para descrever a estrutura, as operações e as restrições de um banco de dados. Ele define como os dados são organizados, armazenados e manipulados.

* **Modelo hierárquico** (década de 1960)
* **Modelo em rede** (CODASYL)
* **Modelo relacional** (1970 – E. F. Codd)
* **Modelo orientado a objetos**
* **Modelo NoSQL** (documento, chave-valor, colunar, grafo)

### 2.1 - Modelo Relacional

O modelo relacional organiza os dados em **tabelas** (relações), onde cada **linha** representa uma **entidade** ou **fato**, e cada **coluna** representa um **atributo**. **As relações entre tabelas são feitas por meio de chaves primárias e chaves estrangeiras**.

#### 2.1.1 Exemplo: Planilhas interligadas

Imagine uma planilha de Excel para "Clientes" e outra para "Pedidos". Na planilha de Pedidos, há uma coluna "ID_Cliente" que referencia a linha correspondente na planilha de Clientes. Essa é a ideia de chave estrangeira. Exemplo prático

Tabela `clientes`

|id_cliente|nome|email|
|----------|----|-----|
|1|Ana Souza|ana@email.com|
|2|Bruno Lima|bruno@email.com|

Tabela `pedidos`

|id_pedido|id_cliente|data|valor|
|---------|----------|----|-----|
|101|1|2026-08-01|150.00|
|102|2|2026-08-02|89.90|

A relação entre `pedidos.id_cliente` e `clientes.id_cliente` garante que todo pedido pertence a um cliente válido.

#### 2.1.2 - Características técnicas

* **Álgebra relacional**: operações como seleção (σ), projeção (π), junção (⋈).
* **Restrições de integridade**: entidade, referencial e de domínio.
* **Normalização**: evita redundância e anomalias de atualização (1FN, 2FN, 3FN, FNBC).
* **ACID**: Atomicidade, Consistência, Isolamento, Durabilidade.

#### 2.1.3 - ALCOA++ e o Banco de Dados Relacional

|Princípio ALCOA++|Recurso em SGBD relacional|
|-----------------|--------------------------|
|Attributable|Colunas de auditoria, autenticação de usuários, roles|
|Legible|Dados tipados, formatação consistente, logs legíveis|
|Contemporaneous|Timestamps automáticos (`DEFAULT CURRENT_TIMESTAMP`)|
|Original|Versionamento, tabelas `historico_*`, triggers de auditoria|
|Accurate|Restrições (`CHECK`, `NOT NULL`, `FOREIGN KEY`)|
|Complete|Logs de transações, auditoria de eventos|
|Consistent|Integridade referencial, transações ACID|
|Enduring|Backups, replicação, storage imutável (WORM)|
|Available|Índices, views, replicação, alta disponibilidade|

Imagine uma tabela de resultados de testes laboratoriais em um banco *PostgreSQL*:

```sql
CREATE TABLE resultados_teste (
    id              SERIAL PRIMARY KEY,
    lote            VARCHAR(20)  NOT NULL,
    parametro       VARCHAR(50)  NOT NULL,
    valor           DECIMAL(10,2) NOT NULL,
    observacao      TEXT,
    criado_por      VARCHAR(50)  NOT NULL,  -- Attributable
    criado_em       TIMESTAMP    DEFAULT CURRENT_TIMESTAMP, -- Contemporaneous
    atualizado_por  VARCHAR(50),
    atualizado_em   TIMESTAMP,
    versao          INTEGER      DEFAULT 1, -- Original
    ativo           BOOLEAN      DEFAULT TRUE -- Legible / Complete (soft delete)
);

-- Tabela de auditoria para todas as alterações
CREATE TABLE resultados_teste_audit (
    id_audit        SERIAL PRIMARY KEY,
    id_registro     INTEGER      NOT NULL,
    operacao        CHAR(1)      NOT NULL, -- 'I', 'U', 'D'
    usuario         VARCHAR(50)  NOT NULL,
    data_operacao   TIMESTAMP    DEFAULT CURRENT_TIMESTAMP,
    valor_anterior  TEXT,
    valor_novo      TEXT
);
```

Nesse exemplo, cada princípio ALCOA++ é atendido:

* **Attributable**: `criado_por`, `atualizado_por`, usuario na auditoria.
* **Legible**: os dados são tipados e a auditoria armazena valores legíveis.
* **Contemporaneous**: timestamps automáticos.
* **Original**: versão e auditoria preservam o histórico.
* **Accurate**: restrições `NOT NULL`, tipos adequados.
* **Complete**: a auditoria registra todas as operações, inclusive `DELETE`.
* **Consistent**: `FOREIGN KEY` e transações ACID.
* **Enduring**: backups e retenção adequados.
* **Available**: tabela de auditoria pode ser consultada por auditores.

### 2.2 - Modelo Chave-Valor (Key-Value)

É o modelo mais simples. Cada item é armazenado como um par chave → valor, onde a chave é única e o valor pode ser qualquer dado (string, JSON, número, binário).

#### 2.2.1 - Analogia: Armário de vestiário

Pense em um armário com gavetas numeradas. A chave é o número da gaveta e o valor é o conteúdo. Para acessar, você precisa saber a chave.

```plaintext
SET usuario:1 "Ana Souza"
GET usuario:1
```

Ou com JSON:

```plaintext
SET sessao:abc123 '{"id":1,"carrinho":[101,102]}'
```

#### 2.2.2 - Casos de uso

* Cache de sessão.
* Carrinhos de compras.
* Fila de mensagens.

#### 2.2.3 - Limitações

* Consultas apenas pela chave.
* Sem relacionamentos nativos.
* Dificuldade para consultas complexas.

### 2.3 - Modelo Documento

Armazena documentos estruturados (geralmente JSON ou BSON). Cada documento é uma unidade autônoma e pode conter estruturas aninhadas.

#### 2.3.1 - Analogia: Fichas de cadastro

Imagine fichas de papel de clientes, onde cada ficha pode conter campos diferentes, com subfichas para endereços ou telefones. Você guarda tudo junto, sem precisar de tabelas separadas. Como nesse exemplo prático com MongoDB.

```json
{
  "_id": 1,
  "nome": "Ana Souza",
  "email": "ana@email.com",
  "enderecos": [
    {"tipo": "casa", "cidade": "SP", "cep": "01000-000"},
    {"tipo": "trabalho", "cidade": "SP", "cep": "02000-000"}
  ],
  "pedidos": [
    {"id": 101, "valor": 150.00},
    {"id": 105, "valor": 230.00}
  ]
}
```

#### 2.3.2 - Casos de uso

* Catálogos de produtos.
* Blogs e sistemas de conteúdo.
* Aplicações que exigem evolução rápida do esquema.

#### 2.3.3 - Vantagens e desvantagens

* **Vantagem**: flexibilidade de esquema, leitura rápida de dados agregados.
* **Desvantagem**: redundância e risco de inconsistência.

### 2.4 - Modelo Colunar (Column-Family)

Os dados são organizados por famílias de colunas, e não por linhas. É otimizado para leitura de muitas colunas de poucas linhas ao mesmo tempo.

#### 2.4.1 -  Analogia: Planilha invertida

Imagine uma planilha onde cada coluna é armazenada separadamente. Para somar todos os valores de uma coluna, você lê apenas essa coluna, não a planilha inteira. Como nesse exemplo usando Cassandra.

```sql
CREATE TABLE vendas (
  produto_id UUID,
  data timestamp,
  quantidade int,
  valor decimal,
  PRIMARY KEY (produto_id, data)
);
```

Os dados de `quantidade` e `valor` são armazenados em estruturas separadas por coluna, otimizando agregações.

#### 2.4.2 - Casos de uso

* Séries temporais (sensores, logs).
* Análise de grandes volumes de dados (OLAP).
* Sistemas de recomendação.

#### 2.4.3 - Vantagens e desvantagens

* **Vantagem**: compressão e leitura rápida de colunas específicas.
* **Desvantagem**: complexidade de modelagem e consultas limitadas.

### 2.5 - Modelo Grafo

Os dados são representados como nós (entidades) e arestas (relacionamentos). Cada nó e aresta pode ter propriedades.

#### 2.5.1 - Analogia: Mapa de amizades

Imagine um mapa de amigos em uma rede social. Cada pessoa é um nó, e a amizade é uma aresta. Você pode navegar de pessoa para pessoa seguindo as arestas. Como nesse exemplo usando Neo4j.

```cypher
CREATE (ana:Cliente {nome: "Ana"})
CREATE (bruno:Cliente {nome: "Bruno"})
CREATE (ana)-[:COMPROU]->(produto:Produto {nome: "Notebook"})
CREATE (bruno)-[:COMPROU]->(produto)
```

Consulta de recomendação:

```cypher
MATCH (a:Cliente)-[:COMPROU]->(p:Produto)<-[:COMPROU]-(b:Cliente)
WHERE a.nome = "Ana"
RETURN b.nome, p.nome
```

#### 2.5.2 - Casos de uso

* Redes sociais.
* Detecção de fraudes.
* Sistemas de recomendação.
* Rotas e logística.

#### 2.5.3 - Vantagens e desvantagens

* **Vantagem**: consultas de relacionamentos complexos de forma eficiente e intuitiva.
* **Desvantagem**: menos maduro para transações financeiras; escala vertical limitada.

### 2.6 - Quando usar cada modelo?

|Situação|Modelo recomendado|
|--------|------------------|
|Transações financeiras, ERP, CRM|Relacional (PostgreSQL, Oracle)|
|Sessões de usuário, cache|Chave-Valor (Redis)|
|Conteúdo flexível, e-commerce|Documento (MongoDB)|
|Análise de dados massivos, IoT|Colunar (Cassandra, BigTable)|
|Recomendação, redes sociais|Grafo (Neo4j)|

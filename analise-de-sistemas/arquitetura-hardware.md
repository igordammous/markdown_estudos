# Arquitetura de Hardware

## Dúvidas

### 1- Bases númericas e codificação de dados:
Temos 4 bases númericas, binário(base 2), Decimal(base 10), Octal(base 8) e Hexadecimal(base 16):
|Binário|Decimal|Octal|HexaDecimal|
|-------|-------|-----|-----------|
|0000   |0      | 0   | 0         |
|0001   |1      | 1   | 1         |
|0010   |2      | 2   | 2         |
|0011   |3      | 3   | 3         |
|0100   |4      | 4   | 4         |
|0101   |5      | 5   | 5         |
|0110   |6      | 6   | 6         |
|0111   |7      | 7   | 7         |
|1000   |8      | -   | 8         |
|1001   |9      | -   | 9         |
|1010   |10     | -   | A         |
|1011   |11     | -   | B         |
|1100   |12     | -   | C         |
|1101   |13     | -   | D         |
|1110   |14     | -   | E         |
|1111   |15     | -   | F         |

#### Base Binária
Base binária principalmente usada em *lógica digital (portas lógicas), circuitos processadores, endereçamento de memória, armazenamento em disco*. Focando na **linguagem de programação da máquina(hardware)**.
* **Representação de Estados**: É a base fundamental porque corresponde diretamente aos dois estados físicos de um transistor: ligado (1) / desligado (0) , ou presença/ausência de tensão elétrica. Tudo o que o computador faz é, em última instância, a manipulação de milhões desses 1s e 0s .

* **Lógica Digital**: Toda a lógica de processamento é construída sobre a álgebra booleana, que opera com valores verdadeiro (1) e falso (0). As portas lógicas (AND, OR, NOT) que formam os circuitos do processador são implementadas para trabalhar exclusivamente com bits.

* **Endereçamento de Memória**: Cada posição na memória RAM tem um endereço único, que é representado e manipulado internamente como um número binário.

* **Armazenamento**: Em um disco rígido ou SSD, a informação é gravada como áreas magneticamente carregadas (norte/sul) ou células de memória que retêm carga, representando os bits 0 e 1.

#### Base Decimal
Base decimal principalmente usada na *exibição de dados para o usuário, cálculos financeiros, programação de alto nível*. Focando na **iteração máquina/usuário**.
* É a base para a qual todas as outras são convertidas para que possamos ler e entender os dados. Quando você vê o número 42 na tela, o hardware o processou em binário, mas o apresentou em decimal para você.

* Linguagens de programação de alto nível (como Python, Java, C) permitem que você escreva números literais em decimal, pois é a forma mais natural para o programador.

* É utilizado em cálculos financeiros e contábeis, onde a precisão exata das casas decimais é exigida por lei (embora o computador armazene esses números internamente de forma binária ou usando formatos especiais como BCD - Binary-Coded Decimal).

#### Base Octal
Base octal era usada antes da invenção da base hexadecimal, então pode-se dizer que uma é evolução da outra.Sistemas PDP-8 e PDP-11 (Digital Equipment Corporation - DEC): Estes foram computadores icônicos que utilizavam a base octal como padrão. Manuais, documentação e até mesmo linguagem assembly para essas máquinas eram escritos em octal. Se você encontrar um livro antigo ou um código legado desses sistemas, verá os números representados em octal. Facilidade de Conversão (Assim como o Hexa): A razão pela qual o octal era usado é a mesma do hexadecimal: a conversão direta com o binário. Como 8 = 2³.

* **Unix e Permissões de Arquivo**: Historicamente, o sistema Unix e seus manuais (man pages) usavam **(e ainda usam)** a base octal para definir as permissões de arquivo. Você provavelmente já viu comandos como `chmod 755 arquivo`. O número 755 é uma representação octal de três conjuntos de permissões (dono, grupo, outros).
* `7` (em octal) = `111` em binário = permissões `rwx` ativadas.

* `5` (em octal) = `101` em binário = permissões `r-x` (leitura e execução ativadas, escrita desativada).

#### Base Hexadecimal
Base hexadecimal principalmente usada em *dumps de memória, endereços de depuração, cores em Web design, endereços MAC, programação Assembly*. Focando em ser **uma Abstração para Humanos Interagirem com o Binário**.
* **Notação Compacta para Binário**: Como um dígito hexadecimal representa exatamente 4 bits (um nibble), ele é usado como uma "taquigrafia" para escrever longas sequências de binários de forma mais legível. Por exemplo, o binário 1111 1010 1100 1110 é muito mais facilmente representado como FACE.

* **Endereços de Memória**: É extremamente comum ver endereços de memória e de dispositivos (em depuradores, dumps de memória) representados em hexadecimal. É muito mais fácil lidar com 0x7FFF do que com 0111111111111111.

* **Códigos de Cores (Web/Design)**: Em páginas da web e design gráfico, as cores são frequentemente definidas pelo sistema RGB (Vermelho, Verde, Azul) usando valores hexadecimais. A cor branca, por exemplo, é ffffff, que significa Vermelho=255, Verde=255, Azul=255 em decimal.

* **Endereços MAC**: Os endereços únicos das placas de rede (MAC Address) são tradicionalmente representados em hexadecimal, como 00:1A:2B:3C:4D:5E.

* **Assembly e Programação de Baixo Nível**: Ao programar próximo ao hardware, é muito comum usar hexadecimal para definir valores de registradores, máscaras de bits e endereços específicos.


### 2- Lógica Digital
#### Operação Lógica
Ela é a base de tudo: é o conjunto de regras e componentes que permitem ao computador tomar decisões e realizar cálculos usando apenas 0s e 1s. Antes do hardware, vem a matemática. A lógica digital é a implementação física da Álgebra de Boole (ou Booleana), onde elas só podem ter dois valores:
* **1 = Verdadeiro(True)**
* **0 = Falso(False)**

E as operações feitas são apenas lógicas, **AND**, **OR** e **NOT**.

|Operação|Nome|Comportamento|
|--------|----|------------|
|AND     | E  |A saída é 1 somente se todas as entradas forem 1.|
|OR      | OU |A saída é 1 se pelo menos uma das entradas for 1.|
|NOT     | NÃO|Inverte o valor da entrada. Se entra 1, sai 0. Se entra 0, sai 1.|

Tabelas Verdades, supondo duas entradas ou no caso da porta NOT, apenas uma:
|Porta|Entrada|Saída|
|-----|-------|-----|
|NOT  | 1     |0    |
|NOT  | 0     |1    |

|Porta|Entrada A|Entrada B|Saída|
|-----|---------|---------|-----|
|AND | 0        |  0      |  0  |
|AND | 0        |  1      |  0  |
|AND | 1        |  0      |  0  |
|AND | 1        |  1      |  1  |
|----|----------|---------|-----|
|OR  | 0        |    0    |  0  |
|OR  | 0        |    1    |  1  |
|OR  | 1        |    0    |  1  |
|OR  | 1        |    1    |  1  |

Observação Importante: Existem também portas combinadas muito usadas, como a **NAND (AND + NOT)** e a **NOR (OR + NOT)**, que são chamadas de "portas universais" porque, com elas, dá pra construir qualquer outro circuito.
#### Combinação Lógica
Combinando portas lógicas, formam-se circuitos lógicos. E ao combinando milhares (ou bilhões) dessas portas simples, criamos circuitos complexos. Dois exemplos clássicos que você verá no Capítulo 3 de Null & Lobur:

* **Meio Somador (Half Adder)**: Um circuito que soma dois bits (0+0, 0+1, 1+0, 1+1). Ele tem duas saídas: a Soma (S) e o Vai-um (Carry - C). Ele é feito com uma porta XOR (OU Exclusivo, uma variação) e uma porta AND.

* **Somador Completo (Full Adder)**: Um circuito mais complexo que soma dois bits considerando também um "vem-um" de uma soma anterior. É assim que o computador soma números de vários bits (como 8, 16 ou 32 bits).

### 3- Porque computadores usam base binária e como seria se usassem outra base, a respeito principal de custos e perfomance. (CURIOSIDADE)
A escolha da base binária não foi acidental, mas sim uma decisão de engenharia baseada em custo, confiabilidade e performance. A resposta curta é: **simplicidade e confiabilidade na implementação física**. Os computadores são construídos com milhões (ou bilhões) de transistores, que funcionam como interruptores. Esses interruptores têm dois estados fundamentaism **1(conduzindo corrente)** e **0(não conduzindo)**.

Se usasse-mos uma base com três estados (ternária), precisaríamos distinguir entre três níveis diferentes de tensão, como 0V, 2.5V e 5V. E o **grande problema** é que a **tensão** em circuitos eletrônicos **não é perfeitamente estável** - ela pode variar com a temperatura, interferências e ruído . Distinguir três níveis com precisão é muito mais difícil e propenso a erros do que distinguir apenas dois.

Um circuito que precisa detectar três estados é significativamente mais complexo e caro de fabricar . Ele exigiria componentes mais precisos e tolerâncias mais apertadas, aumentando os custos de produção . A lógica para operações aritméticas também se torna mais complexa - enquanto um somador binário tem 4 combinações de entrada possíveis (2x2), um ternário teria 9 combinações (3x3).

Baseando-se em um conceito chamado **"economia de base"(radix economy)**, é possivel dizer que matematicamente, o ternário (base 3) é mais eficiente que o binário. Esse conceito que mede a eficiência com que um sistema de numeração representa informações considerando o "custo" dos dígitos.
Para representar um número muito grande, calculamos: base × número de dígitos necessários

|Base|Dígitos para representar 100.000|Cálculo de Economia|Resultado|
|----|--------------------------------|-------------------|---------|
|Base 10| 6 dígitos    | 10 x 6 | 60 |
|Base 2 | 17 dígitos   | 2 x 17 | 34 |
|Base 3 | 11 dígitos   | 3 x 11 | 33 |

Quanto menor o resultado, mais eficiente é a base. O ternário ganha 1. Teoricamente, a base mais eficiente de todas seria o número irracional e (aproximadamente 2,718) e o inteiro mais próximo é o 3.

#### SETUN
Na década de 1950, a União Soviética desenvolveu um computador ternário chamado Setun (Сетунь) . Ele usava um sistema "balanceado" com os valores -1, 0 e +1, representados por tensões negativas, zero e positivas .

Características impressionantes do Setun :

* Era extremamente confiável e estável
* Teve um protótipo que funcionou por 17 anos com apenas 3 substituições de componentes
* Era mais barato que os computadores binários da época (custava 27.500 rublos, menos da metade dos concorrentes)
* Teve 50 unidades produzidas e espalhadas por toda a União Soviética

Por que ele não vingou? Infelizmente, razões políticas e burocráticas :

* O Ministério da Indústria soviético não apoiava o projeto por ser uma iniciativa "não planejada"
* O Setun era tão durável e barato que ameaçava os interesses estabelecidos
* A produção foi deliberadamente limitada e depois cancelada em 1965
* Um sucessor (Setun 70) foi desenvolvido, mas sem apoio oficial, o projeto morreu

#### Conclusão

|Aspecto   |Binário (Base 2) | Ternário (Base 3)|
|----------|-----------------|------------------|
|Estados por dígito | 2 (0 e 1) | 3 (-1, 0, 1 ou 0, 1, 2)|
|Implementação física | Transistores como interruptores (ligado/desligado) | Três níveis de tensão ou corrente |
|Confiabilidade | Alta - fácil distinguir dois estados | Menor - difícil manter precisão dos níveis |
|Complexidade de circuitos | Baixa - lógica simples | Alta - portas lógicas mais complexas |
|Custo de fabricação | Baixo (dominante no mercado) | Alto (exige componentes mais precisos) |
|Eficiência teórica | Boa (34 para 100.000) | Excelente (33 para 100.000) |
|Densidade de informação | n bits representam 2ⁿ valores | n trits representam 3ⁿ valores |
|Existência comercial | Massiva e consolidada | Apenas protótipos (Setun) |

Por fim, apesar da vantagem matemática do ternário, o binário se consolidou por razões práticas:

* **Simplicidade tecnológica**: Na época do desenvolvimento dos primeiros computadores, construir circuitos binários confiáveis já era desafiador. Ternário seria ainda mais difícil .
* **Efeito de rede**: Uma vez que a indústria se estabeleceu em torno do binário, todo o ecossistema - softwares, processadores, memórias, ferramentas de desenvolvimento - foi construído sobre essa base. Mudar exigiria reescrever tudo .
* **Custo-benefício**: Embora o ternário seja teoricamente mais eficiente, a complexidade adicional de implementação supera os ganhos teóricos . Como um especialista comentou: "se o espaço (potência, etc) necessário para implementar uma operação em um dígito de base b é proporcional a b, então ternário é melhor. Mas na prática, a maioria das operações ocupa espaço que aumenta mais do que proporcionalmente a b" .
* **Curiosidade moderna**: Hoje, tecnologias como memórias flash multicélula usam múltiplos níveis de carga para armazenar mais de um bit por célula (4 níveis = 2 bits, 8 níveis = 3 bits), mostrando que em contextos específicos, usamos mais de dois estados.

### 4- O que são registradores e porque são limitados para 64 bits?
#### O que são
Se imaginarmos a CPU como uma mesa de trabalho. Você tem:

* **Memória RAM (HD/SSD)**: Seriam as gavetas e estantes da sala - muito espaço, mas demora para pegar as coisas .
* **Registradores**: São os itens que estão em cima da sua mesa, ao alcance imediato das mãos. São pequenas áreas de armazenamento dentro do próprio processador .

Em termos técnicos: registradores são memórias de altíssima velocidade localizadas no chip da CPU. Eles armazenam temporariamente os dados que estão sendo usados no momento . Quando a CPU precisa fazer um cálculo, os valores envolvidos são transferidos da memória RAM para os registradores.

#### Caracteristicas principais
|Característica|Descrição|
|--------------|---------|
|Velocidade    |Acesso extremamente rápido (muito mais que a RAM)|
|Tamanho       |Extremamente limitado (geralmente alguns bytes por registrador)|
|Localização   |Dentro do próprio processador|
|Função        |Armazenar dados e instruções em uso no momento|

#### Principais tipos
|Registrador (64 bits)|Nome|Função típica|
|---------------------|----|-------------|
|RAX|Acumulador       |Armazenar resultado de operações e valor de retorno de funções|
|RBX|Base             |Ponteiro base para acesso à memória|
|RCX|Contador         |Contador em operações de loop|
|RDX|Dados            |Armazenar dados genéricos|
|RSI|Índice de origem |Ponteiro de origem em operações com strings|
|RDI|Índice de destino|Ponteiro de destino em operações com strings|
|RSP|Ponteiro de pilha|Aponta para o topo da pilha|
|RBP|Ponteiro base    |Aponta para a base da pilha|

|Curiosidade: Em arquitetura 32 bits, os mesmos registradores são chamados de EAX, EBX, ECX, etc. O "E" significa "Extended" e o "R" significa "Register" . É como se fosse o mesmo espaço, mas com nomes diferentes dependendo do tamanho que você quer acessar.|
|--|

#### Por que 64 bits é o limite? (E porque não 128?)
A razão principal para aumentar os bits é poder endereçar mais memória RAM.

* **32 bits**: Pode endereçar até 4 GB de RAM (2³² endereços) . Isso já é insuficiente para qualquer computador moderno.
* **64 bits**: Pode endereçar até 16 exabytes (2⁶⁴ endereços) .

Quanto é 16 exabytes?

* **16 exabytes** = 16 bilhões de gigabytes

É um número tão astronômico que, na prática, os processadores nem implementam tudo. O AMD64, por exemplo, usa 40 bits para endereçamento físico (1 TB) e 48 bits para virtual (256 TB) . Isso já é mais que suficiente para qualquer aplicação atual ou previsível. E baseando-se na lei dos rendimentos decrescentes temos a seguinte tabela.


|Aspecto|64 bits|128 bits (hipotético)|Problema|
|-----|----|----|-----|
|Memória endereçável|16 EB (já exagerado)|340 undecilhões de GB|Desnecessário - não há como fabricar tanta RAM |
|Largura dos barramentos|64 linhas|128 linhas|Mais fios = mais espaço no chip, mais calor, mais consumo |
|Registradores|64 bits|128 bits|Todo dado ocuparia o dobro de espaço, mesmo os pequenos |
|Consumo de energia|Atual|Maior|Mais bits = mais transistores chaveando = mais calor|

### 5- Computador quântico, quais são as suas bases e diferenças com um hardware padrão?

### 6- Em um hardware de 64 bits, o que diferencia dos bits mais significativos para os menos?

### 7- Como uma porta lógica funciona em latches, registradores e memórias cache?

### 8- Qual a diferença entra um microprocessador de uso generalizado para os de uso específico, principalmente os que estão sendo usados na I.A.?

### 9- ASIC, resumo.

### 10- Decodificadores, como funcionam?

### 11- 
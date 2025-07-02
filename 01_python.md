# Python
## Builtin Functions
#### Input
A Função `input()` coleta apenas textos, caso seja necessário, é só converter `int(dado_para_conversão)`, `float(dado_para_conversão)`, `str(dado_para_conversão)`, `bool(dado_para_conversão)`

### Formatação
#### Operador
Esse operador de formatação permite a inserção de variáveis em pontos específicos na string com o `operador %`. Esse operador funciona como um marcador, informando onde o valor da variável vai ser exposto na string.
O `%` precisa ser acompanhado de uma palavra-chave para cada tipo de variável que se deseja adicionar. Seguindo a tabela abaixo:
| Tipo de variável | Palavra-chave |
|------------------|---------------|
| string           |	%s    |
| inteiro	       |    %d    |
| float	           |    %f    |
| caractere	       |    %c    |

#### Format

É um método da classe str. Substitui os marcadores `{}` na string pelos argumentos fornecidos. Oferece mais opções de formatação, como **alinhamento, largura de campo**, etc. Exemplo: 
```python
nome = "Bob"; print("Olá, {}!".format(nome))
```

#### f-strings
Começam com `f` ou `F` antes das aspas. Permitem interpolar expressões diretamente dentro de chaves `{}`. Avaliam as expressões em tempo de execução. Exemplo: 
```python
nome = "Alice"; idade = 30; print(f"Olá, {nome}! Você tem {idade} anos.") 
```

### Manipulação 
* `append()` = Adiciona um elemento ao final da lista.
* `extend()` = Adiciona vários elementos ao final da lista.
* `remove()` = Remove um elemento específico da lista.
Sintaxe > `elemento.append(novo dado)`
Para todos os casos usaremos a lista `raca_caes` a seguir: O primeiro método é o `insert()` que insere o elemento em uma determinada posição da lista.Para isso, seguimos a sintaxe `lista.insert(indice, elemento)`, na qual lista é a lista que vai receber o novo elemento, indice é o índice onde será inserido o novo elemento e elemento é o novo elemento a ser inserido.
```python
raca_caes = ['Labrador Retriever', 'Bulldog Francês', 'Pastor Alemão', 'Poodle']
raca_caes.insert(1, 'Golden Retriever') # 1 é o indice que onde você quer colocar o dado 'Golden Retriever' 
raca_caes
Saída: ['Labrador Retriever', 'Golden Retriever', 'Bulldog Francês', 'Pastor Alemão', 'Poodle']
```
* `pop()` = remove o elemento de uma determinada posição da lista e o retorna como saída na execução do método.   
Nele só precisamos especificar, nos parênteses, qual o *índice do elemento que queremos remover e ele será apagado da lista*. Portanto, vamos remover a raça `'Golden Retriever'` que adicionamos no método anterior.
```python
raca_caes.pop(1)
raca_caes
Saída: ['Labrador Retriever', 'Bulldog Francês', 'Pastor Alemão', 'Poodle']
```
* `index()` = retorna o índice de um elemento específico na lista.  
Para isso, especificamos o elemento entre parênteses. Para identificar o índice da raça `'Pastor Alemão'` na lista, fazemos:
```python
raca_caes.index('Pastor Alemão')
Saída: 2
```
* `sort()` = organiza os elementos da lista em ordem crescente ou decrescente.  
Caso sejam palavras, a ordem é dada por sequência alfabética ou inversa à ela. Para ordenar os valores, podemos apenas declarar o método sort que a lista será organizada em ordem. Para ordenar alfabeticamente a lista `raca_caes` temos o seguinte código:
```python
raca_caes.sort()
raca_caes
Saída: ['Bulldog Francês', 'Labrador Retriever', 'Pastor Alemão', 'Poodle']
```

## Fórmulas matemáticas
* `+, - , *, /` = soma, subtração, multiplicação, divisão
* `**` = potência
* `%` = Módulo
O operador de módulo pode retornar o resto da divisão inteira entre dois números. Lembrando que o resto de uma divisão é o número que sobra quando uma divisão não é exata.
Para calcularmos o módulo de uma divisão, colocamos o dividendo à esquerda no operador `%` e o divisor à direita. Para encontramos o resto da divisão de 7 por 3.
* `\\` = Divisão inteira
Essa operação retorna o resultado da divisão inteira entre dois números, ou seja, retorna apenas a parte inteira de uma divisão. Por exemplo, sabemos que a divisão exata de * * resulta no valor *2.333333….* Caso essa fosse uma divisão inteira, o resultado dela seria apenas **2**. Sua sintaxe consiste em colocar o valor do numerador, o operador `\\` e depois o denominador.

## Tabela de Símbolos
[Simbolos Unicode](https://en.wikipedia.org/wiki/List_of_Unicode_characters#:~:text=U%2B0040-,%40,-64)



## Manipulando dados no python
Usando python, tem como criar no google colab um programa que solicite dois valores numéricos à pessoa usuária tudo na mesma linha? Ou as boas práticas pedem para criar dois input diferentes?
Sim, é possível solicitar dois valores numéricos à pessoa usuária em uma única linha no Google Colab! Você pode usar a função `input()` e, em seguida, dividir a entrada em duas partes.
Aqui está um exemplo:

```python
valores = input("Digite dois números separados por espaço: ")
numero1, numero2 = map(float, valores.split())
```

Nesse código, a função `input()` solicita que a pessoa usuária digite dois números separados por espaço. A função `split()` divide a string em uma lista, e o `map(float, ...)` converte cada um dos valores para o tipo float.
Quanto às boas práticas, não há uma regra rígida que proíba fazer isso em uma única linha, mas é *importante garantir que a interface do usuário seja clara*. Se você optar por solicitar os valores em uma única linha, certifique-se de que as instruções sejam claras para que a pessoa usuária saiba como inserir os dados corretamente.

## Variáveis
Cada célula de código é independente, mas elas compartilham o mesmo ambiente de execução. Isso significa que você pode usar a mesma variável em mais de uma célula de código, e o valor atribuído a essa variável será mantido.
Por exemplo, se você definir uma variável em uma célula e, em seguida, usar essa variável em outra célula, o valor que você atribuiu anteriormente ainda estará disponível.
Aqui está um pequeno exercício para você praticar:
```python
# Se criar uma variável chamada x e atribuir a ela o valor 10.
x = 10
print(x)
# Saída = 10
# Se criar uma nova variável chamada y e atribua a ela o valor de x multiplicado por 2.
y = 2 * x
# Saída = 20.
```
 
## Laços de repetição
### `for():`
Dentro da área de dados, existem diversos exemplos de elementos e conjuntos que você pode utilizar com o laço for. Aqui estão algumas sugestões:
* **Listas**: Uma lista pode conter dados como `nomes` de pessoas, `idades` ou até mesmo `notas`. Por exemplo, você pode ter uma lista de nomes e usar um `for` para imprimir cada `nome`.
```python
nomes = ["Ana", "Bruno", "Carlos"]
for nome in nomes:
    print(nome)
```
* **Dicionários**: Um dicionário é uma estrutura que armazena pares de chave-valor. Você pode iterar sobre as chaves ou os valores. Por exemplo, se você tiver um dicionário com notas de alunos, pode usar um for para acessar cada aluno e sua respectiva nota.
notas = {"Ana": 8.5, "Bruno": 7.0, "Carlos": 9.0}
for aluno, nota in notas.items():
    print(f'{aluno}: {nota}')
2.	**Conjuntos**: Um conjunto é uma coleção de elementos únicos. Você pode usar um for para iterar sobre os elementos de um conjunto e, por exemplo, contar quantos elementos únicos você tem.
numeros = {1, 2, 3, 4, 5}
for numero in numeros:
    print(numero)
3.	**Strings**: Uma string pode ser tratada como uma sequência de caracteres. Você pode usar um for para iterar sobre cada caractere de uma string.
palavra = "Python"
for letra in palavra:
    print(letra)
4.	**DataFrames (com pandas)**: Se você estiver trabalhando com bibliotecas como o pandas, pode iterar sobre as linhas de um DataFrame. Por exemplo, se você tiver um DataFrame com informações de vendas, pode usar um for para calcular a soma das vendas de cada linha.
```python
import pandas as pd

df = pd.DataFrame({
    'Produto': ['A', 'B', 'C'],
    'Vendas': [100, 200, 300]})

for index, row in df.iterrows():
    print(f'Produto: {row["Produto"]}, Vendas: {row["Vendas"]}')
```


## Boas Práticas
* Strings em Letras maiúsculas por convenção do Python, significa que é uma constante e não variável.
* Strings ou objetos que tem um _ antes mostram para quem for mexer no código, que não deve mexer naquele objeto ou string.
* Ao usar o “classmethod” o parâmetro “self” vira “cls”

```python
class Caminhao(Veiculo):
    # fazer apenas dessa maneira -> def __init__(self, cor, placa, numero_rodas, carregado): -> sobreescreve a implementação
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas) # com o método super, ele resgata a implementação
        self.carregado = carregado
```

### Encapsulamento
Para argumento privados, você usa o sinal `‘ – ‘`, e para argumentos públicos o sinal `‘ + ‘`. Serve para colocar proteção em determinados argumentos e funções.
Em Python não existem palavras para definir o nível de acesso, entre público ou privado. Por isso usa-se uma **convenção**.

## Programação Orientada a Objetos
### Classes
Métodos de classe geralmente são usados para criar métodos de fábrica. Métodos de fábrica que retornam instâncias de uma classe. E métodos estáticos para criar funções utilitárias. Exemplo uma função que valida se uma pessoa é maior de idade ou não.
Interfaces definem o que uma classe deve fazer e não como. Exemplo uma lapiseira tem sua funcionalidade, independente da sua cor e tamanho, todas funcionam da mesma maneira. Em Python utiliza-se classes abstratas para criar contatos, que são nada menos do que a interface. Classes abstratas não devem e não podem ser instanciadas. Utiliza-se o módulo fornecido pelo Python e nome dele é **ABC**.`(@abstractmethod)`
**O método abstrato não tem um corpo, apenas define a função. E cada classe filha que instancia a função de sua maneira.**

### Iteradores e Geradores
* O iterador é um objeto que contém um número contável de valores que podem ser iterados. 
Exemplo de uso é ler arquivos grandes, excel ou txt. Usando os métodos `__iter__` e o `__next__`. O `__iter__` devolve o objeto que será iterado e o `__next__` tratará os valores. E lembrar sempre do `“raise StopIteration”`

* E geradores são um tipo de iterador. Eles não armazenam todos os seus valores na memória, portanto usa menos memória. 
Características dos geradores:
* Uso do `“yield”` no lugar do `“return”`
* Uma vez que o item é consumido, não pode ser acessado novamente
* Ela pausa ao declarar `yield` e para retomar, é necessário chamar novamente

*Geradores geralmente são utilizadas com códigos mais simples, onde não precisa criar toda uma classe para fazer o que deseja*.

Para Python e outras linguagens, enquanto estiver trabalhando com a manipulação de arquivos, é importante lembrar de abrir`(open())` e `fechar(close())` os arquivos, para poupar trabalho desnecessário da máquina. Diferentes modos para abrir um arquivo, somente *leitura* (“`r`”), *gravação*(“`w`”) e *anexar*(“`a`”). O método “readline” lê uma linha por vez enquanto o “realinhes” retorna uma lista onde cada elemento é uma linha do arquivo
* `File.open(‘example.txt”, “r”)`
* `Print(file.readline())`
* `File.close()`

### ERROS ao manipular arquivos
* `FileNotFoundError`: Quando o arquivo não pode ser encontrado no diretório especificado;
* `PermissionError`: Quando ocorre uma tentativa de abrir um arquivo sem as permissões par leitura ou gravação
* `IOError`: Quando ocorre um problema geral de entrada e saída, como problemas de permissão, falta de espaço, etc
* `UnicodeDecodeError`: Quando tenta decodificar um arquivo de texto, usando uma decodificação inadequada. E aqui para escrever.
* `UnicodeEncodeError`: Semelhante ao acima, aqui para gravar.
* `IsADirectoryError`: Quando tenta abrir um diretório como se fosse um arquivo de texto.




## ATALHOS VSCODE (à fazer)
Seleciona tudo o que quer
Edição multipla
Shift + Alt + i -> vai para o fim, enquanto seleciona todas as linhas que você quer
Selecionar string
Ctrl + D para cada seleção que você quer

# Estatística

## Variáveis
### Qualitativas(Categóricas)
As variáveis categóricas são um tipo de variável usado em Ciência de Dados para representar dados que podem ser classificados em diferentes categorias ou grupos. Por exemplo, se uma pessoa cientista de dados estiver analisando o desempenho acadêmico de estudantes em uma escola, ela pode usar variáveis categóricas para classificar o desempenho dessas pessoas em diferentes grupos, como *"excelente", "bom" ou "regular"*. Isso permite identificar padrões ou tendências no desempenho.
#### 1. Ordinais
Possuem uma ordem específica entre as categorias. Por exemplo, se a pessoa cientista de dados estiver analisando a escolaridade de um grupo de pessoas, ela pode usar esse tipo de variável para classificar as pessoas em diferentes grupos, como: **"ensino fundamental completo"**, **"ensino médio completo"** ou **"ensino superior completo"** e assim por diante.

#### 2. Nominais
São aquelas que não possuem uma ordem ou hierarquia específica entre as categorias. Por exemplo, se uma pessoa cientista de dados estiver analisando a preferência musical de um grupo de pessoas, ela pode usar variáveis categóricas nominais para classificar as pessoas em diferentes grupos, como: **"rock"**, **"jazz"** ou **"pop"**.

#### 3. Binárias
São um tipo especial de variável categórica nominal que possui apenas duas categorias possíveis, por exemplo: **sim/não**, **verdadeiro/falso** ou **presente/ausente**. As variáveis categóricas binárias são úteis porque permitem que cientistas de dados analisem a distribuição de dados em apenas duas categorias possíveis.


### Quantitativas
São as características que podem ser medidas em uma escala **quantitativa**, ou seja, apresentam valores numéricos que fazem sentido. Podem ser contínuas ou discretas.

Por exemplo, a variável `idade`, medida em anos completos, é **quantitativa** (contínua); mas, se for informada apenas a `faixa etária` (0 a 5 anos, 6 a 10 anos, etc...), é **qualitativa** (ordinal). Outro exemplo é o `peso` dos lutadores de boxe, uma variável **quantitativa** (contínua) se trabalhamos com o valor obtido na balança, mas **qualitativa** (ordinal) se o classificarmos nas `categorias` do boxe (peso-pena, peso-leve, peso-pesado, etc.).

Outro ponto importante é que nem sempre uma variável representada por números é quantitativa. O número do `telefone` de uma pessoa, o `número da casa`, o número de sua `identidade`. Às vezes o `sexo` do indivíduo é registrado na planilha de dados como *1 se macho e 2 se fêmea*, por exemplo. Isto não significa que a variável sexo passou a ser **quantitativa**!

## Probabilidade
### valor-p
p < 0,05 é um critério estatístico frequentemente usado em pesquisas científicas para determinar significância estatística. Vamos explicar o que isso significa:

**O que é o valor-p (p-value)?**
O valor-p é uma probabilidade que indica quão compatíveis os dados coletados são com a hipótese nula (geralmente, a hipótese de que não há efeito ou não há diferença).

*Valores de p variam de 0 a 1.*

**Interpretação de p < 0,05:**
Se p < 0,05, significa que há menos de 5% de chance de que os resultados observados ocorram se a hipótese nula for verdadeira.

Em outras palavras, se p < 0,05, os resultados são considerados estatisticamente significativos, e os pesquisadores costumam rejeitar a hipótese nula, aceitando que há um efeito ou diferença real.

**Exemplo:**
Situação: Um estudo testa se um novo remédio é mais eficaz que um placebo.

Resultado: Encontra-se p = 0,03.

Interpretação: Há apenas 3% de probabilidade de que a diferença observada seja devido ao acaso. Portanto, conclui-se que o remédio realmente funciona melhor.

**Cuidados:**
Não prova causalidade: Um p < 0,05 não significa que o efeito seja grande ou importante, apenas que é improvável que seja devido ao acaso.

Não é uma "verdade absoluta": Algumas áreas da ciência estão questionando o uso rígido do p < 0,05, sugerindo análises mais rigorosas (como intervalos de confiança ou tamanho do efeito).

*P-hacking*: Alguns pesquisadores podem manipular testes para obter p < 0,05, então é importante avaliar o contexto do estudo.

**Resumo:**
* p < 0,05 → Resultado estatisticamente significativo (baixa probabilidade de ser devido ao acaso).

* p ≥ 0,05 → Resultado não significativo (não há evidência suficiente para rejeitar a hipótese nula).

**1. Valor-p (p-value)**
**O que é?**
O valor-p é a probabilidade de obter um resultado pelo menos tão extremo quanto o observado no estudo, assumindo que a hipótese nula (H₀) é verdadeira.

**Exemplo:** Se p = 0,03, há 3% de chance de que a diferença observada (ou maior) ocorra se não houver efeito real (ou seja, se H₀ for verdadeira).

Decisão:

Se p < 0,05, rejeita-se H₀ (resultado estatisticamente significativo).

Se p ≥ 0,05, não se rejeita H₀ (resultado não significativo).

#### Intervalo de confiança
**O que é?**
Quando você diz que o intervalo de confiança (IC) é de 95, significa que há 95% de chance do parâmetro que estou procurando estar dentro do intervalo dos dados.

#### Com desvio padrão populacional conhecido

## $\mu = \bar{x} \pm z\frac{\sigma}{\sqrt{n}}$

#### Com desvio padrão populacional desconhecido

## $\mu = \bar{x} \pm z\frac{s}{\sqrt{n}}$
Onde:

$\mu = parâmetro populacional (média)

$\bar{x}$ = média da amostragem

$z \frac{\sigma}{\sqrt{n}}$ = erro inferencial

&plusmn; = Tanto mais quanto menos porque irá encontrar o intervalo superior e o inferior

### Valores de $z$ para os níveis de confiança mais utilizados

|Nível de<br>confiança|Valor da área sob<br>a curva normal| $z$ |
|:----------------:|:---------------------------------:|:---:|
|90%               |0,95                               |1,645|
|95%               |0,975                              |1,96 |
|99%               |0,995                              |2,575|

**Comparação Direta**
|Critério                | Valor-p (p-value)                                           | Intervalo de Confiança 95% (IC 95%)               |
|------------------------|-------------------------------------------------------------|---------------------------------------------------|
|O que mede?             | Probabilidade de obter dados extremos se H₀ for verdadeira. | Faixa de valores plausíveis para o parâmetro real.|
|Limiar de significância | p < 0,05 → Significativo.                                   | IC 95% não inclui o valor nulo → Significativo.   |
|Vantagem                | Simples para testes de hipóteses.                           |Mostra a magnitude e precisão do efeito.           |
|Exemplo                 | p = 0,03 → Significativo.                                   | IC 95% = [2, 8] (não inclui 0) → Significativo.   |


## Distribuições de Probabilidade 

#### Distribuição Binomial

## $P(k)=\binom{n}{k} p^k q^{n-k}$
Onde:
$p$ = probabilidade de sucesso
$q = (1 - p)$ = probabilidade de fracasso
$n$ = número de eventos estudados
$k$ = número de eventos desejados que tenham sucesso

**Média da Distribuição Binomial**
O valor esperado ou a média da distribuição binomial é igual ao número de experimentos realizados multiplicado pela chance de ocorrência do evento.
## $\mu = n \times p$

**Desvio Padrão da Distribuição Binomial**
O desvio padrão é o produto entre o número de experimentos, a probabilidade de sucesso e a probabilidade de fracasso.
## $\sigma = \sqrt{n \times p \times q}$

**Combinações**
Número de combinações de  n  objetos, tomados  k  a cada vez, é:
## $C_{k}^{n} = \binom{n}{k} = \frac{n!}{k!(n - k)!}$
Onde
## $n! = n\times(n-1)\times(n-2)\times...\times(2)\times(1)$
## $k! = k\times(k-1)\times(k-2)\times...\times(2)\times(1)$
Por definição
## $0! = 1$
*Exemplo: Mega Sena*
Em um volante de loteria da Mega Sena temos um total de **60 números** para escolher onde a aposta mínima é de **seis números**. Você que é curiosa(o) resolve calcular a probabilidade de se acertar na Mega Sena com apenas **um jogo**. Para isso precisamos saber quantas **combinações de seis números podem ser formadas com os 60 números disponíveis**.

### $C_{6}^{60} = \binom{60}{6} = \frac{60!}{6!(60 - 6)!}$

```python
from scipy.special import comb
combinacoes = comb(60, 6)
probabilidade = 1 / combinacoes
print("%0.15f" % probabilidade)
```

`Saída = 0.000000019974489`


#### Distribuição de Poisson
É empregada para descrever o número de ocorrências em um intervalo de tempo ou espaço específico. Os eventos são caracterizados pela possibilidade de contagem dos sucessos, mas a não possibilidade de contagem dos fracassos.
## $P(k) = \frac{e^{-\mu}(\mu)^k}{k!}$
Onde:
$e$ = constante cujo valor aproximado é 2,718281828459045
$\mu$ = representa o número médio de ocorrências em um determinado intervalo de tempo ou espaço
$k$ = número de sucessos no intervalo desejado


#### Distribuição Normal
A distribuição normal é uma das mais utilizadas em estatística. É uma distribuição contínua, onde a distribuição de frequências de uma variável quantitativa apresenta a forma de sino e é simétrica em relação a sua média.
**Características Importantes**
1. É simétrica em torno da média;
2. A área sob a curva corresponde à proporção 1 ou 100%;
3. As medidas de tendência central (média, mediana e moda) apresentam o mesmo valor;
4. Os extremos da curva tendem ao infinito em ambas as direções e, teoricamente, jamais tocam o eixo $x$;
5. O desvio padrão define o achatamento e largura da distribuição. Curvas mais largas e mais achatadas apresentam valores maiores de desvio padrão;
6. A distribuição é definida por sua média e desvio padrão;
7. A probabilidade sempre será igual à área sob a curva, delimitada pelos limites inferior e superior.
# $f(x) = \frac{1}{\sqrt{2\pi\sigma}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$
Onde:
$x$ = variável normal
$\sigma$ = desvio padrão
$\mu$ = média
<img src="https://help.highbond.com/helpdocs/analytics/141/user-guide/pt-br/Content/images/an/outliers_1.png" alt="Gráfico de Sino, com limites" />

## $P(L_i<x<L_s) = \int_{L_i}^{L_s}\frac{1}{\sqrt{2\pi\sigma}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$

Onde:
$x$ = variável normal
$\sigma$ = desvio padrão
$\mu$ = média
$L_i$ = limite inferior
$L_s$ = limite superior

Normalmente são usadas tabelas que já foram padronizadas, basta transformar a variável em Z, com a seguinte fórmula:
## $Z = \frac{x-\mu}{\sigma}$
Onde:
$x$ = variável normal com média $\mu$ e desvio padrão $\sigma$
$\sigma$ = desvio padrão
$\mu$ = média

**Código para tabela normal padronizada**
```python
import pandas as pd
import numpy as np
from scipy.stats import norm

tabela_normal_padronizada = pd.DataFrame(
    [],
    index=["{0:0.2f}".format(i / 100) for i in range(0, 400, 10)],
    columns = ["{0:0.2f}".format(i / 100) for i in range(0, 10)])

for index in tabela_normal_padronizada.index:
    for column in tabela_normal_padronizada.columns:
        Z = np.round(float(index) + float(column), 2)
        tabela_normal_padronizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(Z))

tabela_normal_padronizada.rename_axis('Z', axis = 'columns', inplace = True)

tabela_normal_padronizada
```

<img src="https://caelum-online-public.s3.amazonaws.com/1178-estatistica-parte2/01/img003.png" alt="Tabela de área ou probabilidade" />

A tabela acima fornece a área sob a curva entre $-\infty$ e $Z$ desvios padrão acima da média. Lembrando que por se tratar de valores padronizados temos $\mu = 0$.


### Biblioteca *NORM* do [*scipy.stats*](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html)

|Methods                                                     |Results|
|------------------------------------------------------------|-------|
|rvs(loc=0, scale=1, size=1, random_state=None)              |Random variates.|
|pdf(x, loc=0, scale=1)                                      |Probability density function.|
|logpdf(x, loc=0, scale=1)                                   |Log of the probability density function.|
|cdf(x, loc=0, scale=1)                                      |Cumulative distribution function.|
|logcdf(x, loc=0, scale=1)                                   |Log of the cumulative distribution function.|
|sf(x, loc=0, scale=1)                                       |Survival function (also defined as 1 - cdf, but sf is sometimes more accurate).|
|logsf(x, loc=0, scale=1)                                    |Log of the survival function.|
|ppf(q, loc=0, scale=1)                                      |Percent point function (inverse of cdf — percentiles).|
|isf(q, loc=0, scale=1)                                      |Inverse survival function (inverse of sf).|
|moment(order, loc=0, scale=1)                               |Non-central moment of the specified order.|
|stats(loc=0, scale=1, moments=’mv’)                         |Mean(‘m’), variance(‘v’), skew(‘s’), and/or kurtosis(‘k’).|
|entropy(loc=0, scale=1)                                     |(Differential) entropy of the RV.|
|fit(data)                                                   |Parameter estimates for generic data. See scipy.stats.rv_continuous.fit for detailed documentation of the keyword arguments.|
|expect(func, args=(), loc=0, scale=1, lb=None, ub=None, conditional=False, **kwds)| Expected value of a function (of one argument) with respect to the distribution.|
|median(loc=0, scale=1)                                      |Median of the distribution.|
|mean(loc=0, scale=1)                                        |Mean of the distribution.|
|var(loc=0, scale=1)                                         |Variance of the distribution.|
|std(loc=0, scale=1)                                         |Standard deviation of the distribution.|
|interval(confidence, loc=0, scale=1)                        |Confidence interval with equal areas around the median.|


## Amostra e População
**População**
Conjunto de todos os elementos de interesse em um estudo. Diversos elementos podem compor uma população, por exemplo: pessoas, idades, alturas, carros etc.
Com relação ao tamanho, as populações podem ser limitadas (populações finitas) ou ilimitadas (populações infinitas).

**Populações finitas**
Permitem a contagem de seus elementos. Como exemplos temos o número de funcionário de uma empresa, a quantidade de alunos em uma escola etc.

**Populações infinitas**
Não é possível contar seus elementos. Como exemplos temos a quantidade de porções que se pode extrair da água do mar para uma análise, temperatura medida em cada ponto de um território etc.
Quando os elementos de uma população puderem ser contados, porém apresentando uma quantidade muito grande, assume-se a população como infinita..

**Amostra**
Subconjunto representativo da população.
Os atributos numéricos de uma população como sua média, variância e desvio padrão, são conhecidos como parâmetros. O principal foco da inferência estatística é justamente gerar estimativas e testar hipóteses sobre os parâmetros populacionais utilizando as informações de amostras.


#### *Quando utilizar amostras e tipos*
*Populações infinitas*
O estudo não chegaria nunca ao fim. Não é possível investigar todos os elementos da população.

*Testes destrutivos*
Estudos onde os elementos avaliados são totalmente consumidos ou destruídos. Exemplo: testes de vida útil, testes de segurança contra colisões em automóveis.

*Resultados rápidos*
Pesquisas que precisam de mais agilidade na divulgação. Exemplo: pesquisas de opinião, pesquisas que envolvam problemas de saúde pública.

*Custos elevados*
Quando a população é finita mas muito numerosa, o custo de um censo pode tornar o processo inviável.

***Amostragem Aleatória Simples, Amostragem Estratificada e Amostragem por Conglomerados***


### Estimação
É a forma de se fazer suposições generalizadas sobre os parâmetros de uma população tendo como base as informações de uma amostra.

- **Parâmetros** são os atributos numéricos de uma população, tal como a média, desvio padrão etc.

- **Estimativa** é o valor obtido para determinado parâmetro a partir dos dados de uma amostra da população.


#### Teorema do Limite Central 
O Teorema do Limite Central afirma que, com o aumento do tamanho da amostra, a distribuição das médias amostrais se aproxima de uma distribuição normal com média igual à média da população e desvio padrão igual ao desvio padrão da variável original dividido pela raiz quadrada do tamanho da amostra. Este fato é assegurado para  n  maior ou igual a 30.

# $\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$

O desvio padrão das médias amostrais é conhecido como **erro padrão da média**


### Nível de Confiança e Nível de Significância
O **nível de confiança** ($1 - \alpha$) representa a probabilidade de acerto da estimativa. De forma complementar o **nível de significância** ($\alpha$) expressa a probabilidade de erro da estimativa.

O **nível de confiança** representa o grau de confiabilidade do resultado da estimativa estar dentro de determinado intervalo. Quando fixamos em uma pesquisa um **nível de confiança** de 95%, por exemplo, estamos assumindo que existe uma probabilidade de 95% dos resultados da pesquisa representarem bem a realidade, ou seja, estarem corretos.

O **nível de confiança** de uma estimativa pode ser obtido a partir da área sob a curva normal como ilustrado na figura abaixo.
<img src="https://caelum-online-public.s3.amazonaws.com/1178-estatistica-parte2/01/img007.png" alt="Nível de Confiança e Nível de Significância" />

#### Erro Inferencial
O **erro inferencial** é definido pelo **desvio padrão das médias amostrais** $\sigma_{\bar{x}}$ e pelo **nível de confiança** determinado para o processo. Ele é necessário pois ao usar amostras ao invês da população, tem que ser considerado um erro.

# $e = z \frac{\sigma}{\sqrt{n}}$

Quando o problema informa um *"erro máximo aceitável"* como um percentual e estamos lidando com uma **variável quantitativa** (como gastos, renda, altura, peso, etc.), esse erro percentual é geralmente interpretado em relação à média da variável em estudo. Pense da seguinte maneira: o intervalo de confiança que construímos para a média populacional é dado por ($\bar{x} - e) e ($$\bar{x} + e$). O $e$$e$ aqui é o erro inferencial ou margem de erro, que é um valor na mesma unidade da variável que estamos medindo (no caso, Reais).

Se o erro máximo aceitável é de 10%, isso significa que queremos que a margem de erro ($e$$e$) seja no máximo 10% do valor da média que estamos tentando estimar ($\mu$, que estimamos com $\bar{x}$).

Portanto, se o erro percentual é de 10% (ou 0.10) e a média da amostra ($\bar{x}$) é R\$ 45,50, o erro máximo aceitável em termos absolutos (R\$ 45,50), o erro máximo aceitável em termos absolutos ($e$) é calculado como:
$e = \text{Média} \times \text{Erro Percentual}$$ -> $$e = 45,50 \times 0.10$$ -> $$e = 4,55$$


### Cálculo do Tamanho da Amostra
É derivada do erro inferencial
#### Cálculo para população infinita
##### Com desvio padrão conhecido

## $n = \left(z\frac{\sigma}{e}\right)^2$

##### Com desvio padrão desconhecido

## $n = \left(z\frac{s}{e}\right)^2$

Onde:
$z$ = variável normal padronizada
$\sigma$ = desvio padrão populacional
$s$ = desvio padrão amostral
$e$ = erro inferencial

#### <font color='red'>Observações</font>

1. O desvio padrão ($\sigma$ ou $s$) e o erro ($e$) devem estar na mesma unidade de medida.
2. Quando o erro ($e$) for representado em termos percentuais, deve ser interpretado como um percentual relacionado à média.

#### Cálculo para população finita
Com uma população conhecida é necessário relativizar o tamanho da amostra com o tamanho da população.
##### Com desvio padrão conhecido

## $n = \frac{z^2 \sigma^2 N}{z^2 \sigma^2 + e^2(N-1)}$

##### Com desvio padrão desconhecido

## $n = \frac{z^2 s^2 N}{z^2 s^2 + e^2(N-1)}$
Onde:
$N$ = tamanho da população
$z$ = variável normal padronizada
$\sigma$ = desvio padrão populacional
$s$ = desvio padrão amostral
$e$ = erro inferencial 
# Desenvolvimento Web

## Índice

1. [Internet, Web e HTML](#1-internet-web-e-html)
   1.1 [Internet e World Wide Web](#11-internet-e-world-wide-web)
   1.2 [O que é HTML?](#12-o-que-é-html)
   1.3 [Estrutura básica de um documento](#13-estrutura-básica-de-um-documento)
2. [Elementos, tags e atributos](#2-elementos-tags-e-atributos)
   2.1 [Elementos de texto](#21-elementos-de-texto)
3. [Listas](#3-listas)
   3.1 [Listas ordenadas e não ordenadas](#31-listas-ordenadas-e-não-ordenadas)
   3.2 [Listas de definição](#32-listas-de-definição)
4. [Imagens](#4-imagens)
5. [Links e navegação](#5-links-e-navegação)
6. [Tabelas](#6-tabelas)
   6.1 [Colspan e rowspan](#61-colspan-e-rowspan)
7. [Formulários](#7-formulários)
   7.1 [Form, action e method](#71-form-action-e-method)
   7.2 [Campos de entrada](#72-campos-de-entrada)
   7.3 [Seleção, agrupamento e botões](#73-seleção-agrupamento-e-botões)
   7.4 [Atributos de formulários](#74-atributos-de-formulários)
8. [Elementos semânticos](#8-elementos-semânticos)
9. [Boas práticas e revisão](#9-boas-práticas-e-revisão)
10. [CSS: especificidade](#10-css-especificidade)
    10.1 [Hierarquia e cálculo](#101-hierarquia-e-cálculo)
    10.2 [Regra !important](#102-regra-important)
11. [Box Model e Flexbox](#11-box-model-e-flexbox)
    11.1 [As quatro partes do Box Model](#111-as-quatro-partes-do-box-model)
    11.2 [Flexbox e seus eixos](#112-flexbox-e-seus-eixos)
    11.3 [Propriedades do Flexbox](#113-propriedades-do-flexbox)
12. [Pseudoclasses em CSS](#12-pseudoclasses-em-css)
    12.1 [Estados de interação](#121-estados-de-interação)
    12.2 [Pseudoclasses posicionais](#122-pseudoclasses-posicionais)
    12.3 [Pseudoclasses de formulários](#123-pseudoclasses-de-formulários)
13. [Media Queries e responsividade](#13-media-queries-e-responsividade)
    13.1 [Sintaxe e condições](#131-sintaxe-e-condições)
    13.2 [Exemplos práticos](#132-exemplos-práticos)
14. [Referências](#14-referências)

---

## 1. Internet, Web e HTML

### 1.1 Internet e World Wide Web

A **Internet** é a infraestrutura de redes que permite a comunicação entre dispositivos. A **World Wide Web (WWW ou Web)** é um dos serviços que utiliza essa infraestrutura para disponibilizar e consultar documentos e recursos interligados.

Internet e Web não são sinônimos: a Internet pode existir sem a Web, mas a Web depende da infraestrutura da Internet para funcionar.

A Web é uma iniciativa de recuperação de informações hipermídia que busca oferecer acesso universal a um grande conjunto de documentos. Esses documentos podem conter textos, hipertextos, imagens, sons e vídeos. O acesso normalmente é feito por meio de um **navegador web**, como Google Chrome, Mozilla Firefox ou outros.

### 1.2 O que é HTML?

**HTML** significa *HyperText Markup Language* (Linguagem de Marcação de Hipertexto). É a linguagem de marcação utilizada para publicar conteúdo na Web e definir o significado e a estrutura desse conteúdo.

- **HTML:** organiza e estrutura o conteúdo.
- **CSS:** descreve a apresentação visual, como cores, fontes, espaçamentos e posicionamento.
- **JavaScript:** acrescenta comportamento e interatividade à página.

O termo *hipertexto* está relacionado aos links que conectam páginas dentro de um mesmo site ou entre sites diferentes. Os links são uma parte fundamental da Web.

### 1.3 Estrutura básica de um documento

Um documento HTML é composto por elementos identificados por tags. A estrutura mínima de uma página pode ser representada assim:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha primeira página</title>
</head>
<body>
    <h1>Olá, mundo!</h1>
    <p>Minha primeira página HTML.</p>
</body>
</html>
```

- `<!DOCTYPE html>` informa ao navegador que o documento utiliza HTML5.
- `<html>` é o elemento raiz da página; o atributo lang informa o idioma.
- `<head>` contém metadados e informações que não são o conteúdo principal exibido.
- `<meta charset="UTF-8">` define a codificação de caracteres.
- `<title>` define o título mostrado na aba do navegador.
- `<body>` contém o conteúdo apresentado ao usuário

## 2. Elementos, tags e atributos

HTML utiliza marcação para indicar ao navegador como interpretar textos, imagens e outros conteúdos. Um elemento geralmente é formado por uma tag de abertura, conteúdo e tag de fechamento.

```html
<p>Este é o conteúdo de um parágrafo.</p>
```

Em geral, tags são escritas entre os sinais `<` e `>`. Os nomes dos elementos não diferenciam letras maiúsculas de minúsculas, mas recomenda-se utilizar letras minúsculas.

Alguns elementos, como `<img>` e `<br>`, não possuem tag de fechamento. São elementos vazios.

**Atributos** fornecem informações adicionais ao elemento e são escritos na tag de abertura, normalmente no formato nome="valor".

```html
<p class="destaque" id="aviso">Texto destacado</p>
```

### 2.1 Elementos de texto

|Elemento|Finalidade|
|--------|----------|
|`<h1>` até `<h6>`|Títulos e subtítulos, do nível mais importante ao menos importante.|
|`<p>`|Parágrafo.|
|`<strong>`|Indica importância forte.|
|`<em>`|Indica ênfase.|
|`<br>`|Quebra de linha.|
|`<div>`|Contêiner genérico em bloco, sem significado semântico próprio.|
|`<span>`|Contêiner genérico em linha, sem significado semântico próprio.|

## 3. Listas

As listas organizam informações relacionadas. Os materiais apresentam três tipos principais: listas ordenadas (`<ol>`), não ordenadas (`<ul>`) e de definição (`<dl>`).

### 3.1 Listas ordenadas e não ordenadas

Lista ordenada: utiliza `<ol>` e apresenta itens em uma sequência numerada ou ordenada.

```html
<ol>
    <li>Planejar a página</li>
    <li>Criar o HTML</li>
    <li>Testar no navegador</li>
</ol>
```

Lista não ordenada: utiliza `<ul>` e apresenta itens sem estabelecer uma ordem numérica.

```html
<ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
</ul>
```

Em ambos os casos, cada item é definido pelo elemento `<li>`. Listas também podem ser aninhadas dentro de outros itens.

### 3.2 Listas de definição

O elemento `<dl>` representa uma lista de descrições. Cada termo é indicado por `<dt>` e sua descrição por `<dd>`.

```html
<dl>
    <dt>HTML</dt>
    <dd>Linguagem de marcação para estruturar conteúdo.</dd>
    <dt>CSS</dt>
    <dd>Linguagem utilizada para definir a apresentação visual.</dd>
</dl>
```

## 4. Imagens

O elemento `<img>` incorpora uma imagem à página. Ele utiliza atributos para indicar o arquivo e fornecer uma descrição textual.

```html
<img src="paisagem.webp"
     alt="Árvore"
     width="896"
     height="675">
```

- **src**: caminho ou endereço do arquivo de imagem.
- **alt**: texto alternativo que descreve a imagem; é importante para acessibilidade e também pode ser exibido quando a imagem não carrega.
- **width**: largura da imagem.
- **height**: altura da imagem, quando definida.

O caminho de src pode ser relativo ao arquivo HTML ou um endereço absoluto. Ao organizar o projeto, mantenha os arquivos de imagem em uma pasta, por exemplo, imagens/.

```html
<!-- Imagem em uma subpasta do projeto -->
<img src="imagens/logo.png" alt="Logotipo da empresa" width="180">
```

## 5. Links e navegação

O elemento `<a>` cria um hiperlink. O atributo href informa o destino do link.

```html
<a href="https://www.google.com">Acessar o Google</a>
```

Os links podem apontar para páginas externas, arquivos do próprio projeto, endereços de e-mail ou partes específicas da mesma página.

```html
<!-- Página externa -->
<a href="https://www.w3.org/">W3C</a>

<!-- Outra página do projeto -->
<a href="contato.html">Contato</a>

<!-- Seção da própria página -->
<a href="#referencias">Ir para referências</a>

<!-- E-mail -->
<a href="mailto:contato@exemplo.com">Enviar e-mail</a>
```

Para abrir um destino em outra aba, pode-se utilizar `target="_blank"`. Recomenda-se combiná-lo com `rel="noopener noreferrer"`.

```html
<a href="https://www.google.com"
   target="_blank"
   rel="noopener noreferrer">
   Abrir em nova aba
</a>
```

Uma imagem também pode funcionar como link, colocando o elemento `<img>` dentro de `<a>`, como no exemplo apresentado na aula:

```html
<a href="https://www.google.com">
    <img src="imagens/google.png"
         alt="Acessar o Google"
         width="200">
</a>
```

## 6. Tabelas

Tabelas são utilizadas para apresentar dados organizados em linhas e colunas. O elemento `<table>` cria a tabela; `<tr>` define uma linha; `<th>` define uma célula de cabeçalho; e `<td>` define uma célula de dados.

```html
<table>
    <caption>Alunos cadastrados</caption>
    <thead>
        <tr>
            <th>Matrícula</th>
            <th>Nome</th>
            <th>Curso</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>001</td>
            <td>Ana</td>
            <td>ADS</td>
        </tr>
        <tr>
            <td>002</td>
            <td>Bruno</td>
            <td>ADS</td>
        </tr>
    </tbody>
</table>
```

- `<caption>`: título ou legenda da tabela.
- `<thead>`: agrupa as linhas de cabeçalho.
- `<tbody>`: agrupa o conteúdo principal.
- `<tfoot>`: pode agrupar linhas de resumo ou rodapé.

### 6.1 Colspan e rowspan

Os atributos `colspan` e `rowspan` permitem que uma célula ocupe mais de uma coluna ou linha, respectivamente.

```html
<table border="1">
    <tr>
        <th colspan="2">Cadastro</th>
    </tr>
    <tr>
        <td rowspan="2">Aluno</td>
        <td>Nome: Ana</td>
    </tr>
    <tr>
        <td>Curso: ADS</td>
    </tr>
</table>
```

`colspan="2"` faz a célula ocupar duas colunas. `rowspan="2"` faz a célula ocupar duas linhas. Em páginas atuais, a aparência das bordas e demais estilos deve ser definida preferencialmente com CSS.

## 7. Formulários

Formulários permitem coletar informações fornecidas pelo usuário. O elemento `<form>` envolve campos de texto, caixas de seleção, botões de opção, listas, botões de envio e outros controles.

### 7.1 Form, action e method

```html
<form action="/processar-cadastro" method="post">
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome">

    <button type="submit">Enviar</button>
</form>
```

- **action**: define o destino que processará os dados quando o formulário for enviado.
- **method**: define o método HTTP utilizado para enviar os dados, normalmente GET ou POST.
- **name**: identifica o campo no conjunto de dados enviado. Um campo sem name normalmente não é enviado.

|Método|Comportamento|Uso indicado|
|------|-------------|------------|
|GET|Os dados são enviados na URL e ficam visíveis no endereço.|Consultas e dados não sensíveis, geralmente em pequenas quantidades.|
|POST|Os dados são enviados no corpo da requisição, não na URL.|Envio de dados pessoais, formulários de cadastro e maiores quantidades de dados.|

> **Importante**: POST não criptografa os dados por si só. Para proteger informações durante a transmissão, é necessário utilizar HTTPS e implementar os controles de segurança adequados no servidor.

O atributo for do elemento `<label>` deve ter o mesmo valor do atributo id do campo correspondente. Isso associa a legenda ao controle e facilita sua utilização.

### 7.2 Campos de entrada

O elemento `<input>` possui diferentes tipos, definidos pelo atributo type.

|Tipo|Finalidade|Exemplo|
|----|----------|-------|
|text|Entrada de texto simples.|`<input type="text">`|
|password|Entrada de senha, ocultando visualmente os caracteres.|`<input type="password">`|
|email|Entrada de endereço de e-mail com validação básica do formato.|`<input type="email">`|
|number|Entrada numérica.|`<input type="number">`|
|date|Seleção de data.|`<input type="date">`|
|datetime-local|Data e hora locais.|`<input type="datetime-local">`|
|time|Seleção de horário.|`<input type="time">`|
|month|Seleção de mês e ano.|`<input type="month">`|
|color|Seleção de cor.|`<input type="color">`|
|file|Seleção de arquivo.|`<input type="file">`|
|radio|Seleção de uma opção em um grupo.|`<input type="radio">`|
|checkbox|Seleção de uma ou mais opções.|`<input type="checkbox">`|
|textarea|Para textos com várias linhas|`<input type="textarea">`|

```html
<label for="mensagem">Mensagem:</label>
<textarea id="mensagem" name="mensagem" rows="4" cols="40"></textarea>
```

### 7.3 Seleção, agrupamento e botões

- **Radio button**: permite escolher uma opção dentro de um grupo. Para que as opções sejam mutuamente exclusivas, elas devem compartilhar o mesmo atributo name.

```html
<input type="radio" id="manha" name="periodo" value="manha">
<label for="manha">Manhã</label>

<input type="radio" id="noite" name="periodo" value="noite">
<label for="noite">Noite</label>
```

- **Checkbox**: permite marcar nenhuma, uma ou várias opções.

```html
<input type="checkbox" id="html" name="tecnologias" value="HTML">
<label for="html">HTML</label>

<input type="checkbox" id="css" name="tecnologias" value="CSS">
<label for="css">CSS</label>
```

- **Select, option e optgroup**: criam uma lista suspensa de opções, que podem ser agrupadas por categorias.

```html
<label for="curso">Curso:</label>
<select id="curso" name="curso">
    <option value="">Selecione</option>
    <optgroup label="Tecnologia">
        <option value="ads" selected>Análise e Desenvolvimento de Sistemas</option>
        <option value="si">Sistemas de Informação</option>
    </optgroup>
</select>
```

O atributo selected indica a opção inicialmente selecionada. O atributo value define o valor enviado.

- **Datalist**: oferece sugestões predefinidas para um campo de entrada. O atributo list do input referencia o id do datalist.

```html
<label for="cidade">Cidade:</label>
<input list="cidades" id="cidade" name="cidade">
<datalist id="cidades">
    <option value="Presidente Prudente">
    <option value="São Paulo">
    <option value="Campinas">
</datalist>
```

- **Fieldset e legend**: agrupam campos relacionados dentro de um formulário e fornecem um título para o grupo.

```html
<fieldset>
    <legend>Dados pessoais</legend>
    <label for="nome2">Nome:</label>
    <input type="text" id="nome2" name="nome">
</fieldset>
```

Botões:

- submit: envia o formulário para o destino definido em action.
- reset: restaura os campos aos valores iniciais.
- button: botão genérico, normalmente utilizado com JavaScript.

```html
<input type="submit" value="Enviar">
<input type="reset" value="Limpar">
<input type="button" value="Ação personalizada">
```

### 7.4 Atributos de formulários

|Atributo|Função|Exemplo|
|--------|------|-------|
|value|Define o valor inicial ou o valor associado ao campo.|`value="Ana"`|
|disabled|Desabilita o campo; ele não pode ser utilizado e seu valor não é enviado.|`disabled`|
|readonly|Deixa o campo somente para leitura, sem permitir edição.|`readonly`|
|size|Especifica a largura visível do campo em caracteres.|`size="30"`|
|maxlength|Define o número máximo de caracteres permitido.|`maxlength="50"`|
|autocomplete|Ativa ou desativa sugestões de preenchimento automático do navegador.|`autocomplete="off"`|
|novalidate|No form, desativa a validação automática do navegador ao enviar.|`<form novalidate>`|
|autofocus|Solicita foco automático no campo quando a página é carregada.|`autofocus`|
|min e max|Definem valores mínimo e máximo para tipos compatíveis.|`min="1" max="100"`|
|required|Indica que o campo precisa ser preenchido antes do envio.|`required`|
|placeholder|Exibe uma dica sobre o valor esperado no campo.|`placeholder="Digite seu nome"`|

Exemplo reunindo vários atributos:

```html
<label for="idade">Idade:</label>
<input type="number" id="idade" name="idade"
       min="16" max="100" required
       placeholder="Informe sua idade">

<label for="usuario">Usuário:</label>
<input type="text" id="usuario" name="usuario"
       value="aluno" maxlength="20" size="25"
       autocomplete="on">
```

> **Observações**: `readonly` e `disabled` não são equivalentes: campos somente para leitura podem ser enviados, enquanto campos desabilitados não são enviados. placeholder é uma dica e não substitui o elemento `<label>`.

## 8. Elementos semânticos

Elementos semânticos descrevem o papel das regiões da página. Um documento pode ser compreendido como uma árvore de regiões, facilitando a leitura do código, a manutenção e a navegação por tecnologias assistivas.

```html
<body>
    <header>
        <h1>Nome do site</h1>
    </header>

    <nav>
        <a href="index.html">Início</a>
        <a href="projetos.html">Projetos</a>
    </nav>

    <main>
        <section>
            <h2>Conteúdo principal</h2>
            <article>
                <h3>Notícia ou publicação</h3>
                <p>Texto do conteúdo.</p>
            </article>
        </section>
        <aside>Conteúdo complementar</aside>
    </main>

    <footer>Informações de rodapé</footer>
</body>
```

|Elemento|Significado / utilização|
|--------|------------------------|
|`<header>`|Cabeçalho de uma página ou de uma região.|
|`<nav>`|Região de navegação e menus de links.|
|`<main>`|Conteúdo principal da página.|
|`<section>`|Agrupa conteúdo relacionado, normalmente com um título.|
|`<article>`|Conteúdo independente, como notícia, artigo ou publicação.|
|`<aside>`|Conteúdo complementar ou relacionado ao conteúdo principal.|
|`<footer>`|Rodapé de uma página ou região.|

Os elementos semânticos indicam a função do conteúdo, mas não determinam automaticamente sua aparência visual. Sem CSS, eles não se transformam necessariamente em colunas, menus horizontais ou caixas coloridas.

## 9. Boas práticas e revisão

- Utilize lang="pt-BR" quando o conteúdo estiver em português do Brasil.
- Prefira tags em letras minúsculas e mantenha a indentação consistente.
- Organize os títulos hierarquicamente, sem escolher níveis apenas pelo tamanho visual.
- Associe cada campo de formulário a um label.
- Forneça texto alternativo adequado em imagens informativas.
- Utilize tabelas para dados tabulares, não para organizar o layout da página.
- Use elementos semânticos quando eles representarem corretamente a função da região.
- Verifique os caminhos de imagens, páginas e demais arquivos do projeto.

Exemplo integrador: página de inscrição. O exemplo abaixo reúne estrutura semântica, títulos, parágrafos, links, listas, tabela e formulário.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Inscrição em oficina</title>
</head>
<body>
    <header><h1>Oficinas de Tecnologia</h1></header>
    <nav><a href="#inscricao">Inscreva-se</a></nav>
    <main>
        <section>
            <h2>Oficinas disponíveis</h2>
            <ul>
                <li>Introdução ao HTML</li>
                <li>Criação de páginas Web</li>
            </ul>
        </section>
        <section id="inscricao">
            <h2>Formulário de inscrição</h2>
            <form action="/inscricao" method="post">
                <label for="nome-inscrito">Nome:</label>
                <input id="nome-inscrito" name="nome"
                       type="text" required>
                <label for="email-inscrito">E-mail:</label>
                <input id="email-inscrito" name="email"
                       type="email" required>
                <button type="submit">Enviar inscrição</button>
            </form>
        </section>
    </main>
    <footer>Mostra de Tecnologia</footer>
</body>
</html>
```

> O atributo `action` do exemplo é ilustrativo: para que o cadastro seja efetivamente processado, é necessário existir uma aplicação no servidor preparada para receber e tratar os dados.

## 10. CSS: especificidade

A especificidade é o critério utilizado pelo navegador para decidir qual declaração CSS será aplicada quando duas ou mais regras atingem o mesmo elemento e definem a mesma propriedade. Em geral, o seletor com maior especificidade prevalece.

Por exemplo, se uma regra define todos os parágrafos como vermelhos e outra define uma classe como verde, um parágrafo que possua essa classe ficará verde, pois o seletor de classe tem maior especificidade que o seletor de elemento.

```css
/* Seletor de elemento */
p {
    color: red;
}

/* Seletor de classe: prevalece sobre p */
.destaque {
    color: green;
}

/* Seletor de ID: prevalece sobre os anteriores */
#aviso {
    color: blue;
}
```

### 10.1 Hierarquia e cálculo

Para compreender a especificidade, podemos organizar os seletores em uma hierarquia. A pontuação didática apresentada nos materiais ajuda a comparar regras:

|Tipo de seletor|Exemplo|Pontuação didática|
|---------------|-------|------------------|
|Estilo inline|s`tyle="color: pink"`|1000|
|ID|`#navbar`|100 por ID|
|Classe, pseudoclasse e atributo|`.menu`, `:hover`, `[href]`|10 por ocorrência|
|Elemento e pseudoelemento|`p`, `h1`, `::before`|1 por ocorrência|
|Seletor universal|`*`|0|

Some os valores de cada categoria para comparar seletores. Exemplos:

|Seletor|Cálculo|Resultado|
|-------|-------|---------|
|`p`|1 elemento|1|
|`.intro`|1 classe|10|
|`p.intro`|1 elemento + 1 classe|11|
|`#menu`|1 ID|100|
|`#menu p`|1 ID + 1 elemento|101|
|`div p.destaque`|2 elementos + 1 classe|12|

O cálculo é uma simplificação para fins de aprendizagem: na comparação real, o navegador considera separadamente as categorias de especificidade, em vez de tratar os números como uma pontuação decimal comum. Um seletor com mais IDs, por exemplo, prevalece sobre qualquer quantidade de classes ou elementos.

Quando duas regras têm a mesma especificidade e importância, a declaração que aparece por último na folha de estilos prevalece. A herança e o seletor universal não aumentam a especificidade.

### 10.2 Regra `!important`

A declaração `!important` atribui prioridade especial a uma declaração CSS e pode fazer com que ela prevaleça sobre declarações normais, mesmo que estas venham de seletores mais específicos.

```css
p {
    color: red !important;
}

#aviso {
    color: blue;
}
```

No exemplo, o parágrafo com ID aviso continuaria vermelho, pois a declaração vermelha foi marcada como importante. Evite utilizar `!important` sem necessidade: seu uso excessivo dificulta a manutenção e a sobrescrita dos estilos.

A cascata também considera origem, camada, importância e contexto; portanto, não é correto afirmar que !important sempre vence absolutamente qualquer regra em todos os cenários.

## 11. Box Model e Flexbox

O layout é a organização visual dos elementos em uma página. O HTML define a estrutura do conteúdo e o CSS controla sua aparência, dimensões, espaçamentos e posicionamento. Para construir layouts, é importante entender o Box Model e o Flexbox.

### 11.1 As quatro partes do Box Model

No modelo de caixas do CSS, cada elemento é representado por uma caixa composta por quatro partes:

- **Content (conteúdo)**: área em que ficam o texto, a imagem ou outros elementos.
- **Padding (preenchimento)**: espaço interno entre o conteúdo e a borda.
- **Border (borda)**: contorno ao redor do conteúdo e do padding.
- **Margin (margem)**: espaço externo que separa a caixa dos demais elementos.

```css
.caixa {
    width: 300px;
    padding: 20px;
    border: 5px solid black;
    margin: 10px;
}
```

No modelo padrão (`content-box`), a largura total da caixa acima, sem considerar as margens, será: `300 px` de *conteúdo* + `40 px` de *padding horizontal* + `10 px` de *bordas* = `350 px`. As *margens* acrescentam mais `20 px` ao espaço ocupado horizontalmente.

Para tornar o cálculo das dimensões mais previsível, é comum utilizar `box-sizing: border-box`. **Nesse modelo, a largura declarada já inclui conteúdo, padding e bordas**.

```css
* {
    box-sizing: border-box;
}

.caixa {
    width: 300px;
    padding: 20px;
    border: 5px solid black;
}
```

Com `border-box`, a caixa permanece com `300 px` de *largura total*, incluindo *padding* e *bordas*. A *margem* continua sendo espaço externo e não está incluída nessa largura.

As propriedades margin e padding aceitam atalhos:

|Declaração|Interpretação|
|----------|-------------|
|`padding: 10px;`|`10 px` em todos os lados.|
|`padding: 10px 20px;`|`10 px` em cima e embaixo; `20 px` nas laterais.|
|`padding: 10px 20px 30px;`|`10 px` em cima; `20 px` nas laterais; `30 px` embaixo.|
|`padding: 10px 20px 30px 40px;`|Topo, direita, base e esquerda, nessa ordem.|

> A mesma lógica de atalhos se aplica à propriedade margin.

### 11.2 Flexbox e seus eixos

Flexbox é um modelo de layout CSS que facilita a organização, o alinhamento e a distribuição de espaço entre elementos. Para ativá-lo, define-se display: flex no elemento pai, que passa a ser o flex container. Seus filhos diretos tornam-se flex items.

```css
.container {
    display: flex;
}
```

O Flexbox trabalha com dois eixos:

- **Eixo principal (main axis)**: direção em que os itens são organizados. Por padrão, é horizontal.
- **Eixo transversal (cross axis)**: eixo perpendicular ao principal. Por padrão, flex-direction: row organiza os itens em linha. Se for utilizado column, os itens serão organizados em coluna. A propriedade justify-content atua no eixo principal, enquanto align-items atua no eixo transversal.

### 11.3 Propriedades do Flexbox

|Propriedade|Função e valores comuns|
|-----------|-----------------------|
|`flex-direction`|Define a direção: row, row-reverse, column ou column-reverse.|
|`flex-wrap`|Controla a quebra de linha: nowrap (padrão), wrap ou wrap-reverse.|
|`flex-flow`|Atalho que combina flex-direction e flex-wrap.|
|`justify-content`|Distribui os itens no eixo principal: flex-start, flex-end, center, space-between, space-around e space-evenly.|
|`align-items`|Alinha os itens no eixo transversal: stretch, center, flex-start, flex-end e baseline.|
|`align-content`|Distribui o conjunto de linhas no eixo transversal. É relevante quando há múltiplas linhas e espaço disponível.|
|`align-self`|Permite alinhar individualmente um item, sobrescrevendo o alinhamento geral definido por align-items.|
|`gap`|Define o espaço entre os itens sem precisar aplicar margens individualmente.|

Exemplo de um conjunto de cards responsivos:

```css
.cards {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-between;
    align-items: stretch;
    gap: 20px;
}

.card {
    flex: 1 1 220px;
}
```

Nesse exemplo, os cards ficam lado a lado enquanto houver espaço e passam para novas linhas quando necessário. A propriedade gap controla a distância entre eles. Também é possível separar os espaços horizontal e vertical usando column-gap e row-gap.

> **Atenção**: `align-content` atua sobre as linhas como um conjunto, enquanto `align-items` alinha os itens dentro de cada linha. `align-self` altera o alinhamento de um item específico.

## 12. Pseudoclasses em CSS

As pseudoclasses selecionam elementos HTML de acordo com um estado, uma interação ou uma posição na estrutura do documento. Sua sintaxe utiliza dois-pontos (:) e não exige que a pseudoclasse seja adicionada ao atributo class do HTML.

```css
seletor:pseudoclasse {
    propriedade: valor;
}
```

### 12.1 Estados de interação

|Pseudoclasse|Quando é aplicada|
|------------|-----------------|
|`:hover`|Quando o ponteiro está sobre o elemento.|
|`:active`|Durante a ativação do elemento, por exemplo, enquanto o botão do mouse está pressionado.|
|`:focus`|Quando o elemento recebe foco, por exemplo, ao clicar em um campo ou navegar até ele com a tecla Tab.|
|`:focus`-visible|Aplica estilo de foco quando o navegador entende que o indicador visual é especialmentenecessário, como na navegação por teclado.|
|`:link`|Seleciona links ainda não visitados.|
|`:visited`|Seleciona links já visitados.|

```css
button {
    background-color: blue;
    color: white;
}

button:hover {
    background-color: green;
}

button:active {
    background-color: red;
    transform: scale(0.98);
}

input:focus {
    border: 2px solid blue;
    background-color: #e0f2fe;
}

a:link { color: blue; }
a:visited { color: purple; }
a:hover { color: green; }
a:active { color: red; }
```

A pseudoclasse `:active` representa um estado momentâneo durante a ativação; não significa que o elemento permanecerá selecionado depois do clique. Preserve sempre um indicador de foco visível para facilitar a navegação por teclado.

### 12.2 Pseudoclasses posicionais

As pseudoclasses posicionais selecionam elementos conforme sua posição entre os filhos de um mesmo elemento pai.

|Pseudoclasse|Significado|
|-----------|-----------|
|`:first-child`|Seleciona o primeiro filho.|
|`:last-child`|Seleciona o último filho.|
|`:nth-child(2)`|Seleciona o segundo filho.|
|`:nth-child(even)`|Seleciona os filhos em posições pares.|
|`:nth-child(odd)`|Seleciona os filhos em posições ímpares.|
|`:nth-of-type(2)`|Seleciona o segundo elemento daquele tipo entre os irmãos.|

```css
li:first-child {
    color: red;
}

li:last-child {
    color: blue;
}

li:nth-child(even) {
    background-color: #eeeeee;
}

li:nth-child(odd) {
    background-color: #ffffff;
}
```

> **Diferença importante**:
>
> - `:nth-child()` considera a posição entre todos os filhos do mesmo pai.
> - `:nth-of-type()` considera a posição entre os irmãos que possuem o mesmo tipo de elemento.
>
> Se houver um parágrafo antes de uma lista, por exemplo, o primeiro `li` poderá ser o segundo filho.

### 12.3 Pseudoclasses de formulários

|Pseudoclasse|Aplicação|
|------------|---------|
|`:required`|Campo marcado como obrigatório.|
|`:valid`|Campo cujo valor atende às regras de validação aplicáveis.|
|`:invalid`|Campo cujo valor não atende às regras de validação.|
|`:disabled`|Controle desabilitado.|
|`:checked`|Checkbox ou radio selecionado.|

```css
input:required {
    border: 2px solid orange;
}

input:invalid {
    border-color: red;
}

input:valid {
    border-color: green;
}

input:checked {
    accent-color: green;
}

input:disabled {
    background-color: #eeeeee;
}
```

Um campo obrigatório vazio pode ser considerado inválido. A validação do navegador auxilia o usuário, mas não substitui a validação dos dados no servidor.

Pseudoclasses e pseudoelementos: pseudoclasses selecionam elementos conforme estado ou posição, como :hover e `:first-child.` Pseudoelementos representam partes específicas de um elemento e normalmente utilizam dois-pontos duplos, como `::first-letter` e `::before`.

```css
p:hover {
    color: blue;
}

p::first-letter {
    font-size: 30px;
}
```

## 13. Media Queries e responsividade

Design responsivo é a criação de páginas que continuam legíveis e confortáveis de utilizar em diferentes tamanhos de tela, como celulares, tablets e computadores. A mesma página HTML pode apresentar estilos diferentes conforme a largura disponível.

As Media Queries são condições escritas no CSS. Quando a condição é atendida, as regras dentro do bloco são aplicadas. Quando não é atendida, continuam valendo os estilos gerais.

### 13.1 Sintaxe e condições

A sintaxe básica utiliza `@media` seguida de uma condição e de um bloco de declarações:

```css
@media (max-width: 600px) {
    h1 {
        font-size: 24px;
    }
}
```

- `max-width`: aplica as regras até uma largura máxima. Por exemplo, `max-width: 600px` vale quando a área de visualização tem 600 px ou menos.
- `min-width`: aplica as regras a partir de uma largura mínima. Por exemplo, `min-width: 800px` vale quando a área de visualização tem 800 px ou mais.

> Os valores de `600 px` e `800 px` são exemplos. O ponto de quebra deve ser escolhido conforme o conteúdo e o comportamento do layout, e não apenas por um modelo fixo de aparelho.
>
> Para que a página seja interpretada corretamente em dispositivos móveis, inclua a `meta viewport` no head do HTML:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

O HTML continua responsável pela estrutura; o CSS controla cores, fontes, tamanhos, espaçamentos e apresentação; e as Media Queries adaptam esses estilos conforme as condições da tela.

### 13.2 Exemplos práticos

Exemplo 1 — alterar cores e tamanho do título:

```css
body {
    background-color: #fef3c7;
}

h1 {
    font-size: 36px;
}

@media (max-width: 600px) {
    body {
        background-color: #dbeafe;
    }

    h1 {
        font-size: 24px;
    }
}
```

- Em telas maiores que `600 px`, o fundo permanece amarelo-claro e o título tem `36 px`.
- Em telas de até `600 px`, o fundo passa a azul-claro e o título é reduzido para `24 px`.

Exemplo 2 — adaptar largura e espaçamento de uma caixa:

```css
.caixa {
    width: 70%;
    padding: 40px;
    background-color: #bbf7d0;
}

@media (max-width: 650px) {
    .caixa {
        width: 95%;
        padding: 15px;
        background-color: #fde68a;
    }
}
```

Exemplo 3 — transformar um menu horizontal em vertical:

```css
nav a {
    display: inline-block;
    padding: 10px 20px;
    background-color: #2563eb;
    color: white;
}

@media (max-width: 600px) {
    nav a {
        display: block;
    }
}
```

Nesse exemplo, não é necessário alterar o HTML: os links ficam lado a lado em telas maiores e passam a ocupar linhas separadas em telas pequenas.

> **Como testar**: abra a página no Chrome ou Edge, pressione F12 para abrir as ferramentas do desenvolvedor e utilize a visualização de dispositivos móveis (Ctrl + Shift + M). Teste diferentes larguras, como `400 px`, `600 px` e `900 px`. No limite exato definido por `max-width`, a regra também é aplicada.
>
> **Erros comuns**: esquecer o caractere `@` antes de media, não fechar corretamente as chaves do bloco ou esquecer de salvar o arquivo CSS. Se a regra não funcionar, confira também se o HTML está conectado ao arquivo CSS correto.

---

### Desafio de revisão — Biblioteca da Escola

Considere uma página com cabeçalho, título, menu de navegação e uma caixa de aviso. Crie uma Media Query para telas de até 600 px e faça as seguintes alterações:

- Mude o fundo da página para azul-claro.
- Reduza o título para 24 px.
- Coloque cada link do menu em uma linha separada.
- Reduza o padding da caixa de aviso para 15 px.

O desafio pode ser resolvido apenas com CSS, sem modificar a estrutura HTML.

## 14. Referências

Materiais-base utilizados na organização deste conteúdo: slides da disciplina Desenvolvimento Web — HTML, listas, imagens, links, tabelas, formulários, atributos de formulários e elementos semânticos, da Profª Elaine P. Affonso / Profª Elaine Parra Affonso.

- [World Wide Web Consortium (W3C) — HTML](https://www.w3.org/html/)
- [W3C — HTML e CSS](https://www.w3.org/standards/webdesign/htmlcss)
- [WHATWG — HTML Living Standard](https://html.spec.whatwg.org/multipage/)
- [W3C — HTML Cheat Sheet](https://www.w3.org/2009/cheatsheet/)
- [MDN Web Docs — HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML)
- [W3Schools — HTML Tutorial](https://www.w3schools.com/html/default.asp)
- [W3Schools — HTML Forms](https://www.w3schools.com/html/html_forms.asp)
- [W3Schools — HTML Form Attributes](https://www.w3schools.com/html/html_form_attributes.asp)
- [W3C Brasil — Curso HTML5](https://www.w3c.br/pub/Cursos/CursoHTML5/html5-web.pdf)
- [Caelum — Apostila HTML, CSS e JavaScript](https://www.caelum.com.br/apostila/apostila-html-css-javascript.pdf)
- [W3Schools — CSS Specificity](https://www.w3schools.com/css/css_specificity.asp)
- [W3Schools — The !important Rule](https://www.w3schools.com/css/css_important.asp)
- CASTRO, Elizabeth; HYSLOP, Bruce. *HTML5 e CSS3: guia prático e visual*. Editora Alta Books, 2013.
- [MDN Web Docs — Flexbox](https://developer.mozilla.org/pt-BR/docs/Learn/CSS/CSS_layout/Flexbox)
- [MDN Web Docs — flex-wrap](https://developer.mozilla.org/pt-BR/docs/Web/CSS/flex-wrap)
- [W3Schools — CSS Flexbox](https://www.w3schools.com/css/css3_flexbox.asp)
- [DevMedia — CSS3 Flexbox: Funcionamento e Propriedades](https://www.devmedia.com.br/css3-flexbox-funcionamento-e-propriedades/29532)
- Slides da disciplina Desenvolvimento Web — CSS: Box Model e Flexbox, Profª Elaine P. Affonso.
- Slides da disciplina Desenvolvimento Web — Pseudoclasses em CSS.
- Slides da disciplina Desenvolvimento Web — Media Queries.

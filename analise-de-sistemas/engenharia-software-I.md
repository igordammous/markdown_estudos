# Engenharia de Software I

## 1. Tipos de softwares

De acordo com *Roger S. Pressmann*, a engenharia de software classifica os programas em diferentes categorias de acordo com seu propósito e público-alvo.

Vale ressaltar que através do tempo algumas definições foram mudadas ou atualizadas. Como ***softwares  utilitários*** passaram a fazer parte dos **softwares de sistema**. Assim como **as ferramentas de programação**. Os ***softwares comerciais*** foram redefinidos para **softwares de aplicação**. E por fim, os ***softwares de tempo real*** foram revertidos para os **embutidos e web/mobile**, de acordo como melhor se aplicam de acordo com as novas definições.

|Tipos de Softwares|Uso principal|Exemplo|
|------------------|-------------|--------|
|Sistema|Feito para atender outros programas. Gerência os recursos de hardware e fornece serviços para as aplicações|S.O. Windows, macOS, Linux; Compiladores (ex: GCC); Drivers de dispositivo|
|Aplicação|Solucionam uma necessidade específica de negócio ou processo para o usuário final|Sistema de Controle de Estoque, Software de RH, ERP (ex: SAP), CRM (ex: Salesforce)|
|Ciêntifico ou de engenharia|Caracterizado por algoritmos de processamento numérico intensivo ("cálculo de massa") para aplicações técnicas|MATLAB, AutoCAD, Simuladores de fenômenos físicos, Software de análise de elementos finitos|
|Embutido (Embedded)|Residente na memória ROM de um produto ou sistema, para controlar suas características e funções para o usuário final|Software do forno micro-ondas, Sistema de injeção eletrônica de automóveis, Firmware de roteadores, placa de arduíno|
|Linhas de produtos|Projetado para prover uma capacidade específica para uso por muitos clientes diferentes. Os populares *"softwares de prateleira"*|Microsoft Office (processador de texto, planilha), Adobe Photoshop, Jogos de computador|
|Aplicações Web / Mobile|Software que reside e é executado em navegadores web ou em dispositivos móveis, centrados na rede e na computação em nuvem|Gmail, Google Maps, Aplicativo do Instagram, Internet Banking|
|Inteligência Artificial|Utiliza algoritmos não numéricos (como lógica simbólica, redes neurais) para resolver problemas complexos que não são passíveis de computação direta|Sistemas especialistas (para diagnóstico médico), Chatbots (ex: ChatGPT), Sistemas de reconhecimento facial, Algoritmos de robótica|

### Por que a classificação mudou?

A principal razão para essa evolução é o próprio avanço da tecnologia. O software se tornou muito mais complexo e "híbrido". A engenharia de software é uma ciência viva e **seus conceitos se atualizam para refletir a realidade do mercado**. Por exemplo:

* **Ferramentas de Programação**: Hoje, um compilador (software de sistema) é desenvolvido e usado dentro de um ambiente de desenvolvimento (IDE), que é um Software de Aplicação. Sua natureza dupla dificulta uma classificação única e isolada .

* **Sistemas de Informação**: Um simples sistema de estoque (antigo "software comercial") hoje roda dentro de um navegador, em nuvem, e pode ser acessado por aplicativo mobile. Ele se tornou uma Aplicação Web/Mobile .

* **Convergência**: Um software embutido no seu carro (categoria clássica) hoje pode se conectar à internet, receber atualizações (como um software de sistema) e rodar aplicativos (como o GPS). As fronteiras ficaram muito mais tênues .

## 2. Etapa de Vida de um Software, teoria e na prática

Na **teoria**, a engenharia de software abrange e é responsável por todas as etapas do ciclo de vida de um software. O objetivo da **engenharia de software** é justamente aplicar uma *abordagem sistemática, disciplinada e quantificável ao desenvolvimento, operação e manutenção* do software. Ou seja, ela não se preocupa apenas com a programação (codificação), mas com o processo como um todo.

<div style = "text-align: center;">
<img src="https://www.levty.com/blog/assets/post/ciclo-de-vida-do-desenvolvimento-de-software-conheca-cada-uma-das-fases-6655ea6c6269d11f04512c7d/ciclo-software.webp?w=960" alt="Ciclo de Vida Software" style="width: 50%" title = "Imagem 1 - Ciclo de Vida de um Software"/>

*Imagem 1 - Ciclo de Vida de um Software*.
</div>

### 2.1 Planejamento

O planejamento é a fase inicial e talvez a *mais crítica* do ciclo de vida de um software. Ele não só *estabelece uma direção clara*, como também *ajuda a evitar problemas futuros*, garantindo que todas as partes envolvidas estejam alinhadas e cientes de suas responsabilidades e expectativas.**É nessa etapa que as bases para todo o projeto são estabelecidas.** E essa etapa é dividida em alguns pontos:

* **Identificação das necessidades e requisitos do projeto**: Antes de iniciar o desenvolvimento é **fundamental compreender as necessidades dos stakeholders e dos usuários finais**. Ela é obtida através de reuniões, entrevistas e pesquisas.
* **Definição dos objetivos de maneira clara e o escopo do trabalho que será realizado**: Após identificar as necessidades, **os objetivos** do projeto devem ser definidos, eles precisam ser **claros, específicos, mensuráveis, alcançáveis, relevantes e temporais(*SMART*)**. E o **escopo** é determinado para que se entenda o que está dentro e fora do alcance do desenvolvimento.
* **Análise da viabilidade e recursos necessários**: Essa análise avalia se o projeto **pode ser realizado**, considerando os *recursos técnicos, financeiros e de tempo*. Pode-se incluir a avaliação de riscos, a alocação de recursos e a análise de custos e benefícios.
* **Criação de um plano de projeto detalhado**: Esse plano criado engloba todas as **atividades, cronogramas, marcos, recursos e responsabilidades**. Para então ele servir como guia para toda equipe de desenvolvimento e para ser usado pela equipe de monitoramento e controle do progresso do projeto.

### 2.2 Análise de Requisitos

Após a fase de planejamento, é preciso fazer a análise de requisitos, uma etapa crucial para garantir que o software atenda às necessidades dos usuários e stakeholders. Essa fase **envolve uma compreensão detalhada dos requisitos funcionais e não funcionais** do sistema. Ela é fundamental para evitar ambiguidades e mal-entendidos. Uma documentação bem elaborada e a validação contínua com os stakeholders são essenciais para garantir que o desenvolvimento esteja alinhado com as expectativas do cliente.
Vamos explorar os principais aspectos:

* **Coleta e documentação dos requisitos dos usuários**: A coleta é feita através de reuniões, questionários, workshops e reuniões com os stakeholders. E é essencial documentar todas as expectativas e necessidades dos usuários.
* **Entrevistas, questionários e reuniões com stakeholders**: Essas técnicas ajudam a identificar os requisitos específicos e expectativas dos diferentes grupos de interesse. As *entrevistas* individuais podem *revelar insights detalhados*, enquanto os *workshops* colaborativos podem *ajudar a alinhar diferentes perspectivas*.
* **Criação de um documento de requisitos de software (SRS)**: O **SRS** é um documento formal que **descreve todas as funcionalidades e restrições do sistema**. Ele serve como uma *referência para todas as fases subsequentes do SDLC* e garante que todos os envolvidos tenham uma compreensão comum do que será desenvolvido. E muitas vezes serve como base para contrato entre cliente e equipe de desenvolvimento.
* **Importância de entender as necessidades dos usuários finais**: A análise de requisitos precisa focar nas necessidades reais dos usuários finais, garantindo que o software seja útil e relevante. Uma compreensão inadequada dos requisitos pode levar a retrabalho e insatisfação do cliente.

### 2.3 Design do sistema

Com os requisitos claramente definidos, o próximo passo é transformar esses requisitos em um design detalhado do sistema. A fase de design do sistema **envolve a criação da arquitetura do software, a definição das interfaces de usuário e a modelagem dos dados**. Ela é crítica para garantir que a solução técnica seja robusta e alinhada com os requisitos de negócio. Quando bem planejado **facilita a implementação** e reduz o risco de problemas técnicos durante o desenvolvimento.
Vejamos a seguir os detalhes:

* **Design de arquitetura do sistema**: A arquitetura do sistema **define a estrutura geral do software**, incluindo a divisão em módulos ou componentes, a interação entre eles e a escolha de tecnologias e frameworks. Uma boa arquitetura é **fundamental para garantir a escalabilidade**, desempenho e manutenibilidade do software.
* **Design de interfaces de usuário (UI/UX)**: O design de interfaces de usuário **foca na criação de uma experiência de usuário intuitiva e eficiente**. Pode-se envolver a criação de wireframes, protótipos e a definição de padrões de design. O objetivo é garantir que o software seja fácil de usar e atenda às necessidades dos usuários.
* **Modelagem de dados e design de banco de dados**: A modelagem de dados envolve a **definição das estruturas de dados necessárias para suportar as funcionalidades do sistema**. O design do banco de dados inclui a criação de diagramas de entidade-relacionamento (ERD) e a definição de tabelas, chaves e relacionamentos.
* **Criação de protótipos e wireframes**: Protótipos e wireframes são ferramentas importantes para **visualizar e validar o design do sistema antes da implementação**. Eles permitem que os stakeholders forneçam feedback antecipado e façam ajustes antes que o desenvolvimento real comece.

### 2.4 Implementação

A fase de implementação é para que as ideias e os planos se transformem em código funcional. Nessa etapa, os **desenvolvedores começam a codificar o software de acordo com o design e os requisitos previamente definidos**. Por isso é a etapa em que a maior parte do esforço de desenvolvimento é concentrada. É crucial **manter a comunicação e a colaboração eficazes** entre os membros da equipe para garantir que o software seja desenvolvido de acordo com os padrões e requisitos estabelecidos.
Vamos explorar os principais aspectos da fase:

* **Codificação e desenvolvimento de software**: Os desenvolvedores utilizam linguagens de programação e ferramentas de desenvolvimento para escrever o código-fonte do software. A implementação deve seguir os padrões de codificação e práticas recomendadas para garantir a qualidade do código.
* **Uso de metodologias de desenvolvimento (Ágil, Scrum, Waterfall, etc.)**: A escolha da metodologia de desenvolvimento **impacta diretamente a maneira como o trabalho é organizado e executado**. Metodologias ágeis, como Scrum, permitem entregas incrementais e feedback contínuo, enquanto o Waterfall segue um processo linear e sequencial.
* **Ferramentas e ambientes de desenvolvimento**: As ferramentas de desenvolvimento incluem IDEs (Integrated Development Environments), sistemas de controle de versão e plataformas de integração contínua (CI). Ambientes de desenvolvimento configurados corretamente são essenciais para a produtividade e colaboração da equipe.
* **Boas práticas de programação e controle de versão**: Boas práticas incluem o **uso de padrões de codificação, revisões de código, testes automatizados e documentação clara**. O controle de versão permite que os desenvolvedores colaborem de forma eficaz, rastreando mudanças no código e revertendo a versões anteriores, se necessário.

### 2.5 Testes

A fase de testes é essencial para garantir que o software desenvolvido esteja **livre de erros e funcione conforme esperado**. Essa etapa **envolve a verificação e validação do software** por meio de diversos tipos de testes. E é crucial para assegurar que o software seja robusto e esteja pronto para a implantação. Quando bem planejados e executados ajudam a evitar problemas futuros, economizando tempo e recursos a longo prazo.

#### 2.5.1 Tipos de Testes (Unitário, Integração, Sistema, Aceitação)

1. **Testes Unitários**: Testam individualmente pequenas partes do código (funções, métodos) para garantir que cada unidade funcione corretamente.
2. **Testes de Integração**: Verificam a interação entre diferentes módulos ou componentes para garantir que funcionem bem juntos.
3. **Testes de Sistema**: Avaliam o sistema completo em um ambiente que simula a produção, verificando se o software atende aos requisitos especificados.
4. **Testes de Aceitação**: Realizados pelos usuários finais para validar se o software atende às suas necessidades e expectativas.
    * **Importância de garantir a qualidade e funcionalidade do software**: Testes rigorosos são necessários para identificar e corrigir bugs, garantindo que o software seja confiável, eficiente e seguro. A qualidade do software afeta diretamente a satisfação do usuário e a reputação da empresa.
    * **Processo de detecção e correção de bugs**: Bugs identificados durante os testes são registrados, priorizados e corrigidos pelos desenvolvedores. Um ciclo de repetição de teste e correção continua até que o software atenda aos critérios de qualidade estabelecidos.

### 2.6 Implantação

A fase de implantação é caracterizada pelo software desenvolvido, testado e colocado em uso no ambiente de produção. Essa fase é crucial para garantir que o software esteja disponível e funcionando conforme o esperado para os usuários finais. Ela exige um planejamento meticuloso e uma execução cuidadosa para minimizar o impacto nos usuários e garantir uma transição suave para o novo sistema.

Vamos explorar os principais aspectos desta fase:

* **Preparação para o lançamento do software:** Antes do lançamento, é essencial realizar verificações finais e garantir que todos os componentes do software estejam prontos. A validação final do código, a configuração do ambiente de produção e a preparação da infraestrutura necessária, são algumas estratégias usadas.
* **Monitoramento e suporte pós-implantação**: Após a implantação, é vital monitorar o desempenho do software em tempo real para detectar e resolver quaisquer problemas rapidamente. Pode-se incluir o uso de ferramentas de monitoramento e a configuração de alertas para falhas críticas.
* **Importância do treinamento de usuários finais**: Para garantir que os usuários finais possam utilizar o software de maneira eficaz, é necessário fornecer treinamento adequado. Estão inclusos a documentação, os tutoriais, os workshops e o suporte técnico contínuo.

### 2.7 Manutenção

A fase de manutenção é **contínua e começa imediatamente após a implantação** do software. Nesta etapa, o foco é garantir que o software continue a funcionar corretamente e a atender às necessidades dos usuários ao longo do tempo. Ela garante que o software **permaneça relevante e funcional ao longo do tempo**, adaptando-se às novas necessidades e mantendo um alto nível de satisfação do usuário.

Vamos explorar os principais aspectos dessa etapa:

Tipos de manutenção (Corretiva, Adaptativa, Perfectiva, Preventiva):

1. **Manutenção corretiva**: Correção de bugs e problemas que surgem durante o uso do software.
2. **Manutenção adaptativa**: Ajustes no software para mantê-lo funcional em um ambiente de TI em mudança (como atualizações de sistema operacional ou novas regulamentações).
3. **Manutenção perfectiva**: Melhorias e otimizações no software para aumentar a eficiência e usabilidade, baseadas no feedback dos usuários.
4. **Manutenção preventiva**: Ações tomadas para evitar futuros problemas e melhorar a estabilidade do software, como a refatoração do código e a atualização de dependências.
    * **Gerenciamento de atualizações e patches**: Manter o software atualizado é crucial para a segurança e o desempenho. Essa abordagem envolve a implementação de atualizações regulares e patches de segurança, garantindo que o software esteja protegido contra vulnerabilidades conhecidas.
    * **Monitoramento contínuo de desempenho e feedback dos usuários**: O monitoramento contínuo permite detectar e resolver problemas antes que afetem os usuários. Coletar e analisar o feedback dos usuários ajuda a identificar áreas de melhoria e a priorizar novas funcionalidades.
    * **Planejamento para ciclos de atualização futuros**: A manutenção eficaz requer um planejamento contínuo para futuros ciclos de atualização. Esse planejamento inclui a preparação para grandes atualizações de versão e a alocação de recursos para projetos de melhoria contínua.

## 3. Processos Gerais do Ciclo de Vida de um Software

<div style = "text-align: center;">
<img src="https://media.licdn.com/dms/image/v2/D4D12AQFSwTQNEVK-Lg/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1666502303386?e=1776902400&v=beta&t=kmeQTt-DNL7XLwm4WE1m0JHhODjfTlerpoxvtL-npFA" alt="Processos Gerais do Ciclo de Vida Software" style="width: 80%" title = "Imagem 2 - Processos Gerais do Ciclo de Vida de um Software"/>

*Imagem 2 - Processos Gerais do Ciclo de Vida de um Software*.
</div>

### 3.1 Processos Fundamentais

São os processos **essenciais para a existência do software**. Eles representam as atividades diretamente ligadas à criação, entrega e operação do produto. Sem eles, simplesmente não há software.

|Processo|Descrição|Atividades Principais|
|--------|---------|---------------------|
|Aquisição|Processo de obter o software (seja comprando, contratando ou desenvolvendo internamente).|Definir escopo, selecionar fornecedor, negociar contrato, aceitar o produto.|
|Fornecimento|Processo de entregar o software ao cliente (o lado do fornecedor/desenvolvedor).|Preparar proposta, executar o contrato, entregar o produto.|
|Desenvolvimento|Processo de construir o software propriamente dito.|Levantamento de requisitos, projeto, codificação, testes, implantação.|
|Operação|Processo de executar o software em ambiente de produção.|Execução do sistema, suporte ao usuário, monitoramento.|
|Manutenção|Processo de modificar o software após a entrega.|Correções, adaptações, melhorias, migrações.|

### 3.2 Processos de Apoio

São os processos que **auxiliam os processos fundamentais** durante toda a execução. Eles são aplicados de forma transversal, ou seja, podem ser acionados em qualquer momento do desenvolvimento ou operação.

|Processo|Descrição|Atividades Principais|
|--------|---------|---------------------|
|Documentação|Registro formal da informação gerada ao longo do projeto.|Criar, revisar, versionar e manter documentos (requisitos, arquitetura, manuais).|
|Garantia da Qualidade|Assegurar que processos e produtos atendem aos padrões e requisitos.|Auditorias, revisões técnicas, definição de métricas de qualidade.|
|Verificação e Validação (V&V)|Confirmar que o software está correto (verificação) e atende às necessidades (validação).|Testes, inspeções, análises estáticas.|
|Auditoria|Avaliação independente para verificar conformidade com requisitos, planos e contratos.|Auditorias de processo, auditorias de produto.|
|Resolução de Problemas|Identificar, analisar e resolver problemas que surgem durante o projeto.|Análise de causa raiz, plano de ação, rastreamento de incidentes.|
|Gerência de Configuração|Controlar versões e integridade dos artefatos do projeto.|Controle de versão (Git), gerenciamento de mudanças, baseline.|

### 3.3 Processos Organizacionais

São os processos que atuam no nível da organização como um todo, criando as condições para que os processos fundamentais e de apoio possam ocorrer de forma eficaz e contínua.

|Processo|Descrição|Atividades Principais|
|--------|---------|---------------------|
|Gestão|Planejamento, monitoramento e controle de projetos e recursos.|Alocação de pessoas, gestão de riscos, acompanhamento de prazos e orçamento.|
|Infraestrutura|Estabelecer e manter a base tecnológica e física para os projetos.|Ambientes de desenvolvimento, servidores, redes, ferramentas corporativas.|
|Melhoria de Processos|Avaliar e aprimorar continuamente os processos da organização.|Avaliação de maturidade (CMMI, MPS.BR), definição de melhorias, treinamentos.|
|Recursos Humanos|Gestão de pessoas, competências e capacitação.|Recrutamento, treinamento, desenvolvimento de carreira.|
|Reúso|Gerenciar ativos reutilizáveis (bibliotecas, componentes, padrões).|Catálogo de componentes, governança de reúso.|

### 3.4 Como um Influencia o Outro?

A [ISO/IEC 12207](https://www.iso.org/standard/63712.html) considera que esses processos **não são estanques**. Eles formam um **sistema de interdependências**. Um processo mal executado compromete todos os outros. Vamos entender essa dinâmica.

#### 3.4.1 Influência dos Processos Organizacionais sobre os Fundamentais e de Apoio

Os processos organizacionais são o *"ambiente"* onde os demais operam. Eles criam as condições de base.

|Influência|Exemplo Concreto|
|----------|----------------|
|Gestão → Desenvolvimento|Uma gestão que não faz controle de riscos adequado pode deixar que problemas críticos (ex: dependência de um fornecedor) explodam no meio do projeto, paralisando o desenvolvimento.|
|Infraestrutura → Testes|Se a organização não provê ambientes de homologação adequados (processo de infraestrutura), os testes (processo d'e apoio) não conseguem ser executados com qualidade, comprometendo a validação.|
|Melhoria de Processos → Garantia da Qualidade|Se a organização não investe em melhoria contínua, o processo de garantia da qualidade fica engessado, repetindo os mesmos erros de projeto para projeto.|
|Recursos Humanos → Aquisição|Se a organização não tem pessoas capacitadas em gestão de contratos, o processo de aquisição pode firmar acordos mal estruturados com fornecedores, gerando litígios e atrasos.|

#### 3.4.2 Influência dos Processos Fundamentais sobre os de Apoio e Organizacionais

Os processos fundamentais são os que geram *produtos* e *artefatos concretos*. Eles alimentam os demais com informações e demandas.

|Influência|Exemplo Concreto|
|----------|----------------|
|Desenvolvimento → Documentação|Um desenvolvimento feito sem seguir padrões de arquitetura gera código confuso. A documentação (apoio) precisa então ser excessivamente detalhada para compensar a falta de clareza, ou o projeto acumula dívida técnica.|
|Desenvolvimento → Garantia da Qualidade|Se o desenvolvimento não produz testes unitários, o processo de garantia da qualidade (apoio) precisa investir muito mais tempo em testes de sistema, aumentando custo e prazo.|
|Operação → Gerência de Configuração|Problemas em produção (falhas, incidentes) geram demandas urgentes para a gerência de configuração (apoio), que precisa controlar versões de hotfix com muito mais rigor e velocidade.|
|Manutenção → Melhoria de Processos|Se a manutenção (fundamental) identifica que 80% dos bugs vêm de um tipo específico de erro (ex: falta de validação de entrada), essa informação alimenta a melhoria de processos (organizacional) para que os próximos projetos evitem o mesmo padrão.|

#### 3.4.3 Influência dos Processos de Apoio sobre os Fundamentais e Organizacionais

Os processos de apoio são os *"vigilantes"* e *"organizadores"*. Eles garantem que os fundamentais não saiam do controle e geram dados para os organizacionais.

|Influência|Exemplo Concreto|
|----------|----------------|
|Verificação e Validação → Desenvolvimento|Testes (V&V) encontram um bug crítico em uma funcionalidade. Isso força o desenvolvimento a refatorar aquela parte, evitando que o defeito chegue à produção.|
|Garantia da Qualidade → Gestão|Auditorias de qualidade apontam que os prazos estão sendo sistematicamente subestimados. Esse dado alimenta a gestão (organizacional) para ajustar as políticas de estimativa.|
|Gerência de Configuração → Operação|Um controle de versão bem estruturado permite que a operação faça rollback imediato de uma atualização problemática, reduzindo o tempo de indisponibilidade.|
|Resolução de Problemas → Melhoria de Processos|A análise de causa raiz de um incidente grave revela falhas no processo de aquisição (fundamental). A melhoria de processos (organizacional) revisa o fluxo de contratação de fornecedores.|

#### Diagrama de Influência

Para visualizar melhor, imagine uma **pirâmide de influência**:

```text
┌─────────────────────────────────────────────────────────────┐
│                   PROCESSOS ORGANIZACIONAIS                  │
│  (Criam o ambiente: gestão, infraestrutura, pessoas,        │
│   melhoria contínua, reúso)                                 │
│              ↓ (condicionam e capacitam)                    │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    PROCESSOS DE APOIO                        │
│  (Monitoram e organizam: documentação, qualidade, testes,   │
│   configuração, auditoria, resolução de problemas)          │
│         ↓ (garantem integridade e qualidade)                │
│              ↓ (geram dados para melhoria)                  │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  PROCESSOS FUNDAMENTAIS                      │
│  (O coração do software: aquisição, fornecimento,           │
│   desenvolvimento, operação, manutenção)                    │
│         ↓ (produzem os artefatos)                           │
│              ↓ (alimentam os processos de apoio)            │
└─────────────────────────────────────────────────────────────┘
```

#### Exemplo Prático: Como se Aplica em um Aplicativo

Em um projeto de aplicativo por exemplo, temos:

|Tipo de Processo|Exemplo no Seu Projeto|
|----------------|----------------------|
|Fundamental - Desenvolvimento|Construir o app (frontend React, backend Django, integração com APIs de pagamento).|
|Fundamental - Operação|O app rodando em produção, usuários fazendo buscas, servidores na nuvem.|
|Fundamental - Manutenção|Correções de bugs, adaptações para novas versões de iOS/Android, novas funcionalidades.|
|Apoio - Documentação|Especificação de requisitos (que estamos fazendo), documentação de API, manual do usuário.|
|Apoio - V&V (Testes)|Testes unitários, testes de integração, testes de aceitação com usuários reais.|
|Apoio - Gerência de Configuração|Código versionado no GitHub, controle de versões, gestão de mudanças.|
|Apoio - Garantia da Qualidade|Revisões de código, auditoria de conformidade com LGPD, definição de métricas.|
|Organizacional - Gestão|Planejamento de sprints, alocação de equipe, controle de orçamento e prazos.|
|Organizacional - Infraestrutura|Contas na AWS/Vercel, ferramentas de CI/CD (GitHub Actions), banco de dados em nuvem.|
|Organizacional - Recursos Humanos|Contratação de desenvolvedores, treinamento em novas tecnologias.|
|Organizacional - Melhoria de Processos|Após o lançamento, avaliar o que deu certo/errado e ajustar processos para a versão 2.0.|


## 4. Métodos Tradicionais de Ciclo de Vida (Não Ágeis)

Antes da popularização das metodologias ágeis, os modelos de processo seguiam abordagens mais estruturadas e sequenciais. Estes são os principais métodos não ágeis:

### 4.1. Modelo Cascata (Waterfall)

<div style = "text-align: center;">
<img src="https://engenhariasoftware.wordpress.com/wp-content/uploads/2013/01/cascata.png" alt="Método de Cascata" style="width: 80%" title = "Imagem 3 - Método de Cascata"/>

*Imagem 3 - Método de Cascata*.
</div>

**O que é**: O modelo mais antigo e clássico. As fases são executadas em sequência rígida: Requisitos → Projeto → Implementação → Testes → Implantação → Manutenção. Tem como características:

* Cada fase só começa quando a anterior é completamente finalizada.
* Forte ênfase em documentação.
* O cliente vê o produto funcionando apenas no final do projeto.

**Quando usar**:

* Projetos com requisitos muito bem compreendidos e estáveis.
* Sistemas críticos onde a segurança exige planejamento exaustivo.
* Projetos de curta duração e baixa complexidade.

**Vantagens**: Simplicidade de gestão, marcos claros, documentação completa.

**Desvantagens**: Baixa flexibilidade a mudanças; o cliente só valida no final; problemas descobertos tardiamente são muito caros de corrigir.

### 4.2. Modelo em V (V-Model)

<div style = "text-align: center;">
<img src="https://media.brainly.com.br/image/rs:fill/w:640/q:75/plain/https://pt-static.z-dn.net/files/db4/107b9807006564a9c26a4a2ab3b1aee3.png" alt="Método V" style="width: 60%" title = "Imagem 4 - Método de V"/>

*Imagem 4 - Método de V*.
</div>

**O que é**: Uma evolução do Cascata que associa cada fase de desenvolvimento a uma fase de teste correspondente, formando um formato de "V".

**Estrutura**:

* **Lado esquerdo**: fases de desenvolvimento (Requisitos → Projeto Arquitetural → Projeto Detalhado → Codificação)
* **Lado direito**: fases de teste (Teste de Unidade → Teste de Integração → Teste de Sistema → Teste de Aceitação)

**Características**:

* Testes são planejados desde o início, em paralelo com o desenvolvimento.
* Maior foco em qualidade e validação.

**Quando usar**: Projetos com alta criticidade (sistemas médicos, aeroespaciais), onde falhas não são toleradas.

### 4.3 Modelo de Prototipação

<div style = "text-align: center;">
<img src="https://www.researchgate.net/profile/Junia-Anacleto/publication/224827635/figure/fig1/AS:340265534541824@1458137033750/Figura-2-Modelo-de-processo-Prototipacao-Apoiado-por-Padroes-para-prototipos.png" alt="Método prototipação" style="width: 75%" title = "Imagem 5 - Método de Prototipação"/>

*Imagem 5 - Método de Prototipação*.
</div>

A Prototipação é um modelo de processo que **enfatiza a construção de versões experimentais** (protótipos) de um sistema antes de desenvolver o produto final completo. É uma abordagem iterativa que coloca o usuário no centro do processo. A ideia é criar rapidamente um modelo funcional da interface e das principais funcionalidades, permitindo que o usuário "veja" e "toque" no sistema desde cedo. O protótipo não é o produto final, mas uma ferramenta para extrair feedback e refinar os requisitos

#### 4.3.1 Tipos de Prototipação

|Tipo|Descrição|Uso Típico|
|----|---------|----------|
|Descartável (Throwaway)|Protótipo criado para validar requisitos e depois descartado; o software final é construído do zero|Requisitos muito incertos; validação de conceito|
|Evolucionária (Evolutionary)|Protótipo é continuamente refinado até se tornar o produto final|Quando os requisitos são razoavelmente conhecidos; projetos menores|

#### 4.3.2 Vantagens e Desvantagens

|Vantagens|Desvantagens|
|---------|------------|
|Redução de riscos e mal-entendidos sobre requisitos|Usuário pode confundir protótipo com produto final|
|Feedback constante do usuário desde o início|Pode levar a "scope creep" (aumento descontrolado do escopo)|
|Identificação precoce de problemas de usabilidade|Se mal gerenciado, pode gerar retrabalho excessivo|
|Maior satisfação do usuário com o produto final|Pode dar falsa sensação de progresso|

#### 4.3.3 Quando Usar

* Requisitos vagos ou mal compreendidos
* Projetos com forte componente de interface com o usuário
* Sistemas onde a experiência do usuário é crítica
* Quando há necessidade de validação rápida de conceitos

### 4.4 Modelo RAD(Rapid Application Development)

<div style = "text-align: center;">
<img src="https://julianakolb.wordpress.com/wp-content/uploads/2013/12/rad.png" alt="Método RAD" style="width: 75%" title = "Imagem 6 - Método RAD"/>

*Imagem 6 - Método RAD*.
</div>

O RAD (Desenvolvimento Rápido de Aplicações) foi formalizado por James Martin em 1991 como uma resposta direta ao modelo Cascata, que era criticado por sua rigidez e ineficiência. O RAD é um modelo de processo incremental que enfatiza ciclos de desenvolvimento extremamente curtos (60 a 90 dias) usando construção baseada em componentes.

#### 4.4.1 As 5 Fases do RAD (segundo Pressman)

**O modelo RAD, conforme descrito por Roger S. Pressman, é dividido em 5 fases principais**:

|Fase|Descrição|Atividades Principais|
|----|---------|---------------------|
|1. Modelagem do Negócio|Levantamento do fluxo de informações entre as funções do negócio|Identificar processos suportados pelo sistema; responder "quem faz o quê" e "qual informação é gerada"|
|2. Modelagem dos Dados|Refinamento do fluxo de informação para extrair os objetos de dados|Identificar composição, localização e relações entre objetos de dados|
|3. Modelagem do Processo|Transformação dos objetos de dados no fluxo necessário para implementar funções do negócio|Descrições de processamento para adicionar, modificar ou recuperar dados|
|4. Geração da Aplicação|Construção do software usando ferramentas automatizadas e componentes reutilizáveis|Uso de linguagens de 4ª geração, CASE tools, componentes prontos|
|5. Teste e Modificação|Testes e integração de todos os componentes|Como muitos componentes já estão testados (reuso), o tempo total de teste é reduzido|

#### 4.4.2 Características Fundamentais do RAD

* **Time-boxing**: Prazos fixos e curtos (geralmente 60-90 dias) para cada ciclo
* **Desenvolvimento paralelo**: Múltiplas equipes trabalham em diferentes componentes simultaneamente
* **Reutilização extensiva**: Aproveitamento de componentes, classes e APIs preexistentes
* **Alto envolvimento do usuário**: Participação ativa em todas as fases
* **Foco nas necessidades do negócio**: Excelência técnica é secundária em relação ao atendimento ao usuário

#### 4.4.3 Vantagens e Desvantagens

|Vantagens|Desvantagens|
|---------|------------|
|Desenvolvimento acelerado (60-90 dias)|Requer equipes experientes e bem treinadas|
|Maior flexibilidade e adaptabilidade|Não adequado para projetos de alto risco técnico|
|Feedback constante e relevante do usuário|Exige recursos humanos suficientes para múltiplas equipes|
|Redução de codificação manual|Pode acumular dívida técnica se não houver disciplina|
|Progresso mensurável a cada ciclo|Menos ênfase em planejamento e documentação formal|

#### 4.4.4 Quando Usar RAD

* Projetos com escopo modularizável (pode ser dividido em componentes independentes)
* Equipes experientes com acesso a ferramentas CASE/4GL
* Orçamento suficiente para ferramentas e múltiplas equipes
* Prazos muito curtos (semanas a poucos meses)
* Disponibilidade de usuários para participação contínua

#### 4.4.5 Quando NÃO Usar RAD

* Alto risco técnico (teste de novas tecnologias)
* Projetos de grande escala (exigem recursos humanos massivos)
* Sistemas com forte interdependência entre módulos
* Equipe pequena ou inexperiente
* Projetos que exigem documentação extensiva e formal

#### 4.4.6 Ferramentas e Técnicas de 4GL no Contexto RAD

O RAD frequentemente utiliza ferramentas de 4ª geração como parte essencial de sua estratégia de desenvolvimento rápido:

|Ferramenta/Técnica|Descrição|Exemplos|
|------------------|---------|--------|
|GUI Builders|Construção visual de interfaces gráficas|Visual Basic, Delphi|
|CASE Tools|Ferramentas de engenharia de software assistida por computador|Rational Rose, PowerDesigner|
|Geradores de Código|Produção automática de código a partir de modelos|Geradores de ORM, scaffolding|
|Componentes Reutilizáveis|Bibliotecas de componentes pré-construídos|APIs, frameworks, componentes COM/.NET|
|DBMS com 4GL integrada|Sistemas de gerenciamento de banco de dados com linguagem própria|SQL (Oracle, SQL Server, MySQL)|

>Nota importante: O RAD frequentemente é confundido ou tratado como sinônimo de "low-code". Na verdade, o RAD é uma metodologia que utiliza ferramentas de 4GL, low-code e outras técnicas para atingir seus objetivos de rapidez. Low-code é uma das ferramentas que viabilizam o RAD

### 4.5 Modelo Evolutivo Incremental

<div style = "text-align: center;">
<img src="https://www.researchgate.net/profile/Washington-Almeida-2/publication/334683819/figure/fig1/AS:784598753636353@1564074328073/Figura-34-Modelo-Incremental-Pressman-2016.jpg" alt="Método Incremental" style="width: 60%" title = "Imagem 7 - Modelo Incremental"/>

*Imagem 7 - Modelo Incremental*.
</div>

**O que é**: O sistema é construído em partes (incrementos), cada uma entregando um conjunto de funcionalidades. O primeiro incremento é o núcleo básico, e os seguintes adicionam mais recursos.

**Características**:

* Entrega parcial e funcional desde o início.
* Combina aspectos lineares (planejamento) com entregas iterativas.

**Vantagens**: Cliente começa a usar valor mais cedo; reduz risco de entregar algo totalmente fora do esperado.

### 4.6. Modelo Evolutivo Espiral

<div style = "text-align: center;">
<img src="https://engenhariasoftware.wordpress.com/wp-content/uploads/2013/02/espiral.gif" alt="Método Espiral" style="width: 60%" title = "Imagem 8 - Modelo Espiral"/>

*Imagem 8 - Modelo Espiral*.
</div>

**O que é**: Modelo que combina desenvolvimento iterativo com análise de riscos. Cada volta na espiral representa uma fase do projeto, com quatro **quadrantes**: Determinar objetivos → Avaliar riscos → Desenvolver e testar → Planejar próximo ciclo.

**Características**:

* Foco intenso em gerenciamento de riscos.
* Iterativo, mas com ênfase em prototipação e avaliação contínua.

**Quando usar**: Projetos grandes, complexos e de alto risco (ex: sistemas de defesa, infraestrutura crítica).

### 4.7 Técnicas de 4ª Geração (4GL)

O que são Linguagens de 4ª Geração?
As linguagens de 4ª Geração (4GL) são linguagens de programação de alto nível de abstração, mais próximas da linguagem humana do que as linguagens de 3ª geração (como Java, C++, Python). Elas foram desenvolvidas para reduzir o esforço e o custo do desenvolvimento de software, permitindo que os programadores especifiquem o que fazer, em vez de como fazer.

#### 4.7.1 Comparação entre Gerações de Linguagens

|Geração|Características|Exemplos|
|-------|---------------|--------|
|1GL|Linguagem de máquina, binário, mais próximo do hardware|Código binário|
|2GL|Linguagem Assembly, para kernels e aplicações de alta performance|Assembly|
|3GL|Linguagens de propósito geral, compiladas, usam palavras em inglês|Java, C++, C#, JavaScript, Python|
|4GL|Alto nível de abstração, focadas em tarefas específicas (bancos de dados, relatórios, GUIs)|SQL, Visual Basic, Delphi, PowerBuilder, MATLAB|
|5GL|Usadas principalmente em IA e sistemas especialistas|Prolog, OPS5, Mercury|

#### 4.7.2 A Evolução: Low-Code e No-Code

As técnicas de 4ª geração evoluíram naturalmente para o que hoje conhecemos como plataformas de low-code e no-code. Essas plataformas:

* Permitem desenvolvimento com mínimo de codificação manual
* Utilizam interfaces visuais de arrastar-e-soltar
* Automatizam grande parte do ciclo de desenvolvimento
* Têm ganhado enorme popularidade (mercado projetado para crescer 42.8% ao ano entre 2022-2027)

## 5. O que são Requisitos de Software e Regras de Negócio?

Antes de detalhar as classificações, é essencial entender a diferença entre esses dois conceitos, que muitas vezes se confundem na prática.

### 5.1 Regras de Negócio

**Definição**: São **políticas**, **diretrizes**, **condições** e **restrições** que governam **como o negócio opera**, independentemente de qualquer sistema de software. Elas expressam a lógica do negócio, não a lógica do sistema.

#### 5.1.1 Características

* Existem mesmo sem computadores (podem ser aplicadas manualmente).
* São definidas pelos especialistas do negócio (stakeholders).
* São estáveis por longos períodos.
* Aplicam-se a toda a organização, não apenas a um sistema.

**Exemplos** (para seu app de comparação de preços):
>"Um mercado só pode se cadastrar com CNPJ válido."
>"Uma promoção não pode ter duração superior a 15 dias consecutivos."
>"Um consumidor pode favoritar produtos e receber alertas de preço mínimo."

### 5.2 Requisitos de Software

**Definição**: São descrições do que o **sistema** de software **deve fazer** para **atender às regras de negócio e às necessidades dos usuários**. Eles são a ponte entre o negócio e a tecnologia.

#### 5.2.1 Características

* Existem porque o sistema de software existe.
* São definidos por analistas, engenheiros e usuários.
* Mudam conforme o sistema evolui.
* Aplicam-se especificamente ao sistema em desenvolvimento.

**Exemplos** (derivados das regras acima):
> "O sistema deve consultar a API da Receita Federal para validar o CNPJ no momento do cadastro do mercado."
> "O sistema deve impedir o cadastro de uma promoção com data final superior a 15 dias a partir da data atual."
> "O sistema deve enviar uma notificação push ao consumidor quando o preço de um produto favoritado atingir ou ficar abaixo do valor mínimo definido."

#### 5.2.2 A Relação entre Regras de Negócio e Requisitos

```text
Regra de Negócio (o que o negócio exige)
        ↓
Deriva um ou mais Requisitos (o que o sistema deve fazer para atender à regra)
        ↓
Implementação técnica (código, banco de dados, APIs)
```

#### 5.2.3 Exemplo prático completo

|Nível|Descrição|
|-----|---------|
|Regra de Negócio|"Um consumidor não pode avaliar um mercado sem ter interagido com ele."|
|Requisito Funcional derivado|"O sistema deve registrar toda interação do consumidor com um mercado (visualização de produto, clique em promoção, compartilhamento)."|
|Requisito Funcional derivado|"O sistema deve permitir que um consumidor avalie um mercado apenas se houver pelo menos uma interação registrada nos últimos 30 dias."|
|Requisito Não Funcional derivado|"Os registros de interação devem ser armazenados com timestamp e retidos por no mínimo 90 dias para fins de auditoria."|

#### 5.2.4 Classificação

##### 5.2.4.1 Quanto ao Nível de Detalhamento

|Tipo|Descrição|Público-Alvo|Exemplo|
|----|---------|------------|-------|
|Requisitos de Usuário|Declarações em linguagem natural (não técnica) sobre quais serviços o sistema deve oferecer e sob quais restrições. Escritos para os usuários.|Clientes, usuários finais, gestores de negócio|"O aplicativo deve permitir que o consumidor busque produtos por nome, código de barras ou categoria."|
|Requisitos de Sistema|Especificação detalhada e técnica das funcionalidades, restrições e comportamento do sistema. Serve como contrato entre cliente e desenvolvedor.|Engenheiros de software, arquitetos, testadores|*"O endpoint GET /api/products/search deve aceitar os parâmetros 'query', 'category_id' e 'market_id', retornando JSON com até 50 resultados ordenados por preço crescente, com tempo de resposta inferior a 2 segundos."*|

> Relação entre eles: Os requisitos de sistema são uma expansão técnica dos requisitos de usuário. Um único requisito de usuário pode gerar dezenas de requisitos de sistema.

##### 5.2.4.2 Quanto à Natureza (Funcionais vs. Não Funcionais)

Esta é a classificação mais clássica e amplamente utilizada.

**Requisitos Funcionais**
Definição: Descrevem o que o sistema deve fazer — as funcionalidades, serviços, comportamentos e reações do sistema a estímulos específicos.

Características:

* Expressam ações, cálculos, processamentos.
* Descrevem entradas, saídas e comportamentos.
* São "visíveis" para o usuário (na maioria dos casos).
* Podem ser testados funcionalmente (se a ação ocorre ou não).

**Requisitos Não Funcionais (ou Requisitos de Qualidade)**
Definição: Descrevem como o sistema deve ser — atributos de qualidade, restrições e propriedades que o sistema deve possuir.

Características:

* Frequentemente "invisíveis" para o usuário final, mas críticos para a experiência.
* Aplicam-se ao sistema como um todo.
* São mensuráveis (ou deveriam ser).
* Podem entrar em conflito entre si (ex: segurança x desempenho).

**Categorias de Requisitos Não Funcionais (segundo ISO 25010):**

|Categoria|Descrição|Exemplo|
|---------|---------|-------|
|Usabilidade|Facilidade de uso, aprendizado, acessibilidade|"Um novo usuário deve conseguir realizar uma busca em menos de 2 minutos sem tutorial."|
|Desempenho|Tempo de resposta, vazão, consumo de recursos|"A busca deve retornar resultados em menos de 2 segundos para 95% das requisições."|
|Confiabilidade|Disponibilidade, tolerância a falhas, recuperação|*"O sistema deve ter disponibilidade de 99,9% (menos de 8,76h de indisponibilidade/ano)."*|
|Segurança|Confidencialidade, integridade, autenticação, autorização|*"Todas as comunicações devem ser criptografadas com TLS 1.2+."*|
|Manutenibilidade|Facilidade de correção, evolução e teste|"O código deve ter cobertura mínima de testes automatizados de 80%."|
|Portabilidade|Capacidade de operar em diferentes ambientes|"O app deve suportar iOS (2 últimas versões) e Android (3 últimas versões)."|
|Escalabilidade|Capacidade de crescer sem degradação|"O sistema deve suportar 10.000 requisições por segundo em horários de pico."|
|Conformidade|Adequação a leis, normas e padrões|"O sistema deve estar em conformidade com a LGPD."|

##### 5.2.4.3 Quanto ao Escopo ou Abrangência

|Tipo|Descrição|Exemplo|
|----|---------|-------|
|Requisitos de Produto|Descrevem características do produto de software em si. São os requisitos "tradicionais" (funcionais + não funcionais).|"O app deve permitir busca por voz."|
|Requisitos de Projeto|Restrições impostas ao processo de desenvolvimento ou ao ambiente de entrega.|"O desenvolvimento deve usar a linguagem TypeScript." "O código deve ser armazenado no repositório GitHub da empresa."|
|Requisitos de Interface|Especificam como o sistema se conecta e interage com outros sistemas, hardware ou usuários.|"O app deve integrar com a API de pagamentos do Stripe." "A tela de cadastro deve seguir o padrão de design do Material Design 3."|

##### 5.2.4.4 Quanto à Origem ou Fonte

|Tipo|Descrição|Exemplo|
|----|---------|-------|
|Requisitos de Negócio|Originados das regras de negócio e objetivos estratégicos da organização.|"Aumentar a concorrência entre mercados para reduzir preços da cesta básica."|
|Requisitos de Usuário|Originados das necessidades, desejos e limitações dos usuários finais.|"Consumidores idosos precisam de fontes grandes e contraste elevado."|
|Requisitos Regulatórios|Originados de leis, normas técnicas e órgãos reguladores.|"Cumprir a LGPD para dados pessoais." "Atender ao Código de Defesa do Consumidor."|
|Requisitos de Sistema|Originados de restrições técnicas do ambiente (hardware, software, rede).|"O backend deve ser compatível com o ambiente Linux da AWS."|

##### 5.2.4.5 Quanto à Prioridade (MoSCoW)

Esta classificação ajuda na negociação de escopo e planejamento de entregas.

|Sigla|Significado|Descrição|Exemplo|
|-----|-----------|---------|-------|
|M|Must have (Obrigatório)|Essencial para o sistema funcionar. Sem ele, o sistema é inviável.|"Buscar produtos por nome."|
|S|Should have (Deveria ter)|Muito importante, mas não crítico para o lançamento. Pode ser entregue depois.|"Buscar por código de barras."|
|C|Could have (Poderia ter)|Desejável, mas de baixo impacto. Implementado se houver tempo/recurso.|"Buscar por imagem do produto."|
|W|Won't have (Não terá agora)|Explicitamente excluído do escopo atual, mas pode ser considerado no futuro.|"Comparar preços de produtos orgânicos certificados."|

##### 5.2.4.6 Quanto à Estabilidade

|Tipo|Descrição|Exemplo|
|----|---------|-------|
|Requisitos Estáveis|Pouco prováveis de mudar durante o projeto. Geralmente regras de negócio centrais.|"Um produto é identificado pelo código EAN."|
|Requisitos Voláteis|Sujeitos a mudanças frequentes, muitas vezes durante o desenvolvimento.|"O layout da tela de resultados de busca." "A ordem dos filtros disponíveis."|
|Requisitos Emergentes|Descobertos ou criados durante o desenvolvimento, não previstos inicialmente.|"Os usuários pediram para comparar até 5 mercados lado a lado."|

##### 5.2.4.7 Quanto à Qualidade (Atributos Desejáveis)

Esta classificação se refere a como um bom requisito deve ser escrito (características de qualidade). É uma classificação "metalinguística" — sobre o requisito em si, não sobre o sistema.

|Atributo|Descrição|Contraexemplo (ruim)|Exemplo (bom)|
|--------|---------|--------------------|-------------|
|Correto|Representa fielmente a necessidade do stakeholder.|"O sistema deve ser rápido."|"A busca deve retornar resultados em menos de 2 segundos."|
|Claro|Unívoco, sem ambiguidades.|"O sistema deve tratar usuários especiais."|"Usuários com mais de 100 compras no último ano recebem badge 'Premium'."|
|Completo|Descreve todas as informações necessárias sem lacunas.|"O sistema deve notificar o usuário."|"O sistema deve enviar notificação push ao usuário quando o preço de um produto favoritado cair 10% ou mais, entre 8h e 20h."|
|Consistente|Não conflita com outros requisitos.|*RF01: "O usuário pode se cadastrar sem e-mail."* vs *RF23: "O envio de notificação exige e-mail confirmado."*|(Não há conflito entre requisitos)|
|Verificável|Pode ser testado objetivamente.|"O sistema deve ser fácil de usar."|"90% dos usuários novos devem completar uma busca em menos de 2 minutos sem ajuda."|
|Rastreável|Pode ser vinculado a fontes (regra de negócio, stakeholder, caso de uso) e a artefatos de projeto/teste.|Requisito sem identificador único e sem referência a fonte.|*"RF-034 (derivado da RN-12): ..."*|
|Modificável|Pode ser alterado sem conflitos com outros requisitos.|Requisitos redundantes ou acoplados.|Cada requisito é único e referenciado por ID|

##### 5.2.4.8 Por Classe: Funcionais (Evidente, Oculto e Decorativo) - Similar ao Item 2

|Termo|Significado Prático|Equivalente na Literatura|Exemplo|
|-----|-------------------|-------------------------|-------|
|Evidente|Funcionalidade que o usuário vê e aciona diretamente|Requisito Funcional explícito; caso de uso primário|"Buscar produto por nome" — o usuário digita e vê o resultado|
|Oculto|Funcionalidade que acontece "por trás", sem interação direta do usuário|Requisito Funcional de suporte; processo de backend|"Registrar log de cada busca para estatísticas" — o usuário não vê, mas acontece|
|Decorativo|Funcionalidade que não afeta a operação principal, mas agrega valor|Requisito de usabilidade ou "bom de se ter"|"Animação sutil ao carregar resultados" — bonito, mas não essencial|

Esta subdivisão, evidente, oculto e decorativo, não está presente em normas como IEEE 830 ou ISO 25010, mas é uma forma válida e didática de detalhar os requisitos funcionais. Ela pode ser vista como uma prática de mercado adotada por algumas organizações para refinar a elicitação.

##### 5.2.4.9 Por Classe: Não Funcionais - Similar ao Item 2

Essa classificação está alinhada com a literatura. Os requisitos **não funcionais** (também chamados de atributos de qualidade) são amplamente reconhecidos em todas as referências. O que está definido como ***"Detalhe"*** (Usuário, Sistema, Interface, Hardware, Software, Comunicação) é, na verdade, uma forma de detalhar os requisitos não funcionais por escopo ou tipo de interface, o que também é recomendado pelo padrão IEEE 830.

|Detalhe|Corresponde a|Exemplo|
|-------|-------------|-------|
|Usuário|Interface com usuário (UI/UX)|"Telas com alto contraste para acessibilidade"|
|Hardware|Restrição de infraestrutura|*"Compatível com dispositivos Android 10+"*|
|Software|Requisito de plataforma/tecnologia|"Backend em Node.js, banco PostgreSQL"|
|Comunicação|Protocolos, APIs, rede|"APIs RESTful com JSON, timeout de 5s"|

O IEEE 830 na seção de **"Interfaces Externas"**, exige exatamente a especificação de:

* Interfaces de usuário
* Interfaces de hardware
* Interfaces de software
* Interfaces de comunicação

##### 5.2.4.10 Por Classe: Inversos

Esta é uma classificação **mais avançada e menos comum, mas extremamente útil**. Há referência que se assemelham aos requisitos inversos (também chamados de negative requirements) na literatura de engenharia de segurança e sistemas críticos e na IEEE 830 menciona que o escopo do produto deve descrever **"o que o software não fará, se for o caso"**, mas não se trata de uma classificação *"oficial"*, como os não funcionais.

>**Exemplo**: "O sistema não deve permitir que um cliente visualize dados de faturamento de outro cliente concorrente."

##### 5.2.4.11 Por Proridade: Essencial, Importante e Desejável

Esta classificação está diretamente alinhada com as recomendações do IEEE 830 e da engenharia de requisitos .

|Termo|Equivalente na Literatura|Significado|
|-----|-------------------------|-----------|
|Essencial|Must-have, crítico, obrigatório|Sem ele, o sistema não funciona ou não atende ao objetivo principal|
|Importante|Should-have, condicional|Muito desejável, mas pode ser postergado para uma próxima versão|
|Desejável|Optional, nice-to-have|Seria bom ter, mas não é crítico; pode ser cortado se houver restrição|

A norma IEEE 830 afirma explicitamente que "cada requisito deve identificar seu grau de importância... essencial, condicional, opcional"

##### 5.2.4.12 Correspondência

Mapa de Correspondência Completo

|Classificação|Presente em Normas?|Presente em Bibliografia Clássica?|Status|
|-------------|-------------------|----------------------------------|------|
|Funcionais|Sim (IEEE 830, ISO 25010)|Sim (Pressman, Sommerville)|✅ Padrão|
|└ Evidente|Não (classificação própria)|Não, mas equivalente a "requisito funcional explícito"|⚠️ Prática de mercado|
|└ Oculto|Não (classificação própria)|Não, mas equivalente a "requisito de suporte/backoffice"|⚠️ Prática de mercado|
|└ Decorativo|Não (classificação própria)|Não, mas se aproxima de "requisito de usabilidade"|⚠️ Prática de mercado|
|Não Funcionais|Sim (ISO 25010, IEEE 830)|Sim (Pressman, Sommerville)|✅ Padrão|
|Inversos|Parcial (IEEE 830 menciona "o que o software não fará")|Raro; mais comum em segurança de sistemas|✅ Válido, mas especializado|
|Prioridade (Essencial/Importante/Desejável)|Sim (IEEE 830)|Sim (Sommerville, Paula Filho)|✅ Padrão|
|Detalhe (Usuário/Hardware/Software/Comunicação)|Sim (IEEE 830 - Interfaces Externas)|Sim|✅ Padrão|

##### 5.2.4.13 Exemplo concreto dentro do ERS(SRS)

Todos esses requisitos (com suas classificações) são organizados em um documento chamado Especificação de Requisitos de Software (ERS) ou Software Requirements Specification (SRS), conforme padrão IEEE 830. Uma estrutura típica do ERS inclui:

* Introdução (propósito, escopo, definições)
* Descrição Geral (perspectiva do produto, usuários, restrições)
* Requisitos Funcionais (listados com IDs, descrições, prioridades)
* Requisitos Não Funcionais (por categoria: usabilidade, desempenho, segurança...)
* Regras de Negócio (derivadas dos stakeholders)
* Modelos e Diagramas (casos de uso, fluxos, protótipos)
* Rastreabilidade (matriz ligando requisitos a regras de negócio e a casos de teste)

**Requisito** (versão de sistema):

>"O sistema deve consultar a API de geolocalização do dispositivo (GPS) para obter a localização do consumidor, e então listar apenas os mercados localizados em um raio de até 30 km. Caso o GPS não esteja disponível, o sistema deve solicitar que o usuário digite manualmente seu CEP ou cidade. O tempo de resposta da busca geolocalizada não pode exceder 3 segundos. Esta funcionalidade é obrigatória para a primeira versão."

|Classificação|Atribuição|
|------------|----------|
|Nível de detalhamento|Requisito de Sistema (pois é técnico e mensurável)|
|Natureza|Misto: Funcional (a ação de consultar e filtrar) + Não Funcional (tempo de resposta de 3 segundos)|
|Escopo|Requisito de Produto (característica do software)|
|Origem|Requisito de Usuário (consumidores querem ver mercados próximos)|
|Prioridade (MoSCoW)|Must have (obrigatório para primeira versão)|
|Estabilidade|Estável (a necessidade de localização não deve mudar)|
|Qualidade|Verificável (pode-se testar os 3 segundos), Claro (sem ambiguidade), Completo (cobre caso sem GPS)|

## 6. Especificação de Requisitos de Software (ERS)

### 6.1 Parte 1: Informações que Devem ser Coletadas

O Documento de **Especificação de Requisitos de Software (ERS)** , também conhecido como *SRS (Software Requirements Specification)* conforme o padrão IEEE 830 (e sua sucessora ISO/IEC/IEEE 29148), deve conter um conjunto específico de informações. Suas categorias são:

#### 6.1.1 Informações sobre o Propósito e Escopo

|Informação|O que deve ser levantado|Exemplo|
|----------|------------------------|-------|
|Propósito do sistema|Por que o software está sendo desenvolvido? Qual problema ele resolve?|"Facilitar a comparação de preços de produtos da cesta básica entre mercados, aumentando a concorrência e beneficiando consumidores."|
|Escopo funcional|Quais funções estão DENTRO e quais estão FORA do sistema?|Dentro: busca, comparação, cadastro de preços, promoções. Fora: entrega de produtos, pagamento in-app (inicialmente).|
|Objetivos de negócio|Quais metas a organização espera alcançar com o sistema?|"Aumentar em 20% a economia média do consumidor na cesta básica em 12 meses."|
|Partes interessadas (stakeholders)|Quem tem interesse ou será afetado pelo sistema?|Consumidores, mercados (pequenos, médios, grandes), desenvolvedores, investidores, órgãos reguladores (LGPD).|

#### 6.1.2 Informações sobre os Usuários

|Informação|O que deve ser levantado|Exemplo|
|----------|------------------------|-------|
|Perfis de usuário|Quais os diferentes tipos de usuários?|Consumidor (pessoa física), Mercado (estabelecimento), Administrador (plataforma), Anunciante (futuro).|
|Características demográficas|Idade, escolaridade, familiaridade com tecnologia, localização geográfica|Consumidor: todas as idades, incluindo idosos com baixa familiaridade digital. Mercado: pequenos e médios empresários.|
|Necessidades e dores|O que cada perfil precisa resolver? O que os frustra hoje?|Consumidor: "não sei se o preço está justo", "perco tempo indo de mercado em mercado". Mercado: "não consigo atrair novos clientes".|
|Restrições e limitações|Quais as limitações de cada perfil?|Consumidor idoso: letras pequenas, gestos complexos. Mercado pequeno: orçamento limitado para TI.|

#### 6.1.3 Informações sobre o Ambiente e Contexto

|Informação|O que deve ser levantado|Exemplo|
|----------|------------------------|-------|
|Ambiente operacional|Onde o sistema será executado?|Android/iOS (app), navegadores web (painel do mercado), servidores em nuvem (backend).|
|Restrições de hardware/software|Quais dispositivos, sistemas operacionais, navegadores são suportados?|Android 10+, iOS 15+, Chrome 100+, Firefox 110+.|
|Regulamentações aplicáveis|Quais leis, normas ou certificações o sistema deve atender?|LGPD (Lei Geral de Proteção de Dados), Código de Defesa do Consumidor.|
|Integrações com sistemas externos|Quais outros sistemas o software precisa conversar?|API de geolocalização (Google Maps), API de validação de CNPJ (Receita Federal), sistemas de pagamento (Stripe/PicPay).|

#### 6.1.4 Informações sobre Funcionalidades (Requisitos Funcionais)

|Informação|O que deve ser levantado|Exemplo|
|----------|------------------------|-------|
|Casos de uso|Quais são as principais interações usuário-sistema?|"Buscar produto por nome", "Cadastrar preço", "Criar promoção", "Comparar preços".|
|Fluxos principais (happy path)|Qual a sequência típica de eventos para uma funcionalidade funcionar?|Usuário abre app → digita "arroz" → vê lista de preços por mercado → clica no menor preço.|
|Fluxos alternativos e exceções|O que acontece em situações não ideais?|Busca sem resultados → sugestão de produtos similares. GPS desligado → solicitar CEP manual.|
|Regras de negócio associadas|Quais regras do negócio esta funcionalidade implementa?|"Promoções duram no máximo 15 dias" → sistema impede cadastro com data final maior.|

#### 6.1.5 Informações sobre Atributos de Qualidade (Requisitos Não Funcionais)

|Informação|O que deve ser levantado|Exemplo|
|----------|------------------------|-------|
|Metas de desempenho|Tempos de resposta, vazão, consumo de recursos.|"Busca em até 2 segundos", *"10.000 requisições/segundo"*.|
|Metas de usabilidade|Facilidade de aprendizado, eficiência, satisfação.|"Novo usuário realiza busca em 2 minutos", "acessibilidade para idosos".|
|Metas de disponibilidade|Percentual de tempo que o sistema deve ficar no ar.|"99,9% de disponibilidade" (menos de 8,76h de indisponibilidade/ano).|
|Metas de segurança|Confidencialidade, integridade, autenticação, autorização.|*"Criptografia TLS 1.2+"*, "2FA para mercados", "logs de auditoria".|
|Metas de manutenibilidade|Facilidade de correção, evolução e teste.|"Cobertura de testes >80%", "código modular".|

#### 6.1.6 Informações sobre Restrições e Suposições

|Informação|O que deve ser levantado|Exemplo|
|----------|------------------------|-------|
|Restrições de projeto|Limitações impostas ao time de desenvolvimento.|"Deve usar React Native para compartilhar código entre iOS e Android", "Prazo de 4 meses para MVP".|
|Restrições orçamentárias|Limite de recursos financeiros disponíveis.|"Orçamento de R$ 150.000 para o desenvolvimento inicial".|
|Restrições de prazo|Datas-limite para entregas parciais ou totais.|*"MVP até 30/06, versão 1.0 até 30/09"*.|
|Suposições|O que a equipe está assumindo como verdadeiro (mas que pode mudar).|"Os mercados terão alguém para atualizar preços diariamente", "Os consumidores têm smartphones com GPS".|
|Dependências|O que precisa acontecer ou estar disponível para o projeto prosseguir.|"A API de geolocalização do Google deve estar disponível", "A equipe de design entregar os protótipos até semana 2".|

#### 6.1.7 Informações sobre Prioridades e Critérios de Aceitação

|Informação|O que deve ser levantado|Exemplo|
|----------|------------------------|-------|
|Prioridades (MoSCoW)|O que é Must, Should, Could, Won't?|Must: busca, comparação. Should: histórico de preços. Could: busca por imagem.|
|Critérios de aceitação|Condições objetivas que indicam que um requisito foi atendido.|"Dado um produto válido, o sistema retorna pelo menos 3 mercados com preços em menos de 2 segundos".|
|Métricas de sucesso (KPIs)|Como medir se o sistema atingiu os objetivos de negócio?|"Redução média de 10% no preço da cesta básica após 6 meses", "50.000 usuários ativos mensais".|

### 6.2 Parte 2: Técnicas de Coleta de Requisitos

A engenharia de requisitos oferece diversas técnicas para extrair as informações acima dos stakeholders . Vou listar as mais eficazes.

#### 6.2.1 Técnicas de Elicitação (Coleta)

|Técnica|Como funciona|Melhor para|Exemplo|
|-------|-------------|-----------|-------|
|Entrevistas|Conversa estruturada ou semiestruturada com stakeholders individuais ou em pequenos grupos|Obter visões aprofundadas de cada perfil de usuário|Entrevistar um dono de mercado pequeno sobre suas dificuldades em atrair clientes; entrevistar um consumidor idoso sobre como ele pesquisa preços hoje.|
|Questionários e pesquisas|Formulários enviados a um grande número de pessoas, com perguntas fechadas e abertas|Coletar dados quantitativos de muitos stakeholders|Pesquisar com 500 consumidores: "Com que frequência você compara preços? Quais produtos da cesta básica você mais compra?"|
|Oficinas (workshops)|Reuniões facilitadas com múltiplos stakeholders simultaneamente, com dinâmicas colaborativas|Alinhar diferentes perspectivas e construir consenso|Oficina com 3 donos de mercado, 5 consumidores e 2 especialistas em varejo para definir as regras de promoção.|
|Observação etnográfica|Analisar os usuários em seu ambiente natural de trabalho/vida, sem interferência|Descobrir necessidades implícitas que os usuários não sabem expressar|Observar um consumidor fazendo compras em um mercado para ver como ele compara preços no mundo real.|
|Análise de documentos|Examinar manuais, formulários, relatórios, sistemas existentes|Entender processos atuais e regras de negócio já documentadas|Analisar relatórios de vendas de mercados parceiros para entender quais produtos são mais pesquisados.|
|Brainstorming|Sessão livre de geração de ideias, sem críticas iniciais|Explorar possibilidades criativas e requisitos inovadores|"Quais funcionalidades surpreendentes poderiam fidelizar consumidores?"|
|Prototipação (baixa fidelidade)|Criar esboços, wireframes ou maquetes clicáveis para os usuários interagirem|Validar entendimento de interface e fluxos antes de codificar|Protótipo no Figma da tela de busca para consumidores testarem e darem feedback.|
|Storyboarding|Narrativa visual sequencial mostrando como o usuário interage com o sistema em um cenário típico|Compreender fluxos completos e necessidades de contexto|Sequência de telas mostrando: consumidor abre app → busca "leite" → encontra promoção no mercado X → vai até o mercado.|

#### 6.2.2 Técnicas de Análise e Modelagem

Após a coleta, as informações precisam ser organizadas e modeladas .

|Técnica|O que produz|Exemplo|
|-------|------------|-------|
|Diagrama de Casos de Uso (UML)|Atores, casos de uso e seus relacionamentos|Atores: Consumidor, Mercado, Administrador. Casos: "Cadastrar produto", "Buscar preço", "Gerar relatório".|
|Especificação de Casos de Uso|Descrição detalhada de fluxos, pré-condições, pós-condições, exceções|Fluxo principal, fluxo alternativo (GPS desligado), fluxo de exceção (produto não encontrado).|
|Histórias de Usuário (Ágil)|"Como [ator], eu quero [ação] para [benefício]"|"Como consumidor, eu quero receber alerta de queda de preço para não perder promoções."|
|Critérios de Aceitação (BDD)|Cenários no formato Dado-Quando-Então|"Dado que o usuário favoritou 'arroz 5kg', quando o preço cair 10%, então o sistema envia notificação push."|
|Diagrama de Atividades (UML)|Fluxos de trabalho e decisões|Fluxo de cadastro de promoção: mercado insere dados → sistema valida duração → sistema aprova ou rejeita.|
|Diagrama de Sequência (UML)|Interações temporais entre objetos|Sequência: app → backend → banco de dados → API de geolocalização → resposta.|
|Modelo de Domínio / Diagrama de Classes|Entidades, atributos, relacionamentos|Classes: Produto, Mercado, Preço, Promoção, Consumidor, Favorito.|

### 6.3 Parte 3: Ferramentas para Facilitar a Coleta e Gestão de Requisitos

#### 6.3.1 Ferramentas de Elicitação e Prototipação

|Ferramenta|Tipo|Descrição|Uso|
|----------|----|---------|---|
|Figma|Prototipação|Design de interfaces, wireframes, protótipos clicáveis|Criar telas de busca, resultado, cadastro de produto para validação com usuários.|
|Miro|Colaboração|Quadro branco virtual para brainstorming, fluxogramas, diagramas|Oficinas remotas com stakeholders para mapear regras de negócio.|
|Lucidchart|Diagramação|Diagramas UML, BPMN, fluxogramas|Criar diagramas de caso de uso e atividades.|
|Draw.io (diagrams.net)|Diagramação|Gratuito, integrado com Google Drive/Confluence|Modelagem UML leve e colaborativa.|
|Typeform / Google Forms|Pesquisas|Questionários online com lógica condicional|Pesquisa de satisfação e necessidades com consumidores.|
|Hotjar / FullStory|Observação|Gravação de sessões de usuários em sites/apps|Observar como consumidores reais usam o protótipo ou MVP.|

#### 6.3.2 Ferramentas de Gestão de Requisitos

|Ferramenta|Tipo|Descrição|Uso|
|----------|----|---------|---|
|Jira|Gestão ágil|Backlog de histórias, épicos, tarefas, rastreabilidade|Gerenciar requisitos como histórias de usuário, priorizar backlog (MoSCoW).|
|Confluence|Documentação colaborativa|Wiki para documentar ERS, regras de negócio, atas de reunião|Documentar a versão final do ERS e mantê-lo atualizado.|
|Notion|Documentação + Gestão|Flexível: docs, bancos de dados, kanban|Criar e compartilhar o ERS com rastreabilidade integrada.|
|Trello|Gestão leve|Kanban simples para pequenos projetos|Gerenciar requisitos de um MVP simples.|
|IBM DOORS|Gestão empresarial|Ferramenta pesada para rastreabilidade em larga escala|Projetos de grande porte, regulados (aeroespacial, médico) — exagerado para seu app.|
|Jama Software|Gestão de requisitos|Alternativa moderna ao DOORS, com rastreabilidade|Projetos complexos com múltiplas versões e conformidade.|

#### 6.3.3 Ferramentas de Teste e Validação

|Ferramenta|Tipo|Descrição|Uso|
|----------|----|---------|---|
|Cucumber / Gherkin|BDD|Execução de cenários Dado-Quando-Então|Validar automaticamente que os requisitos foram implementados corretamente.|
|Postman / Insomnia|Teste de API|Validação de endpoints e contratos|Verificar se as APIs do backend atendem aos requisitos de interface.|
|Selenium / Cypress|Teste automatizado|Testes end-to-end no navegador|Simular ações de usuário e verificar comportamento conforme especificado.|

## 7. Universo de Discurso (Universe of Discourse - UoD)

O **Universo de Informação** ou **Universo de Discurso** (Universe of Discourse - UoD) é um tópico fundamental na fase de análise de requisitos e modelagem conceitual.

Ele é o *ponto de partida para entender sobre o que o sistema precisa tratar* antes mesmo de pensar em telas ou código.

### 7.1 O que é o Universo de Discurso (UoD)?

De acordo com a literatura de engenharia de software e sistemas de informação, o **Universo de Discurso é o contexto geral**, o domínio ou o recorte da realidade no qual o software será desenvolvido e irá operar.

Em termos mais simples: é tudo aquilo que é relevante para o sistema. É a "fatia do mundo real" que o software precisa entender, representar e sobre a qual precisa agir.

Imagine que você vai construir o sistema de uma biblioteca. O Universo de Discurso não é o software em si, mas sim o mundo real da biblioteca:

* **Entidades**: Livros, Usuários, Autores, Empréstimos, Funcionários.
* **Processos**: Como um livro é emprestado, como uma multa é calculada.
* **Regras**: "Um usuário não pode pegar mais de 5 livros ao mesmo tempo" ou "Alunos têm prazo de 7 dias, professores de 30 dias".

Para o um aplicativo de comparação de preços, o Universo de Discurso é o mundo dos mercados e dos consumidores. Ele inclui tudo o que precisa ser entendido para o sistema funcionar:

* **Consumidor**: Pessoa que pesquisa, compara preços, favorita produtos.
* **Mercado**: Estabelecimento que vende produtos, cadastra preços e promoções.
* **Produto**: Item da cesta básica, com nome, marca, código de barras (EAN).
* **Preço**: Valor atual de um produto em um mercado específico.
* **Promoção**: Oferta temporária com regras específicas (ex: "Leve 2, pague 1" ou "10% de desconto").

### 7.2 Por que o UoD é tão importante?

A principal razão é que o **software é uma representação (um modelo) de uma parcela da realidade**. Se essa representação for imprecisa ou incompleta, o software será falho, independentemente da qualidade do código.

Os principais objetivos de estudar o **UoD** são:

* **Estabelecer Limites (Escopo)**: O que ESTÁ dentro do sistema? O que está FORA? Isso evita o temido "scope creep". No seu app, "calcular a rota de entrega" pode estar fora do escopo inicial, enquanto "mostrar a localização do mercado no mapa" está dentro.
* **Garantir um Entendimento Comum**: Serve como um contrato de comunicação entre os engenheiros de software e os stakeholders (clientes, usuários). Todos precisam concordar sobre o que é um "produto", um "mercado" ou uma "promoção".
* **Descobrir Regras de Negócio**: Ao analisar o **UoD**, você identifica as regras que governam aquele domínio. No seu app, uma regra de negócio do **UoD** pode ser: "Uma promoção não pode ser cumulativa com outra para o mesmo produto".
* **Fornecer a Base para a Modelagem**: O **UoD** é a matéria-prima para criar diagramas como o Diagrama de Classes da UML, o Diagrama Entidade-Relacionamento (DER) ou qualquer outra forma de modelo de dados.

### 7.3 Como Modelar o Universo de Discurso? (Técnicas)

Na prática da engenharia de software, especialmente seguindo autores como Pressman, a modelagem do **UoD** se traduz em algumas atividades e artefatos concretos.

#### 7.3.1 - Identificação dos Objetos ou Entidades

Listar todos os substantivos relevantes que fazem parte do domínio do problema. Esses serão as futuras classes ou tabelas do seu sistema.

>Exemplo: Produto, Mercado, Endereço, PreçoHistórico, ListaDeCompras.

#### 7.3.2 - Descoberta dos Relacionamentos

Como essas entidades se conectam no mundo real? Isso define a estrutura do banco de dados.

>Exemplo: Um Mercado possui vários Produtos. Um Produto pode estar em vários Mercados.

#### 7.3.3 - Definição dos Atributos

Quais são as características relevantes de cada objeto?

>Exemplo: Produto tem nome, marca, códigoEAN. Mercado tem CNPJ, nomeFantasia, endereço.

#### 7.3.4 - Mapeamento dos Comportamentos e Regras (Dinâmica)

Como esses objetos se comportam e interagem ao longo do tempo? Aqui entram as regras de negócio e os fluxos.

>Exemplo: Um Preço é alterado por um Mercado. Uma Promoção é aplicada a um Produto por um período.

### 7.4 Resumindo

Quando você está criando os Requisitos Funcionais (o sistema deve fazer X) e as Regras de Negócio (a empresa opera assim), você está, na verdade, descrevendo o Universo de Discurso do seu projeto. A modelagem do **UoD** é a técnica para fazer isso de forma estruturada e completa.

## 8 - Técnicas de Levantamento de Requisitos (Elicitação)

Lembre-se da diferença entre:

* **Elicitação pobre**: "O sistema deve ser rápido."
* **Elicitação rica** (Técnica de Entrevista): "Qual o tempo máximo aceitável para a tela carregar em horário de pico?" -> Resulta no Requisito Não-Funcional de Performance.

Podemos dividir não oficialmente entre métodos para coleta de dados, que são: **Entrevista, Coleta de Documentos e Observação**. Mesmo aplicando os três métodos, é muito comum que ainda falte informações, ou que elas foram passadas todas da maneira correta.

> Há algumas perguntas que podem ajudar a moldar as etapas de levantamento, como:
>
> * Sobre o **Cliente**:
>   * Quem pediu a solução?
>   * Quem usará a solução?
>   * Você é a pessoa certa para responder a essas perguntas?
>   * Quais os benefícios desta solução?
> * Sobre o **Problema**:
>   * Quais informações se espera como resultado dessa solução?
>   * Quais problemas essa solução enfrentaria?
>   * Você poderia me mostrar ou descrever o ambiente de negócios em que a solução será usada?
>   * Existem questões de desempenho ou restrições especiais que afetarão a maneira pela qual a solução é abordada?
> * Sobre a **Efetividade do Encontro**:
>   * Você é a pessoa certa para responder a essas perguntas?
>   * Se não, sei a quem delegar?
>   * Estou fazendo perguntas relevantes?
>   * Há mais alguém que possa fornecer informações adicionais?
>   * Existe algo mais que eu deva lhe perguntar?

Aqui temos mais algumas opções de levantamento Questionário, Brainstorming, FAST, Rastreamento de Processo, Estudos de Casos, Simulações e Protótipos

### 8.1 - Entrevistas

A **Entrevista** temos a estrutura e a não estruturada, ambas dependem da habilidade do entrevistador, considerando que ela é uma "*estrutura viva*" onde a resposta pode guiar ela para locais não planejados anteriormente. A desestruturada ela foca em explorar um problema e é mais informal, enquanto a estruturada foca em informações específicas do problema.

Importante definir com os participantes o método de anotação e tempo de entrevista. E é importante que durante seja fornecido um resumo verbal do problema e sempre relacionar a pergunta feita com o tópico em questão(problema). Após o término da entrevista e da documentação, deve-se envia-lá para o entrevistado para que ele dê sua aprovação final e caso seja necessário marcar outra reunião para esclarescer pontos que não ficaram claros.

Situações que podem surgir durante a entrevista que *interferem nos objetivos da sessão*, **respostas ambíguas**, **comentários irrelevantes**, **respostas genéricas**.

Temos dois *níveis* de perguntas, **primárias** que são aquelas que o entrevistador usa para introduzir áreas ou transições para outras áreas e **secundárias** que são perguntas, na maioria das vezes, exploradoras que visam descobrir mais sobre as informações oferecidas em resposta a alguma pergunta. E podemos ter 2 *tipos* de perguntas:

* **Abertas**:
  * Costumam serem menos específicas
  * Não são seguidas por alternativas
  * Encorajam e permitem uma resposta livre
  * Apropriadas quando deseja-se observar respostas de alto nível para reconhecer o escopo de entendimento do entrevistado
  * Possibilitam ao entrevistado o fornecimento de informações que o entrevistador não tem conhecimento para perguntar
  * (-) As respostas a essas perguntas consomem muito tempo, e podem trazer pouca informação
* **Fechadas**:
  * Definem limites no tipo, nível e quantidade de informação fornecida pelo entrevistado
  * Fornecem escolha de alternativas ou níveis de resposta

#### 8.1.1 - Entrevista Estruturada

|Use Quando|Evite Quando|
|----------|------------|
|Você precisa de dados comparáveis entre múltiplos entrevistados (ex: 10 gerentes de loja).|O domínio é novo para você e você não sabe nem o que perguntar.|
|O stakeholder tem pouco tempo e você precisa ser cirúrgico.|Você suspeita que existe conhecimento tácito (o stakeholder faz coisas que não sabe descrever).|
|Você está validando hipóteses já levantadas, não explorando.|Há risco de viés de confirmação (você só pergunta o que já acredita que é verdade).|
|O compliance exige auditoria (perguntas iguais para todos).|O entrevistado fica intimidado com um questionário formal e se fecha.|

#### 8.1.2 - Entrevista Não Estruturada

|Use Quando|Evite Quando|
|----------|------------|
|Você está entrando em um domínio desconhecido e precisa descobrir o vocabulário, os problemas e as dores.|Você precisa de dados estatísticos ou comparáveis entre departamentos.|
|Você quer descobrir regras de negócio implícitas que ninguém documentou.|O stakeholder é prolixo e divaga facilmente; a reunião vai durar 4 horas sem resultado.|
|A fase é exploratória (início do projeto, antes de qualquer ERS).|O projeto está em fase de validação e você precisa confirmar itens específicos da ERS.|
|Há apenas 1 ou 2 especialistas no domínio e você quer mergulhar fundo na mente deles.|O patrocinador exige ata formal e rastreabilidade de cada pergunta feita.|

### 8.2 - Questionários

O **Questionário** é feito quando se tem informações a respeito do problema antes, para que então sejam feitas **questões objetivas** sobre. É importante identificar os respondetens e deve ter alguma forma de controle para garantir que todos receberão o questionário e para que seja possível monitar o status do mesmo. E junto com o questionário é ideal que seja distribuído instruções de como responder e o prazo para realiza-lo. E uma vez coletadas as respostas, deve-se analisar e consolidar as informações fornecidas, documentar as descobertas e enviar um relatório para todos os respondentes. Há algumas desvantagens, como:

* Comunicação com os usuários é seriamente restringida, não há uma real troca de informações face a face
* Preparação exige tempo
* Questões mal elaboradas ou sem conhecimento apropriado podem impactar negativamente na qualidade das informações

Para preparar um, é necessário seguir uma preparação:

* Identificar o tipo de informação que deseja obter
* Identificar quem deve receber o questionário
* Escolher um formato adequado para o questionário (múltipla escolha, escolha simples, etc.)
* Deixar espaço suficiente para resposta de questões descritivas
* Montar questões de maneira simples, clara e concisa
* Enviar um texto acompanhando o questionário para enfatizar a sua importância

|Use Quando|Evite Quando|
|----------|------------|
|A população de stakeholders é grande e geograficamente dispersa (ex: 200 franqueados).|Você precisa de profundidade, contexto emocional ou linguagem corporal.|
|Você precisa de dados quantitativos para justificar uma decisão de priorização.|O índice de resposta esperado é baixo (menos de 10%) e você não tem poder para obrigar o preenchimento.|
|As perguntas são simples, objetivas e não exigem explicação.|O domínio é complexo e os respondentes podem interpretar as perguntas de maneiras diferentes (ambiguidade).|
|Você quer anonimato para que os respondentes sejam honestos (ex: criticar o chefe).|Você precisa iterar: "Por quê? Me explique melhor." O questionário é estático.|

### 8.3 - Brainstorming

**O principal objetivo é obter o máximo de ideias em um curto espaço de tempo**. Tem como origem as reuniões com alto número de funcionários, para que sejam relatados problemas internos, sugestões de melhorias e assuntos como esses. Foi adaptada para método de levantamento de informações, justamente porque um grande número de pessoas conversando sobre o mesmo tema, pode gerar muitas ideias que não seriam geradas no caso de entrevistas ou até questionários. **Útil para as sessões iniciais de levantamento de requisitos**, pois encoraja a criatividade do grupo. Pois há regras a serem seguidas:

* **Qualquer um pode apresentar espontaneamente uma ideia**
* **As ideias devem ser relacionadas ao tópico em discussão**
* **Críticas e julgamentos devem ser reservados para outra oportunidade**
* **Pode-se criar mais ideias baseadas em outras previamente apresentadas.**
* **Definir um *limite de tempo***

|Use Quando|Evite Quando|
|----------|------------|
|O projeto está em fase inicial (Zero Draft) e você quer explorar possibilidades.|O problema já está bem definido e você precisa de soluções detalhadas, não de ideias soltas.|
|Há um impasse criativo ou uma necessidade de inovação (ex: "Como resolver a fila do estacionamento?").|O grupo tem personalidades dominantes que vão calar os introvertidos (precisa de um facilitador forte).|
|Você quer engajar stakeholders de áreas diferentes e criar senso de propriedade coletiva.|Há conflito político aberto entre os participantes (o brainstorm vira briga).|
|O escopo ainda está nebuloso e você quer identificar funcionalidades que ninguém havia pensado.|O tempo é crítico e você precisa de respostas concretas para amanhã.|

### 8.4 - FAST (Facilitated Application Specification Technique)

Tem como **principal objetivo, criar uma equipe conjunta de clientes e analistas que trabalhem juntos para identificar o problema e propor soluções**. Seguindo diretrizes como, encontro em lugar neutro para evitar que um grupo se sinta como "convidado", seguir regras pré-determinadas tanto para preparação, quanto participação e manter o equilíbrio entre uma abordagem formal o bastante para cobrir os pontos importantes, mas informal para encorajar o livre fluxo de ideias.

Importante definir durante encontros iniciais, perguntas e respostas básicas para ajudar estabelecer um escopo do problema e para que todos estejam "na mesma página" em relação a ele no final do encontro. E então **elaborar um documento** com aval de ambos os grupos, o **escopo do problema e uma percepção global de uma solução**. Para preparar essa técnica, deve-se:

* Escolher o **lugar**, **data**, **hora** e **moderador** para o encontro FAST
* Convidar **outros integrantes** das organizações do analista e do cliente
* Distribuir a **Requisição de Produto** para todos os participantes antes do encontro FAST

Parte do documento a ser elaborado deve conter:

* **Lista de objetos**
  * Fazem parte do ambiente que circunda o sistema
  * São produzidos pelo sistema e
  * São usados pelo sistema para executar suas funções
* **Lista de operações** que manipulam ou interagem com o(s) objeto(s)
* **Lista de restrições**: Custo, regras de negócio, etc
* **Critérios de desempenho**: Velocidade, precisão
* Listar **necessidades** e **justificativa** do novo sistema

> Depois, tem criação de uma **lista combinada** de cada área de assunto: **Objetos, operações, restrições e desempenho**.
> E para finalizar essa etapa, **elaboração de uma Lista Consensual de cada área de assunto.**

A próxima etapa consiste em dividir a equipe em **sub-equipes**, para que sejam criadas **mini-especificações** por cada sub-equipe, que nada mais são do que palavras chaves ou pequenas frases que resumam cada item da lista, esses itens são então colocados em um documento chamado de **Lista de Critérios de Validação** e então apresenta-se para a equipe mais uma vez junta, cria então a **Lista de Consenso**, que então fará parte do **Esboço de Especificação Completo**.

```text
┌─────────────────────────────────────────────────┐   ┌────────┐
|Lista objetos, operações, restrições e desempenho| ← | Equipe |
└─────────────────────────────────────────────────┘   └────────┘
                    ↓
           ┌─────────────────┐                        ┌────────┐
           | Lista Combinada |                      ← | Equipe |
           └─────────────────┘                        └────────┘
                    ↓
           ┌──────────────────┐                       ┌────────────┐
           | Lista Consensual |                     ← | Sub-Equipe |
           └──────────────────┘                       └────────────┘
                    ↓
  ┌─────────────────────────────────┐                 ┌────────────┐
  | Lista de Critérios de Validação |               ← | Sub-Equipe |
  └─────────────────────────────────┘                 └────────────┘
                    ↓
          ┌───────────────────┐                       ┌────────┐
          | Lista de Consenso |                     ← | Equipe |
          └───────────────────┘                       └────────┘
                    ↓
  ┌──────────────────────────────────┐                ┌────────┐
  | Esboço de Especificação Completo |              ← | Equipe |
  └──────────────────────────────────┘                └────────┘
```

|Use Quando|Evite Quando|
|----------|------------|
|Há conflito entre áreas que precisam chegar a um consenso sobre os requisitos.|O projeto é simples e não há stakeholders conflitantes.|
|Você precisa produzir uma ERS preliminar em poucos dias (workshop imersivo de 2 a 5 dias).|Você não tem um facilitador experiente disponível (sem facilitador, vira reunião caótica).|
|Os stakeholders de negócio são de alto nível e têm agenda lotada (você os "tranca" em uma sala por 2 dias e resolve).|Os stakeholders não têm autonomia para decidir (tudo terá que ser "validado com o chefe" depois).|
|O escopo é amplo e você precisa de uma visão de consenso rápido.|A cultura da empresa é avessa a workshops longos e imersivos.|

### 8.5 - Rastreamento de Processos

Conjunto de técnicas que permite determinar o **modo de pensar ou agir** de um indivíduo durante a realização de uma tarefa. Pode ser realizada de maneira *concorrente*, onde o indivíduo vai **verbalizando** o que ele está **fazendo ou considerando fazer** enquanto realiza a tarefa. Ou de maneira *restrospectiva*, onde o indivíduo **verbaliza** seu processo de raciocínio após terminar determinada tarefa. Pode ser feita através de:

* **Observação direta**
* **Cenários simulados**

> O engenheiro de requisitos **registra ou grava o procedimento** utilizado para resolver o problema para, mais tarde, **revisar a sessão junto ao especialista** que levantará as informações necessárias.

#### 8.5.1 - Observação Direta

**Observa-se diretamente quem desenvolve o trabalho para se obter informações de como o processo deve ser feito**. Antes de iniciar esse processo, deve saber qual área ou usuário(s) estão sendo observados, como será a forma de registro, explicar a finalidade do estudo que será feito, obter dados das pessoas observadas e principalmente **autorização/aprovação**, tanto da pessoa, quanto da gerência. Pode ser utilizada como:

* Processamento e confirmação dos resultados de uma entrevista
* Identificação de informações que devem ser coletadas para análise posterior
* Esclarecimento do que e de como está sendo feito no ambiente atual

Durante o período de observação deve-se:

* Familiarizar-se com o local de trabalho que está sendo observado
* Observar as máquinas, ferramentas ou processos manuais e automatizadas em uso atualmente
* Coletar amostras de documentos e procedimentos escritos que serão usados para cada processo específico que está sendo observado
* Acumular informações estatísticas relativas às tarefas:
  * frequência que ocorrem, estimativas de volumes, tempo de duração para cada pessoa que está sendo observado, etc

> Assim como outros métodos, após **documentar as descobertas**, é importante rever os resultados obtidos com as pessoas observadas ou responsáveis, para **confirmar os resultados obtidos**.

|Use Quando|Evite Quando|
|----------|------------|
|O processo é transversal a vários setores e ninguém tem a visão completa (ex: "Do pedido à entrega").|O processo é totalmente digital e logs do sistema já fornecem os dados (não precisa observar humano).|
|Você suspeita que o que as pessoas dizem que fazem é diferente do que elas fazem de fato.|O processo é simples, linear e bem documentado.|
|Você precisa identificar gargalos, retrabalhos, planilhas Excel clandestinas ("shadow IT").|A presença do observador altera o comportamento (efeito Hawthorne) e invalida a observação.|
|O objetivo é redesenhar o processo (BPM) junto com o software.|O projeto é apenas de migração tecnológica (mesmo processo, nova plataforma).|

#### 8.5.2 - Simulação

Quase similar à *observação direta*, mas é feita em casos específicos, por exemplo, onde um processo não é feito com tanta frequência mas ainda assim precisa ser observado. Em alguns casos podem ser feito por simulações computacionais.

|Use Quando|Evite Quando|
|----------|------------|
|O sistema envolve eventos complexos e probabilísticos (ex: fila de estacionamento em horário de pico, Black Friday).|O comportamento do sistema é determinístico e simples (ex: CRUD de cadastro de produtos).|
|Você precisa validar requisitos não-funcionais de performance antes de construir.|O custo de criar a simulação é maior que o custo de errar e corrigir depois.|
|É muito caro ou perigoso testar no mundo real (ex: simular pane no sistema de uma usina).|Os parâmetros da simulação são tão incertos que o resultado não será confiável (GIGO: garbage in, garbage out).|
|Você quer treinar usuários para situações raras (ex: como agir na queda do sistema).|O projeto é um MVP simples e a simulação é overengineering.|

### 8.6 - Estudo de casos

Ele geralmente é adotado como método auxiliar de outros métodos, porque nenhuma empresa ou problema é 100% semelhante à outro(a). Portanto apenas com **estudo de casos**, não seria possível determinar soluções para o problema enfrentado pois podem haver **particularidades** que só serão encontrados ao se aprofundar no problema com os outros métodos de levantamento.

Tem como características:

* Sistemas semelhantes ao que está sendo proposto
* Obtêm-se o conhecimento do especialista a partir de casos já documentados
* Solicita-se ao especialista que fale sobre casos reais que tenha solucionado
* Os casos devem cobrir várias possibilidades dentro do domínio
* Útil para identificar sutilezas do especialista na tomada de decisões
* O sucesso depende dos casos escolhidos

### 8.7 - Métodos Tradicionais

|Técnica|Descrição|Quando usar|Exemplo na Prática|
|-------|---------|-----------|------------------|
|Entrevistas|Conversa estruturada (fechada/questionário) ou não estruturada (aberta) com stakeholders.|Quando se precisa de profundidade, entender o "porquê".|Entrevistar o gerente financeiro para entender a lógica de estorno de 10%.|
|Questionários|Formulários com perguntas abertas ou fechadas, aplicados a um grande grupo.|Quando há muitos usuários geograficamente dispersos.|Enviar um Google Forms para 200 franqueados perguntando sobre dificuldades no fechamento de caixa.|
|Observação|Analista observa o usuário no ambiente real de trabalho.|Para detectar falhas de usabilidade ou regras implícitas.|Assistir um operador de caixa registrando produtos para ver se ele usa atalhos de teclado não documentados.|
|Análise de Documentos|Estudar formulários, manuais, leis ou sistemas legados.|Base regulatória forte ou migração de sistemas.|Ler a Portaria 671 do MTE para definir a interface de ponto eletrônico.|
|Workshops (JAD)|Sessão colaborativa intensiva com vários stakeholders e um facilitador.|Resolver conflitos entre áreas e definir prioridades.|Reunir TI, Vendas e Logística para definir o fluxo de um pedido que tem produtos de estoque e de marketplace.|

* **Etapas Iniciais**
  * **Entrevista desestruturada**
  * **Questionário**
  * **Brainstorming**
* **Etapas Intermediárias**
  * **Entrevista estruturada**
* **Etapas Finais**
  * **Rastreamento de Processo**
  * **Estudos de Casos**
  * **Simulações e Protótipos**

### 8.8 Métodos Ágeis (Segundo Semestre)

Ambos são complementares. O ideal é construir um Story Map para definir o MVP e, em seguida, Prototipar as telas do primeiro fatiamento horizontal (Release 1) para garantir que a interação está correta antes de codificar.

#### 8.8.1 Story Mapping (Jeff Patton)

Para visualizar a jornada do usuário e fatiar funcionalidades em releases, baseado no conceito de Design Thinking e User-Centered Design.

Enquanto um Backlog tradicional é uma lista vertical e sem alma ("RF001: Login", "RF002: Busca", "RF003: Pagamento"), o *Story Mapping* é uma ferramenta visual 2D que organiza as funcionalidades em dois eixos fundamentais:

##### 8.8.1.1 - A Anatomia do Mapa (Os Dois Eixos)

* Eixo Horizontal (Esquerda para Direita): Representa o tempo narrativo, o passo a passo cronológico da jornada do usuário. Chamamos isso de "Espinha Dorsal" (Backbone).
  * São as atividades macro que o usuário executa do início ao fim.

* Eixo Vertical (Cima para Baixo): Representa a prioridade/criticidade.
  * Quanto mais alto no mapa (topo), mais essencial (indispensável) é a funcionalidade.
  * Quanto mais baixo, mais opcional ou refinado.

##### 8.8.1.2 - Construção na Prática (Passo a Passo)

>Vamos usar um cenário de App de Mobilidade Urbana como exemplo.
>
>**Passo 1**: *Defina a Espinha Dorsal (O Caminho Feliz)*
>Reúna o time e coloque post-its em sequência lógica respondendo: "Qual é a história da pessoa que pede um carro?"
>
>* Solicitar Veículo
>* Aguardar Motorista
>* Realizar Viagem
>* Finalizar e Avaliar
>
>**Passo 2**: *Quebre as Atividades em Tarefas (O Walking Skeleton)*
>Para cada etapa da espinha, pergunte: "O que o sistema faz aqui?" e cole os post-its de tarefas abaixo.
>
>* **Solicitar Veículo**: Inserir Destino, Confirmar Local Atual, Escolher Categoria (X, Black, Moto), Ver Estimativa de Preço, Tocar em "Confirmar".
>* **Aguardar Motorista**: Ver foto do motorista, Ver modelo do carro, Cancelar Corrida, Chamar Motorista.
>
>**Passo 3**: *Fatie as Releases (O "Corte" Horizontal)*
>Este é o segredo do método. Ao invés de entregar o projeto inteiro pronto, você traça linhas horizontais.
>
>* Release 1 (MVP - Mínimo Produto Viável): Apenas o topo do mapa. Apenas o suficiente para o carro chegar.
>   * Features: Selecionar no mapa, Confirmar corrida, Motorista aceita, Pagamento automático com cartão cadastrado.
>
>* Release 2: A linha de baixo.
>   * Features: Escolher categoria de carro (Moto), Inserir cupom de desconto.
>
>* Release 3 (Futuro): O diferencial.
>   * Features: Agendamento de viagem, Compartilhamento de rota em tempo real com amigos.

##### 8.8.1.3 - Por que isso é superior ao Backlog?

* **Visão do Todo**: Evita a "cegueira do backlog", onde o time foca em detalhes técnicos e esquece a experiência completa. Se um cartão cair da parede (post-it), você vê que quebrou a jornada.
* **Facilita a priorização (MoSCoW viva)**: O debate deixa de ser "O que é importante?" (abstrato) para "Isso fica acima ou abaixo da linha de corte do MVP?" (visual e colaborativo).

#### 8.8.2 - Prototipação

A Prototipação é uma abordagem que resolve a falácia do levantamento por questionário: você pergunta ao usuário como ele faz algo, ele diz X, mas na realidade faz Y. O protótipo faz o usuário reagir a algo concreto. É pore meio de onstrução de telas "de mentira" (baixa/média fidelidade) para descobrir requisitos de interface. “O usuário não sabe o que quer até ver algo funcionando.”

##### 8.8.2.1 - O Espectro de Fidelidade (Não é só "tela de mentira")

Existem níveis muito distintos:

|Nível|Nome|Material|Objetivo (O que testar)|Duração|
|-----|----|--------|-----------------------|-------|
|1|Protótipo de Papel (Baixíssima)|Caneta, post-it, papel craft. Uma pessoa "manipula" os post-its enquanto outra "clica" com o dedo.|Fluxo de navegação, lógica de negócio, terminologia. Totalmente longe de estética.|Horas|
|2|Wireframe Navegável (Média)|Ferramentas como Balsamiq, Figma (modo esboço). Preto e branco, fontes rabiscadas, caixas para imagens.|Arquitetura da informação, posicionamento dos botões. "Está fácil achar o botão 'Finalizar'?"|Dias|
|3|Mockup Interativo (Alta)|Figma, Adobe XD. Cores reais, fotos reais, animações. Parece um App pronto, mas sem backend.|Design visual, branding, microinterações, acessibilidade de contraste.|Semanas|
|4|Piloto (Funcional Parcial)|Código real, mas com funcionalidades limitadas (ex: só a tela de login com a API real).|Teste de performance com usuários reais, integração com hardware (ex: câmera).|Meses|

##### 8.8.2.2 - O Ciclo de Vida da Prototipação

É um processo de engenharia em si:

* **Reunião Inicial**: Defina o escopo. *“Vamos prototipar apenas o fluxo de devolução de produto.”*
* **Desenvolvimento Rápido**: Ignore qualidade de código, segurança e tratamentos de erro. A velocidade é a métrica.
* **Sessão de Avaliação**: Coloque o usuário para usar.
* **Técnica do Think Aloud (Pensar em Voz Alta)**: O usuário narra tudo o que está pensando. "Estou procurando o botão de cancelar... Ah, achei... Mas está cinza, por que não clica?" -> Descoberta de Requisito Inverso.
* **Descarte (Throw-away Prototype)**: A regra de ouro. O protótipo foi feito para gerar a ERS (Especificação de Requisitos). Depois de aprovado o conceito, jogue o protótipo no lixo e codifique do zero, seguindo os padrões de qualidade de software. Resistir à tentação de "dar um jeitinho e colocar em produção" evita débito técnico.

##### 8.8.2.3 - Conexão com a Engenharia de Requisitos

* **Revelando Requisitos de Interface (RI)**: É aqui que nascem os seus RIs. Ao ver o protótipo, o cliente fala: "Se eu clicar em 'Pagar', o sistema está validando o saldo antes de emitir a nota?"
* **Revelando Regras de Negócio**: O protótipo força a descoberta de detalhes que estavam implícitos. "O que acontece com o frete grátis se eu adicionar um item pesado? O sistema deixa acumular? Ah, não... então precisamos de um aviso."

##### 8.8.2.4 - Exemplo Prático: Estacionamento Inteligente

Para evoluir nosso sistema de estacionamento, imagine que vamos prototipar o fluxo de *Estabelecimentos Conveniados* de um shopping.

> Protótipo de Papel (20min):
>
> * **Tela 1**: O lojista tem um leitor. Desenhamos um botão grande "Escanear Ticket".
> * **Tela 2**: Após escanear, um campo "Valor da Compra". O lojista digita 80,00.
> * **Tela 3** (Descoberta): O lojista olha e fala: "E se o ticket já tiver sido validado em outra loja?"
>   * **Ação do Engenheiro**: Você anota imediatamente: Requisito Inverso: O sistema NÃO DEVE aplicar o desconto se o ticket já tiver o flag `CONVENIO_APLICADO = TRUE`.

Sem protótipo, essa regra só seria descoberta em produção, quando o shopping tivesse prejuízo com descontos duplos.

##### 8.8.2.5 - Quando usar

|Use Quando|Evite Quando|
|----------|------------|
|O usuário não sabe expressar o que quer em palavras, mas sabe reagir a algo visual.|O sistema é puramente back-end, sem interface (ex: uma API de cálculo de frete).|
|Há alto risco de rejeição do sistema final (você quer comprar adesão emocional cedo).|O time técnico não resiste à tentação de "aproveitar o protótipo" e colocar código de baixa qualidade em produção.|
|Você precisa testar usabilidade e fluxo de navegação antes de codificar a arquitetura completa.|O cliente acha que o protótipo de alta fidelidade é o sistema quase pronto e pressiona por prazos irreais.|
|O projeto é de inovação (startup, novo produto) e você precisa pivotar rápido.|Os requisitos são regulatórios e não há margem para experimentação (ex: sistema de emissão de nota fiscal, que deve seguir a lei à risca).|

## 9 - Estudo de Viabilidade

Antes de sair codificando, é preciso responder: "*Vale a pena construir esse software?*" É um mini-projeto de análise de riscos. É o ponto de decisão mais crítico antes de um projeto de software começar, o estudo de viabilidade atua como um filtro de investimento.

```text
Ideia do Projeto  →  Estudo de Viabilidade  →  Decisão Go/No-Go  →  Elicitação de Requisitos  →  ERS
                         ↑
                    Você está aqui
```

* **Go**: O projeto segue para a fase de análise detalhada.
* **No-Go**: O projeto é cancelado, adiado ou radicalmente reformulado.

É um estudo breve e direcionado, destinado a responder algumas questões, visando a tomada de decisão e a sugestão de possíveis alternativas de solução:

* O sistema contribui para os objetivos gerais da organização?
* O sistema pode ser implementado com a utilização de tecnologia atual dentro das restrições de custo e de prazo?
* O sistema pode ser integrado com outros sistemas já em operação?

Para todos novo sistemam o ideal é que haja um estudo de viabilidade e como todo estudo ele pode usar como base uma estrutura já pré-determinada. Esse estudo entra mais na área de engenharia de sistemas, que é uma engenharia focada em desenvolver sistemas complexos, foi nela que a viabilidade se estruturou e suas funções são:

* Definir, de maneira precoce no ciclo de desenvolvimento de um sistema, as **necessidades** do usuário, bem como as **funcionalidades requeridas**;
* Abordar a **síntese do projeto** e a **etapa de validação** para considerar o problema completo:
  * Operação; Custo; Cronograma; Desempenho; Treinamento; Suporte; Teste

E com isso aparecem 4 áreas de interesse, que depois foram expandidas por *Hall (2007)* com o método **TELOS**, eram elas:

* Viabilidade econômica
* Viabilidade técnica
* Viablidade legal
* Alternativas

### 9.1 - Modelo TELOS (Hall, 2007)

O acrônimo TELOS é a forma mais técnica e cobrada de estruturar essa análise. Vale lembrar que as **alternativas** não entram aqui, mas ainda continuam fazendo parte de um estudo de viabilidade.

#### 9.1.1 - Técnica (Technical Feasibility)

Pergunta central: **"Conseguimos construir com a tecnologia disponível?"**. Não se trata apenas de hardware/software, mas de maturidade tecnológica e competência da equipe.

|Subdimensão|Pergunta Investigativa|Exemplo (App de Mobilidade)|Exemplo (Estacionamento)|
|-----------|----------------------|---------------------------|------------------------|
|Maturidade|A tecnologia é comprovada ou experimental?|Algoritmo de matching entre motorista e passageiro já existe em APIs como Google Maps. Viável.|Câmera OCR para ler placas em dias de chuva forte. Precisamos testar a taxa de acerto.|
|Competência|O time sabe usar essa stack?|Time só sabe Java, mas o app precisa ser nativo iOS (Swift) e Android (Kotlin). Inviável sem contratação.|O firmware da cancela usa protocolo RS-485. O time de back-end conhece comunicação serial?|
|Capacidade|A infraestrutura atual aguenta?|O servidor de mapas suporta 10.000 requisições simultâneas de GPS?|O banco de dados consegue armazenar 5 anos de logs de entrada/saída para auditoria fiscal?|
|Integração|Os sistemas externos têm APIs documentadas?|A API de pagamentos do banco parceiro tem sandbox para testes?|A máquina de cartão do estacionamento aceita PIX via QR Code dinâmico?|

> **Resultado Técnico**: Um documento de 1-2 páginas listando os riscos técnicos e as *provas de conceito* (PoCs) necessárias. Se uma PoC falhar, o projeto é tecnicamente inviável.

#### 9.1.2 - Econômica (Economic Feasibility)

Pergunta central: **"O retorno justifica o investimento?"**. Aqui entram as técnicas de análise financeira aplicadas a software.

##### 9.1.2.1 - Fluxo de Caixa do Projeto

* **Custos de Desenvolvimento**: Salários da equipe, licenças de ferramentas, infraestrutura cloud, consultorias.
* **Custos de Operação (Manutenção)**: Hospedagem, suporte, correções. Sommerville alerta que a manutenção consome de 50% a 70% do custo total do ciclo de vida de um software.
* **Benefícios Tangíveis**: Economia com demissão de mão de obra, aumento de vendas, redução de erros manuais (ex: menos estornos de ticket).
* **Benefícios Intangíveis**: Melhoria da imagem da marca, satisfação do cliente, conformidade legal (evitar multas).

##### 9.1.2.2 - Métodos de Análise

|Método|Descrição|Exemplo (Sistema de Folha de Pagamento)|
|------|---------|---------------------------------------|
|Payback (Tempo de Retorno)|Quanto tempo até os benefícios acumulados igualarem o investimento inicial.|Investi 200 mil reais. O sistema economiza R$ 10 mil/mês em multas trabalhistas e horas de contador. Payback = 20 meses.|
|ROI (Return on Investment)|Percentual de lucro sobre o investimento.|Se em 3 anos o benefício líquido foi 360 mil reais e o custo foi R$ 200 mil, ROI = (360-200)/200 = 80%.|
|VPL (Valor Presente Líquido)|Traz os fluxos de caixa futuros para valor presente, descontando a inflação/taxa SELIC.|Um projeto que gera 500 mil reais em 5 anos pode valer menos que R$400 mil hoje. VPL positivo = viável.|
|TIR (Taxa Interna de Retorno)|A taxa de desconto que faz o VPL ser zero. Se TIR > taxa de mercado (ex: 12% a.a.), o projeto é atrativo.|TIR calculada em 18% a.a. para o App de Estacionamento. Melhor que deixar o dinheiro na renda fixa.|

> **Armadilha comum**: Subestimar a manutenção. O estudo de viabilidade econômica deve incluir os 5 anos seguintes, não apenas a construção.

#### 9.1.3 - Legal (Legal Feasibility)

Pergunta central: **"Podemos fazer isso sem violar leis ou contratos?"**. Com a LGPD (Lei Geral de Proteção de Dados) e regulações setoriais, este pilar se tornou tão importante quanto o técnico.

|Área Legal|Pergunta Investigativa|Exemplo|
|----------|----------------------|-------|
|Privacidade de Dados (LGPD/GDPR)|Quais dados pessoais coletamos? Onde armazenamos? Temos consentimento?|O App de Mobilidade coleta localização em tempo real. Isso é dado sensível. Precisamos de um DPO (Encarregado de Dados)? O servidor está no Brasil?|
|Retenção Fiscal|Por quanto tempo devemos guardar registros?|O Sistema de Vendas (PDV) deve armazenar NFC-e por 5 anos (Lei do SPED). O banco de dados aguenta?|
|Direitos do Consumidor|O fluxo respeita o CDC?|O sistema de E-commerce permite cancelamento em até 7 dias (Lei do Arrependimento)? Se não, é legalmente inviável.|
|Regulação Setorial|O órgão regulador permite?|O App de Mobilidade precisa de licença da prefeitura? O sistema de folha de pagamento calcula o eSocial corretamente?|
|Propriedade Intelectual|Estamos usando código open-source com licença contaminante (ex: GPL)?|Usar uma biblioteca GPL em software proprietário pode forçar a abertura do código fonte. Inviável para uma fintech.|

> **Resultado Legal**: Um checklist assinado pelo jurídico da empresa. Qualquer "não" bloqueia o projeto ou exige uma mudança de escopo imediata.

#### 9.1.4 - Operacional (Operational Feasibility)*

Pergunta central: **"A organização vai absorver essa mudança?"**. Este é o pilar mais humano e, frequentemente, o que mais causa fracasso em projetos.

|Subdimensão|Pergunta Investigativa|Exemplo (Sistema de Vendas)|
|-----------|----------------------|---------------------------|
|Usuários Finais|Eles querem esse sistema? Eles participaram da elicitação?|O operador de caixa vai achar que o sistema o vigia (RN0X: cada produto registrado gera log de auditoria). Isso gera resistência sindical?|
|Processos Atuais|O fluxo novo quebra alguma regra cultural?|A loja sempre fez "vendas fiado" (caderneta). O sistema novo bloqueia vendas sem pagamento imediato. Os vendedores vão boicotar?|
|Estrutura Organizacional|Quem será o "dono" do sistema?|O PDV gera dados de estoque. Isso é responsabilidade do gerente de vendas ou do almoxarifado? Há disputa política?|
|Treinamento|Existe orçamento e tempo para capacitar?|Trocar o sistema de folha de pagamento em dezembro (13º salário) é suicídio operacional. A data de implantação é viável?|

> **Ferramenta de Análise**: Matriz de Stakeholders (Poder x Interesse). Mapeie quem ganha e quem perde poder com o novo software. Se os perdedores têm alto poder, o projeto é operacionalmente inviável sem um plano de gestão de mudança (Change Management).

#### 9.1.5 - Cronograma (Schedule Feasibility)

Pergunta central: **"Dá tempo de fazer antes que a necessidade desapareça?"**.

|Subdimensão|Exemplo|
|-----------|-------|
|Janela de Mercado|O App de Mobilidade precisa ser lançado antes de um grande evento na cidade. Faltam 2 meses. A equipe estima 6 meses. Inviável.|
|Restrição Legal|A nova lei trabalhista entra em vigor em julho. O sistema de folha precisa estar homologado até lá. Multa diária por descumprimento. Se não der tempo, é melhor comprar um software pronto (COTS).|
|Dependências Externas|O sistema de estacionamento depende da instalação de fibra óptica no shopping. A operadora de internet prometeu para daqui a 8 meses. O software fica pronto em 3. Cronograma inviável.|

### 9.2 - O Documento de Viabilidade (Artefato de Saída)

Não é um documento burocrático e sim um argumento de venda para a diretoria. Possui uma estrutura recomendada baseada no IEEE Std 1058 para Plano de Projeto, mas cada empresa pode ter seu módelo:

* **Sumário Executivo (1 página)**: Resumo da recomendação (Go / No-Go / Condicional).
* **Escopo do Sistema Proposto**: Uma frase clara. "Automatizar a operação de estacionamento dos 5 shoppings da rede."
* **Análise TELOS Detalhada**:
  * Tabela de Riscos Técnicos com Plano de Mitigação.
  * Planilha de Fluxo de Caixa (5 anos) com Payback e VPL.
  * Checklist Legal com assinatura do jurídico.
  * Mapa de Stakeholders e Plano de Treinamento (Operacional).
  * Cronograma Macro (Gráfico de Gantt simplificado).
* **Alternativas Consideradas**:
  * Opção A (Construir): R$ 500 mil, 12 meses, alto risco de atraso.
  * Opção B (Comprar ERP): R$ 200 mil de licença + 50 mil reais de implantação, 3 meses, baixo risco, mas perde diferencial competitivo.
  * Opção C (Não fazer nada): Custo zero, mas risco de perder market share.
* **Recomendação Final.**

Na hora de **identificar as alternativas**, quanto mais detalhes, mais claro será para determinar qual melhor alternativa. Assim como a análise de custos de cada uma, fazer uma tabela com os **itens necessários** (*recursos de hardware, software, pessoal*) para o **desenvolvimento** do software e para o **uso** do software na empresa, suas quantidades, valor unitário e valor total e também um texto descritivo que **justifique a escolha** desta alternativa.

## 10 - A Norma IEEE 830: Estrutura e Características da ERS

A IEEE 830-1998 foi substituída conceitualmente pela **ISO/IEC/IEEE 29148:2018**, mas ainda a base da literatura clássica. Todas as técnicas vistas anteriormente visam **clarificar as informações** e **reduzir os erros de comunicação**. Mas depois temos que **documentar as informações coletadas**. As informações coletadas devem estar organizadas e claras para que não haja erros, ou pelo menos minimizar esses erros, pois eles são custosos para serem resolvidos. Exemplo de erros encontrados em diferentes etapas do ciclo de vida de um software:

* **Fase de Requisitos**
  * Corrigir um erro de especificação exige apenas a revisão de documentos e alinhamento de expectativas.
* **Fase de Desenvolvimento/Codificação**
  * O bug é detectado pelo próprio desenvolvedor logo após escrever o código.
* **Fase de Testes/QA**
  * O bug é encontrado pelo QA. O custo aumenta devido ao retrabalho, necessidade de novos testes e possíveis atrasos no cronograma de lançamento.
* **Produção**
  * O bug afeta o usuário final, gerando falhas no sistema, perda de dados, necessidade de patches urgentes, suporte ao cliente e danos à reputação da empresa.

### 10.1 - O Que é e Qual o Propósito da ERS (SRS)?

A Especificação de Requisitos de Software é o contrato técnico entre todas as partes interessadas. A IEEE 830 define que uma ERS deve declarar o que o software deve fazer, e não como fará. Os 4 Propósitos Fundamentais da ERS (segundo a IEEE 830):

* **Base para Acordo**: Cliente, desenvolvedores e testadores sentam-se à mesa e dizem: "**É isso que será construído. Estamos de acordo.**" Isso evita disputas judiciais futuras.
* **Base para Estimativas**: A equipe de projeto usa a ERS para **estimar custo, prazo e esforço**. Se a ERS é ambígua, a estimativa será furada.
* **Base para Projeto e Implementação**: Arquitetos e programadores **transformam os requisitos** em módulos de **código**.
* **Base para Validação e Verificação**: Testadores escrevem casos de teste para **provar que cada requisito foi implementado corretamente**.

### 10.2 - Estrutura Recomendada para o Documento (IEEE 830, Seção 4)

A norma sugere um template com três seções principais. Não é obrigatório segui-lo cegamente, mas qualquer bom documento de ERS contempla esses elementos.

* **Introdução**
  * **Propósito**: Declarar o objetivo do software e o público-alvo do documento.
  * **Escopo**: Nomear o produto, explicar o que ele fará e, crucialmente, o que não fará (fundamental para alinhar expectativas).
  * **Definições e Acrônimos**: Glossário (ex: "PDV: Ponto de Venda", "NFC-e: Nota Fiscal ao Consumidor Eletrônica").
* **Descrição Geral**
  * **Estudo de Viabilidade**: É um mini-projeto de análise de riscos.
  * **Perspectiva do Produto**: Como o software se relaciona com outros sistemas? É um módulo independente ou parte de um ERP maior? Deve ser descrita de maneira resumida, de forma textual, sem detalhamento.
    * **Interfaces de Sistema**: com quais outros sistemas o produto de software interage (se houver).
    * **Interfaces de Usuário**: formatos de telas, relatórios ou consulta, formatos de mensagens, acesso por níveis de usuário.
    * **Interfaces de Hardware**: como o produto interage com os dispositivos de hardware; características de configuração
  * **Funções do Produto**: Um resumo gráfico (diagrama de contexto) das macro-funcionalidades. Nada detalhado ainda.
    * Funções Básicas: referem-se às operações CRUD necessárias para a execução das funções fundamentais.
    * Funções Fundamentais: referem-se às transações de negócio (movimentações);
    * Funções de Saída: referem-se às funções que geram informações de saída relevantes para atender às necessidades do usuário (consultas/relatórios com cruzamento de informações). Devem ser descritos os itens de entrada (filtros) e os itens de saída (informação) pertinentes.
  * **Características do Usuário**: Perfis. "O Operador de Caixa possui ensino médio e opera o sistema em alta pressão. O Gerente Financeiro precisa de dashboards."
  * **Restrições Gerais**: Leis (LGPD), hardware específico (ex: o sistema só roda em Windows Embedded), deadlines.
* **Requisitos Específicos (O Coração da ERS)**
  * **Requisitos Funcionais**: Nossos RFs, organizados por módulo ou caso de uso.
  * **Requisitos Não-Funcionais**: Nossos RNFs (Desempenho, Segurança, Usabilidade, Confiabilidade).
  * **Requisitos de Interface**: Nossos RIs (Hardware, Software, Comunicação, Interface com o Usuário).

### 10.3 - As 8 Características de Qualidade

#### 10.3.1 - Correto (Correct)

Um requisito é correto se representa algo que o sistema deve fazer, conforme validado pelo stakeholder.

* **Ruim (Incorreto)**: "O sistema deve enviar um SMS para o cliente." (O cliente não quer SMS, quer notificação push. Isso foi inventado pelo analista).
* **Bom (Correto)**: "O sistema deve enviar notificação push via aplicativo." (Validado com o cliente durante a prototipação).
* **Verificação**: Rastreabilidade. Temos um protocolo de entrevista assinado que pede isso?

#### 10.3.2 - Não Ambíguo (Unambiguous)

Toda sentença tem uma e apenas uma interpretação. Esse é o maior desafio da língua natural.

* **Ruim (Ambíguo)**: "O sistema deve calcular o frete adequadamente."
* **Bom (Não Ambíguo)**: "O sistema deve calcular o frete utilizando a tabela da transportadora 'RápidoLog' vigente na data do pedido, considerando o peso total do carrinho e o CEP de destino."
* **Ferramenta de Validação**: Revisão por pares (um lê, o outro interpreta). Glossário de termos. Uso de "Deve" (obrigatório) vs. "Pode" (opcional).

#### 10.3.3 - 3. Completo (Complete)

Não há "a definir" (TBDs - To Be Defined) no texto final. Todas as respostas do sistema a entradas inválidas estão descritas.

* **Ruim (Incompleto)**: "Quando o usuário errar a senha, o sistema trata."
* **Bom (Completo)**: "O sistema deve permitir 3 tentativas de senha. Após a 3ª tentativa incorreta, o usuário deve ser bloqueado por 30 minutos e um e-mail de alerta de segurança deve ser enviado ao titular da conta."
* **Checklist de Completeza**:
  * Todas as funções requeridas estão lá?
  * Todas as entradas (válidas e inválidas) têm resposta definida?
  * Todas as telas/referências a figuras estão inclusas?
  * Todas as unidades de medida (segundos, minutos, R$) estão especificadas?

#### 10.3.4 - Consistente (Consistent)

Nenhum requisito no documento contradiz outro. O conflito clássico de terminologia e lógica.

* **Conflito de Terminologia**: `RF0X`: "O sistema deve gerar um boleto para pagamento" vs. `RF0Y`: "O comprovante de pagamento em PDF será enviado por e-mail". (Afinal, é boleto registrado, cópia do boleto, ou um comprovante genérico?).
* **Conflito de Lógica**: `RN0X` diz que não se aceita cheque. Mas `RFXX` diz que o sistema deve imprimir formulário para depósito de cheque. Isso é uma inconsistência grave.
* **Prevenção**: Matriz de rastreabilidade cruzada durante a revisão.

#### 10.3.5 - Priorizado para Importância e/ou Estabilidade (Ranked)

Cada requisito deve ter um indicador de importância. É abordado mais profundamento nos tópics *MoSCoW* e a *Matriz Esforço-Impacto*. A ERS precisa materializar isso.

* **Ruim (Plano)**: Lista de 500 requisitos sem distinção.
* **Bom (Priorizado)**: Uso de etiquetas nos requisitos.
  * **Essencial**: O sistema morre sem isso (ex: Registrar venda - RN05).
  * **Condicional**: Necessário, mas pode esperar o incremento 2 (ex: Aceitar Vale-Alimentação).
  * **Opcional**: Desejável, baixo custo-benefício imediato (ex: Tema escuro no PDV).

#### 10.3.6 - Verificável (Verifiable)

Existe um processo finito e com custo aceitável para provar que o software atende ao requisito. Este é o critério que separa a engenharia da poesia.

* **Não Verificável (Poesia)**: "A interface deve ser amigável e intuitiva."
* **Verificável (Engenharia)**: "Durante o teste de usabilidade, 8 de 10 usuários novatos devem conseguir completar a compra de um produto sem pedir ajuda." -> Critério de aceite objetivo.
* **Outro Exemplo (Performance)**: "O sistema deve ser rápido." (Não verificável).
* **Verificável**: "O tempo de resposta da API de consulta de estoque não deve exceder 300ms para 95% das requisições, medido na AWS us-east-1."

#### 10.3.7 - Modificável (Modifiable)

A estrutura da ERS permite mudanças sem quebrar a consistência. Imagine mudar a regra de frete e ter que revisar o documento inteiro.

* **Ruim (Monolítico)**: Um arquivo único de 300 páginas em Word, sem sumário automático, com requisitos de interface grudados com regras de negócio.
* **Bom (Modular)**:
  * Organização por módulos/subsistemas.
  * Separação física de seções: Regras de Negócio em um anexo, Requisitos Funcionais em outro.
  * Uso de Tabelas para parâmetros. Ex: Tabela_Frete (UF, Valor_Minimo, Taxa_Peso) ao invés de 27 regras textuais.
  * Índice remissivo e sumário atualizável automaticamente.

#### 10.3.8 - Rastreável (Traceable)

A origem de cada requisito é conhecida, e seu impacto futuro é projetado.

* **Rastreabilidade para Trás (Origem)**: Por que isso está aqui?
  * `RF02 - Frete Grátis` -> Origem: `RN01` (Regra de Negócio definida em reunião com Marketing em 02/04).
* **Rastreabilidade para Frente (Destino)**: O que quebra se eu tirar isso?
  * `RF02 - Frete Grátis` -> Implementado em `CarrinhoService.calcularFrete()` -> Caso de Teste `CT-045`.

### 10.4 - Os Dois Públicos da ERS: Um Documento, Duas Leituras

A norma alerta que a ERS é lida por dois grupos muito distintos, e deve servir a ambos:

|Público|Quem são|O que buscam na ERS|Linguagem Ideal|
|-------|--------|-------------------|---------------|
|Stakeholders de Negócio|Cliente, Gerente de Produto, Domínio (Experts)|Diagramas de fluxo, Regras de Negócio, Critérios de Aceite. "O sistema faz o que eu pedi?"|Linguagem natural, gráficos, protótipos.|
|Stakeholders Técnicos|Arquiteto, Desenvolvedor, QA|Requisitos Funcionais detalhados, Restrições Técnicas, APIs. "Como vou construir e testar isso?"|UML, tabelas de decisão, especificações formais de entrada/saída.|

> **Estratégia de Engenharia**: A seção 3 da ERS (Requisitos Específicos) pode ser escrita em linguagem natural para o negócio, mas complementada por um Anexo Técnico com os modelos formais (Diagramas de Caso de Uso, DFD, Diagramas de Estados) para os desenvolvedores.

### 10.5 - Exemplo de aplicação da IEEE 830 em um estacionamento

Vamos pegar duas regras de negócios hipotéticas RN05/RN06 (Preço de hora normal e adicional) de um sistema de estacionamento e ver como ela seria transformada/adaptada para um requisito de qualidade IEEE 830.

* **Requisito Bruto (Elicitação)**: "Cobra preço normal até um tempo e depois cobra adicional."
* **Análise de Qualidade**:
  * Correto? Validamos com o dono do shopping que moto tem isenção de 2h e carro de 4h? Sim.
  * Não Ambíguo? "Hora adicional" é fração de hora? Esclarecemos: fração de 15 minutos conta como hora cheia.
  * Completo? Definimos o teto da diária (estadia de 24h)?

Resultado na ERS (Seção 3.1 - Requisitos Funcionais):

**RF-EST-010**: Cálculo de Tarifa por Tempo (*Requisito Funcional Estrutura*)
**Descrição**: O sistema deve calcular o valor a pagar com base no tipo de veículo e na duração da estadia (diferença entre horário de saída e horário de entrada, arredondada para cima na fração de hora).

**Entradas**: Tipo do Veículo (Moto ou Carro), Data/Hora de Entrada, Data/Hora de Saída.

**Processamento** (Tabela de Decisão IEEE 830):

|Tipo Veículo|Duração (D)|Cálculo do Valor (V)|
|------------|-----------|--------------------|
|Moto|D <= 15 min|V = `R$ 0,00` (Regra de Carência - RN07)|
|Moto|15 min < D <= 2h|V = `R$ 8,00`|
|Moto|D > 2h|V = `R$ 8,00 + (ceil(D−2h) ∗ R$ 8,00 + (ceil(D−2h) ∗ R$ 2,00)`|
|Carro|D <= 15 min|V = `R$ 0,00` (Regra de Carência - RN07)|
|Carro|15 min < D <= 4h|V = `R$ 12,00`|
|Carro|D > 4h|V = `R$ 12,00 + (ceil(D−4h) ∗ R$ 12,00 + (ceil(D−4h) ∗ R$ 2,00))`|

**Saída**: Valor monetário em reais (R$).

**Prioridade**: Essencial (Must Have).
Rastreabilidade: Origem: RN05, RN06, RN07 (Regras de Negócio).

> **Perceba a diferença**: a *Regra de Negócio* é a lei. O *Requisito* na ERS (no padrão IEEE 830) *é a especificação completa, verificável e tabelada dessa lei*, pronta para o programador codificar e o testador escrever o script de teste automatizado.

## 11 - Priorização de Requisitos

Vale lembrar que para Engenharia de Software I, focamos na técnica *MoSCoW*. Se nos falta recursos ou tempo, então precisamos analisar e
priorizar os requisitos. *O quê é importante?* *O quão importante ele é?* *O quanto custa a implementação e a manutenção?* *Quanto tempo para implementar?*

### 11.1 - Porque priorizar?

Antes das técnicas, é preciso entender a dor que a priorização resolve. *Wiegers & Beatty* (2013) apresentam a **"Pirâmide do Desperdício"** em projetos sem priorização:

* 45% das funcionalidades entregues nunca são usadas pelos usuários (Standish Group, CHAOS Report).
* 19% são usadas raramente.
* Apenas 7% são usadas sempre.

**Conclusão**: Sem priorização, desperdiçamos mais da metade do orçamento construindo software que ninguém usa.

Os 4 Fatores que Competem (Triângulo de Prioridades de Davis):

* **Valor para o Negócio**: Quanto dinheiro isso gera ou economiza?
* **Custo/Esforço Técnico**: Quantas horas de desenvolvimento?
* **Risco**: Se não fizermos, o que pode dar errado? (Legal, Segurança, Técnico).
* **Urgência**: Precisa ser agora ou pode esperar?

Cada técnica de priorização tenta equilibrar esses fatores de forma objetiva.

### 11.2 - Técnicas qualitativas (Baseadas em Opinião Estruturada)

Temos uma a matriz de valor x esforço visa tornar a decisão de priorização mais objetiva, com menos “eu acho”.

Imagine um plano cartesiano onde classificamos cada requisito da ERS em dois eixos:

* **Eixo Vertical (Valor)**: Representa o benefício que o requisito traz. Pode ser valor financeiro, satisfação do usuário ou alinhamento estratégico.
* **Eixo Horizontal (Esforço)**: Representa o custo de implementação. Inclui tempo de desenvolvimento, recursos financeiros, complexidade técnica e riscos.

<img src="https://pt.smartsheet.com/sites/default/files/styles/1300px/public/2025-05/IC-Simple-Impact-Effort-Matrix-Template-58143-EXAMPLE-EXCEL_PT.webp?itok=yKoF6Rvn" style="width: 80%" title = "Imagem 4 - Método de V"/>

Os 4 Quadrantes da Matriz:

* **Ganhos Rápidos (Quick Wins)**
  * **Perfil**: Alto Valor e Baixo Esforço.
  * **Ação**: Faça imediatamente.
  * **Exemplo**: Adicionar um botão de "Esqueci minha senha". É relativamente simples de implementar e resolve um problema crítico para o usuário.
* **Grandes Projetos (Major Projects)**
  * **Perfil**: Alto Valor e Alto Esforço.
  * **Ação**: Planeje com cuidado. São as funcionalidades "core" do sistema.
  * **Exemplo**: Desenvolver o módulo de processamento de pagamentos criptografados. Agrega muito valor, mas exige meses de engenharia.
* **Preenchimento de Lacunas (Fill-ins / Low Priority)**
  * **Perfil**: Baixo Valor e Baixo Esforço.
  * **Ação**: Faça apenas se sobrar tempo (ou se a equipe estiver ociosa entre grandes tarefas).
  * **Exemplo**: Alterar a cor de um ícone secundário ou adicionar uma animação sutil no menu lateral.
* **Tarefas Ingratas (Money Pit / Thankless Tasks)**
  * **Perfil**: Baixo Valor e Alto Esforço.
  * **Ação**: Descarte ou reavalie.
  * **Exemplo**: Integrar o sistema com uma rede social que ninguém mais usa. O esforço de API é alto e o retorno para o negócio é quase nulo.

#### 11.2.1 - MoSCoW (Clegg & Barker, 1994)

**Regra de Ouro do MoSCoW**: O time deve alocar percentuais máximos de esforço por categoria:

* **Must Have (Obrigatório)**: Máximo de 60% do esforço total. *Sem eles o sistema não faz sentido.*
  * Se o "Must" consumir 90% do esforço, você não tem um MVP, tem um sistema completo disfarçado. É preciso negociar para rebaixar alguns itens a Should.
* **Should Have (Importante)**: Cerca de 20% do esforço. *Importantes, mas podemos “segurar” o sistema sem eles.*
  * Diferenciação chave: um "Should" não bloqueia o Go-Live, mas causa dor significativa. Ex: "Relatório de Vendas por Período". Dá para fazer manual no Excel por algumas semanas, mas é doloroso.
* **Could Have (Desejável)**: Cerca de 20% do esforço. *Queremos, mas serão feitos apenas se sobrar tempo e recursos.*
  * Se sobrar tempo. Se o time está 100% dentro do cronograma, entra. Se atrasou, é o primeiro a ser cortado sem dó.
* **Won't Have (Não para agora)**: Fora do escopo. Apenas para deixar claro que foi discutido e conscientemente excluído. *Lembrando que pode ser adicionado em outras versões*.

Exemplo Prático (App de Mobilidade):

|ID|Requisito|MoSCoW|Justificativa (Regra de Ouro)|
|--|---------|------|-----------------------------|
|RF01|Solicitar Corrida (Origem/Destino)|M (Must)|Sem isso, o app não existe. Ocupa 15% do esforço.|
|RF02|Pagamento via Cartão de Crédito|M (Must)|Essencial para monetização. Ocupa 20% do esforço.|
|RF03|Pagamento via PIX|S (Should)|Importante, mas o cartão cobre 80% dos casos. Pode vir na Release 2 (15% esforço).|
|RF04|Chat com Motorista|S (Should)|Importante para resolver problemas, mas a ligação telefônica quebra o galho (10% esforço).|
|RF05|Agendamento de Viagem Futura|C (Could)|Diferencial, mas não essencial para validar o negócio (25% esforço).|
|RF06|Recompensas Gamificadas (badges)|W (Won't)|Interessante, mas não agora. Foco no básico.|

#### 11.2.2 - Modelo de Kano (Noriaki Kano, 1984)

Kano não prioriza por importância temporal, mas por impacto emocional no cliente. É fundamental para decidir o que realmente encanta vs. o que é obrigação.

As Três Categorias Principais:

|Categoria|Descrição|Comportamento do Cliente|Exemplo (Estacionamento)|
|---------|---------|------------------------|------------------------|
|Básico (Must-Be)|Obrigatório. Se faltar, o cliente se irrita. Se tiver, ele não nota (é neutro).|"Óbvio que a cancela abre quando eu pago. Se não abrir, vou reclamar."|RN02 (Entrada de veículos emitindo ticket), RN04 (Validação de ticket).|
|Desempenho (One-Dimensional)|Quanto mais, melhor. Linear.|"Quanto mais rápido abrir a cancela, mais satisfeito eu fico."|Velocidade de leitura do QR Code no totem de saída (Quanto menor o tempo, maior a satisfação).|
|Atrativo (Attractive)|Inesperado. Se faltar, o cliente não sente falta. Se tiver, ele se encanta (fica extremamente satisfeito).|"Nossa, o aplicativo lembrou onde estacionei da última vez e já sugeriu a vaga!"|Conectar o App do shopping ao estacionamento e sugerir a vaga mais próxima do elevador baseado no histórico do usuário.|

>**A Armadilha Temporal de Kano**:
>O que é *"Atrativo"* hoje, vira *"Desempenho"* amanhã e *"Básico"* depois de amanhã.
>
>* **2008**: App de banco fazer depósito por cheque fotografado era Atrativo (Nubank nem existia).
>* **2018**: Virou Desempenho (bancos tradicionais correram atrás).
>* **2024**: É Básico. Se um banco digital lançar sem isso, é motivo de chacota.
>
>**Aplicação na Priorização**: Invista uma parte do esforço da Release 1 em um ou dois requisitos Atrativos. Eles são o seu diferencial competitivo. Mas nunca às custas dos Básicos. Um produto com Básicos faltando é um produto quebrado.

### 11.3 - Técnicas Quantitativas (Baseadas em Fórmulas e Matrizes)

#### 11.3.1 - Matriz de Priorização (Wiegers & Beatty, Cap. 16)

A abordagem mais sistemática para pequenas e médias listas de requisitos. Cada requisito recebe notas de 1 a 5 em quatro dimensões. A prioridade é a média ponderada.

Dimensões Avaliadas:

* **Benefício Relativo (B)**: Quanto valor entrega ao negócio? (5 = Altíssimo, 1 = Baixíssimo).
* **Penalidade Relativa (P)**: Qual o dano se não for implementado? (5 = Multa legal, perda de clientes; 1 = Ninguém sente falta).
* **Custo Relativo (C)**: Quanto custa implementar? (5 = Altíssimo custo/esforço; 1 = Custo baixo, muda uma linha de CSS).
* **Risco Técnico (R)**: Qual a chance de dar errado ou atrasar? (5 = Incerteza total, depende de PoC; 1 = Tecnologia dominada).

**Fórmula de Priorização (Prioridade = Valor / Esforço)**:
$$
Prioridade = \frac{(Benefício * Peso_B) + (Penalidade * Peso_P)}{(Custo * Peso_C) +(Risco * Peso_R)}
$$

**Exemplo Prático (Sistema de Vendas - Caixa/PDV)**:
Suponha os pesos: Benefício = 2, Penalidade = 1, Custo = 1, Risco = 1 (dando mais peso ao valor que ao esforço, se a empresa é de inovação).

|Requisito|Benefício (1-5)|Penalidade (1-5)|Custo (1-5)|Risco (1-5)|Fórmula|Prioridade|
|---------|---------------|----------------|-----------|-----------|-------|----------|
|RF01 - Registrar Venda (RN05)|5|5|2|1|(10+5)/(2+1) = 15/3|5.00|
|RF02 - Pagamento via PIX|4|3|3|1|(8+3)/(3+1) = 11/4|2.75|
|RF03 - Vale Alimentação|2|2|3|1|(4+2)/(3+1) = 6/4|1.50|
|RF04 - Dashboard Gerencial Bonito|3|1|4|3|(6+1)/(4+3) = 7/7|1.00|

> **Análise do Resultado**: A equipe deve atacar `RF01` imediatamente (Quick Win, baixo custo, alto valor). `RF04` (Dashboard bonito) tem baixa prioridade: é caro, arriscado e a penalidade de não ter é mínima (o gerente usa relatório feio por enquanto).

#### 11.3.2 - WSJF (Weighted Shortest Job First — Priorização Ágil SAFe)

Método dominante no framework SAFe (Scaled Agile Framework), mas aplicável em qualquer backlog ágil. A lógica é brutalmente financeira: faça primeiro o que gera mais dinheiro no menor tempo possível.

**Fórmula do WSJF**:
$$
WSJF = \frac{Custo-do-Atraso}{Duracao-do-Trabalho}
$$
Onde o **Custo do Atraso** (Cost of Delay) é a soma de três fatores:

* **Valor para o Negócio/Usuário**: A funcionalidade gera receita? Fideliza?
* **Criticidade Temporal (Urgência)**: O valor decai com o tempo? Tem uma data limite (Lei, Black Friday)?
* **Redução de Risco/Habilitação**: Isso libera outras equipes? Reduz risco regulatório?

Exemplo (App de Mobilidade — 3 Funcionalidades no Backlog):

|Funcionalidade|Valor Neg.|Urgência|Redução Risco|Custo do Atraso (Soma)|Duração (Sprints)|WSJF|
|--------------|----------|--------|-------------|----------------------|-----------------|----|
|A: Cadastro de Motorista|8|10|10|28|2|14.0|
|B: Pagamento via PIX|13|5|5|23|5|4.6|
|C: Algoritmo de Surge Pricing|13|13|8|34|13|2.6|

> **Decisão WSJF**: Mesmo que o Pagamento via PIX (B) e o Surge Pricing (C) tenham alto valor, o Cadastro de Motorista (A) tem o maior WSJF (14.0). Por quê?
>
>* Sem motorista cadastrado, não há oferta de carros. Ele habilita todo o resto (Redução de Risco = 10).
>* É rápido de fazer (2 sprints).
>* "**Coma as sobremesas primeiro**": WSJF força o time a entregar valor rápido e constantemente, evitando projetos gigantescos que só entregam no final.

### 11.4 - Dinâmica de Priorização em Grupo (O Processo Humano)

Priorização não é um ato solitário do analista. *Wiegers & Beatty* descrevem dinâmicas para evitar vieses.

* **Planning Poker** (para esforço, mas impacta prioridade)
  * O time técnico estima esforço (Story Points). Isso alimenta o denominador da fórmula WSJF ou da Matriz.
* **Buy a Feature** (Compre uma Funcionalidade)
  * Dinâmica com stakeholders de negócio.
  * Cada stakeholder recebe um orçamento fictício (ex: R$ 1000 em dinheiro de mentira).
  * Cada requisito tem um preço (baseado no custo de desenvolvimento).
  * Eles "compram" os requisitos que querem ver implementados.
    * **Resultado**: O que ninguém comprou é "Won't Have". O que esgotou rapidamente é "Must Have". Isso elimina o "tudo é prioritário" porque força escolhas reais com recurso limitado.
* **Votação por Pontos** (Dot Voting)
  * Cada stakeholder recebe 5 adesivos (dots). Os requisitos são colados na parede. Os stakeholders colam seus dots nos que julgam prioritários. Visual, rápido e democrático. Ideal para pré-priorizar antes de aplicar uma técnica quantitativa.

### 11.5 - O Anti-Padrão: "Tudo é Prioridade Máxima"

Toda equipe de requisitos enfrenta o cliente que diz: "Todos esses 50 requisitos são críticos. Preciso de todos para ontem."

**Resposta da Engenharia de Requisitos (*Wiegers, 2013*)**:
> **"Se tudo é prioridade, nada é prioridade**. Prioridade implica escolha, e escolha implica abdicar de algo. Vamos ajudá-lo a decidir o que doerá menos abdicar."

**Técnica de Desempate (Desbloqueio)**: Se o cliente insiste que dois itens são igualmente críticos, use o critério "Sequenciamento por Dependência": "Qual desses dois, se ficar pronto, habilita o outro a começar?" Isso quebra o empate, pois um deles será predecessor.

### 11.6 -  Exemplo Integrado: Aplicando no Sistema de Vendas

Imagine que somos a equipe de requisitos do nosso sistema de PDV. Temos 6 requisitos brutos para priorizar.

|ID|Requisito|Kano (O que é?)|MoSCoW|Matriz B/C (Valor)|
|--|---------|---------------|------|------------------|
|RF01|Registrar venda de produtos cadastrados (RN05/06)|Básico|M (Must)|Alto benefício, baixo custo.|
|RF02|Aceitar PIX (RN01)|Básico (hoje)|M (Must)|Alto benefício, médio custo.|
|RF03|Parcelamento no crédito (RN03)|Básico (Brasil)|M (Must)|Alto benefício, médio custo.|
|RF04|Pagamento segmentado (RN04)|Desempenho|S (Should)|Médio benefício, alto custo (complexo).|
|RF05|Emitir relatório de vendas em tempo real|Atrativo (gerente)|C (Could)|Médio benefício, alto custo (dashboard).|
|RF06|Integração com programa de fidelidade|Atrativo (cliente)|W (Won't) - Release 1|Alto benefício futuro, mas baixa urgência.|

#### 11.6.1 - Plano de Release (Combinando as Técnicas)

>* **Release 1 (MVP - Semana 1 a 6)**: RF01 + RF02 + RF03. São os Básicos de Kano. Sem eles, o sistema é inútil. Classificados como Must Have.
>* **Release 2 (Semana 7 a 10)**: RF04. É Desempenho. Importante, mas o sistema sobrevive sem ele no primeiro mês (o cliente faz dois pagamentos separados e depois acerta manualmente, doloroso mas possível).
>* **Backlog (Futuro)**: RF05 e RF06. Atrativos que podem ser prototipados e testados depois que o core estiver estável e gerando receita.
>
> **Este é o poder de combinar as técnicas**: Kano explica o porquê (psicologia do usuário), MoSCoW define o quando (Release), e a Matriz B/C justifica o investimento (finanças).

## 12 - ISO 12207 - Uma Constituição, Não um Manual de Instruções

A confusão mais comum é achar que a ISO 12207 diz *"faça assim"*. Na verdade, ela diz "*estes são os processos que você deve definir*". Ela fornece um framework de processos que cada organização deve adaptar (tailoring) ao seu contexto. Define ao todo **25 processos, 95 atividades e 325 tarefas**.

* Uma **tarefa** é uma ação com entradas e saídas. Pode ser um requisito (deve, shall), recomendação (deveria, should) ou permissão (pode, may).
* Uma **atividade** é um conjunto de tarefas.
* Um **processo** é um conjunto de atividades relacionadas

>**Os Dois Objetivos Estratégicos**:
>
>* **Linguagem Comum**: Um comprador pode exigir do fornecedor: "Seu processo de Garantia de Qualidade (Processo 7.2.3) está em conformidade com a ISO 12207?" Isso cria um entendimento global.
>* **Completeza**: Ao mapear seu ciclo de vida contra a 12207, você descobre buracos. "Estamos esquecendo o processo de Auditoria (7.2.8)?" "Temos processo formal de Validação (7.2.6) ou só de Verificação (7.2.5)?"

### 12.1 - A estrutura do processo

A edição de 2017 reorganizou os processos em quatro grupos conceituais. Vamos percorrê-los como uma jornada lógica.

#### 12.1.1 - Grupo 1: Processos de Acordo (Agreement Processes)

São os processos de contratação. **Definem a relação cliente-fornecedor**. Antes de qualquer linha de código, existe um acordo.

|Processo|Descrição|Exemplo Concreto|
|--------|---------|----------------|
|Aquisição (Acquisition)|Atividades do **cliente** (adquirente): definir necessidade, emitir RFP (Request for Proposal), selecionar fornecedor, aceitar o produto.|O Shopping contrata o desenvolvimento do Sistema de Estacionamento. O gerente de TI do shopping executa este processo: escreve o edital, avalia as propostas de software houses.|
|Fornecimento (Supply)|Atividades do **fornecedor**: preparar proposta, negociar contrato, entregar o software, dar suporte.|A Software House "ParkTech" responde ao edital, assina o contrato e se compromete a entregar o sistema com as regras RN01 a RN10.|

#### 12.1.2 - Grupo 2: Processos Organizacionais (Organizational Project-Enabling)

São processos de gestão que acontecem fora do projeto individual, no nível da empresa. **Criam a infraestrutura para que os projetos existam**.

|Processo|Descrição|Exemplo na Prática|
|--------|---------|------------------|
|Gestão do Modelo de Ciclo de Vida (Life Cycle Model Management)|A empresa define, mantém e melhora seus modelos de processo (ex: "Usamos Scrum com sprints de 2 semanas" ou "Usamos Cascata com marcos formais").|A ParkTech decide que todo projeto seguirá o Scrum. Este processo existe independentemente do projeto do Shopping.|
|Gestão de Infraestrutura (Infrastructure Management)|Prover hardware, software, ferramentas, licenças, ambientes de desenvolvimento e homologação.|A ParkTech provisiona servidores na AWS para o time de desenvolvimento, compra licenças do Jira e do Figma.|
|Gestão de Portfólio (Portfolio Management)|Selecionar quais projetos a empresa vai investir, dado seu orçamento e estratégia.|A diretoria da ParkTech decide se aceita o projeto do Shopping (que paga pouco, mas é vitrine) ou prioriza o projeto da Fintech (que paga mais).|
|Gestão de Recursos Humanos (Human Resource Management)|Contratar, treinar, alocar e avaliar a equipe.|Contratar um Especialista em OCR para o módulo de leitura de placas do estacionamento.|
|Gestão da Qualidade (Quality Management)|Definir a política de qualidade da empresa. Estabelecer métricas, auditorias internas.|A ParkTech define que todo código deve ter 80% de cobertura de testes unitários. Isso é uma política organizacional, não de um projeto específico.|
|Gestão do Conhecimento (Knowledge Management)|Capturar lições aprendidas, documentar, fazer wiki corporativa.|Após o projeto do Estacionamento, a equipe documenta os problemas com a integração da cancela (protocolo RS-485) para que o próximo projeto de IoT não sofra as mesmas dores.|

#### 12.1.3 - Grupo 3: Processos de Projeto Técnico (Technical Management)

Estes sim são os **processos dentro do projeto**. É aqui que a engenharia de software acontece no dia a dia.

|Processo|Descrição|Exemplo no App de Mobilidade|
|--------|---------|----------------------------|
|Planejamento do Projeto (Project Planning)|Definir escopo, cronograma, recursos, orçamento. Produz o Plano de Projeto.|Definir que o App de Mobilidade terá 6 sprints de 2 semanas. Sprint 1: Cadastro; Sprint 2: Solicitar Corrida.|
|Avaliação e Controle (Project Assessment and Control)|Monitorar progresso, comparar planejado vs. realizado, agir nos desvios. Reuniões de status.|Daily Scrum: O time reporta que o algoritmo de matching está atrasado. O Scrum Master decide alocar mais um desenvolvedor.|
|Tomada de Decisão (Decision Management)|Estruturar decisões complexas (ex: análise de trade-off). Formalizar quem decide o quê.|O arquiteto decide se usa Firebase ou WebSocket para a comunicação em tempo real motorista-passageiro. Documenta os critérios da decisão.|
|Gestão de Riscos (Risk Management)|Identificar, analisar, mitigar e monitorar riscos.|Risco Técnico: "A API de geolocalização do Google pode ter latência alta em áreas rurais." Mitigação: Implementar cache de coordenadas e fallback para GPS nativo.|
|Gestão da Configuração (Configuration Management)|Controlar versões de código, documentos, ambientes. Baseline de requisitos.|Uso de Git. A versão 1.0 da ERS do App é "baselineada" (congelada) no SharePoint. Qualquer mudança passa por um Change Request.|
|Gestão da Informação (Information Management)|Como os dados do projeto (documentos, e-mails, decisões) são armazenados, versionados e recuperados.|Todos os documentos do projeto ficam no Confluence, organizados por sprint.|
|Medição (Measurement)|Coletar métricas para avaliar qualidade, progresso e desempenho.|Métricas: Velocidade do time (Story Points por Sprint), Densidade de defeitos (bugs por módulo), Cobertura de testes.|
|Garantia da Qualidade (QA - Quality Assurance)|Auditoria independente para garantir que os processos estão sendo seguidos. Foco no processo.|O QA Manager audita se o time está realmente fazendo code review antes do merge, como manda o processo organizacional.|
|Verificação (Verification)|O produto foi construído corretamente? (Conformidade com a especificação).|O testador executa o caso de teste CT-045 e confirma que o cálculo do frete grátis (RF02) bate com a tabela da ERS.|
|Validação (Validation)|O produto certo foi construído? (Atende à necessidade real do usuário?).|Teste de aceite com o cliente real. O dono do shopping usa o sistema de estacionamento em um ambiente de homologação e diz: "É isso mesmo que eu queria."|
|Revisão Técnica (Technical Review)|Inspeções por pares para encontrar defeitos cedo.|Revisão de Código (Pull Request), Revisão de Arquitetura, Walkthrough de requisitos.|

#### 12.1.4 - Grupo 4: Processos de Software (Technical Software)

São os processos **específicos da engenharia de software**, do nascimento à aposentadoria do código.

|Processo|Descrição|Conexão com Nossos Estudos|
|--------|---------|--------------------------|
|Análise de Requisitos do Software (Software Requirements Analysis)|Elicitar, analisar, especificar e validar os requisitos. Produz a ERS (IEEE 830).|É aqui que aplicamos Story Mapping, Prototipação, MoSCoW, e geramos o documento ERS.|
|Projeto de Arquitetura do Software (Software Architectural Design)|Definir componentes, módulos, interfaces, banco de dados. Decisões de alto nível.|Definir que o App de Mobilidade terá um back-end em microsserviços (Serviço de Pagamento, Serviço de Matching, Serviço de Notificação) comunicando via REST.|
|Projeto Detalhado do Software (Software Detailed Design)|Projetar cada módulo em detalhes: algoritmos, estruturas de dados internas.|Desenhar o algoritmo exato da `CalcularTarifa()` (tabela de decisão do Estacionamento) no diagrama de classes.|
|Construção do Software (Software Construction)|Codificação e testes unitários.|O desenvolvedor escreve a classe `TicketService.java` e os testes unitários `TicketServiceTest.java` com JUnit.|
|Integração do Software (Software Integration)|Juntar os módulos e testar a comunicação entre eles.|Integrar o módulo de pagamento com o módulo de emissão de nota fiscal. Testar se ao pagar com PIX a nota é emitida automaticamente.|
|Teste do Software (Software Testing)|Testes de sistema, aceite, performance, segurança. Executar a verificação e validação.|Testar o sistema de estacionamento completo: emitir ticket, validar com desconto de lojista (`RN0X`), pagar, sair.|
|Implantação do Software (Software Installation)|Colocar o software no ambiente de produção. Migrar dados. Treinar usuários.|Instalar os totens no shopping, configurar a rede, migrar a base de clientes do sistema antigo.|
|Operação do Software (Software Operation)|Manter o sistema rodando no dia a dia. Monitorar, fazer backup.|O time de operações monitora se as cancelas estão online. Se uma cancela para de responder, um alerta é disparado.|
|Manutenção do Software (Software Maintenance)|Corrigir defeitos, adaptar a novas leis, melhorar performance.|O governo muda a lei de nota fiscal. O time de manutenção altera o layout da NFC-e. Surge a Release 1.1.|
|Descontinuação do Software (Software Disposal)|Aposentar o sistema com segurança. Migrar/arquivar dados.|O sistema legado de estacionamento é desligado. Os dados de 5 anos são migrados para um data lake de arquivo morto, em conformidade com a retenção fiscal.|

### 12.2 - Mapa visual

```text
┌──────────────────────────────────────────────────────────────┐
│              PROCESSOS ORGANIZACIONAIS (Grupo 2)             │
│  Gestão de Portfólio, Infraestrutura, RH, Qualidade,         │
│  Conhecimento, Ciclo de Vida                                 │
│  (Acontecem FORA do projeto, no nível da empresa)            │
└──────────────────────────┬───────────────────────────────────┘
                           │ (Habilitam)
┌──────────────────────────▼───────────────────────────────────┐
│               PROCESSOS DE ACORDO (Grupo 1)                  │
│  Aquisição (Cliente) ←──────────→ Fornecimento (Fornecedor)  │
│  (Contratam o projeto)                                       │
└──────────────────────────┬───────────────────────────────────┘
                           │ (Disparam)
┌──────────────────────────▼───────────────────────────────────┐
│         PROCESSOS DE PROJETO TÉCNICO (Grupo 3)               │
│  Planejamento, Avaliação, Decisão, Riscos, Configuração,     │
│  Medição, QA, Verificação, Validação, Revisão                │
│  (Gerenciam o projeto do início ao fim)                      │
└──────────────────────────┬───────────────────────────────────┘
                           │ (Executam)
┌──────────────────────────▼───────────────────────────────────┐
│            PROCESSOS DE SOFTWARE (Grupo 4)                   │
│  Requisitos → Arquitetura → Projeto Detalhado → Construção   │
│  → Integração → Teste → Implantação → Operação → Manutenção  │
│  → Descontinuação                                            │
│  (Constroem e sustentam o produto de software)               │
└──────────────────────────────────────────────────────────────┘
```

### 12.3 - Tailoring (Adaptação): A Chave para Usar a ISO 12207 sem Burocracia

A norma inteira tem mais de 200 páginas. Ninguém aplica tudo. A Seção 5 da ISO 12207:2017 trata do Tailoring — a adaptação para o contexto. A beleza da 12207 é que ela serve tanto para uma startup de 3 pessoas quanto para a NASA.

#### 12.3.1 - Exemplo de Tailoring para um Projeto Ágil (Startup)

|Processo da ISO 12207|Ação de Tailoring|
|---------------------|-----------------|
|Planejamento do Projeto|**Simplificado**. Fazemos um Product Backlog priorizado e um Sprint Plan. Sem documento de 50 páginas.|
|Revisão Técnica|**Informal**. Code Review no GitHub, pair programming. Sem ata formal.|
|Gestão de Riscos|**Leve**. Quadro de riscos visível no Kanban, revisitado a cada Sprint Planning.|
|Verificação vs. Validação|**Unificados**. Testes automatizados + Sprint Review com o cliente. Sem separação formal de equipes.|

#### 12.3.2 - Exemplo de Tailoring para Software Embarcado Crítico (Medicina/Aviação)

|Processo da ISO 12207|Ação de Tailoring|
|---------------------|-----------------|
|Verificação e Validação|**Rigor Máximo**. Equipes independentes. Cada requisito rastreado a um caso de teste. Evidência documental obrigatória.|
|Gestão de Riscos|**Formal**. FMEA (Failure Mode and Effects Analysis). Cada risco com probabilidade e severidade calculadas.|
|Gestão da Configuração|**Estrita**. Baseline de código congelada. Toda mudança passa por um Change Control Board (CCB).|

### 12.4 - Conexão com Nossos Exemplos: O Ciclo de Vida do Estacionamento

Vamos mapear o sistema de estacionamento contra os Processos de Software (Grupo 4):

|Fase do Processo (ISO 12207)|Atividade Real no Projeto|
|----------------------------|-------------------------|
|Análise de Requisitos|Elicita as 10 Regras de Negócio (RN01-RN10), priorização com MoSCoW, escreve a ERS no padrão IEEE 830, prototipação do totem.|
|Projeto de Arquitetura|Decisão: Back-end em Java Spring Boot, Front-end do totem em React, Banco PostgreSQL, Comunicação com a cancela via protocolo serial RS-485.|
|Projeto Detalhado|Desenha a classe `Ticket`, a interface `IPagamento`, o algoritmo `CalcularTarifa()` com a tabela de decisão.|
|Construção|Codifica `TicketService.java`, `PagamentoPIXService.java`, `CancelaController.java`. Escreve testes unitários.|
|Integração|Conecta o totem de saída com o servidor de pagamentos. Testa: "Ao pagar com PIX, a cancela abre em menos de 2 segundos?"|
|Teste|Testa o sistema completo no laboratório, simulando 100 tickets simultâneos. Valida com o gerente do shopping a usabilidade do totem.|
|Implantação|Instala 5 totens no shopping, configuramos a rede, treina os operadores do caixa manual (para o caso de extravio).|
|Operação|O sistema está no ar. Monitora o dashboard: 200 carros/dia, tempo médio de saída 15 segundos. Backup noturno automático.|
|Manutenção|O shopping inaugura uma nova ala. Adiciona mais 2 totens. Corrigi um bug onde a carência (`RN0X`) não funcionava entre 23:45 e 00:15 (virada do dia).|

## Dúvidas

### 1. O que foi a crise de Software ? E quais foram as causas?

A "crise do software" foi um termo cunhado na primeira conferência da OTAN sobre Engenharia de Software, em 1968, para descrever um problema generalizado que afetava a indústria de software. A definição clássica, endossada pela visão de Pressman, é a de que os **projetos de software estavam se tornando grandes e complexos demais para serem gerenciados com as abordagens "amadoras" e intuitivas da época**. Na prática, a crise se manifestava por uma série de sintomas recorrentes que tornavam o desenvolvimento de software uma atividade de altíssimo risco . Os softwares eram, cronicamente :

* **Entregues com atraso**: Os prazos nunca eram cumpridos.
* **Acima do orçamento**: Os custos extrapolavam em muito as estimativas iniciais.
* **De baixa qualidade e baixa confiabilidade**: O software entregue era cheio de defeitos.
* **Com requisitos não atendidos**: O produto final não resolvia os problemas do cliente ou do usuário .
* **Difíceis de manter**: O código era complexo, desorganizado e sem documentação, tornando qualquer correção ou melhoria futura um pesadelo .

Pressman também notou que o perfil do programador havia mudado, passando de um trabalho solitário para um esforço de equipe, mas sem que as práticas de gestão e técnicas tivessem evoluído para dar suporte a essa nova realidade

As causas da crise do software não são atribuídas a um único fator, mas a uma confluência de mudanças tecnológicas e práticas inadequadas. Segundo o contexto da obra de Pressman, podemos agrupar as causas da seguinte forma:

#### 1.1. O "Gargalo" do Hardware vs. Software

Esta foi a grande causa estrutural. Enquanto o hardware evoluía exponencialmente com a introdução dos microchips, tornando-se mais barato e poderoso, o software não conseguia acompanhar esse ritmo .

* **Aumento da complexidade**: O hardware mais potente permitiu a criação de sistemas de software muito mais complexos e ambiciosos (como sistemas de tempo real e de controle militar), para os quais não havia métodos de desenvolvimento maduros .
* **Demanda crescente**: A redução do custo do hardware popularizou os computadores em empresas e outros setores, aumentando dramaticamente a demanda por softwares dos mais variados tipos e para usuários não especialistas, uma heterogeneidade para a qual a indústria não estava preparada .

#### 1.2. Ausência de Métodos e Disciplina

O desenvolvimento de software era visto como uma arte ou uma atividade puramente criativa, sem a aplicação de princípios de engenharia .

* **Falta de planeamento e processos**: Não havia processos definidos, e as fases de levantamento de requisitos, projeto e testes eram negligenciadas. A comunicação com o cliente era frequentemente insuficiente, partindo-se para a codificação com base em ideias vagas . Como Pressman destaca, um gestor que não fomenta a comunicação com o cliente "se arrisca a construir uma elegante solução para um problema equivocado" .
* **Ausência de métricas**: Não se sabia como estimar custos, prazos ou medir a produtividade e a qualidade de forma objetiva . O primeiro livro sobre métricas de software só surgiu em 1976 .

#### 1.3. A "Mão de Obra" e a Gestão Inadequada

A forma como as equipas eram geridas e os profissionais trabalhavam também contribuía para o problema.

* Cultura do "herói" e do "codificador solitário": O desenvolvimento era visto como um esforço individual, com programadores trabalhando de forma isolada, o que se tornou inviável com o aumento da complexidade e do tamanho das equipes .
* Mitos de gestão: Pressman identificou e combateu vários "mitos" que pioravam a crise, como acreditar que adicionar mais programadores a um projeto atrasado resolvia o problema (quando, na verdade, tende a atrasá-lo ainda mais devido à sobrecarga de comunicação), ou que a qualidade só poderia ser avaliada com o programa em funcionamento

#### Principais bibliografias

Pressmann, Esmenger ou Brooks Jr. Eles defendem que ao conhecer o passado, será possível usar pensamento sistêmico como solução para problemas modernos.

### 2. Engenharia de Software, como é aplicada no mercado?

A teoria raramente se aplica de forma pura no mercado, que é mais dinâmico e adaptado às realidades de cada negócio. As principais diferenças e nuances são:

#### 2.1. Modelos de Ciclo de Vida (Metodologias)

Na teoria, estudamos modelos como Cascata, Espiral, Incremental. No mercado, o que impera hoje são as metodologias ágeis (Scrum, Kanban, XP).

* Em vez de fases sequenciais e longas, o trabalho é dividido em pequenos ciclos (sprints) . Em cada sprint, você passa por todas as etapas (requisitos, design, código, teste) de forma acelerada para entregar uma pequena parte funcional do software.
* Isso torna o processo mais flexível e adaptável a mudanças, algo que os modelos tradicionais (como o Cascata) não conseguem lidar bem.

#### 2.2. A Divisão do Trabalho (Especialização x Generalização)

Na teoria, um engenheiro de software pode fazer um pouco de tudo. Na prática, em empresas de médio e grande porte, o trabalho é mais especializado, embora a linha seja tênue:

* **Analista de Requisitos / Product Owner (PO)**: Foca nas etapas iniciais (levantamento de requisitos) e na priorização do que será desenvolvido, agindo como a "voz do cliente" dentro do time.
* **Arquiteto de Software**: Responsável pelas decisões de alto nível do projeto (design da arquitetura), definindo as tecnologias e a estrutura geral do sistema.
* **Desenvolvedor (Programador)**: Foco principal na implementação (codificação) e nos testes de unidade.
* **QA (Quality Assurance) / Testador**: Especialista em testes. Projeta e executa os planos de teste para garantir a qualidade do software.
* **Engenheiro de DevOps**: Foca na implantação, automação e operação do software, garantindo que ele possa ser entregue de forma rápida e confiável (o "como" entregar).
* **Engenheiro de Software (Generalista)**: Comum em startups ou times pequenos, onde uma pessoa pode atuar em várias frentes, desde a conversa com o cliente até a implantação.

#### 2.3. A Manutenção é a "Rainha"

A teoria diz que a manutenção é a fase mais longa. No mercado, isso é uma verdade absoluta. A grande maioria dos engenheiros de software não trabalha em projetos "do zero" (greenfield), mas sim evoluindo e mantendo sistemas legados (brownfield). Grande parte do dia a dia é:

* Corrigir bugs.
* Refatorar código antigo para melhorá-lo.
* Adicionar pequenas funcionalidades a um sistema existente.
* Integrar sistemas diferentes.

#### 2.4. Nem Tudo é Seguido à Risco

Em muitas empresas, principalmente as menores ou com menos maturidade em processos, algumas etapas formais da engenharia de software são "puladas" ou feitas de maneira muito informal:

* A documentação pode ser mínima (resumida a ferramentas como o Jira e comentários no código).
* Os testes podem ser menos rigorosos (foco apenas no teste manual).
* O projeto (design) pode ser feito "na cabeça" ou em um guardanapo, sem uma documentação formal de arquitetura.

### 3. Principais Causas de Cancelamento de Projetos de Software

Os números são impressionantes: cerca de 31,1% dos projetos de software são cancelados antes da conclusão, e apenas 16,2% são entregues no prazo e dentro do orçamento .

#### 3.1 Principais Causas (segundo pesquisas e especialistas)

|Causa|Descrição|Dados|
|-----|---------|-----|
|Gestão de projeto inadequada|Falta de planejamento, controle e liderança eficaz.|47% dos projetos fracassados sofrem com isso .|
|Inflação de escopo (scope creep)|Novos requisitos vão sendo adicionados sem controle, sem ajuste de prazo e orçamento.|Ocorre em 78% dos projetos.|
|Definição de requisitos deficiente|Iniciar o projeto sem saber exatamente o que precisa ser feito.|Mais de 80% dos gerentes admitem lançar produtos sabendo que há falhas.|
|Estimativas irrealistas|Subestimar prazos e custos, gerando atrasos e estouro financeiro.|52,7% dos projetos ultrapassam o orçamento em até 189%.|
|Comunicação insuficiente|Falta de alinhamento entre equipe, stakeholders e clientes.|Considerada por especialistas como a "causa raiz" da maioria das falhas.|
|Escolha da tecnologia errada|Adotar ferramentas ou frameworks que não se adequam ao problema ou que não estão maduros.|—|
|Mudanças fundamentais de recursos|Alterações profundas nos requisitos no meio do projeto, exigindo retrabalho massivo.|—|
|Falta de patrocínio executivo|Sem apoio da alta liderança, o projeto perde prioridade e recursos.|—|
|Conflitos políticos|Disputas internas entre equipes ou departamentos que paralisam decisões.|—|
|Negligência de testes e qualidade|Bugs descobertos tardiamente ou após o lançamento, gerando retrabalho e insatisfação.|—|

### 4. Como Orçar o Desenvolvimento de um Software

Orçar software é uma das atividades mais desafiadora
s da engenharia de software. As principais abordagens são:

#### 4.1. Principais Métodos de Estimativa

|Método|Como Funciona|Quando Usar|
|------|-------------|-----------|
|Estimativa por Analogia|Compara o novo projeto com projetos anteriores similares.|Quando há histórico de projetos semelhantes.|
|Ponto de Função (PF)|Mede o software com base em funcionalidades entregues ao usuário (entradas, saídas, consultas, arquivos, interfaces).|Projetos onde se pode quantificar as funcionalidades.|
|Estimativa por Especialistas|Consulta a especialistas que opinam com base em experiência.|Fase inicial, com pouca informação disponível.|
|Estimativa Paramétrica (COCOMO, SEER-SEM)|Usa fórmulas matemáticas baseadas em linhas de código estimadas e fatores de ajuste.|Projetos de médio a grande porte.|
|Estimativa Ágil (Planning Poker)|A equipe atribui pontos de história (story points) a cada tarefa, baseando-se em complexidade relativa.|Metodologias ágeis (Scrum).|

#### 4.2. Fatores que Influenciam o Custo

* **Complexidade funcional:** Quantidade e complexidade das funcionalidades.
* **Qualidade esperada**: Testes rigorosos, segurança, desempenho.
* **Tamanho da equipe e senioridade**: Profissionais mais experientes custam mais, mas entregam mais rápido e com mais qualidade.
* **Infraestrutura**: Custos de servidores, banco de dados, serviços em nuvem .
* **Integrações**: Conexão com sistemas de pagamento, ERP, APIs externas .
* **Prazos**: Prazos curtos exigem mais recursos paralelos e aumentam custo.

### 5. Frameworks e Templates Mais Usados no Desenvolvimento de Software

Os frameworks são estruturas pré-construídas que fornecem uma base para o desenvolvimento, evitando que você comece "do zero" .

#### 5.1. Classificação por Tipo

|Tipo|Função|Exemplos Populares|
|----|------|------------------|
|Frontend|Interface visual, interação com usuário|React, Vue.js, Angular, Svelte |
|Backend|Lógica de negócio, APIs, banco de dados|Django (Python), Laravel (PHP), Express.js (Node.js), Spring Boot (Java) |
|Fullstack|Frontend + Backend integrados|Next.js (React), Nuxt.js (Vue), Ruby on Rails |
|CSS/UI|Estilização e componentes visuais|Bootstrap, Tailwind CSS |

#### 5.2. Frameworks Mais Populares (2025/2026)

|Framework|Linguagem|Tipo|Uso Principal|
|---------|---------|----|-------------|
|React|JavaScript/TypeScript|Biblioteca frontend|Interfaces dinâmicas e interativas; mantido pelo Meta|
|Next.js|JavaScript/TypeScript|Fullstack (React)|Aplicações com SSR e otimização SEO|
|Vue.js|JavaScript/TypeScript|Frontend progressivo|Curva de aprendizado suave, flexível|
|Angular|TypeScript|Frontend completo|Grandes aplicações empresariais; mantido pelo Google|
|Django|Python|Backend|Desenvolvimento rápido, seguro e com baterias inclusas|
|Laravel|PHP|Backend|Sintaxe elegante, rico ecossistema|
|Spring Boot|Java|Backend|Microserviços e aplicações empresariais Java|
|Ruby on Rails|Ruby|Fullstack|Prototipação rápida, convenção sobre configuração|
|Express.js|JavaScript/Node.js|Backend minimalista|APIs e aplicações Node.js|
|Svelte|JavaScript/TypeScript|Frontend (compilador)|Código mais leve e performático|

#### 5.3. Templates e Ferramentas Complementares

Além dos frameworks, os desenvolvedores utilizam templates (projetos iniciais prontos) e ferramentas que aceleram o desenvolvimento:

|Categoria|Ferramentas/Exemplos|
|---------|--------------------|
|Boilerplates / Starter Kits|HTML5 Boilerplate, Create React App, Next.js starter, Vite templates|
|Infraestrutura em Nuvem|Vercel, Fly.io, DigitalOcean, AWS, Cloudflare|
|Bancos de Dados|PostgreSQL (Supabase, Neon), MongoDB Atlas, PlanetScale|
|Autenticação|Clerk, Auth.js, Supabase Auth|
|Pagamentos|Stripe (global), AbacatePay (Brasil)|
|Monitoramento|Sentry (erros), Uptime Kuma (disponibilidade)|
|E-mails|Resend (transacionais), Loops.so (marketing)|
|Design/Protótipo|Figma, Coolors, Undraw|

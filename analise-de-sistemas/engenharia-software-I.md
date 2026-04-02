# Engenharia de Software I

## 1. Tipos de softwares

De acordo com *Roger S. Pressmann*, a engenharia de software classifica os programas em diferentes categorias de acordo com seu propósito e público-alvo.

Vale ressaltar que através do tempo algumas definições foram mudadas ou atualizadas. Como ***softwares  utilitários*** passaram a fazer parte dos **softwares de sistema**. Assim como **as ferramentas de programação**. Os ***softwares comerciais*** foram redefinidos para **softwares de aplicação**. E por fim, os ***softwares de tempo real*** foram revertidos para os **embutidos e web/mobile**, de acordo como melhor se aplicam de acordo com as novas definições.

| Tipos de Softwares | Uso principal | Exemplo |
|--------------------|---------------|---------|
| Sistema | Feito para atender outros programas. Gerência os recursos de hardware e fornece serviços para as aplicações | S.O. Windows, macOS, Linux; Compiladores (ex: GCC); Drivers de dispositivo |
|Aplicação | Solucionam uma necessidade específica de negócio ou processo para o usuário final | Sistema de Controle de Estoque, Software de RH, ERP (ex: SAP), CRM (ex: Salesforce) |
| Ciêntifico ou de engenharia | Caracterizado por algoritmos de processamento numérico intensivo ("cálculo de massa") para aplicações técnicas | MATLAB, AutoCAD, Simuladores de fenômenos físicos, Software de análise de elementos finitos |
| Embutido (Embedded) | Residente na memória ROM de um produto ou sistema, para controlar suas características e funções para o usuário final | Software do forno micro-ondas, Sistema de injeção eletrônica de automóveis, Firmware de roteadores, placa de arduíno |
| Linhas de produtos |  Projetado para prover uma capacidade específica para uso por muitos clientes diferentes. Os populares *"softwares de prateleira"* | Microsoft Office (processador de texto, planilha), Adobe Photoshop, Jogos de computador |
| Aplicações Web / Mobile | Software que reside e é executado em navegadores web ou em dispositivos móveis, centrados na rede e na computação em nuvem | Gmail, Google Maps, Aplicativo do Instagram, Internet Banking |
| Inteligência Artificial | Utiliza algoritmos não numéricos (como lógica simbólica, redes neurais) para resolver problemas complexos que não são passíveis de computação direta | Sistemas especialistas (para diagnóstico médico), Chatbots (ex: ChatGPT), Sistemas de reconhecimento facial, Algoritmos de robótica | 

#### Por que a classificação mudou?
A principal razão para essa evolução é o próprio avanço da tecnologia. O software se tornou muito mais complexo e "híbrido". A engenharia de software é uma ciência viva e **seus conceitos se atualizam para refletir a realidade do mercado**. Por exemplo:

* **Ferramentas de Programação**: Hoje, um compilador (software de sistema) é desenvolvido e usado dentro de um ambiente de desenvolvimento (IDE), que é um Software de Aplicação. Sua natureza dupla dificulta uma classificação única e isolada .

* **Sistemas de Informação**: Um simples sistema de estoque (antigo "software comercial") hoje roda dentro de um navegador, em nuvem, e pode ser acessado por aplicativo mobile. Ele se tornou uma Aplicação Web/Mobile .

* **Convergência**: Um software embutido no seu carro (categoria clássica) hoje pode se conectar à internet, receber atualizações (como um software de sistema) e rodar aplicativos (como o GPS). As fronteiras ficaram muito mais tênues .

## 2. Etapa de Vida de um Software, teoria e na prática.
Na **teoria**, a engenharia de software abrange e é responsável por todas as etapas do ciclo de vida de um software. O objetivo da **engenharia de software** é justamente aplicar uma *abordagem sistemática, disciplinada e quantificável ao desenvolvimento, operação e manutenção* do software. Ou seja, ela não se preocupa apenas com a programação (codificação), mas com o processo como um todo.

<div style = "text-align: center;">
<img src="https://www.levty.com/blog/assets/post/ciclo-de-vida-do-desenvolvimento-de-software-conheca-cada-uma-das-fases-6655ea6c6269d11f04512c7d/ciclo-software.webp?w=960" alt="Ciclo de Vida Software" style="width: 50%" title = "Imagem 1 - Ciclo de Vida de um Software"/>

*Imagem 1 - Ciclo de Vida de um Software*.
</div>

### Planejamento 
O planejamento é a fase inicial e talvez a *mais crítica* do ciclo de vida de um software. Ele não só *estabelece uma direção clara*, como também *ajuda a evitar problemas futuros*, garantindo que todas as partes envolvidas estejam alinhadas e cientes de suas responsabilidades e expectativas.**É nessa etapa que as bases para todo o projeto são estabelicidas.** E essa etapa é dividida em alguns pontos:
* **Identificação das necessidades e requisitos do projeto**: Antes de iniciar o desenvolvimento é **fundamental compreender as necessidades dos stakeholders e dos usuários finais**. Ela é obtida através de reuniões, entrevistas e pesquisas.
* **Definição dos objetivos de maneira clara e o escopo do trabalho que será realizado**: Após identificar as necessidades, **os objetivos** do projeto devem ser definidos, eles precisam ser **claros, específicos, mensuráveis, alcançáveis, relevantes e temporais(*SMART*)**. E o **escopo** do determinado para que se entenda o que está dentro e fora do alcance do desenvolvimento.
* **Análise da viabilidade e recursos necessários**: Essa análise avalia se o projeto **pode ser realizado**, considerando os *recursos técnicos, financeiros e de tempo*. Pode-se incluir a avaliação de riscos, a alocação de recursos e a análise de custos e benefícios.
* **Criação de um plano de projeto detalhado**: Esse plano criado engloba todas as **atividades, cronogramas, marcos, recursos e responsabilidades**. Para então ele servir como guia para toda equipe de desenvolvimento e para ser usado pela equipe de monitoramento e controle do progresso do projeto.

### Análise de Requisitos
Após a fase de planejamento, é preciso fazer a análise de requisitos, uma etapa crucial para garantir que o software atenda às necessidades dos usuários e stakeholders. Essa fase **envolve uma compreensão detalhada dos requisitos funcionais e não funcionais** do sistema. Ela é fundamental para evitar ambiguidades e mal-entendidos. Uma documentação bem elaborada e a validação contínua com os stakeholders são essenciais para garantir que o desenvolvimento esteja alinhado com as expectativas do cliente.
Vamos explorar os principais aspectos:
* **Coleta e documentação dos requisitos dos usuários**: A coleta é feita através de reuniões, questionários, workshops e reuniões com os stakeholders. E é essencial documentar todas as expectativas e necessidades dos usuários.
* **Entrevistas, questionários e reuniões com stakeholders**: Essas técnicas ajudam a identificar os requisitos específicos e expectativas dos diferentes grupos de interesse. As *entrevistas* individuais podem *revelar insights detalhados*, enquanto os *workshops* colaborativos podem *ajudar a alinhar diferentes perspectivas*.
* **Criação de um documento de requisitos de software (SRS)**: O **SRS** é um documento formal que **descreve todas as funcionalidades e restrições do sistema**. Ele serve como uma *referência para todas as fases subsequentes do SDLC* e garante que todos os envolvidos tenham uma compreensão comum do que será desenvolvido.
* **Importância de entender as necessidades dos usuários finais**: A análise de requisitos precisa focar nas necessidades reais dos usuários finais, garantindo que o software seja útil e relevante. Uma compreensão inadequada dos requisitos pode levar a retrabalho e insatisfação do cliente.

### Design do sistema
Com os requisitos claramente definidos, o próximo passo é transformar esses requisitos em um design detalhado do sistema. A fase de design do sistema **envolve a criação da arquitetura do software, a definição das interfaces de usuário e a modelagem dos dados**. Ela é crítica para garantir que a solução técnica seja robusta e alinhada com os requisitos de negócio. Quando bem planejado **facilita a implementação** e reduz o risco de problemas técnicos durante o desenvolvimento.
Vejamos a seguir os detalhes:
* **Design de arquitetura do sistema**: A arquitetura do sistema **define a estrutura geral do software**, incluindo a divisão em módulos ou componentes, a interação entre eles e a escolha de tecnologias e frameworks. Uma boa arquitetura é **fundamental para garantir a escalabilidade**, desempenho e manutenibilidade do software.
* **Design de interfaces de usuário (UI/UX)**: O design de interfaces de usuário **foca na criação de uma experiência de usuário intuitiva e eficiente**. Pode-se envolver a criação de wireframes, protótipos e a definição de padrões de design. O objetivo é garantir que o software seja fácil de usar e atenda às necessidades dos usuários.
* **Modelagem de dados e design de banco de dados**: A modelagem de dados envolve a **definição das estruturas de dados necessárias para suportar as funcionalidades do sistema**. O design do banco de dados inclui a criação de diagramas de entidade-relacionamento (ERD) e a definição de tabelas, chaves e relacionamentos.
* **Criação de protótipos e wireframes**: Protótipos e wireframes são ferramentas importantes para **visualizar e validar o design do sistema antes da implementação**. Eles permitem que os stakeholders forneçam feedback antecipado e façam ajustes antes que o desenvolvimento real comece.

### Implementação
A fase de implementação é para que as ideias e os planos se transformem em código funcional. Nessa etapa, os **desenvolvedores começam a codificar o software de acordo com o design e os requisitos previamente definidos**. Por isso é a etapa em que a maior parte do esforço de desenvolvimento é concentrada. É crucial **manter a comunicação e a colaboração eficazes** entre os membros da equipe para garantir que o software seja desenvolvido de acordo com os padrões e requisitos estabelecidos.
Vamos explorar os principais aspectos da fase:
* **Codificação e desenvolvimento de software**: Os desenvolvedores utilizam linguagens de programação e ferramentas de desenvolvimento para escrever o código-fonte do software. A implementação deve seguir os padrões de codificação e práticas recomendadas para garantir a qualidade do código.
* **Uso de metodologias de desenvolvimento (Ágil, Scrum, Waterfall, etc.)**: A escolha da metodologia de desenvolvimento **impacta diretamente a maneira como o trabalho é organizado e executado**. Metodologias ágeis, como Scrum, permitem entregas incrementais e feedback contínuo, enquanto o Waterfall segue um processo linear e sequencial.
* **Ferramentas e ambientes de desenvolvimento**: As ferramentas de desenvolvimento incluem IDEs (Integrated Development Environments), sistemas de controle de versão e plataformas de integração contínua (CI). Ambientes de desenvolvimento configurados corretamente são essenciais para a produtividade e colaboração da equipe.
* **Boas práticas de programação e controle de versão**: Boas práticas incluem o **uso de padrões de codificação, revisões de código, testes automatizados e documentação clara**. O controle de versão permite que os desenvolvedores colaborem de forma eficaz, rastreando mudanças no código e revertendo a versões anteriores, se necessário.

### Testes
A fase de testes é essencial para garantir que o software desenvolvido esteja **livre de erros e funcione conforme esperado**. Essa etapa **envolve a verificação e validação do software** por meio de diversos tipos de testes. E é crucial para assegurar que o software seja robusto e esteja pronto para a implantação. Quando bem planejados e executados ajudam a evitar problemas futuros, economizando tempo e recursos a longo prazo.

#### Tipos de Testes (Unitário, Integração, Sistema, Aceitação):
1. **Testes Unitários**: Testam individualmente pequenas partes do código (funções, métodos) para garantir que cada unidade funcione corretamente.
2. **Testes de Integração**: Verificam a interação entre diferentes módulos ou componentes para garantir que funcionem bem juntos.
3. **Testes de Sistema**: Avaliam o sistema completo em um ambiente que simula a produção, verificando se o software atende aos requisitos especificados.
4. **Testes de Aceitação**: Realizados pelos usuários finais para validar se o software atende às suas necessidades e expectativas.
    * **Importância de garantir a qualidade e funcionalidade do software**: Testes rigorosos são necessários para identificar e corrigir bugs, garantindo que o software seja confiável, eficiente e seguro. A qualidade do software afeta diretamente a satisfação do usuário e a reputação da empresa.
    * **Processo de detecção e correção de bugs**: Bugs identificados durante os testes são registrados, priorizados e corrigidos pelos desenvolvedores. Um ciclo de repetição de teste e correção continua até que o software atenda aos critérios de qualidade estabelecidos.

### Implantação
A fase de implantação é caracterizada pelo software desenvolvido, testado e colocado em uso no ambiente de produção. Essa fase é crucial para garantir que o software esteja disponível e funcionando conforme o esperado para os usuários finais. Ela exige um planejamento meticuloso e uma execução cuidadosa para minimizar o impacto nos usuários e garantir uma transição suave para o novo sistema.

Vamos explorar os principais aspectos desta fase:
* **Preparação para o lançamento do software:** Antes do lançamento, é essencial realizar verificações finais e garantir que todos os componentes do software estejam prontos. A validação final do código, a configuração do ambiente de produção e a preparação da infraestrutura necessária, são algumas estratégias usadas.
* **Monitoramento e suporte pós-implantação**: Após a implantação, é vital monitorar o desempenho do software em tempo real para detectar e resolver quaisquer problemas rapidamente. Pode-se incluir o uso de ferramentas de monitoramento e a configuração de alertas para falhas críticas.
* **Importância do treinamento de usuários finais**: Para garantir que os usuários finais possam utilizar o software de maneira eficaz, é necessário fornecer treinamento adequado. Estão inclusos a documentação, os tutoriais, os workshops e o suporte técnico contínuo.

### Manutenção
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

#### Tipos de Prototipação
|Tipo|Descrição|Uso Típico|
|----|---------|----------|
|Descartável (Throwaway)|Protótipo criado para validar requisitos e depois descartado; o software final é construído do zero|Requisitos muito incertos; validação de conceito|
|Evolucionária (Evolutionary)|Protótipo é continuamente refinado até se tornar o produto final|Quando os requisitos são razoavelmente conhecidos; projetos menores|
#### Vantagens e Desvantagens

|Vantagens|Desvantagens|
|---------|------------|
|Redução de riscos e mal-entendidos sobre requisitos|Usuário pode confundir protótipo com produto final|
|Feedback constante do usuário desde o início|Pode levar a "scope creep" (aumento descontrolado do escopo)|
|Identificação precoce de problemas de usabilidade|Se mal gerenciado, pode gerar retrabalho excessivo|
|Maior satisfação do usuário com o produto final|Pode dar falsa sensação de progresso|
#### Quando Usar

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

#### As 5 Fases do RAD (segundo Pressman)
**O modelo RAD, conforme descrito por Roger S. Pressman, é dividido em 5 fases principais**:

|Fase|Descrição|Atividades Principais|
|----|---------|---------------------|
|1. Modelagem do Negócio|Levantamento do fluxo de informações entre as funções do negócio|Identificar processos suportados pelo sistema; responder "quem faz o quê" e "qual informação é gerada"|
|2. Modelagem dos Dados|Refinamento do fluxo de informação para extrair os objetos de dados|Identificar composição, localização e relações entre objetos de dados|
|3. Modelagem do Processo|Transformação dos objetos de dados no fluxo necessário para implementar funções do negócio|Descrições de processamento para adicionar, modificar ou recuperar dados|
|4. Geração da Aplicação|Construção do software usando ferramentas automatizadas e componentes reutilizáveis|Uso de linguagens de 4ª geração, CASE tools, componentes prontos|
|5. Teste e Modificação|Testes e integração de todos os componentes|Como muitos componentes já estão testados (reuso), o tempo total de teste é reduzido|
#### Características Fundamentais do RAD
* **Time-boxing**: Prazos fixos e curtos (geralmente 60-90 dias) para cada ciclo
* **Desenvolvimento paralelo**: Múltiplas equipes trabalham em diferentes componentes simultaneamente
* **Reutilização extensiva**: Aproveitamento de componentes, classes e APIs preexistentes
* **Alto envolvimento do usuário**: Participação ativa em todas as fases
* **Foco nas necessidades do negócio**: Excelência técnica é secundária em relação ao atendimento ao usuário

#### Vantagens e Desvantagens
|Vantagens|Desvantagens|
|---------|------------|
|Desenvolvimento acelerado (60-90 dias)|Requer equipes experientes e bem treinadas|
|Maior flexibilidade e adaptabilidade|Não adequado para projetos de alto risco técnico|
|Feedback constante e relevante do usuário|Exige recursos humanos suficientes para múltiplas equipes|
|Redução de codificação manual|Pode acumular dívida técnica se não houver disciplina|
|Progresso mensurável a cada ciclo|Menos ênfase em planejamento e documentação formal|
#### Quando Usar RAD
* Projetos com escopo modularizável (pode ser dividido em componentes independentes)
* Equipes experientes com acesso a ferramentas CASE/4GL
* Orçamento suficiente para ferramentas e múltiplas equipes
* Prazos muito curtos (semanas a poucos meses)
* Disponibilidade de usuários para participação contínua

#### Quando NÃO Usar RAD
* Alto risco técnico (teste de novas tecnologias)
* Projetos de grande escala (exigem recursos humanos massivos)
* Sistemas com forte interdependência entre módulos
* Equipe pequena ou inexperiente
* Projetos que exigem documentação extensiva e formal

#### Ferramentas e Técnicas de 4GL no Contexto RAD
O RAD frequentemente utiliza ferramentas de 4ª geração como parte essencial de sua estratégia de desenvolvimento rápido:

|Ferramenta/Técnica|Descrição|Exemplos|
|------------------|---------|--------|
|GUI Builders|Construção visual de interfaces gráficas|Visual Basic, Delphi|
|CASE Tools|Ferramentas de engenharia de software assistida por computador|Rational Rose, PowerDesigner|
|Geradores de Código|Produção automática de código a partir de modelos|Geradores de ORM, scaffolding
|Componentes Reutilizáveis|Bibliotecas de componentes pré-construídos|APIs, frameworks, componentes COM/.NET|
|DBMS com 4GL integrada|Sistemas de gerenciamento de banco de dados com linguagem própria|SQL (Oracle, SQL Server, MySQL)|

>Nota importante: O RAD frequentemente é confundido ou tratado como sinônimo de "low-code". Na verdade, o RAD é uma metodologia que utiliza ferramentas de 4GL, low-code e outras técnicas para atingir seus objetivos de rapidez. Low-code é uma das ferramentas que viabilizam o RAD

### 4.5. Modelo Evolutivo Incremental
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

#### Comparação entre Gerações de Linguagens
|Geração|Características|Exemplos|
|-------|---------------|--------|
|1GL|Linguagem de máquina, binário, mais próximo do hardware|Código binário|
|2GL|Linguagem Assembly, para kernels e aplicações de alta performance|Assembly|
|3GL|Linguagens de propósito geral, compiladas, usam palavras em inglês|Java, C++, C#, JavaScript, Python|
|4GL|Alto nível de abstração, focadas em tarefas específicas (bancos de dados, relatórios, GUIs)|SQL, Visual Basic, Delphi, PowerBuilder, MATLAB|
|5GL|Usadas principalmente em IA e sistemas especialistas|Prolog, OPS5, Mercury|

#### A Evolução: Low-Code e No-Code
As técnicas de 4ª geração evoluíram naturalmente para o que hoje conhecemos como plataformas de low-code e no-code. Essas plataformas:
* Permitem desenvolvimento com mínimo de codificação manual
* Utilizam interfaces visuais de arrastar-e-soltar
* Automatizam grande parte do ciclo de desenvolvimento
* Têm ganhado enorme popularidade (mercado projetado para crescer 42.8% ao ano entre 2022-2027)

## O que são Requisitos de Software e Regras de Negócio?
Antes de detalhar as classificações, é essencial entender a diferença entre esses dois conceitos, que muitas vezes se confundem na prática.

### Regras de Negócio
**Definição**: São **políticas**, **diretrizes**, **condições** e **restrições** que governam **como o negócio opera**, independentemente de qualquer sistema de software. Elas expressam a lógica do negócio, não a lógica do sistema.

#### Características:

* Existem mesmo sem computadores (podem ser aplicadas manualmente).
* São definidas pelos especialistas do negócio (stakeholders).
* São estáveis por longos períodos.
* Aplicam-se a toda a organização, não apenas a um sistema.

**Exemplos** (para seu app de comparação de preços):
>"Um mercado só pode se cadastrar com CNPJ válido."
>"Uma promoção não pode ter duração superior a 15 dias consecutivos."
>"Um consumidor pode favoritar produtos e receber alertas de preço mínimo."

### Requisitos de Software
**Definição**: São descrições do que o **sistema** de software **deve fazer** para **atender às regras de negócio e às necessidades dos usuários**. Eles são a ponte entre o negócio e a tecnologia.

#### Características:

* Existem porque o sistema de software existe.
* São definidos por analistas, engenheiros e usuários.
* Mudam conforme o sistema evolui.
* Aplicam-se especificamente ao sistema em desenvolvimento.

**Exemplos** (derivados das regras acima):
> "O sistema deve consultar a API da Receita Federal para validar o CNPJ no momento do cadastro do mercado."
> "O sistema deve impedir o cadastro de uma promoção com data final superior a 15 dias a partir da data atual."
> "O sistema deve enviar uma notificação push ao consumidor quando o preço de um produto favoritado atingir ou ficar abaixo do valor mínimo definido."

#### A Relação entre Regras de Negócio e Requisitos
```text
Regra de Negócio (o que o negócio exige)
        ↓
Deriva um ou mais Requisitos (o que o sistema deve fazer para atender à regra)
        ↓
Implementação técnica (código, banco de dados, APIs)
```
#### Exemplo prático completo:
|Nível|Descrição|
|-----|---------|
|Regra de Negócio|"Um consumidor não pode avaliar um mercado sem ter interagido com ele."|
|Requisito Funcional derivado|"O sistema deve registrar toda interação do consumidor com um mercado (visualização de produto, clique em promoção, compartilhamento)."|
|Requisito Funcional derivado|"O sistema deve permitir que um consumidor avalie um mercado apenas se houver pelo menos uma interação registrada nos últimos 30 dias."|
|Requisito Não Funcional derivado|"Os registros de interação devem ser armazenados com timestamp e retidos por no mínimo 90 dias para fins de auditoria."|

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

#### 2.1. Modelos de Ciclo de Vida (Metodologias):
Na teoria, estudamos modelos como Cascata, Espiral, Incremental. No mercado, o que impera hoje são as metodologias ágeis (Scrum, Kanban, XP).

* Em vez de fases sequenciais e longas, o trabalho é dividido em pequenos ciclos (sprints) . Em cada sprint, você passa por todas as etapas (requisitos, design, código, teste) de forma acelerada para entregar uma pequena parte funcional do software.
* Isso torna o processo mais flexível e adaptável a mudanças, algo que os modelos tradicionais (como o Cascata) não conseguem lidar bem.

#### 2.2. A Divisão do Trabalho (Especialização x Generalização):
Na teoria, um engenheiro de software pode fazer um pouco de tudo. Na prática, em empresas de médio e grande porte, o trabalho é mais especializado, embora a linha seja tênue:
* **Analista de Requisitos / Product Owner (PO)**: Foca nas etapas iniciais (levantamento de requisitos) e na priorização do que será desenvolvido, agindo como a "voz do cliente" dentro do time.
* **Arquiteto de Software**: Responsável pelas decisões de alto nível do projeto (design da arquitetura), definindo as tecnologias e a estrutura geral do sistema.
* **Desenvolvedor (Programador)**: Foco principal na implementação (codificação) e nos testes de unidade.
* **QA (Quality Assurance) / Testador**: Especialista em testes. Projeta e executa os planos de teste para garantir a qualidade do software.
* **Engenheiro de DevOps**: Foca na implantação, automação e operação do software, garantindo que ele possa ser entregue de forma rápida e confiável (o "como" entregar).
* **Engenheiro de Software (Generalista)**: Comum em startups ou times pequenos, onde uma pessoa pode atuar em várias frentes, desde a conversa com o cliente até a implantação.

#### 2.3. A Manutenção é a "Rainha":
A teoria diz que a manutenção é a fase mais longa. No mercado, isso é uma verdade absoluta. A grande maioria dos engenheiros de software não trabalha em projetos "do zero" (greenfield), mas sim evoluindo e mantendo sistemas legados (brownfield). Grande parte do dia a dia é:

* Corrigir bugs.
* Refatorar código antigo para melhorá-lo.
* Adicionar pequenas funcionalidades a um sistema existente.
* Integrar sistemas diferentes.

#### 2.4. Nem Tudo é Seguido à Risco:
Em muitas empresas, principalmente as menores ou com menos maturidade em processos, algumas etapas formais da engenharia de software são "puladas" ou feitas de maneira muito informal:
* A documentação pode ser mínima (resumida a ferramentas como o Jira e comentários no código).
* Os testes podem ser menos rigorosos (foco apenas no teste manual).
* O projeto (design) pode ser feito "na cabeça" ou em um guardanapo, sem uma documentação formal de arquitetura.

### 3. Vivemos uma Crise do Hardware?
#### O que seria uma "crise do hardware"?
Diferente da crise do software, que foi sobre métodos inadequados para lidar com a complexidade, uma **crise do hardware seria caracterizada por**:

* Estagnação ou desaceleração drástica do avanço tecnológico.
* Limites físicos intransponíveis.
* Escassez de componentes ou materiais críticos.
* Custos crescentes que inviabilizam a evolução.

#### Os Argumentos a Favor de uma Crise do Hardware
|Fator|Descrição|
|-----|---------|
|Fim da Lei de Moore|Gordon Moore previu que o número de transistores em um chip dobraria a cada 18-24 meses. Essa curva tem se achatado significativamente desde os 7nm, 5nm, 3nm. Os ganhos de desempenho por redução de litografia são cada vez menores e mais caros.|
|Custo fabril astronômico|Uma fábrica de chips (foundry) de ponta custa hoje mais de US$ 20 bilhões. Apenas três empresas no mundo (TSMC, Samsung, Intel) conseguem competir nesse nível. Isso cria um oligopólio e barreiras de entrada intransponíveis.|
|Escassez global de semicondutores (2020-2023)|A pandemia expôs a fragilidade da cadeia global de suprimentos. Setores inteiros (automotivo, eletrônicos) pararam por falta de chips. Essa vulnerabilidade é um sinal de crise estrutural.|
|Aquecimento e consumo energético|Chips de alta performance consomem cada vez mais energia e geram calor extremo. O resfriamento de data centers e supercomputadores já é um dos maiores desafios de infraestrutura.|
|Geopolítica e soberania tecnológica|A produção de semicondutores está concentrada em Taiwan (TSMC responde por mais de 50% dos chips avançados do mundo). Tensões geopolíticas (China vs. Taiwan) colocam toda a indústria global em risco. Países estão correndo para criar cadeias produtivas locais (EUA com o CHIPS Act, Europa com o European Chips Act).|

#### Os Argumentos Contra uma Crise do Hardware
|Fator|Descrição|
|-----|---------|
|Inovação em arquitetura, não só em litografia|Embora a miniaturização esteja desacelerando, a inovação continua em outras frentes: arquiteturas heterogêneas (chiplet, 3D stacking), processamento neuromórfico, computação quântica, GPUs massivamente paralelas.|
|Crescimento explosivo em nichos|Enquanto os CPUs tradicionais desaceleram, GPUs (NVIDIA), TPUs (Google), aceleradores de IA e chips especializados estão em crescimento exponencial, impulsionados pela inteligência artificial.|
|Demanda e investimento sem precedentes|A indústria de semicondutores está recebendo investimentos bilionários de governos e empresas privadas. Em vez de uma crise de estagnação, vivemos um momento de realinhamento e reindustrialização.|
|Software compensa hardware|Onde o hardware não avança tão rápido, o software compensa com otimizações, computação distribuída e novas arquiteturas. A nuvem permitiu que empresas escalassem sem depender de hardware próprio.|

#### Conclusão Parcial: Crise ou Transição?
A visão mais equilibrada é que não vivemos uma crise do hardware no mesmo sentido da crise do software, mas sim uma transição de paradigma:

* O modelo de crescimento "mais transistores a cada 18 meses com o mesmo custo"(*Lei de Moore*) chegou ao fim. Isso é um fato físico.
* Estamos entrando em uma era de hardware diversificado e especializado, onde o ganho de desempenho virá mais de arquiteturas inovadoras do que de simples miniaturização.
* A cadeia de suprimentos de semicondutores é um ponto único de fragilidade global, o que tem causado choques de oferta e movimentos de reindustrialização.

### 4. Principais Causas de Cancelamento de Projetos de Software
Os números são impressionantes: cerca de 31,1% dos projetos de software são cancelados antes da conclusão, e apenas 16,2% são entregues no prazo e dentro do orçamento .

#### Principais Causas (segundo pesquisas e especialistas)
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

### 5. Como Orçar o Desenvolvimento de um Software
Orçar software é uma das atividades mais desafiadoras da engenharia de software. As principais abordagens são:

#### 5.1. Principais Métodos de Estimativa
|Método|Como Funciona|Quando Usar|
|------|-------------|-----------|
|Estimativa por Analogia|Compara o novo projeto com projetos anteriores similares.|Quando há histórico de projetos semelhantes.|
|Ponto de Função (PF)|Mede o software com base em funcionalidades entregues ao usuário (entradas, saídas, consultas, arquivos, interfaces).|Projetos onde se pode quantificar as funcionalidades.|
|Estimativa por Especialistas|Consulta a especialistas que opinam com base em experiência.|Fase inicial, com pouca informação disponível.|
|Estimativa Paramétrica (COCOMO, SEER-SEM)|Usa fórmulas matemáticas baseadas em linhas de código estimadas e fatores de ajuste.|Projetos de médio a grande porte.|
|Estimativa Ágil (Planning Poker)|A equipe atribui pontos de história (story points) a cada tarefa, baseando-se em complexidade relativa.|Metodologias ágeis (Scrum).|
#### 5.2. Fatores que Influenciam o Custo
* **Complexidade funcional:** Quantidade e complexidade das funcionalidades.
* **Qualidade esperada**: Testes rigorosos, segurança, desempenho.
* **Tamanho da equipe e senioridade**: Profissionais mais experientes custam mais, mas entregam mais rápido e com mais qualidade.
* **Infraestrutura**: Custos de servidores, banco de dados, serviços em nuvem .
* **Integrações**: Conexão com sistemas de pagamento, ERP, APIs externas .
* **Prazos**: Prazos curtos exigem mais recursos paralelos e aumentam custo.

### 6. Frameworks e Templates Mais Usados no Desenvolvimento de Software
Os frameworks são estruturas pré-construídas que fornecem uma base para o desenvolvimento, evitando que você comece "do zero" .

#### 6.1. Classificação por Tipo
|Tipo|Função|Exemplos Populares|
|----|------|------------------|
|Frontend|Interface visual, interação com usuário|React, Vue.js, Angular, Svelte |
|Backend|Lógica de negócio, APIs, banco de dados|Django (Python), Laravel (PHP), Express.js (Node.js), Spring Boot (Java) |
|Fullstack|Frontend + Backend integrados|Next.js (React), Nuxt.js (Vue), Ruby on Rails |
|CSS/UI|Estilização e componentes visuais|Bootstrap, Tailwind CSS |

#### 6.2. Frameworks Mais Populares (2025/2026)
|Framework|Linguagem|Tipo|Uso Principal|
|---------|---------|----|-------------|
|React|JavaScript/TypeScript|Biblioteca frontend|Interfaces dinâmicas e interativas; mantido pelo Meta |
|Next.js|JavaScript/TypeScript|Fullstack (React)|Aplicações com SSR e otimização SEO |
|Vue.js|JavaScript/TypeScript|Frontend progressivo|Curva de aprendizado suave, flexível |
|Angular|TypeScript|Frontend completo|Grandes aplicações empresariais; mantido pelo Google |
|Django|Python|Backend|Desenvolvimento rápido, seguro e com baterias inclusas |
|Laravel|PHP|Backend|Sintaxe elegante, rico ecossistema |
|Spring Boot|Java|Backend|Microserviços e aplicações empresariais Java |
|Ruby on Rails|Ruby|Fullstack|Prototipação rápida, convenção sobre configuração |
|Express.js|JavaScript/Node.js|Backend minimalista|APIs e aplicações Node.js |
|Svelte|JavaScript/TypeScript|Frontend (compilador)|Código mais leve e performático |

#### 6.3. Templates e Ferramentas Complementares
Além dos frameworks, os desenvolvedores utilizam templates (projetos iniciais prontos) e ferramentas que aceleram o desenvolvimento:

|Categoria|Ferramentas/Exemplos|
|---------|--------------------|
|Boilerplates / Starter Kits|HTML5 Boilerplate, Create React App, Next.js starter, Vite templates |
|Infraestrutura em Nuvem|Vercel, Fly.io, DigitalOcean, AWS, Cloudflare |
|Bancos de Dados|PostgreSQL (Supabase, Neon), MongoDB Atlas, PlanetScale |
|Autenticação|Clerk, Auth.js, Supabase Auth |
|Pagamentos|Stripe (global), AbacatePay (Brasil) |
|Monitoramento|Sentry (erros), Uptime Kuma (disponibilidade) |
|E-mails|Resend (transacionais), Loops.so (marketing) |
|Design/Protótipo|Figma, Coolors, Undraw |
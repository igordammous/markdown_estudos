# Sistemas Operacionais
## 1- História dos SO e tipos existentes
A evolução dos SOs é diretamente impulsionada pela evolução do hardware. Cada salto tecnológico no hardware criou uma nova classe de problemas que os SOs precisaram resolver.
### 1940s - 1950s: Ausência de SO (Processamento em Lote Simples)
* **Hardware**: Válvulas, sem transistores. Máquinas enormes, lentas, extremamente caras.
* **Como funcionava**: Não havia SO. O programador se inscrevia para um horário, ia até a sala da máquina, conectava cabos em painéis de controle (programação "plug-board"), operava os painéis de fita perfurada e aguardava o resultado. Entre um programa e outro, o operador humano reconectava fisicamente o sistema.
* **Problema**: O tempo do computador (o recurso mais caro) era desperdiçado nos intervalos entre programas e na configuração manual.

<div style = "text-align: center;">
<img src="https://www.thenmusa.org/wp-content/uploads/2019/08/eniac-1.jpg" alt="ENIAC" style="width: 60%" title = "Imagem 1 - Marlyn Wescoff (left) and Ruth Lichterman were two of the ENIAC’s first programmers. U.S. National Archives Education Updates"/>

*Marlyn Wescoff (standing) and Ruth Lichterman were two of the ENIAC’s first programmers.
</div>

### 1950s - 1960s: Sistemas em Lote (Batch Systems)
* **Hardware**: Transistores, fitas magnéticas, primeiros discos magnéticos (bem caros).
* **Inovação**: Surge o resident monitor (primeiro rudimento de SO). Um programa residente na memória que automatizava a transição entre programas. Os operadores agrupavam ("batelada") vários jobs em uma fita.
* **Funcionamento**: O monitor residente carregava um job, executava até o fim (sem interrupção), descarregava a saída, carregava o próximo. A CPU ficava ociosa durante operações lentas de E/S (leitura de fita, impressão).
* **Problema**: Subutilização severa da CPU. A CPU, componente mais caro, passava a maior parte do tempo esperando E/S.
<div style = "text-align: center;">
<img src="https://miro.medium.com/v2/resize:fit:4800/format:webp/1*H9nKpY7rq902o72JUCBxTg.jpeg" alt="Batch processing to Multitasking" style="width: 70%" title = "Imagem 2 - Batch Processing Systems"/>

*The batch systems enhanced the use of CPUs however, their biggest blemish was that when a job was waiting to be served or act on I/O, the CPU remained idle.*
</div>


### 1960s: Multiprogramação e Sistemas de Tempo Compartilhado (Time-Sharing)
* **Hardware**: Discos magnéticos mais rápidos e baratos, proteção de memória (base e limite), interrupções de hardware maduras, início dos mainframes como IBM System/360.
* **Inovação Crucial**: Percebeu-se que, enquanto um job esperava E/S, a CPU poderia executar outro job. Nasce a multiprogramação.
* **Funcionamento**: Vários programas são mantidos na memória RAM simultaneamente. Quando um programa faz uma operação de E/S (lenta), o SO salva seu contexto e escalona outro programa para usar a CPU.
* **Time-Sharing**: Evolução da multiprogramação para sistemas interativos. Cada usuário tem um terminal (teletype) conectado ao computador central. O SO alterna a CPU entre os usuários tão rapidamente que cada um tem a ilusão de ter a máquina só para si. Nasce o conceito de escalonamento e troca de contexto.
* **Exemplo histórico**: CTSS (MIT), Multics (projeto que inspirou tudo o que veio depois, incluindo Unix).
<img src="https://www.storiainformatica.it/images/stories/history/os/origin/ibm_7094_ctss.jpeg" alt="IBM 7094" style="width: 100%" title = "Imagem 3 - IBM 7094 at MIT with CTSS"/>

### 1970s: Unix e o Surgimento dos Sistemas Modernos
* Hardware: Mini-computadores (DEC PDP-11) com memória virtual, barramentos padronizados, linguagem C.
* Inovação: Ken Thompson e Dennis Ritchie (Bell Labs) criam o Unix. Escrito em C (não assembly), o que o tornou portável. Introduziu conceitos que são padrão até hoje: hierarquia de arquivos, pipes (comunicação entre processos), shell como um programa separado, filosofia de ferramentas pequenas que fazem uma coisa bem.
* Simultaneamente: A IBM desenvolve sistemas robustos para seus mainframes (OS/360, MVS), focados em processamento transacional e confiabilidade extrema.
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/IBM_System_360_model_30_profile.agr.jpg/1280px-IBM_System_360_model_30_profile.agr.jpg" alt="By ArnoldReinhold - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=47096462" style="width: 100%" title = "Imagem 4 - IBM System 360/30 at the Computer History Museum."/>

### 1980s: A Era do PC e Sistemas de Rede
* **Hardware**: Microprocessadores (Intel 8086, 80286, 80386), PCs baratos, redes locais (Ethernet).
* **Eventos**:

  * **MS-DOS**: Para IBM PC. Inicialmente rudimentar, sem proteção de memória (qualquer programa podia escrever em qualquer lugar), sem multitarefa real (preemptiva). Refletia as limitações e o foco em baixo custo do hardware da época.
  * **Macintosh System (Mac OS)**: Interface gráfica (GUI) para o público, mas ainda com multitarefa cooperativa.
  * **Unix comercial e BSD**: Avanços em redes (TCP/IP). O BSD (Berkeley Software Distribution) trouxe a pilha TCP/IP que tornou a internet possível.
  * **NFS (Network File System)**: Sistemas de arquivos distribuídos.

* **Nasce o Linux**: Linus Torvalds (1991) cria um kernel Unix-like para a plataforma 386, aproveitando os recursos de memória virtual e proteção que o hardware Intel finalmente oferecia (modo protegido).

### 1990s - 2000s: SOs Modernos, Distribuídos e Móveis
* **Hardware**: Sistemas multiprocessados (SMP), clusters, virtualização (VMware), chips para celulares (ARM).
* **Eventos**:

  * **Windows NT/2000/XP**: Microsoft cria um SO com kernel moderno (microkernel híbrido), suporte a SMP, memória virtual robusta, segurança de usuários. Substitui a linhagem DOS/Windows 9x.
  * **Linux amadurece**: Torna-se dominante em servidores, supercomputadores e sistemas embarcados (roteadores, depois Android).
  * **SOs de tempo real (RTOS)**: Para sistemas embarcados, controle industrial, automotivo (QNX, VxWorks).
  * **Virtualização**: Xen, KVM – permitem rodar múltiplos SOs em uma única máquina física, separando o hardware do SO.
  * **Android e iOS**: SOs móveis baseados em Linux (Android) e Darwin/mach (iOS). Introduzem novas preocupações: gerenciamento agressivo de energia, sandboxing de aplicativos, segurança.

### 2010s - Presente: Nuvem, Contêineres e Computação Ubíqua
* **Hardware**: Computação heterogênea (CPU + GPU + NPU), SSDs NVMe, muitos núcleos (64+ cores), hardware de segurança (TPM, TrustZone).
* **Tendências**:
  * **Contêineres (Docker, Kubernetes)**: Compartilham o mesmo kernel do SO, mas isolam processos em namespaces, oferecendo eficiência superior à virtualização completa.
  * **Sistemas operacionais para nuvem**: Kernel otimizado para máquinas virtuais (Firecracker) e workloads massivamente paralelos.
  * **SOs orientados a segurança**: SeLinux, securOS, foco em mitigação de vulnerabilidades de hardware (Spectre, Meltdown).

### Tipos de Sistemas Operacionais (Classificação)
|Tipo|Características|Exemplos|Hardware Relacionado|
|----|---------------|--------|--------------------|
|Mainframe OS       |Ênfase em E/S massiva, confiabilidade, processamento transacional (transactions)|IBM z/OS|Hardware redundante, hot-swap, canais de E/S dedicados|
|Servidor           |Ênfase em rede, estabilidade, segurança, suporte a muitos usuários simultâneos|Linux (distros server), Windows Server, FreeBSD|Múltiplos CPUs/sockets, grandes quantidades de RAM, redes de alta velocidade|
|Desktop/PC         |Ênfase em interface gráfica, interatividade, suporte a uma vasta gama de periféricos|Windows 10/11, macOS, Linux (Ubuntu/Fedora)|GPUs, USB, áudio, multicore (4-16 núcleos típicos)|
|Tempo Real (RTOS)  |Ênfase em determinismo e latência previsível (garantias de tempo)|FreeRTOS, QNX, VxWorks|Microcontroladores (ARM Cortex-M), sistemas embarcados críticos (freios ABS, marca-passo)|
|Móvel/Embarcado    |Ênfase em eficiência energética, gerenciamento de sensores, sandboxing|Android (Linux), iOS (Darwin)|SoC (System-on-Chip) com cores big.LITTLE, modem celular, sensores diversos, bateria|
|Distribuído/Cluster|Ênfase em coordenação de múltiplas máquinas, tolerância a falhas|Plan9, sistemas que usam middleware (não um SO único)|Múltiplos nós interconectados por rede de alta velocidade|

## 2- Estrutura principal de um SO
Visão Geral da Arquitetura. Um sistema operacional moderno é estruturado em camadas, com o núcleo (kernel) no centro, protegido do resto.
```text
+--------------------------------------------------+
|                     Usuários                      |
+--------------------------------------------------+
|   Aplicativos (Editores, Navegadores, Jogos)     |
+--------------------------------------------------+
|                   Shell (CLI/GUI)                 |
+--------------------------------------------------+
|                  Chamadas de Sistema              |
|  (System Calls - interface entre usuário/kernel) |
+--------------------------------------------------+
|                                                  |
|                    KERNEL                        |
|  (Gerenciador de Processos, Memória, Arquivos,   |
|   Drivers de Dispositivo, Escalonador, IPC)      |
|                                                  |
+--------------------------------------------------+
|                 Camada de Abstração               |
|                 de Hardware (HAL)                 |
+--------------------------------------------------+
|                     HARDWARE                      |
|     (CPU, RAM, Discos, Placas de Rede, etc)      |
+--------------------------------------------------+
```
### Kernel
O kernel é o **núcleo do SO**. Ele roda em um modo especial do processador chamado **modo kernel** (ou modo supervisor, modo privilegiado), que lhe dá acesso total ao hardware e permite executar instruções privilegiadas.

#### Modos de Execução (Conexão com Hardware)
A CPU, através do registrador de status (ex: `CS` em x86, ou `CPSR` em ARM), mantém um bit que indica o modo atual:

|Modo|Privilégio|O que pode fazer|
|----|--------|---------------|
|Modo Usuário|Restrito|Não pode acessar dispositivos de E/S diretamente, não pode alterar tabelas de páginas, não pode desabilitar interrupções. Se tentar, ocorre uma exceção (trap).|
|Modo Kernel|Total|Pode executar qualquer instrução (HALT, acesso a portas de E/S, manipulação de registradores de controle, desabilitação de interrupções).|

**Mecanismo de transição**: Um programa em modo usuário só entra em modo kernel através de:
* Chamadas de Sistema (intencionais)
* Interrupções (externas, como timer ou teclado)
* Exceções (erros como page fault, divisão por zero)

#### Tipos de Kernel

|Tipo|Características|Vantagens|Desvantagens|Exemplos|
|----|---------------|---------|------------|--------|
|Monolítico|**Todo o SO** (gerenciamento de processos, memória, sistemas de arquivos, drivers) roda em um único espaço de endereço, em modo kernel.|Performance alta (pouca troca de contexto), chamadas de sistema rápidas.|Grande complexidade, um bug em um driver pode derrubar todo o sistema.|Linux (na prática), FreeBSD, Windows (NT é híbrido, mas predominantemente monolítico)|
|Microkernel|**Apenas o essencial roda em kernel**: comunicação entre processos (IPC), escalonamento básico, gerenciamento de memória mínima. Drivers, sistemas de arquivos são processos em modo usuário.|Estabilidade, modularidade, segurança.|Performance reduzida devido ao IPC constante entre componentes.|QNX, L4, Mach (base do macOS/XNU)
|Híbrido|**Combina abordagens**. Geralmente um núcleo monolítico com partes em modo usuário, ou um microkernel com mais serviços no kernel por performance.|Equilíbrio entre performance e modularidade.|Complexidade de design.|Windows NT/10/11, macOS (XNU)|

#### Principais Responsabilidades do Kernel
* **Gerenciamento de Processos e Threads**: Escalonamento, criação, término, comunicação entre processos (IPC), sincronização.
* **Gerenciamento de Memória**: Manutenção das tabelas de páginas, tratamento de page faults, alocação de memória para processos, memória virtual.
* **Gerenciamento de Dispositivos**: Drivers, tratamento de interrupções, abstração do hardware para o usuário (arquivos de dispositivo em `/dev` no Unix).
* **Gerenciamento de Sistemas de Arquivos**: Abstração de armazenamento persistente, controle de permissões, cache de disco.
* **Chamadas de Sistema**: Interface de entrada para o modo usuário solicitar serviços.

### Shell
O shell não é o kernel. O shell é um programa comum de usuário (embora especial) que fornece uma interface para interagir com o SO.

#### Tipos de Shell
**Shell de Linha de Comando (CLI)**
* **O que é**: Um programa que lê comandos digitados pelo usuário, interpreta-os e faz as chamadas de sistema correspondentes.
* **Funcionamento**: O shell executa um loop: exibe um prompt ($ ou >), aguarda entrada, analisa (parseia) o comando, e tipicamente:
  * Para comandos internos (`cd`, `exit`), executa internamente.
  * Para comandos externos, faz uma chamada de sistema `fork()` (cria um novo processo) e `exec()` (substitui o processo pelo programa solicitado), e aguarda ou coloca em segundo plano.
* **Exemplos:** Bash, Zsh, PowerShell, cmd.exe.
* **Conexão com hardware**: Quando você digita, o teclado gera interrupções → o driver do teclado no kernel repassa os dados → o terminal virtual (no kernel ou em modo usuário) entrega ao processo do shell → o shell processa.

**Shell Gráfico (GUI)**
* **O que é**: Geralmente parte de um sistema de janelas (como X11 no Linux, ou o compositor do Windows/macOS).
* **Funcionamento**: O servidor gráfico (ex: Xorg, Wayland compositor) gerencia a tela, mouse, teclado. O shell gráfico (ex: GNOME Shell, explorer.exe, Dock do macOS) é um cliente que desenha janelas, barras de tarefas, e responde a eventos de clique e tecla.
* **Conexão com hardware**: A GPU (placa de vídeo) é programada pelo driver de vídeo. O servidor gráfico usa chamadas de sistema (como `ioctl`) para enviar comandos de desenho para o driver, que por sua vez programa a GPU.

### Chamadas de Sistema
As chamadas de sistema são a interface oficial entre os programas em modo usuário e o kernel. Elas são o único caminho para um programa solicitar um serviço privilegiado.

#### Mecanismo (Como funciona em baixo nível)
* **Preparação**: O programa em modo usuário coloca os argumentos em locais conhecidos (geralmente registradores da CPU). Exemplo em x86-64:

  * `rax` = número da chamada de sistema (ex: 1 para `write`, 60 para `exit`)
  * `rdi` = primeiro argumento
  * `rsi` = segundo argumento
  * `rdx` = terceiro argumento

* **Trap (Armadilha)**: O programa executa uma instrução especial que gera uma exceção síncrona:

* `x86-64`: syscall (instrução moderna)
* `x86`: int 0x80 (interrupção software)
* `ARM`: svc (supervisor call)

* **Modo de Troca**: A CPU:

  * Salva o contexto atual (PC, registradores de modo usuário) em uma pilha de kernel.
  * Alterna o modo de usuário para modo kernel.
  * Desvia a execução para uma função específica do kernel (a tabela de syscalls) com base no número em rax.

* **Execução do Kernel**: O kernel executa a função solicitada (ex: `sys_write`), verificando permissões, validando argumentos, acessando o hardware se necessário.

* **Retorno**: O kernel coloca o resultado em rax (modo usuário), restaura o contexto, executa a instrução `sysret` (ou `iret`), que retorna ao modo usuário e retoma a execução do programa logo após a instrução `syscall`.

#### Categorias de Chamadas de Sistema

|Categoria|Exemplos (Linux)|Descrição|
|---------|----------------|---------|
|Controle de Processos|`fork()`, `exec()`, `wait()`, `exit()`, `getpid()`|Criar, destruir, gerenciar processos.|
|Gerenciamento de Memória|`mmap()`, `brk()`, `mprotect()`|Alocar memória virtual, mapear arquivos, alterar permissões de página.|
|E/S de Arquivos|`open()`, `read()`, `write()`, `close()`, `lseek()`|Operações em arquivos e diretórios.|
|E/S de Dispositivos|`ioctl()`, `read()`, `write()` (para dispositivos especiais)|Comunicação com drivers de dispositivo.|
|Gerenciamento de Arquivos|`mkdir()`, `rmdir()`, `unlink()`, `chmod()`|Manipular diretórios e permissões.|
|Informação do Sistema|`time()`, `uname()`, `sysinfo()`|Obter informações de sistema, data, hora.|
|Comunicação entre Processos|`pipe()`, `socket()`, `shmget()`, `msgget()`|Trocas de dados entre processos (IPC).|
|Segurança/Usuário|`setuid()`, `getuid()`, `chroot()`|Controle de identidade e permissões.|

Exemplo Concreto (C para assembly conceitual)
```c
// Programa C que escreve "Hello" no terminal
#include <unistd.h>

int main() {
    write(1, "Hello\n", 6);  // 1 = stdout
    return 0;
}
```
O que o compilador gera (conceitualmente, para x86-64):

```assembly
mov rax, 1          ; número da syscall write
mov rdi, 1          ; primeiro arg: file descriptor (stdout)
mov rsi, endereço_da_string
mov rdx, 6          ; terceiro arg: tamanho
syscall             ; faz a chamada de sistema
```
## 3- UserMod e KernelMod
### **Fundamentos de Proteção de Hardware**
A separação entre User Mode e Kernel Mode não é uma decisão de software — é uma **característica do processador** projetada para garantir segurança e estabilidade. Todo processador moderno (x86, x86-64, ARM, RISC-V) implementa pelo menos dois níveis de privilégio.

**Arquitetura x86/x86-64: Anéis de Proteção (Protection Rings)**
O x86 implementa 4 níveis de privilégio (Ring 0 a Ring 3), embora a maioria dos SOs use apenas dois:

|Anel|Privilégio|Uso Típico|
|----|----------|----------|
|Ring 0|Mais alto|Kernel do SO|
|Ring 1|Médio|Raramente usado (drivers em alguns sistemas)|
|Ring 2|Médio|Raramente usado|
|Ring 3|Mais baixo|Aplicações de usuário|

```text
                    +------------------+
                    |   Ring 0 (Kernel) |
                    |   Privilégio Total|
                    +------------------+
                           |
                    +------------------+
                    |   Ring 1 (Driver) |  (opcional)
                    +------------------+
                           |
                    +------------------+
                    |   Ring 2 (Driver) |  (opcional)
                    +------------------+
                           |
                    +------------------+
                    |   Ring 3 (User)   |
                    |   Privilégio Restrito|
                    +------------------+
```

**Arquitetura ARM: Exception Levels (EL)**
ARM utiliza um sistema de níveis de exceção (EL0 a EL3):

|Nível|Privilégio|Uso|
|-----|----------|---|
|EL0|Menos privilegiado|Aplicações de usuário|
|EL1|Privilegiado|Kernel do SO|
|EL2|Hipervisor|Virtualização|
|EL3|Mais privilegiado|Monitor de segurança (TrustZone)|

#### **Mecanismos de Proteção (Como o Hardware Garante a Separação)**
**1. Registrador de Status (EFLAGS/RFLAGS no x86, CPSR no ARM)**
A CPU mantém um bit que indica o nível de privilégio atual. Este bit não pode ser alterado por código em modo usuário — a única forma de mudar é via instruções específicas que geram traps (como `syscall`, `int`, `svc`).

**2. Conjunto de Instruções Restrito**
No modo usuário, certas instruções causam exceções (trap) se tentadas:

|Instrução|Efeito se executada em User Mode|
|---------|--------------------------------|
|`LGDT` (carregar tabela de descritores global)|General Protection Fault|
|`HLT` (parar CPU)|General Protection Fault|
|`IN`/`OUT` (acesso direto a portas de E/S)|General Protection Fault|
|`CLI`/`STI` (desabilitar/habilitar interrupções)|General Protection Fault|
|`WRMSR` (escrever em Model Specific Registers)|General Protection Fault|
|Instruções que modificam tabelas de páginas|General Protection Fault|

**Exemplo concreto**: Um programa em modo usuário que tenta acessar diretamente a porta do teclado (`0x60`):

```assembly
; Em modo usuário, esta instrução causa exceção
in al, 0x60    ; tenta ler do controlador do teclado
```
A CPU gera uma exceção (#GP - General Protection Fault), e o kernel decide como responder (geralmente terminando o processo).

**3. Proteção de Memória (MMU/TLB)**
A separação User/Kernel também se reflete nas tabelas de páginas:

* Cada entrada de página tem um bit User/Supervisor (U/S bit no x86)
* Se o bit U/S = 0, apenas código em modo kernel pode acessar essa página
* Se o bit U/S = 1, tanto user quanto kernel podem acessar (depende também do bit R/W)

```text
Tabela de Páginas (x86-64):
+------------------------------------------+
| Endereço Físico | U/S | R/W | Presente |
+------------------------------------------+
| 0x00001000      | 0   | 1   | 1        | <- Página do kernel (apenas kernel)
| 0x00002000      | 1   | 1   | 1        | <- Página de usuário (leitura/escrita)
| 0x00003000      | 1   | 0   | 1        | <- Página de código (apenas leitura)
+------------------------------------------+
```
Quando a CPU está em modo usuário, qualquer acesso a uma página com U/S=0 causa um page fault. O kernel trata essa falha e geralmente envia um sinal `SIGSEGV` (segmentation fault) para o processo.

### Usermod
**Características**:

* Privilégio restrito (Ring 3 no x86, EL0 no ARM)
* Código não pode acessar hardware diretamente
* Código não pode modificar estruturas críticas do SO
* Cada processo tem seu próprio espaço de endereço virtual
* Acesso à memória é limitado pelas tabelas de páginas configuradas pelo kernel
* Para solicitar serviços privilegiados, deve fazer uma chamada de sistema

**O que roda em User Mode**:
* Aplicações (navegadores, editores, jogos)
* Serviços e daemons (em alguns SOs, parte deles)
* Shells (bash, zsh, PowerShell)
* Bibliotecas de usuário (libc, GLib, etc.)

### Kernelmod
**Características**:

* Privilégio total (Ring 0 no x86, EL1 no ARM)
* Acesso irrestrito a todo o hardware
* Pode executar qualquer instrução
* Pode acessar todo o espaço de memória (kernel + todos os processos)
* Executa com uma pilha separada (kernel stack)
* Opera em um único espaço de endereço compartilhado (espaço do kernel)

**O que roda em Kernel Mode**:
* Núcleo do kernel (escalonador, gerente de memória)
* Manipuladores de interrupção (ISR - Interrupt Service Routines)
* Drivers de dispositivo (em kernels monolíticos)
* Código de chamadas de sistema

### A Transição User → Kernel
As transições entre modos são caras em termos de desempenho. Vamos ver os custos envolvidos:

|Operação|Ações da CPU/SO|Custo Aproximado (ciclos)|
|--------|---------------|-------------------------|
|Syscall simples|Salvar contexto, trocar modo, validar argumentos, executar|100-500 ciclos|
|Page fault|Salvar contexto, traduzir endereço, carregar página do disco (domina)|milhares a milhões de ciclos|
|Interrupção de hardware|Salvar contexto, identificar dispositivo, executar ISR|100-1000 ciclos|

**Processo detalhado de uma syscall**:

```text
Modo Usuário                     Modo Kernel
      |                               |
      |---> executa instrução ------->|
      |     syscall                   |
      |                               |
      |                         CPU salva contexto:
      |                         - RIP (próxima instrução)
      |                         - CS (modo usuário)
      |                         - RFLAGS
      |                         - SS, RSP
      |                               |
      |                         CPU alterna para Ring 0
      |                         Carrega CS/RIP da tabela IST
      |                         Carrega pilha do kernel (RSP)
      |                               |
      |                         Executa manipulador de syscall
      |                         (ex: entry_SYSCALL_64 no Linux)
      |                               |
      |                         Valida argumentos
      |                         Executa syscall específica
      |                         Coloca resultado em RAX
      |                               |
      |<--- executa sysret -----------|
      |     restaura contexto         |
      |                               |
```
### **Mapeamento de Memória entre User e Kernel**
Um aspecto crucial: o kernel **mapeia parte de seu espaço de endereço em cada processo**.
No Linux x86-64 típico:

```text
Espaço de Endereço Virtual (64 bits, configuração comum):
+-------------------+ 0xFFFFFFFFFFFFFFFF
|                   |
|   Espaço Kernel   |  (1 TB ou mais)
|   (marcado U/S=0) |
|                   |
+-------------------+ 0xFFFF800000000000
|                   |
|   Gap (não usado) |
|                   |
+-------------------+ 0x0000800000000000
|                   |
|   Espaço Usuário  |  (128 TB)
|   (marcado U/S=1) |
|                   |
+-------------------+ 0x0000000000000000
```
Implicações:
* Quando ocorre uma syscall, **não há necessidade de trocar tabelas de páginas** — as páginas do kernel já estão visíveis
* Apenas o ponteiro de pilha (RSP) muda para a pilha do kernel
* Isso torna as syscalls mais rápidas (não há TLB flush)

## 4- Tipos de SO
Agora que entendemos a base de proteção (User/Kernel), podemos classificar os SOs pelo modo como gerenciam a execução e os recursos.

### 4.1 Monotarefa
**Definição**: O SO executa apenas um programa por vez. Quando um programa está rodando, ele tem controle exclusivo da CPU, memória e dispositivos.

Características:
* Não há conceito de troca de contexto (não há outro processo para trocar)
* Geralmente não há proteção de memória entre programas
* Programas podem acessar hardware diretamente
* Simples, pequeno, previsível

**Exemplos históricos e atuais**:

* MS-DOS (até versão 3.x)
* CP/M
* Sistemas embarcados muito simples (FreeRTOS em configuração mínima pode atuar como monotarefa)
* Bootloaders (U-Boot, GRUB durante o processo de boot)

Funcionamento no MS-DOS:

```text
Inicialização:
[BIOS] → [Bootloader] → [DOS Kernel] → [COMMAND.COM]

Execução de um programa:
1. COMMAND.COM (shell) usa função 0x4B da INT 21h para carregar programa
2. DOS carrega o programa no endereço 0x100 (comando .COM) ou gerencia segmentos (.EXE)
3. Programa executa até o fim
4. Controle retorna ao COMMAND.COM
```
**Limitações** (que motivaram a evolução):

* Se um programa trava, o sistema inteiro trava
* Não é possível rodar um programa em segundo plano enquanto se trabalha em outro
* Desperdício de recursos (CPU fica ociosa durante operações de E/S)

### 4.2 Multitarefas
Definição: Capacidade do SO de executar múltiplos programas (processos/threads) aparentemente em paralelo, alternando a CPU entre eles.

4.2.1 Processos Preemptivos e Não-Preemptivos
Esta é uma distinção fundamental sobre quem decide quando um processo perde a CPU.

|Característica|Não-Preemptivo (Cooperativo)|Preemptivo|
|--------------|----------------------------|----------|
|Controle|Processo decide quando liberar a CPU|SO decide quando interromper o processo|
|Troca de contexto|Ocorre apenas quando processo faz syscall ou termina|Pode ocorrer a qualquer momento (via timer interrupt)|
|Confiabilidade|Um processo que não libera trava o sistema|SO mantém controle mesmo com processos mal-comportados|
|Complexidade|Baixa|Alta (requer sincronização, atomicidade)|

#### Processos preemptivos.
Mecanismo: O SO utiliza o timer interrupt (gerado pelo hardware de temporização) para periodicamente retomar o controle da CPU, independentemente do que o processo está fazendo.

```text
Timer Interrupt (a cada quantum, ex: 10ms):
+--------------------------------------------------+
|                                                  |
|    Processo A      Processo A      Processo B    |
|    rodando         rodando         rodando       |
|        |               |               |         |
|        |               |               |         |
|   [---|-------]   [---|-------]   [---|-------]  |
|        |               |               |         |
|   Timer IRQ      Timer IRQ      Timer IRQ        |
|   SO escolhe     SO escolhe     SO escolhe       |
|   próximo        próximo        próximo          |
|                                                  |
+--------------------------------------------------+
```
**Componentes críticos para preempção**:

1. Timer Programável: Hardware (PIT - Programmable Interval Timer, ou APIC Timer) gera interrupções em intervalos regulares
2. Manipulador de Interrupção: O kernel captura cada timer interrupt e chama o escalonador
3. Salvamento de Contexto: A CPU salva automaticamente parte do contexto; o kernel salva o restante
4. Escalonador: Decide qual processo executar a seguir
5. Restauração de Contexto: O kernel carrega o contexto do próximo processo e retorna

**Exemplo de fluxo preemptivo** (Linux simplificado):

```assembly
; Pseudo-código do manipulador de timer interrupt

timer_interrupt_handler:
    ; Salva contexto do processo atual
    push rax
    push rbx
    push rcx
    push rdx
    push rsi
    push rdi
    push rbp
    push r8, r9, r10, r11, r12, r13, r14, r15
    
    ; Salva ponteiro de pilha atual
    mov [current_process->kernel_stack], rsp
    
    ; Chama escalonador
    call scheduler
    
    ; Restaura ponteiro de pilha do próximo processo
    mov rsp, [next_process->kernel_stack]
    
    ; Restaura contexto do próximo processo
    pop r15, r14, r13, r12, r11, r10, r9, r8
    pop rbp
    pop rdi
    pop rsi
    pop rdx
    pop rcx
    pop rbx
    pop rax
    
    ; Retorna para o próximo processo
    iretq  ; Interrupt Return
```
##### **Vantagens**:

* Sistema responsivo mesmo com processos mal-comportados
* Melhor utilização de recursos
* Essencial para sistemas de tempo compartilhado

##### **Desvantagens**:

* Mais complexo (precisa proteger seções críticas com locks)
* Overhead do timer interrupt e trocas de contexto frequentes

#### Processos Não-preemptivos
**Mecanismo**: O SO aguarda que o processo ativo faça uma chamada de sistema (`yield()`, `sleep()`, `wait()`, ou operações de E/S) para então trocar para outro processo.

```text
Processo A          Processo B          Processo C
    |                   |                   |
    |---executa-------->|                   |
    |                   |---executa-------->|
    |                   |                   |
    |<---yield()--------|                   |
    |                   |                   |
    |---executa--------------------------->|
    |                   |                   |
    |                   |<---espera E/S-----|
    |                   |                   |
    |---executa-------->|                   |
    |                   |                   |
```    
##### **Vantagens**:

* Simples de implementar
* Menos overhead de sincronização (não há interrupções inesperadas)
* Previsível para o desenvolvedor (sabe quando pode ser interrompido)

##### **Desvantagens**:

* Um processo com loop infinito trava todo o sistema
* Programador precisa explicitamente ceder a CPU em pontos estratégicos
* Má utilização de CPUs multicore (pouco usado nesse contexto)

##### **Exemplos**:

* Mac OS Classic (System 1-9)
* Windows 3.1/9x (cooperativo para aplicações 16-bit)
* Threads em modo usuário (green threads) em algumas linguagens (Go inicialmente, Erlang)

### 4.3 RTOS
Definição: SO projetado para processar dados à medida que chegam, com garantias de tempo (determinismo). O correto funcionamento depende não apenas do resultado lógico, mas também do tempo em que ele é entregue.

**Classificação de RTOS**
|Tipo|Característica|Exemplo de Aplicação|
|----|--------------|--------------------|
|Hard Real-Time|Perder um prazo é uma falha catastrófica|Airbag de carro, controle de voo, marca-passo|
|Soft Real-Time|Perder prazos degrada performance, mas não causa falha catastrófica|Streaming de vídeo, áudio, jogos|

**Características Fundamentais**
1. **Determinismo**: O tempo de resposta deve ser previsível e constante
2. **Preempção por prioridade**: Tarefas de maior prioridade interrompem tarefas de menor prioridade imediatamente
3. **Latência de Interrupção mínima**: Tempo entre a interrupção de hardware e o início do tratamento deve ser pequeno e constante
4. **Inversão de Prioridade tratada**: Mecanismos como Priority Inheritance Protocol (PIP) evitam que tarefas de alta prioridade fiquem bloqueadas por tarefas de baixa

**Exemplo de problema de inversão de prioridade**:

```text
Situação sem PIP:
Tarefa L (baixa prioridade) adquire mutex M
Tarefa H (alta prioridade) tenta adquirir M → bloqueia
Tarefa M (média prioridade) executa e atrasa H indefinidamente

Com Priority Inheritance:
Quando H bloqueia em M, L herda a prioridade de H temporariamente
L termina, libera M, H executa
```
**Exemplos de RTOS**:

* **FreeRTOS**: Open source, leve, muito usado em microcontroladores (STM32, ESP32)
* **VxWorks**: Comercial, usado em sistemas críticos (NASA, equipamentos médicos)
* **QNX**: Microkernel, usado em automotivo (sistemas de infoentretenimento e ADAS)
* **Zephyr**: Linux Foundation, foco em IoT

**Exemplo FreeRTOS** (criação de tarefa com prioridade):

```c
// Cria uma tarefa de alta prioridade que deve responder em tempo real
void vHighPriorityTask(void *pvParameters) {
    TickType_t xLastWakeTime = xTaskGetTickCount();
    const TickType_t xFrequency = pdMS_TO_TICKS(10);  // 10ms período
    
    for(;;) {
        // Executa ação crítica
        read_sensor();
        calculate_control_signal();
        actuate();
        
        // Espera pelo próximo ciclo com latência controlada
        vTaskDelayUntil(&xLastWakeTime, xFrequency);
    }
}

// Criação: prioridade 5 (maior que a do idle, que é 0)
xTaskCreate(vHighPriorityTask, "Sensor", 1024, NULL, 5, NULL);
```
### 4.4 Distribuídos
Definição: Um conjunto de computadores independentes que se apresentam ao usuário como um único sistema coerente. O SO gerencia recursos que estão fisicamente separados.

#### **Características**
* **Transparência**: O usuário não sabe (nem precisa saber) onde os recursos estão fisicamente
* **Escalabilidade**: Adicionar mais nós aumenta a capacidade de processamento
* **Tolerância** a falhas: Se um nó falha, o sistema continua operando
* **Middleware**: Camada de software que abstrai a distribuição

#### **Arquiteturas Comuns**
|Arquitetura|Descrição|Exemplos|
|-----------|---------|--------|
|Cliente-Servidor|Clientes solicitam serviços, servidores fornecem|NFS, servidores web|
|Peer-to-Peer|Todos os nós são iguais, compartilham recursos|BitTorrent, blockchain|
|Cluster|Múltiplas máquinas trabalhando como uma única|Kubernetes, Hadoop|

#### **Exemplos de SO Distribuídos**
* **Plan 9**: Bell Labs, tudo é representado como sistema de arquivos, rede transparente
* **Amoeba**: Tanenbaum, microkernel para ambientes distribuídos
* **Inferno**: Sucessor do Plan 9, com máquina virtual Dis
* **Linux + Middleware**: A maioria dos sistemas distribuídos atuais usa Linux como base com camadas como Kubernetes, Hadoop, Spark

### Embarcados
Definição: SO projetado para operar em dispositivos com recursos limitados (CPU, memória, energia) e propósito específico.

#### **Características**
* **Resource-constrained**: Memória RAM e flash limitadas (KB a MB)
* **Eficiência energética**: Crítico para dispositivos com bateria
* **Confiabilidade**: Muitas vezes operam sem supervisão por anos
* **Propósito específico**: Diferente de um PC que roda aplicações variadas
* **Boot rápido**: Segundos ou milissegundos

#### Classificação de Sistemas Embarcados
|Tipo|Recursos|Exemplos|
|----|--------|--------|
|Bare-metal|Sem SO, apenas loop principal|Microcontroladores simples (ATmega)|
|RTOS embarcado|SO mínimo com escalonamento|FreeRTOS, Zephyr, ThreadX|
|Linux embarcado|Linux reduzido (Yocto, Buildroot)|Raspberry Pi, roteadores, sistemas automotivos|
|Android Embedded|Android adaptado para dispositivos específicos|TVs, quiosques, sistemas automotivos (Android Automotive)|

Exemplo de aplicação: ESP32 com FreeRTOS
O ESP32 é um SoC (System-on-Chip) que integra CPU dual-core, Wi-Fi, Bluetooth, e periféricos. O ESP-IDF (framework oficial) é baseado no FreeRTOS.

```c
// Exemplo de tarefa para leitura de sensor em um sistema embarcado
void sensor_task(void *pvParameters) {
    // Configuração do ADC (conversor analógico-digital)
    adc1_config_width(ADC_WIDTH_BIT_12);
    adc1_config_channel_atten(ADC1_CHANNEL_0, ADC_ATTEN_DB_11);
    
    int sensor_value;
    
    for(;;) {
        sensor_value = adc1_get_raw(ADC1_CHANNEL_0);
        ESP_LOGI("SENSOR", "Valor: %d", sensor_value);
        
        // Consome pouca energia entre leituras
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}
```
### Resumo Comparativo
|Tipo de SO|User/Kernel|Preempção|Garantia Temporal|Aplicação Típica|
|----------|-----------|---------|-----------------|----------------|
|Monotarefa|Geralmente sem separação|Não aplicável|Não|Bootloaders, sistemas muito simples|
|Multitarefa não-preemptivo|Presente|Não (cooperativo)|Não|Windows 3.1, Mac OS Classic|
|Multitarefa preemptivo|Presente|Sim (timer interrupt)|Não (geralmente)|Linux, Windows, macOS|
|RTOS|Presente|Sim, por prioridade|Sim (determinístico)|Controle industrial, automotivo, médico|
|Distribuído|Presente em cada nó|Depende do nó|Não (consistência eventual)|Data centers, nuvem|
|Embarcado|Varia (bare-metal a Linux)|Depende|Depende da classe|IoT, eletrodomésticos, wearables|

**Conexão com Hardware**: Síntese
O que você estudou em arquitetura de hardware se conecta diretamente a estes tópicos:

|Conceito de Hardware|Aplicação no SO|
|--------------------|---------------|
|Rings de proteção / Exception Levels|Base para User Mode vs Kernel Mode|
|Timer Interrupt (PIT/APIC Timer)|Base para preempção em multitarefa|
|MMU com bit U/S|Protege memória do kernel contra acesso de usuário|
|TLB|Acelera tradução de endereços durante syscalls|
|Interrupt Controller (PIC/APIC)|Gerencia interrupções de dispositivos e timer|
|Contexto da CPU (registradores)|Salvos/restaurados em cada troca de contexto|
|SoC (System-on-Chip)|Base para sistemas embarcados (CPU + periféricos no mesmo chip)|

## 5- Escalonamento. O que é, e seus exemplos.
**Definição**: Escalonamento é o mecanismo pelo qual o sistema operacional decide qual processo/thread será executado pela CPU e por quanto tempo.

O escalonador é ativado em quatro momentos principais:
* Timer interrupt (preempção por tempo)
* Processo faz chamada de sistema que pode bloqueá-lo (ex: `wait()`, `read()`)
* Processo termina (`exit()`)
* Recurso fica disponível (ex: E/S concluída, semáforo liberado)

**Objetivos do Escalonamento**
|Objetivo|Descrição|
|--------|---------|
|Justiça|Todos os processos recebem tempo de CPU proporcional à sua importância|
|Eficiência|Manter a CPU ocupada o máximo possível (evitar idle)|
|Tempo de resposta|Baixa latência para sistemas interativos|
|Turnaround|Minimizar tempo total desde a criação até a conclusão do processo|
|Throughput|Maximizar número de processos concluídos por unidade de tempo|
|Prioridade|Processos críticos devem ser atendidos primeiro|

**Métricas de Avaliação**
* Turnaround Time = Tempo de conclusão - Tempo de chegada
* Waiting Time = Tempo total que o processo esperou na fila de prontos
* Response Time = Tempo desde a chegada até o primeiro atendimento (importante para interatividade)

### 5.1 Algoritmos clássicos
Algoritmos Clássicos de Escalonamento
Vamos analisar cada algoritmo com exemplos práticos, considerando a seguinte lista de processos:
|Processo|Tempo de Chegada|Tempo de Execução (Burst Time)|
|--|-|-|
|P1|0|8|
|P2|1|4|
|P3|2|2|
|P4|3|6|

#### 5.1.1 First Come First Serve(FCFS)
**Mecanismo**: O primeiro processo que chega é o primeiro a ser executado. É ***não-preemptivo***.
**Funcionamento**:

```text
Tempo: 0    2    4    6    8    10   12   14   16   18   20
       |----|----|----|----|----|----|----|----|----|----|
P1:    [#########]                                        
P2:              [####]                                        
P3:                   [##]                                      
P4:                      [##########]                        

Escala:
P1: 0-8
P2: 8-12
P3: 12-14
P4: 14-20
```
**Cálculos**:

* Turnaround P1 = 8 - 0 = 8
* Turnaround P2 = 12 - 1 = 11
* Turnaround P3 = 14 - 2 = 12
* Turnaround P4 = 20 - 3 = 17
> Turnaround médio = 12

* **Vantagens**: Simples, fácil implementar com uma fila.
* **Desvantagens**: Efeito "convoy" (processos curtos esperam por processos longos), turnarounds ruins para processos curtos.

**Conexão com hardware**: Utiliza uma fila simples em memória; não requer timer interrupt para preempção.

#### 5.1.2 Shortest Job First (SJF)
Mecanismo: Executa o processo com o menor tempo de execução total. Pode ser não-preemptivo ou preemptivo (SRTF - Shortest Remaining Time First).

**1. Versão Não-Preemptiva**
Apenas quando um processo termina, escolhe-se o próximo com menor burst time entre os disponíveis.

```text
Tempo: 0    2    4    6    8    10   12   14   16   18   20
       |----|----|----|----|----|----|----|----|----|----|
P1:    [#########]                                        
P3:         [##]                                          
P2:              [####]                                    
P4:                   [##########]                        

Escala:
P1: 0-8 (é o único disponível no tempo 0)
P3: 8-10 (chegou em 2, burst 2)
P2: 10-14 (chegou em 1, burst 4)
P4: 14-20 (chegou em 3, burst 6)
```
> Turnaround médio = (8 + 13 + 8 + 17) / 4 = 11.5 (melhor que FCFS)

**2. Versão Preemptiva (SRTF)**
A cada novo processo que chega, o escalonador verifica se ele tem tempo restante menor que o processo atual. Se sim, preempta.

```text
Tempo: 0    2    4    6    8    10   12   14   16   18   20
       |----|----|----|----|----|----|----|----|----|----|
P1:    [##]                                                
P2:       [####]                                           
P3:           [##]                                         
P1:              [######]                                   
P4:                   [##########]                         

Escala detalhada:
0-1: P1 executa
1-2: P2 chega (burst 4), P1 tem 7 restantes → P2 preempta? Não, P1 já está rodando (SRTF só preempta ao chegar novo)
Na verdade, SRTF avalia a cada chegada:
t=0: P1 inicia (restante 8)
t=1: P2 chega (restante 4). P1 restante 7. P2 é menor? SIM → preempta P1
t=1-5: P2 executa (completa em t=5)
t=5: P3 chega em t=2 (restante 2), P1 restante 7 → escolhe P3
t=5-7: P3 executa (completa em t=7)
t=7: P4 chega em t=3 (restante 6), P1 restante 7 → P4 é menor? Não (6 < 7? Sim, 6 é menor) → escolhe P4
t=7-13: P4 executa (completa em t=13)
t=13: apenas P1 restante
t=13-20: P1 completa
```
> Turnaround médio = (20 + 4 + 5 + 10) / 4 = 9.75 (melhor ainda)

* **Vantagens**: Otimiza turnaround médio.
* **Desvantagens**: Requer conhecimento do futuro (tempo de execução), pode causar starvation de processos longos.

**Conexão com hardware**: A versão preemptiva exige timer interrupt para permitir preempção a cada nova chegada.

#### 5.1.3 Round Robin(RR)
Mecanismo: Cada processo recebe um quantum (fatia de tempo). Se não termina dentro do quantum, é preemptado e vai para o final da fila.

**Quantum** = 4 unidades de tempo

```text
Tempo: 0    2    4    6    8    10   12   14   16   18   20
       |----|----|----|----|----|----|----|----|----|----|
P1:    [####]                                              
P2:         [####]                                         
P3:              [##]                                      
P1:                 [####]                                 
P4:                     [####]                             
P4:                         [##]                           

Fila:
t=0: [P1] → P1 executa 0-4
t=4: P1 vai ao final, chegam P2(1), P3(2), P4(3) → fila [P2,P3,P4,P1]
t=4-8: P2 executa (completa em t=8)
t=8: fila [P3,P4,P1]
t=8-12: P3 executa (completa em t=10), depois P4 entra (t=10-12)
t=12: fila [P1,P4]
t=12-16: P1 executa (restante 4 → completa t=16)
t=16: fila [P4]
t=16-20: P4 executa (restante 6 → completa t=22? Vamos recalcular)
```
Melhor representação:
Representação precisa com quantum=4:

|Intervalo|Processo|Observação|
|---------|--------|----------|
|0-4|P1|Executa 4, restam 4|
|4-8|P2|Completa (4 unidades)|
|8-10|P3|Completa (2 unidades)|
|10-14|P1|Executa mais 4, restante 0 (completa)|
|14-20|P4|Executa os 6 restantes|

>Turnaround médio = (14 + 7 + 8 + 17) / 4 = 11.5

Escolha do Quantum:

* Quantum muito grande → RR vira FCFS
* Quantum muito pequeno → overhead alto (muitas trocas de contexto)

|Quantum|Efeito|
|-------|------|
|1-5 ms|Alta sobrecarga, boa responsividade|
|10-100 ms|Equilíbrio típico (Linux usa ~100ms padrão)|
|100 ms|Menos trocas, pior responsividade interativa|

**Conexão com hardware**: O quantum é implementado através do timer interrupt. O kernel configura o timer (PIT ou APIC) para gerar interrupção após o quantum. Quando a interrupção ocorre, o escalonador é invocado.

#### 5.1.4 Por Prioridade
Mecanismo: Cada processo tem uma prioridade (numérica). O escalonador sempre escolhe o processo com maior prioridade (ou menor número, dependendo da convenção).

**Exemplo com prioridade** (menor número = maior prioridade):

|Processo|Chegada|Burst|Prioridade|
|--|-|-|-|
|P1|0|8|3|
|P2|1|4|1|
|P3|2|2|2|
|P4|3|6|4|

**Execução (não-preemptivo)**:

```text
t=0: apenas P1 → executa
t=0-8: P1 completa
t=8: disponíveis P2, P3, P4 → P2 (prioridade 1) executa
t=8-12: P2 completa
t=12: P3 e P4 → P3 (prio 2) executa
t=12-14: P3 completa
t=14-20: P4 executa
```
Problema: Starvation (Fome)
Processos de baixa prioridade podem nunca executar se sempre houver processos de alta prioridade.

**Soluções**:

* **Aging (Envelhecimento)**: Aumentar gradualmente a prioridade de processos que esperam muito tempo
* **Feedback (MLFQ)**: Mover processos entre filas de prioridade baseado no comportamento

**Multilevel Feedback Queue (MLFQ)** - usado no Linux, Windows, macOS

**É o algoritmo mais sofisticado e amplamente utilizado**. Combina múltiplas filas com prioridades diferentes e promove/demove processos baseado no comportamento.

```text
Filas de Prioridade:
┌─────────────────────────────────────┐
│ Prioridade Alta (RR, quantum curto) │ ← Processos interativos (I/O-bound)
├─────────────────────────────────────┤
│ Prioridade Média (RR, quantum médio)│
├─────────────────────────────────────┤
│ Prioridade Baixa (RR, quantum longo)│ ← Processos computacionais (CPU-bound)
└─────────────────────────────────────┘

Regras típicas:
1. Se processo usa pouco CPU → sobe de prioridade (interativo)
2. Se processo usa muito CPU → desce de prioridade (computacional)
3. Após quantum, vai para fila inferior
4. Aging: após certo tempo, sobe para evitar starvation
```
## 3- Diferença entre processo e thread
### Processo
**Definição**: Um processo é uma instância de um programa em execução. É a unidade de alocação de recursos.

**Estrutura de um Processo** (PCB - Process Control Block):

```text
┌─────────────────────────────────────────┐
│         Process Control Block (PCB)      │
├─────────────────────────────────────────┤
│ PID (Process ID)                         │
│ Estado (Running, Ready, Blocked, etc)    │
│ Contexto de Hardware (registradores)     │
│ Contador de Programa (PC)                │
│ Ponteiro de Pilha (SP)                   │
├─────────────────────────────────────────┤
│ Gerenciamento de Memória:                │
│   - Tabelas de Páginas (PTBR)            │
│   - Segmentos (text, data, heap, stack)  │
│   - Mapeamento de memória virtual        │
├─────────────────────────────────────────┤
│ Gerenciamento de Arquivos:               │
│   - Tabela de arquivos abertos (FDs)     │
│   - Diretório de trabalho                │
├─────────────────────────────────────────┤
│ Informação de Controle:                  │
│   - Prioridade                           │
│   - Contador de tempo de CPU             │
│   - Processo pai (PPID)                  │
│   - Sinais pendentes                     │
└─────────────────────────────────────────┘
```
Características do Processo:

* **Espaço de endereço isolado**: Cada processo tem sua própria tabela de páginas, com mapeamentos independentes
* **Recursos exclusivos**: Arquivos abertos, dispositivos, etc.
* **Criação custosa**: `fork()` duplica tabelas de páginas (COW - Copy on Write)
* **Troca de contexto entre processos**: Cara (troca tabelas de páginas → TLB flush)

Representação na Memória:

```text
Espaço de Endereço de um Processo (Linux x86-64 típico):
0x7FFFFFFFFFFFFF  ┌─────────────────────┐
                   │      Stack          │ ← CRESCE PARA BAIXO
                   │      (variáveis     │
                   │       locais)       │
                   ├─────────────────────┤
                   │        ↓            │
                   │        ↑            │
                   ├─────────────────────┤
                   │        Heap         │ ← CRESCE PARA CIMA
                   │ (alocação dinâmica) │
                   ├─────────────────────┤
                   │   Dados Inicializados│
                   │   ( .data )         │
                   ├─────────────────────┤
                   │   Dados Não-Inicializados│
                   │   ( .bss )          │
                   ├─────────────────────┤
                   │   Código ( .text )  │ ← Geralmente somente leitura
0x0000000000400000 └─────────────────────┘
```
### Thread
Definição: Uma thread é uma unidade de execução dentro de um processo. Várias threads compartilham os recursos do mesmo processo.

**Estrutura de uma Thread** (TCB - Thread Control Block):

```text
┌─────────────────────────────────────────┐
│         Thread Control Block (TCB)       │
├─────────────────────────────────────────┤
│ TID (Thread ID)                          │
│ Estado                                   │
│ Contexto de Hardware (registradores)     │
│ Contador de Programa (PC)                │
│ Ponteiro de Pilha (SP) - pilha própria   │
├─────────────────────────────────────────┤
│ Compartilhado com outras threads do mesmo processo:│
│   - Espaço de endereço (tabelas de páginas)│
│   - Arquivos abertos                     │
│   - Sinais e manipuladores               │
│   - Diretório de trabalho                │
└─────────────────────────────────────────┘
```
**O que é compartilhado vs. privado em threads**:

|Compartilhado entre threads do mesmo processo|Privado por thread|
|---------------------------------------------|------------------|
|Espaço de endereço (código, heap, dados globais)|Pilha (stack)|
|Arquivos abertos (file descriptors)|Registradores da CPU|
|Sinais e manipuladores|Contador de programa (PC)|
|Diretório de trabalho|Thread-local storage (TLS)|
|Identidade do processo (PID)|TID (Thread ID)|
|Privilégios e credenciais|

**Representação na Memória** (Processo com 3 threads):

```text
Espaço de Endereço do Processo:
┌─────────────────────────────────────────┐
│  Stack Thread 1  │  (privada)           │
├─────────────────────────────────────────┤
│  Stack Thread 2  │  (privada)           │
├─────────────────────────────────────────┤
│  Stack Thread 3  │  (privada)           │
├─────────────────────────────────────────┤
│                                         │
│              Heap                       │ ← COMPARTILHADO
│              (malloc)                   │
│                                         │
├─────────────────────────────────────────┤
│         Dados Globais (.data/.bss)      │ ← COMPARTILHADO
├─────────────────────────────────────────┤
│         Código (.text)                  │ ← COMPARTILHADO
└─────────────────────────────────────────┘
```

### Comparação Detalhada
|Aspecto|Processo|Thread|
|-------|--------|------|
|Recursos|Cada processo tem seus próprios recursos (memória, arquivos)|Threads compartilham recursos do processo|
|Espaço de endereço|Isolado (tabela de páginas própria)|Compartilhado (mesma tabela de páginas)|
|Troca de contexto|Cara (troca PCB + tabelas de páginas → TLB flush)|Barata (apenas registradores, pilha)|
|Criação|Lenta (fork duplica estruturas)|Rápida (apenas alocar TCB e pilha)|
|Comunicação|IPC (pipes, sockets, filas) - mais lenta|Memória compartilhada - muito rápida|
|Sincronização|Menos necessária (espaços isolados)|Essencial (mutex, semáforos)|
|Segurança/Isolamento|Alto (falha em um processo não afeta outros)|Baixo (falha em uma thread derruba todo o processo)|
|Escalonamento|O escalonador escolhe qual processo executar|O escalonador escolhe qual thread executar|

**Modelos de Threads** (User vs Kernel Threads)
|Modelo|Descrição|Vantagens|Desvantagens|
|------|---------|---------|------------|
|User-Level Threads|Threads gerenciadas por biblioteca em modo usuário, kernel enxerga apenas um processo|Criação/context switch extremamente rápidos (sem syscall)|Se uma thread bloqueia (E/S), todas bloqueiam; não aproveita múltiplos cores|
|Kernel-Level Threads|Threads gerenciadas pelo kernel, cada thread é unidade de escalonamento|Aproveita multicore, bloqueio de uma não bloqueia as outras|Criação/context switch mais caros (syscall)|
|Modelo Híbrido (M:N)|Combina ambos (ex: inicial do Go, Scheduler Activations)|Equilíbrio entre eficiência e escalabilidade|Complexidade alta|

**Exemplo de criação de thread** (pthreads no Linux):

```c
#include <pthread.h>
#include <stdio.h>

void* thread_function(void* arg) {
    int* num = (int*)arg;
    printf("Thread %d executando\n", *num);
    return NULL;
}

int main() {
    pthread_t threads[4];
    int ids[4] = {1, 2, 3, 4};
    
    for (int i = 0; i < 4; i++) {
        // Cria uma nova thread (kernel-level no Linux)
        pthread_create(&threads[i], NULL, thread_function, &ids[i]);
    }
    
    for (int i = 0; i < 4; i++) {
        pthread_join(threads[i], NULL);  // Aguarda término
    }
    
    return 0;
}
```
## Dúvidas

### 1- RAM e SWAP, como funcionam e qual é a razão da mudança de velocidade do HD para o SSD
#### Funcionamento e Evolução HD → SSD
**Hierarquia de Memória**
```text
┌─────────────────────────────────────────────────────────────┐
│                        CPU                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Registradores (1 ciclo) - KB                        │   │
│  └─────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Cache L1 (2-4 ciclos) - 32-64 KB por core           │   │
│  └─────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Cache L2 (10-20 ciclos) - 256 KB - 1 MB por core    │   │
│  └─────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ Cache L3 (30-50 ciclos) - 4-64 MB compartilhado     │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│ RAM (100-300 ciclos) - GB                                   │
│ Latência: ~80-120 ns                                        │
│ Largura de banda: ~20-50 GB/s (DDR4/DDR5)                   │
└─────────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────────┐
│ SWAP (Dispositivo de Armazenamento)                         │
│                                                             │
│ HD (Hard Disk):                                             │
│   - Latência: ~5-10 ms (50.000x mais lento que RAM)        │
│   - Transferência: ~100-200 MB/s                           │
│                                                             │
│ SSD (Solid State Drive):                                    │
│   - Latência: ~0.1-0.2 ms (500x mais lento que RAM)        │
│   - Transferência: ~500-7000 MB/s (NVMe)                   │
└─────────────────────────────────────────────────────────────┘
```
#### **O que é SWAP?**
SWAP (ou espaço de troca) é uma área no disco (ou partição) usada como extensão da memória RAM. Quando a RAM física está cheia, o SO move páginas de memória menos utilizadas para o SWAP, liberando espaço para páginas mais ativas.

**Mecanismo de Paginação com SWAP**:

```text
Memória Virtual (cada processo vê um espaço enorme)
                    ↓
            ┌───────────────┐
            │  Tabela de    │ ← MMU traduz endereço virtual
            │  Páginas      │   para endereço físico
            └───────────────┘
                    ↓
    ┌───────────────────────────────┐
    │           RAM (Física)         │
    │  ┌─────────────────────────┐  │
    │  │ Páginas ativas          │  │
    │  │ (sendo usadas agora)    │  │
    │  └─────────────────────────┘  │
    │  ┌─────────────────────────┐  │
    │  │ Páginas menos ativas    │  │ ← Page daemon (kswapd) move
    │  │ (candidatas a swap)     │  │   páginas para SWAP quando RAM está cheia
    │  └─────────────────────────┘  │
    └───────────────────────────────┘
                    ↓ (quando necessário)
    ┌───────────────────────────────┐
    │           SWAP (Disco)         │
    │  ┌─────────────────────────┐  │
    │  │ Páginas swapped out     │  │
    │  │ (inativas, não usadas)  │  │
    │  └─────────────────────────┘  │
    └───────────────────────────────┘
Page Fault e Swapping
Quando um processo tenta acessar uma página que não está na RAM:

text
1. Processo tenta acessar endereço virtual
                ↓
2. MMU verifica a tabela de páginas
   Bit Present = 0 (página não está em RAM)
                ↓
3. CPU gera exceção PAGE FAULT (#PF)
                ↓
4. Kernel entra em ação (modo kernel):
   - Identifica o endereço virtual que causou o fault
   - Localiza a página no SWAP (ou no arquivo mapeado)
   - Encontra um quadro de página livre na RAM
   - Se não há página livre, seleciona uma página para "sacrificar"
     (algoritmo de substituição de páginas - LRU, Clock, etc.)
   - Se a página sacrificada foi modificada (dirty), escreve no SWAP
                ↓
5. Kernel carrega a página solicitada do SWAP para a RAM
                ↓
6. Atualiza a tabela de páginas (bit Present = 1)
                ↓
7. Retorna ao processo, que reexecuta a instrução que causou o fault
```

**Algoritmos de Substituição de Páginas**

|Algoritmo|Descrição|Exemplo de Uso|
|---------|---------|--------------|
|FIFO|Remove a página mais antiga|Simples, mas ineficaz (Belady's anomaly)|
|LRU (Least Recently Used)|Remove a página menos usada recentemente|Bom, mas caro de implementar|
|Clock (Second Chance)|Aproximação de LRU com bits de referência|Linux usa variante (NRU)|
|NRU (Not Recently Used)|Combina bits Referenciado e Modificado|Linux, Windows|

**Razão da Mudança de Velocidade HD → SSD**
A diferença de desempenho entre HD e SSD é drástica e impacta diretamente a experiência de uso do SWAP e do sistema como um todo.

**Diferenças Físicas**
|Característica|HD (Hard Disk)|SSD (Solid State Drive)|
|--------------|--------------|-----------------------|
|Tecnologia|Discos magnéticos giratórios, cabeçote móvel|Memória flash NAND (sem partes móveis)|
|Latência|5-10 ms (tempo de seek + rotação)|0.05-0.2 ms (acesso eletrônico)|
|Tempo de seek|2-10 ms (movimento do braço)|Não aplicável|
|Latência rotacional|2-6 ms (aguardar setor passar)|Não aplicável|
|IOPS (operações aleatórias)|~100-200 IOPS|10.000 - 1.000.000+ IOPS|
|Acesso aleatório|Extremamente lento (busca física)|Essencialmente igual ao acesso sequencial|
|Acesso sequencial|Razoável (100-200 MB/s)|Excelente (500-7000 MB/s)|

**Impacto no SWAP e na Experiência**

**Com HD**:

* Page fault = busca no disco = 5-10 ms de latência
* Se o sistema começa a usar SWAP, fica extremamente lento (thrashing)
* Mover uma página para SWAP (swap out) também é lento
* Usuário sente o sistema "travando" quando a RAM está cheia

**Com SSD**:

* Page fault = busca no SSD = 0.05-0.2 ms de latência
* SWAP ainda é mais lento que RAM, mas a diferença é muito menor
* Thrashing ainda existe, mas é menos perceptível
* Sistemas podem operar com menos RAM, usando SWAP mais agressivamente

**Dados Comparativos** (Aproximados)
|Operação|RAM (DDR4)|SSD NVMe|HD (7200rpm)|
|--------|----------|--------|------------|
|Leitura aleatória (4KB)|80 ns|100 µs|10 ms|
|Fator de diferença|1x|1.250x|125.000x|
|Largura de banda|25 GB/s|3.5 GB/s|150 MB/s|

**Tradução prática:**

* Acessar dados na RAM é **1.250 vezes** mais rápido que no SSD
* Acessar dados no SSD é **100 vezes** mais rápido que no HD
* Acessar dados na RAM é **125.000 vezes** mais rápido que no HD

#### Thrashing (Condição de "Travamento")
Definição: Thrashing ocorre quando o sistema gasta mais tempo movendo páginas entre RAM e SWAP do que executando processos.

**Ciclo do Thrashing**:

```text
RAM cheia
    ↓
SO começa a usar SWAP
    ↓
Page faults aumentam
    ↓
Mais tempo gasto em I/O (SWAP)
    ↓
Processos produzem menos trabalho
    ↓
Escalonador vê CPU ociosa e tenta trazer mais processos
    ↓
Mais processos competem por RAM
    ↓
RAM fica ainda mais cheia (piora!)
    ↓
Loop se retroalimenta
```
**Soluções**:

* Aumentar RAM física
* Reduzir o número de processos ativos
* Usar SSD em vez de HD (mitiga, mas não elimina)
* Ajustar parâmetros do kernel (swappiness no Linux)

**Swappiness (Linux)**: Parâmetro que controla a agressividade do uso de SWAP (0-200). Valor baixo = menos SWAP, valor alto = mais SWAP.

```bash
# Ver swappiness atual
cat /proc/sys/vm/swappiness

# Ajustar para usar SWAP apenas quando necessário (valor típico: 10-60)
echo 10 > /proc/sys/vm/swappiness
```
#### Resumo Visual
```text
                    PROCESSO vs THREAD
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│    PROCESSO A                    PROCESSO B                     │
│  ┌─────────────────┐          ┌─────────────────┐              │
│  │ PCB (PID, etc)  │          │ PCB (PID, etc)  │              │
│  ├─────────────────┤          ├─────────────────┤              │
│  │ Tabela de Páginas│         │ Tabela de Páginas│              │
│  │ (espaço isolado) │         │ (espaço isolado) │              │
│  ├─────────────────┤          ├─────────────────┤              │
│  │ ┌─────┐ ┌─────┐ │          │ ┌─────┐ ┌─────┐ │              │
│  │ │Thread│ │Thread│ │          │ │Thread│ │Thread│ │              │
│  │ │  T1  │ │  T2  │ │          │ │  T1  │ │  T2  │ │              │
│  │ └─────┘ └─────┘ │          │ └─────┘ └─────┘ │              │
│  │ Compartilham:   │          │ Compartilham:   │              │
│  │ - Código        │          │ - Código        │              │
│  │ - Heap          │          │ - Heap          │              │
│  │ - Arquivos      │          │ - Arquivos      │              │
│  └─────────────────┘          └─────────────────┘              │
│         ↑                              ↑                       │
│         └──────────────┬───────────────┘                       │
│                        │                                       │
│                   NÃO COMPARTILHAM                             │
│              (cada processo é isolado)                         │
└─────────────────────────────────────────────────────────────────┘
```

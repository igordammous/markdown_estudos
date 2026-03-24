# Sistemas Operacionais
## Matéria
### 1- História dos SO e tipos existentes
A evolução dos SOs é diretamente impulsionada pela evolução do hardware. Cada salto tecnológico no hardware criou uma nova classe de problemas que os SOs precisaram resolver.
#### 1940s - 1950s: Ausência de SO (Processamento em Lote Simples)
* **Hardware**: Válvulas, sem transistores. Máquinas enormes, lentas, extremamente caras.
* **Como funcionava**: Não havia SO. O programador se inscrevia para um horário, ia até a sala da máquina, conectava cabos em painéis de controle (programação "plug-board"), operava os painéis de fita perfurada e aguardava o resultado. Entre um programa e outro, o operador humano reconectava fisicamente o sistema.
* **Problema**: O tempo do computador (o recurso mais caro) era desperdiçado nos intervalos entre programas e na configuração manual.
<img src="[https://www.aps.org/_ipx/w_828,q_90/https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fi2z87pbo%2Fproduction%2Fa9132a54f148d9eef366dbf5f7a8cb5c25603971-2500x1597.webp%3Fauto%3Dformat%26fit%3Dmax%26w%3D828%26q%3D90](https://admin.cnnbrasil.com.br/wp-content/uploads/sites/12/2021/06/26776_1798DEE935286D54.jpg?w=1200&h=900&crop=0)" alt="ENIAC" style="width: 100%" title = "Imagem 1 - Marlyn Wescoff (left) and Ruth Lichterman were two of the ENIAC’s first programmers. U.S. National Archives Education Updates"/>
*Marlyn Wescoff (left) and Ruth Lichterman were two of the ENIAC’s first programmers.
U.S. National Archives Education Updates.*

#### 1950s - 1960s: Sistemas em Lote (Batch Systems)
* **Hardware**: Transistores, fitas magnéticas, primeiros discos magnéticos (bem caros).
* **Inovação**: Surge o resident monitor (primeiro rudimento de SO). Um programa residente na memória que automatizava a transição entre programas. Os operadores agrupavam ("batelada") vários jobs em uma fita.
* **Funcionamento**: O monitor residente carregava um job, executava até o fim (sem interrupção), descarregava a saída, carregava o próximo. A CPU ficava ociosa durante operações lentas de E/S (leitura de fita, impressão).
* **Problema**: Subutilização severa da CPU. A CPU, componente mais caro, passava a maior parte do tempo esperando E/S.
<div style = "text-align: center;">
<img src="https://miro.medium.com/v2/resize:fit:4800/format:webp/1*H9nKpY7rq902o72JUCBxTg.jpeg" alt="Batch processing to Multitasking" style="width: 70%" title = "Imagem 2 - Batch Processing Systems"/>

*The batch systems enhanced the use of CPUs however, their biggest blemish was that when a job was waiting to be served or act on I/O, the CPU remained idle.*
</div>


#### 1960s: Multiprogramação e Sistemas de Tempo Compartilhado (Time-Sharing)
* **Hardware**: Discos magnéticos mais rápidos e baratos, proteção de memória (base e limite), interrupções de hardware maduras, início dos mainframes como IBM System/360.
* **Inovação Crucial**: Percebeu-se que, enquanto um job esperava E/S, a CPU poderia executar outro job. Nasce a multiprogramação.
* **Funcionamento**: Vários programas são mantidos na memória RAM simultaneamente. Quando um programa faz uma operação de E/S (lenta), o SO salva seu contexto e escalona outro programa para usar a CPU.
* **Time-Sharing**: Evolução da multiprogramação para sistemas interativos. Cada usuário tem um terminal (teletype) conectado ao computador central. O SO alterna a CPU entre os usuários tão rapidamente que cada um tem a ilusão de ter a máquina só para si. Nasce o conceito de escalonamento e troca de contexto.
* **Exemplo histórico**: CTSS (MIT), Multics (projeto que inspirou tudo o que veio depois, incluindo Unix).
<img src="https://www.storiainformatica.it/images/stories/history/os/origin/ibm_7094_ctss.jpeg" alt="IBM 7094" style="width: 100%" title = "Imagem 3 - IBM 7094 at MIT with CTSS"/>

#### 1970s: Unix e o Surgimento dos Sistemas Modernos
* Hardware: Mini-computadores (DEC PDP-11) com memória virtual, barramentos padronizados, linguagem C.
* Inovação: Ken Thompson e Dennis Ritchie (Bell Labs) criam o Unix. Escrito em C (não assembly), o que o tornou portável. Introduziu conceitos que são padrão até hoje: hierarquia de arquivos, pipes (comunicação entre processos), shell como um programa separado, filosofia de ferramentas pequenas que fazem uma coisa bem.
* Simultaneamente: A IBM desenvolve sistemas robustos para seus mainframes (OS/360, MVS), focados em processamento transacional e confiabilidade extrema.
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/IBM_System_360_model_30_profile.agr.jpg/1280px-IBM_System_360_model_30_profile.agr.jpg" alt="By ArnoldReinhold - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=47096462" style="width: 100%" title = "Imagem 4 - IBM System 360/30 at the Computer History Museum."/>

#### 1980s: A Era do PC e Sistemas de Rede
* **Hardware**: Microprocessadores (Intel 8086, 80286, 80386), PCs baratos, redes locais (Ethernet).
* **Eventos**:

  * **MS-DOS**: Para IBM PC. Inicialmente rudimentar, sem proteção de memória (qualquer programa podia escrever em qualquer lugar), sem multitarefa real (preemptiva). Refletia as limitações e o foco em baixo custo do hardware da época.
  * **Macintosh System (Mac OS)**: Interface gráfica (GUI) para o público, mas ainda com multitarefa cooperativa.
  * **Unix comercial e BSD**: Avanços em redes (TCP/IP). O BSD (Berkeley Software Distribution) trouxe a pilha TCP/IP que tornou a internet possível.
  * **NFS (Network File System)**: Sistemas de arquivos distribuídos.

* **Nasce o Linux**: Linus Torvalds (1991) cria um kernel Unix-like para a plataforma 386, aproveitando os recursos de memória virtual e proteção que o hardware Intel finalmente oferecia (modo protegido).

#### 1990s - 2000s: SOs Modernos, Distribuídos e Móveis
* **Hardware**: Sistemas multiprocessados (SMP), clusters, virtualização (VMware), chips para celulares (ARM).
* **Eventos**:

  * **Windows NT/2000/XP**: Microsoft cria um SO com kernel moderno (microkernel híbrido), suporte a SMP, memória virtual robusta, segurança de usuários. Substitui a linhagem DOS/Windows 9x.
  * **Linux amadurece**: Torna-se dominante em servidores, supercomputadores e sistemas embarcados (roteadores, depois Android).
  * **SOs de tempo real (RTOS)**: Para sistemas embarcados, controle industrial, automotivo (QNX, VxWorks).
  * **Virtualização**: Xen, KVM – permitem rodar múltiplos SOs em uma única máquina física, separando o hardware do SO.
  * **Android e iOS**: SOs móveis baseados em Linux (Android) e Darwin/mach (iOS). Introduzem novas preocupações: gerenciamento agressivo de energia, sandboxing de aplicativos, segurança.

#### 2010s - Presente: Nuvem, Contêineres e Computação Ubíqua
* **Hardware**: Computação heterogênea (CPU + GPU + NPU), SSDs NVMe, muitos núcleos (64+ cores), hardware de segurança (TPM, TrustZone).
* **Tendências**:
  * **Contêineres (Docker, Kubernetes)**: Compartilham o mesmo kernel do SO, mas isolam processos em namespaces, oferecendo eficiência superior à virtualização completa.
  * **Sistemas operacionais para nuvem**: Kernel otimizado para máquinas virtuais (Firecracker) e workloads massivamente paralelos.
  * **SOs orientados a segurança**: SeLinux, securOS, foco em mitigação de vulnerabilidades de hardware (Spectre, Meltdown).

#### Tipos de Sistemas Operacionais (Classificação)
|Tipo|Características|Exemplos|Hardware Relacionado|
|----|---------------|--------|--------------------|
|Mainframe OS       |Ênfase em E/S massiva, confiabilidade, processamento transacional (transactions)|IBM z/OS|Hardware redundante, hot-swap, canais de E/S dedicados|
|Servidor           |Ênfase em rede, estabilidade, segurança, suporte a muitos usuários simultâneos|Linux (distros server), Windows Server, FreeBSD|Múltiplos CPUs/sockets, grandes quantidades de RAM, redes de alta velocidade|
|Desktop/PC         |Ênfase em interface gráfica, interatividade, suporte a uma vasta gama de periféricos|Windows 10/11, macOS, Linux (Ubuntu/Fedora)|GPUs, USB, áudio, multicore (4-16 núcleos típicos)|
|Tempo Real (RTOS)  |Ênfase em determinismo e latência previsível (garantias de tempo)|FreeRTOS, QNX, VxWorks|Microcontroladores (ARM Cortex-M), sistemas embarcados críticos (freios ABS, marca-passo)|
|Móvel/Embarcado    |Ênfase em eficiência energética, gerenciamento de sensores, sandboxing|Android (Linux), iOS (Darwin)|SoC (System-on-Chip) com cores big.LITTLE, modem celular, sensores diversos, bateria|
|Distribuído/Cluster|Ênfase em coordenação de múltiplas máquinas, tolerância a falhas|Plan9, sistemas que usam middleware (não um SO único)|Múltiplos nós interconectados por rede de alta velocidade|

### 2- Estrutura principal de um SO
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
#### Kernel
O kernel é o **núcleo do SO**. Ele roda em um modo especial do processador chamado **modo kernel** (ou modo supervisor, modo privilegiado), que lhe dá acesso total ao hardware e permite executar instruções privilegiadas.

##### Modos de Execução (Conexão com Hardware)
A CPU, através do registrador de status (ex: `CS` em x86, ou `CPSR` em ARM), mantém um bit que indica o modo atual:

|Modo|Privilégio|O que pode fazer|
|----|--------|---------------|
|Modo Usuário|Restrito|Não pode acessar dispositivos de E/S diretamente, não pode alterar tabelas de páginas, não pode desabilitar interrupções. Se tentar, ocorre uma exceção (trap).|
|Modo Kernel|Total|Pode executar qualquer instrução (HALT, acesso a portas de E/S, manipulação de registradores de controle, desabilitação de interrupções).|

**Mecanismo de transição**: Um programa em modo usuário só entra em modo kernel através de:
* Chamadas de Sistema (intencionais)
* Interrupções (externas, como timer ou teclado)
* Exceções (erros como page fault, divisão por zero)

##### Tipos de Kernel

|Tipo|Características|Vantagens|Desvantagens|Exemplos|
|----|---------------|---------|------------|--------|
|Monolítico|**Todo o SO** (gerenciamento de processos, memória, sistemas de arquivos, drivers) roda em um único espaço de endereço, em modo kernel.|Performance alta (pouca troca de contexto), chamadas de sistema rápidas.|Grande complexidade, um bug em um driver pode derrubar todo o sistema.|Linux (na prática), FreeBSD, Windows (NT é híbrido, mas predominantemente monolítico)|
|Microkernel|**Apenas o essencial roda em kernel**: comunicação entre processos (IPC), escalonamento básico, gerenciamento de memória mínima. Drivers, sistemas de arquivos são processos em modo usuário.|Estabilidade, modularidade, segurança.|Performance reduzida devido ao IPC constante entre componentes.|QNX, L4, Mach (base do macOS/XNU)
|Híbrido|**Combina abordagens**. Geralmente um núcleo monolítico com partes em modo usuário, ou um microkernel com mais serviços no kernel por performance.|Equilíbrio entre performance e modularidade.|Complexidade de design.|Windows NT/10/11, macOS (XNU)|

##### Principais Responsabilidades do Kernel
* **Gerenciamento de Processos e Threads**: Escalonamento, criação, término, comunicação entre processos (IPC), sincronização.
* **Gerenciamento de Memória**: Manutenção das tabelas de páginas, tratamento de page faults, alocação de memória para processos, memória virtual.
* **Gerenciamento de Dispositivos**: Drivers, tratamento de interrupções, abstração do hardware para o usuário (arquivos de dispositivo em `/dev` no Unix).
* **Gerenciamento de Sistemas de Arquivos**: Abstração de armazenamento persistente, controle de permissões, cache de disco.
* **Chamadas de Sistema**: Interface de entrada para o modo usuário solicitar serviços.

#### Shell
O shell não é o kernel. O shell é um programa comum de usuário (embora especial) que fornece uma interface para interagir com o SO.

##### Tipos de Shell
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

#### Chamadas de Sistema
As chamadas de sistema são a interface oficial entre os programas em modo usuário e o kernel. Elas são o único caminho para um programa solicitar um serviço privilegiado.

##### Mecanismo (Como funciona em baixo nível)
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

##### Categorias de Chamadas de Sistema

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
### 3- UserMod e KernelMod
#### Usermod
#### Kernelmod
### 4- Tipos de SO
#### Monotarefa
#### Multitarefas
##### Processos preemptivos e não-preemptivos.
Preemptivos
Não-preemptivos
#### RTOS
#### Distribuídos
#### Embarcados


## Dúvidas

### 1- Escalonamento. O que é, e seus exemplos.
#### Algoritmos clássicos
##### First Come First Serve(FCFS)
##### Shortest Job First (SJF)
##### Round Robin(RR)
##### Por Prioridade
### 3- Diferença entre processo e thread
#### Processo
#### Thread
### 4- RAM e SWAP, como funcionam e qual é a razão da mudança de velocidade do HD para o SSD

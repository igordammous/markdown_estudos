# Faça um programa que receba a medida de um ângulo em graus. Calcule e mostre o quadrante em que se localiza esse ângulo. Considere os quadrantes
#  da trigonometria e, para ângulos maiores que 360° ou menores que −360°, reduzí-los, mostrando também o número de voltas e o sentido da volta 
# (horário ou anti-horário).

# %%
import math
angulo = int(input("Digite o ângulo em graus: "))

# Reduzindo o ângulo para o intervalo [-360, 360]
voltas = 0
if angulo >= 360:
    voltas = angulo // 360
    angulo_restante = angulo % 360
elif angulo <= -360:
    voltas = math.ceil(angulo / 360)
    angulo_restante = angulo % 360
else:
    angulo_restante = angulo

# Determinando quadrante baseado no ângulo reduzido
if angulo_restante == 0 or angulo_restante % 90 == 0:
    quadrante = 0  # sobre eixo
elif 0 < angulo_restante < 90:
    quadrante = 1
elif 90 < angulo_restante < 180:
    quadrante = 2
elif 180 < angulo_restante < 270:
    quadrante = 3
elif 270 < angulo_restante < 360:
    quadrante = 4
elif -360 < angulo_restante < -270:
    quadrante = 1
elif -270 < angulo_restante < -180:
    quadrante = 2
elif -180 < angulo_restante < -90:
    quadrante = 3
elif -90 < angulo_restante < 0:
    quadrante = 4

# Exibindo resultado
if quadrante == 0:
    print(f"O ângulo {angulo}° está sobre um eixo.")
else:
    if voltas > 0 and angulo > 0:
        print(f"O ângulo {angulo}° está localizado no quadrante {quadrante} e deu {voltas} volta(s) no sentido anti-horário.")
    elif voltas < 0 and angulo < 0:
        voltas = abs(voltas)
        print(f"O ângulo {angulo}° está localizado no quadrante {quadrante} e deu {voltas} volta(s) no sentido horário.")
    else:
        print(f"O ângulo {angulo}° está localizado no quadrante {quadrante}.")

# %%
# Faça um programa para o curso de ADS (6 módulos), cada sala tem vários alunos, calcule e apresente os seguintes itens:
# a) Quantidade de homens e mulheres de cada módulo;
# b) Média de alturas de cada módulo;
# c) Quantidade de pessoas com cor de olho azul de cada módulo;
# d) Quantidade de homens e mulheres do curso todo;
# e) Média de alturas do curso todo;
# f) Quantidade de pessoas com cor de olho azul do curso.
# Observação: este exercício utiliza DUAS estruturas de repetição. Na estrurura de repetição interna, digite zero na altura para sair.
mod1 = mod2 = mod3 = mod4 = mod5 = mod6 = 0
fem1 = fem2 = fem3 = fem4 = fem5 = fem6 = 0
masc1 = masc2 = masc3 = masc4 = masc5 = masc6 = 0
alt1 = alt2 = alt3 = alt4 = alt5 = alt6 = 0
olho1 = olho2 = olho3 = olho4 = olho5 = olho6 = 0
soma_alt1 = soma_alt2 = soma_alt3 = soma_alt4 = soma_alt5 = soma_alt6 = 0

modulo = int(input("Digite o número do módulo (1 a 6): "))
while modulo in range (1,7):
    if modulo == 1:
        mod1 += 1
        altura = float(input("Digite a altura do aluno (0 para sair): "))
        while altura > 0:
            soma_alt1 += altura
            olho = input("O aluno tem olhos azuis? (s/n) ").lower()
            if olho == 's':
                olho1 += 1
            sexo = input("Digite o sexo do aluno (m/f): ").lower()
            if sexo == 'm':
                masc1 += 1
            elif sexo == 'f':
                fem1 += 1
            altura = float(input("Digite a altura do aluno (0 para sair): "))
    elif modulo == 2:
        mod2 += 1
        altura = float(input("Digite a altura do aluno (0 para sair): "))
        while altura > 0:
            soma_alt2 += 1
            olho = input("O aluno tem olhos azuis? (s/n) ").lower()
            if olho == 's':
                olho2 += 1
            sexo = input("Digite o sexo do aluno (m/f): ").lower()
            if sexo == 'm':
                masc2 += 1
            elif sexo == 'f':
                fem2 += 1
            altura = float(input("Digite a altura do aluno (0 para sair): "))
    elif modulo == 3:
        mod3 += 1
        altura = float(input("Digite a altura do aluno (0 para sair): "))
        while altura > 0:
            soma_alt3 += 1
            olho = input("O aluno tem olhos azuis? (s/n) ").lower()
            if olho == 's':
                olho3 += 1
            sexo = input("Digite o sexo do aluno (m/f): ").lower()
            if sexo == 'm':
                masc3 += 1
            elif sexo == 'f':
                fem3 += 1
            altura = float(input("Digite a altura do aluno (0 para sair): "))
    elif modulo == 4:
        mod4 += 1
        altura = float(input("Digite a altura do aluno (0 para sair): "))
        while altura > 0:
            soma_alt4 += 1
            olho = input("O aluno tem olhos azuis? (s/n) ").lower()
            if olho == 's':
                olho4 += 1
            sexo = input("Digite o sexo do aluno (m/f): ").lower()
            if sexo == 'm':
                masc4 += 1
            elif sexo == 'f':
                fem4 += 1
            altura = float(input("Digite a altura do aluno (0 para sair): "))
    elif modulo == 5:
        mod5 += 1
        altura = float(input("Digite a altura do aluno (0 para sair): "))
        while altura > 0:
            soma_alt5 += 1
            olho = input("O aluno tem olhos azuis? (s/n) ").lower()
            if olho == 's':
                olho5 += 1
            sexo = input("Digite o sexo do aluno (m/f): ").lower()
            if sexo == 'm':
                masc5 += 1
            elif sexo == 'f':
                fem5 += 1
            altura = float(input("Digite a altura do aluno (0 para sair): "))
    elif modulo == 6:
        mod6 += 1
        altura = float(input("Digite a altura do aluno (0 para sair): "))
        while altura > 0:
            soma_alt6 += 1
            olho = input("O aluno tem olhos azuis? (s/n) ").lower()
            if olho == 's':
                olho6 += 1
            sexo = input("Digite o sexo do aluno (m/f): ").lower()
            if sexo == 'm':
                masc6 += 1
            elif sexo == 'f':
                fem6 += 1
            altura = float(input("Digite a altura do aluno (0 para sair): "))
    modulo = int(input("Digite o número do módulo (1 a 6): "))

if (masc1 + fem1) == 0:
    media_alt1 = 0
elif (masc1 + fem1) != 0:
    media_alt1 = soma_alt1 / (masc1 + fem1)

if (masc2 + fem2) == 0:
    media_alt2 = 0
elif (masc2 + fem2) != 0:
    media_alt2 = soma_alt2 / (masc2 + fem2)

if (masc3 + fem3) == 0:
    media_alt3 = 0
elif (masc3 + fem3) != 0:
    media_alt3 = soma_alt3 / (masc3 + fem3)

if (masc4 + fem4) == 0:
    media_alt4 = 0
elif (masc4 + fem4) != 0:
    media_alt4 = soma_alt4 / (masc4 + fem4)

if (masc5 + fem5) == 0:
    media_alt5 = 0
elif (masc5 + fem5) != 0:
    media_alt5 = soma_alt5 / (masc5 + fem5)

if (masc6 + fem6) == 0:
    media_alt6 = 0
elif (masc6 + fem6) != 0:
    media_alt6 = soma_alt6 / (masc6 + fem6)

media_alt_curso = (media_alt1 + media_alt2 + media_alt3 + media_alt4 + media_alt5 + media_alt6) / 6
total_olhos_azul = olho1 + olho2 + olho3 + olho4 + olho5 + olho6
masc_total = masc1 + masc2 + masc3 + masc4 + masc5 + masc6
fem_total = fem1 + fem2 + fem3 + fem4 + fem5 + fem6 
# a) Quantidade de homens e mulheres de cada módulo;
print("Módulo 1 - Informações")
print("-" * 45)
print(f"Homens: {masc1}")
print(f"Mulheres: {fem1}")
print(f"Média de altura: {media_alt1}")
print(f"Olhos Azuis: {olho1}")
print()
print("Módulo 2 - Informações")
print("-" * 45)
print(f"Homens: {masc2}")
print(f"Mulheres: {fem2}")
print(f"Média de altura: {media_alt2}")
print(f"Olhos Azuis: {olho2}")
print()
print("Módulo 3 - Informações")
print("-" * 45)
print(f"Homens: {masc3}")
print(f"Mulheres: {fem3}")
print(f"Média de altura: {media_alt3}")
print(f"Olhos Azuis: {olho3}")
print()
print("Módulo 4 - Informações")
print("-" * 45)
print(f"Homens: {masc4}")
print(f"Mulheres: {fem4}")
print(f"Média de altura: {media_alt4}")
print(f"Olhos Azuis: {olho4}")
print()
print("Módulo 5 - Informações")
print("-" * 45)
print(f"Homens: {masc5}")
print(f"Mulheres: {fem5}")
print(f"Média de altura: {media_alt5}")
print(f"Olhos Azuis: {olho5}")
print()
print("Módulo 6 - Informações")
print("-" * 45)
print(f"Homens: {masc6}")
print(f"Mulheres: {fem6}")
print(f"Média de altura: {media_alt6}")
print(f"Olhos Azuis: {olho6}")
print()
print("Curso - Informações")
print("-" * 45)
print(f"Homens: {masc_total}")
print(f"Mulheres: {fem_total}")
print(f"Média de altura: {media_alt_curso}")
print(f"Olhos Azuis: {total_olhos_azul}")
print()
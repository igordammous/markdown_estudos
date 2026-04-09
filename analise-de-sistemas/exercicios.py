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

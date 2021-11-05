# Ler ângulo e mostrar seno, cosseno e tangente
import math

print('='*5, ' DESAFIO 18 ', '='*5)
angulo = float(input('Informe o valor do ângulo: '))

rad_angulo = math.radians(angulo)
seno = math.sin(rad_angulo)
cosseno = math.cos(rad_angulo)
tangente = math.tan(rad_angulo)

print(f'\n\033[7;40m= Resultados da Análise do ângulo {angulo:.2f}°: \033[m')
print(f'\033[1;40mValor em radianos: {rad_angulo:.4f} \033[m')
print(f'\033[1;32mSeno {seno:10.4f}\033[m    |   \033[1;33mCosseno {cosseno:10.4f}\033[m    |  \033[1;36mTangente {tangente:10.4f}\033[m')
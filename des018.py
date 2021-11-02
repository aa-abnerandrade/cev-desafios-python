# Ler ângulo e mostrar seno, cosseno e tangente
import math

print('='*5, ' DESAFIO 18 ', '='*5)
angulo = float(input('Informe o valor do ângulo: '))

rad_angulo = math.radians(angulo)
seno = math.sin(rad_angulo)
cosseno = math.cos(rad_angulo)
tangente = math.tan(rad_angulo)

print(f'\n= Resultados da Análise do ângulo {angulo:.2f}°:')
print(f'Valor em radianos: {rad_angulo:.4f}')
print(f'Seno {seno:10.4f}    |   Cosseno {cosseno:10.4f}    |  Tangente {tangente:10.4f}')
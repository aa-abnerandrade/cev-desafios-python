# Ler o comprimento dos catetos e calcular a hipotenusa
import math
print('='*5, ' DESAFIO 17 ', '='*5)
catopo = float(input('Digite o comprimento do cateto oposto: '))
catadj = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catopo, catadj)

print(f'\n= Com catetos {catopo:.2f} e {catadj:.2f} o triângulo retângulo apresenta hipotenusa {hipotenusa:.2f}.')

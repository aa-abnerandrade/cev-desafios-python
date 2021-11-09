print(' '*14, 'DESAFIO 43', ' '*14)
'''
Ler altura e peso e calcular IMC
0 - 18.5 / 18.5 - 25 / 25 - 30 / 30 - 40 / 40+ (respec) abaixo / ideal / sobre / obesidade / obesidade severa
'''
print('\n\033[7;40;1m=== ÍMC - ÍNDICE DE MASSA CORPORAL ===\033[m')
weight = float(input('Informe seu peso (kg):  '))
height = float(input('Informe sua altura (mt): '))
imc = weight / (height*height)

print('\n\033[1;30;47m', 'Resultado:', ' '*25, '\033[m')

if imc > 0 and imc <19:
    cat = 'ABAIXO DO PESO'
elif imc >= 19 and imc < 25:
    cat = 'PESO IDEAL'
elif imc >= 25 and imc < 30:
    cat = 'SOBREPESO'
elif imc >= 30 and imc < 40:
    cat = 'OBESIDADE'
elif imc >= 40:
    cat = 'OBESIDADE SEVERA'


print(f'\033[1mSeu IMC é {imc:.2f}. \nFaixa: {cat}\033[m')
# Ler um valor em metros e converter para centímetros e milímetros
print('='*5, ' DESAFIO 08 ', '='*5)
number = float(input('Informe a dimensão em metros: '))
kil = number/1000
cent = number*100
mili = number*1000

print()
print('\033[7;40m', '='*3, 'Resultados: \033[m')
print('{:.2f} metros equivalem a \n{:.4f} kilômetros  \n{:.0f} centímetros \n{:.0f} milímetros ' .format(number, kil, cent, mili))

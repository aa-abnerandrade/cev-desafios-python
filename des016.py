# Ler número real e mostrar a parte inteira
print('='*5, ' DESAFIO 16 ', '='*5)

from math import sqrt, trunc, factorial

num = float(input('Digite um número qualquer: '))
print(f'\n\033[7;40;1m= Resultado da análise do número {num}: \033[m')
print(f'Sua metade é {num/2}')
print(f'Seu dobro é {num*2}')
print(f'A raiz quadrada é {sqrt(num):.4f}')
print(f'A porção inteira é {trunc(num)}')
print(f'O fatorial da porção inteira é {factorial(trunc(num))}')

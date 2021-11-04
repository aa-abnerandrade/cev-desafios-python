# Mostrar se um número é par ou ímpar
print('='*8, ' DESAFIO 30', '='*8)
print('VERIFICADOR DE PAR OU ÍMPAR')

number = int(input('Informe um número inteiro qualquer: '))
rest = number % 2
if rest == 0:
    print(f'\nO número {number} é par! ')
else:
    print(f'\nO número {number} é ímpar! ')
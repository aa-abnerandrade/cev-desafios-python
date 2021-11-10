print(' '*16, 'DESAFIO 52', ' '*16)
'''
Ler um número inteiro e retornar se é primo
'''
print(' '*5, '\033[7;40m VERIFICADOR DE NÚMEROS PRIMOS  \033[m', ' '*5)
primo = 0
naoprimo = 0

colors = {'clean': '\033[m', 'red': '\033[31m', 'blue': '\033[34m', 'bold': '\033[1m'}
number = int(input('Digite um número: '))
print('-'*42)

for cont in range(1, number+1):
    if (number % cont == 0):
        print(colors['blue'], cont, colors['clean'], end=' |')
        primo += 1
    else:
        print(colors['red'], cont, colors['clean'], end=' |')
        naoprimo += 1

print()
print(colors['bold'])
if (primo == 2):
    print('O número {} é divisível {} vezes,'
          '\nPortanto, É PRIMO.' .format(number, primo))
else:
    print('O número {} é divisível {} vezes,'
          '\nPortanto, NÃO É PRIMO.' .format(number, primo))


print(' '*16, 'DESAFIO 52', ' '*16)
'''
Ler um número inteiro e retornar se é primo
'''

print(' '*5, '\033[7;40m VERIFICADOR DE NÚMEROS PRIMOS  \033[m', ' '*5)

number = int(input('Digite um número: '))

print('-'*42)
# for cont in range(2, number): 2

print('\033[1;35m')
if (number != 2) and (number != 3) and (number != 5) and (number != 7): # não primo
    if (number % 2 == 0) or (number % 3 == 0) or (number % 5 == 0) or (number % 7 == 0): # não primo
        print(f'O número {number} não é primo.')
    else:
        print(f'O número {number} é primo. ')
else:
    print(f'O número {number} é primo.')
print('\033[m')


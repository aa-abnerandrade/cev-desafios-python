print(' '*16, 'DESAFIO 60', ' '*16)
'''
Fatorial
'''
print(' = CALCULADORA DE FATORIAL = '.center(44))

number = int(input('\nDigite um número para calcularmos o fatorial: '))
product = number

print('\n\033[7;40m', 'RESULTADO'.center(44), '\033[m')
while number > 1:
    print(number, 'x ', end='')
    product *= (number - 1)
    number = number - 1


print('1 =', product)

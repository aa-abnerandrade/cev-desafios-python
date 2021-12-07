print('DESAFIO 72'.center(40))
'''
Criar um tupla totalmente preenchida com contagem por extenso de 0 a 20
Ler um número do usuário e mostrar o valor por extenso - sem IF
'''
numbers = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
# print(numbers)
print('LEITOR DE NÚMEROS'.center(40))

usernumber = int(input('\nDigite um valor entre 0 e 20: '))

while usernumber < 0 or usernumber > 20:
    usernumber = int(input('\033[33mDigite um valor válido:  \033[m'))

print('\nRESULTADO DO LEITOR: ')
print(f'Você digitou o número {numbers[usernumber]}.')
print()
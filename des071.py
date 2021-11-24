print('DESAFIO 71'.center(50))
from math import trunc
'''
Simular funcionamento de caixa eletrônico. Ler o valor a ser sacado
Retornar quantas cédulas de cada valor serão entregues
Cédulas de 50, 20, 10 e 1
'''
print('\033[7;1;40m', end='')
print(f"{' A    T   M  ':*^50} \033[m")
cedula = 50

saque = int(input('Qual valor deseja sacar? '))

while True:
    print('Total de: '.rjust(45))

    div50 = saque / 50  # 3,4
    qtd50 = trunc(div50)
    saque = saque - (50 * qtd50)  # restam 20
    print(f'{qtd50} cédulas de R$ 50,00'.rjust(45))
    if saque == 0:
        break

    div20 = saque / 20  # 1
    qtd20 = trunc(div20)
    saque = saque - (20 * qtd20)  # restam 0
    print(f' {qtd20} cédulas de R$ 20,00'.rjust(45))
    if saque == 0:
        break

    div10 = saque / 10  # 0
    qtd10 = trunc(div10)
    saque = saque - (10 * qtd10)  # restam 0
    print(f' {qtd10} cédulas de R$ 10,00'.rjust(45))
    if saque == 0:
        break

    div01 = saque / 1  # 0
    qtd01 = trunc(div01)
    saque = saque - (1 * qtd01)  # restam 0
    print(f' {qtd01} cédulas de R$ 1,00'.rjust(45))
    if saque == 0:
        break

print('Obrigado por utilizar o ATM.')



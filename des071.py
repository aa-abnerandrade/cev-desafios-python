ced = 50
while True

# print('\n'*2)
print('DESAFIO 71'.center(50))
'''
Simular funcionamento de caixa eletrônico. Ler o valor a ser sacado
Retornar quantas cédulas de cada valor serão entregues
Cédulas de 50, 20, 10 e 1
'''
print('\033[7;1;40m', end='')
print(f"{' A    T   M  ':*^50} \033[m")
cedula = 50

Osaque = int(input('Qual valor deseja sacar? '))
saque = Osaque

while True:
    print('Total de: '.rjust(45))

    qtd50 = saque // 50 # 3,4
    saque = saque - (50 * qtd50)  # restam 20
    print(f'{qtd50} cédulas de R$ 50,00'.rjust(45))
    if saque == 0:
        break

    qtd20 = saque // 20  # 1
    saque = saque - (20 * qtd20)  # restam 0
    print(f' {qtd20} cédulas de R$ 20,00'.rjust(45))
    if saque == 0:
        break

    qtd10 = saque // 10 # 0
    saque = saque - (10 * qtd10)  # restam 0
    print(f' {qtd10} cédulas de R$ 10,00'.rjust(45))
    if saque == 0:
        break

    qtd01 = saque // 1
    saque = saque - (1 * qtd01)  # restam 0
    print(f' {qtd01} cédulas de R$ 1,00'.rjust(45))
    if saque == 0:
        break

print('Obrigado por utilizar o ATM.')

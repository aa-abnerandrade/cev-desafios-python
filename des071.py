print('DESAFIO 71'.center(40))
'''
Simular funcionamento de caixa eletrônico. Ler o valor a ser sacado
Retornar quantas cédulas de cada valor serão entregues
Cédulas de 50, 20, 10 e 1
'''
print('\033[7;1;40m', end='')
print(f"{' A    T   M  ':*^40} \033[m")
qtdced = 0
cedula = 100

Osaque = int(input('Qual valor deseja sacar? '))
saque = Osaque
print()

while True:
    if saque >= cedula:
        saque -= cedula
        qtdced += 1
    else:
        if qtdced > 0:
            print(f'{qtdced} cédulas de R${cedula:.2f}'.rjust(40))
        if cedula == 100:
            cedula = 50
            qtdced = 0
        elif cedula == 50:
            cedula = 20
            qtdced = 0
        elif cedula == 20:
            cedula = 10
            qtdced = 0
        elif cedula == 10:
            cedula = 5
            qtdced = 0
        elif cedula == 5:
            cedula = 1
            qtdced = 0
        if saque == 0:
            break

print()
print('\033[1;40mObrigado por utilizar o ATM\033[m'.center(50))

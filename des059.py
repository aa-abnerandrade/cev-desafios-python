print('DESAFIO 59'.center(52))
'''
Ler dois valores. Exibir menu para operação. 
somar / multiplicar / maior / novos números / sair
'''
print(' = CALCULADORA COM OPÇÕES = '.center(52))
opt = 1

print()
while opt != 0:
    num1 = int(input('Digite o primeiro valor: '))
    num2 = int(input('Digite o segundo valor: '))
    opt = int(input('Escolha uma opção: '
                    '\n     [1] Somar'
                    '\n     [2] Multiplicar'
                    '\n     [3] Maior/Menor'
                    '\n     [4] Novos Números'
                    '\n     [0] Sair'
                    '\n- Digite aqui -> '))
    print('\033[7;40m', 'RESULTADO'.center(52), '\033[m')
    if opt == 1:
        print(f'A soma dos valores inseridos é {num1 + num2}.')
    elif opt == 2:
        print(f'{num1} multiplicado por {num2} é {num1 * num2}')
    elif opt == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        elif num2 > num1:
            print(f'O número {num2} é maior do que {num1}')
        elif num1 == num2:
            print('Os números são iguais.')
    elif opt == 4:
        print(' Programa reiniciado. Insira novos valores a seguir.')
    print('\n' + '-'*52)

print('Programa Encerrado.'.center(52))

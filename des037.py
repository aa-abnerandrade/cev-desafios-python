print('='*10, ' DESAFIO 37 ', '='*10)
'''
Ler um número inteiro qualquer e permitir conversão
1 para binário, 2 para octal, 3 para hexadecimal
'''
print('='*32, '\n')
number = int(input('Informe um número inteiro: '))
opt = int(input('Deseja converter para qual base:'
                '\n     [1] Binário'
                '\n     [2] Octal'
                '\n     [3] Hexadecimal '
                '\n     [esc] Sair'
                '\n  === Digite a opção deseja aqui: '))
if opt == 1:
    print(f'\n\033[32mA conversão de {number} para Binário é: {bin(number)[2:]}\033[m')
elif opt ==2:
    print(f'\n\033[32mA conversão de {number} para Octal é {oct(number)[2:]}\033[m')
elif opt == 3:
    print(f'\n\033[32mA conversão de {number} para Hexadecimal {hex(number)[2:]}\033[m')
else:
    print('\n\033[31mOpção inválida. Por favor reinicie o programa e esolha uma opção desejada.\033[m')

print('\n\033[1mPrograma encerrado. Volte sempre.\033[m')
print('DESAFIO 66'.center(50))
'''
Ler vários números inteiros. Digitar 999 para sair
Não considerar flag
Exibir quantidade de números inseridos e soma
'''
print('CALCULADORA DE SOMA'.center(50))
print('Insira 999 para finalizar a soma e encerrar o programa'.center(50), '\n')
soma = cont = 0

while True:
    cont += 1
    number = int(input(f'{cont}° valor: '))
    if number == 999:
        cont -= 1
        break
    soma += number

print(f'\n\033[1mSoma dos {cont} valores digitados: {soma}\033[m')


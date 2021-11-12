print('DESAFIO 61'.center(50))
'''
Ler vários números inteiros. No final, exibir média e os menor e maior valores.
Perguntar ao usuário se deseja continuar.
'''
answer = 'S'
total = 0
cont = 1
maior = 0
print('\033[1;4mCADASTRO TOTAL\033[m'.center(60))
print('-'*50)

while answer != 'N':
    number = int(input(f'Informe o {cont}º valor: '))
    if cont == 1:
        menor = number
    total += number
    cont += 1
    if number > maior:
        maior = number
    if number < menor:
        menor = number
    answer = str(input('\033[30mInserir mais um valor? [S/N] \033[m')).strip().upper()

print()
print('\033[7;40m', 'RESULTADO'.center(48), '\033[m')
media = total / (cont-1)
print('Foram inseridos um total de {} valores.' .format(cont-1))
print('A média dos valores digitados é {:.2f}.' .format(media))
print('O maior valor inserido foi {} e o menor foi {}.' .format(maior, menor))


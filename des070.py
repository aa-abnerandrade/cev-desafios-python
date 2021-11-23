print('DESAFIO 70'.center(40))
'''
Ler o nome e preço de vários produtos. Perguntar se deseja continuar
Retornar: a) total gasto na compra; b) quantos produtos custam mais de 1000 reais; c) nome do produto mais barato
'''

print(f"\033[1;7;40m{' BRAZILIAN SHOPS ':=^40}\033[m")
total = contmil = lowest = soma = 0
cont = 1

while True:
    print('_'*40)
    print(f'ITEM {cont}'.center(40))
    item = str(input('Nome do produto: '))
    value = float(input('Valor: R$'))
    soma += value
    if value >= 1000:
        contmil += 1
    if lowest == 0:
        lowest = value
        namelow = item
    else:
        if value < lowest:
            lowest = value
            namelow = item
    out = str(input(' = = = Deseja continuar? [S/N] ')).strip().upper()
    if out == 'N':
        break
    cont += 1

print()
print('\033[1;40m RESULTADOS \033[m'.center(50))
print(f'Total de itens: {cont}')
print(f'Valor total: R${soma:.2f}')
print(f'Média: R${soma/cont:.2f} | Produtos R$1000+ : {contmil}')
print(f'Item de menor valor: {namelow} = R${lowest:.2f}')
print(f"\n\033[1;7;40m{' programa encerrado ':=^40}\033[m")
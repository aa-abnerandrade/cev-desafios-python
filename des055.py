print(' '*18, 'DESAFIO 55', ' '*18)
'''
Ler o peso de 5 pessoas e no fim mostrar o maior e o menor peso
'''
print(' '*16, '\033[7;40m BALANÇA PESO  \033[m', ' '*16)
print('-'*49, '\n')
Ppesado = 0
Pleve = 100


qtd = int(input('Quantos produtos deseja checar? '))
print('-'*42, '\n')

for cont in range(1, qtd+1):
    item = str(input(f'Informe o nome do {cont}º item: ')).strip().title()
    peso = float(input(f'Peso de {item}: '))
    print('- '*20)
    if (peso > Ppesado):
        Ppesado = peso
        Ipesado = item
        Cpesado = cont
    if (peso < Pleve):
        Pleve = peso
        Ileve = item
        Cleve =cont

print()
print('\033[1;40m', ' '*18, 'RESULTADOS', ' '*18, '\033[m')
print('\033[1mItem mais pesado: {} \033[m'
      '\nPeso: {}'
      '\nPosição: {}' .format(Ipesado, Ppesado, Cpesado))
print('\033[1mItem mais leve: {} \033[m'
      '\nPeso: {}'
      '\nPosição: {}' .format(Ileve, Pleve, Cleve))


print(' '*16, 'DESAFIO 50', ' '*16)
'''
Ler seis números inteiros e somar apenas os pares
'''
print()
print(' '*11, '\033[7;40m CALCULADORA DE PARES \033[m', ' '*11)
soma = 0
qtd = 0
contpar = 0

qtd = int(input('Quantos valores deseja inserir? '))
print('-'*45)

for cont in range(1, qtd+1):
    number = int(input(f'Digite o {cont}º valor: '))
    if (number % 2 == 0):
        soma += number
        contpar += + 1

print('\n\033[4mResultado da análise: \033[m')
print(f'\033[1mDe {qtd} valores inseridos, {contpar} são pares. A soma deles é {soma}. \033[m')

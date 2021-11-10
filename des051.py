print(' '*27, 'DESAFIO 51', ' '*27)
'''
Ler o primeiro termo e razão de uma Progressão Aritmética. Mostrar os 10 primeiros termos
'''

print(' '*20, '\033[7;40m PROGRESSÃO ARITMÉTICA  \033[m', ' '*20)

primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Informe a razão: '))
termo = primeiro

print()
print('\033[1;40m', ' '*22, 'TERMOS DA P.A.:', ' '*25, '\033[m')
for cont in range(1, 10+1):
    print(f'\033[1m{termo}\033[m → ', end=' ')
    termo += razao
print('FIM.')


print('DESAFIO 61'.center(44))
'''
Refazer o 51. Ler termo e razão, exibir 10 primeiros termos.
'''
print()
print('\033[1;4mPROGRESSÃO ARITMÉTICA\033[m'.center(52))
print('-'*44)
primeiro = int(input('Digite o primeiro termo da PA: '))
termo = primeiro
razao = int(input('Informe a razão: '))
cont = 1

print('\n\033[1mOs termos são: \033[m')
while cont < 10 + 1:
    print(termo, '→', end=' ')
    termo += razao
    cont += 1
print('FIM.')

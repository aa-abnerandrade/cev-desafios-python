print(' '*16, 'DESAFIO 62', ' '*16)
'''
Melhorar o 61. Após os 10 termos, perguntar pro usuário se quer exibir mais. 
Ler 0 encerra o laço. 
'''
print()
print('\033[1;4mPROGRESSÃO ARITMÉTICA II\033[m'.center(52))
print('-'*44)
qtd = 10
primeiro = int(input('Digite o primeiro termo da PA: '))
termo = primeiro
razao = int(input('Informe a razão: '))
cont = 1
qtd = 10
tot = 0

print('\n\033[1mOs termos são: \033[m')
while qtd != 0:
    while cont < qtd+1:
        print(termo, '→', end=' ')
        termo += razao
        cont += 1
        tot += 1
    print('FIM.', end=' ||| ')
    cont = 1
    qtd = int(input('\033[33mQuantos termos mais deseja exibir? \033[m'))
    print()

print(f'\033[1mPrograma encerrado. Foram exibidos um total de {tot} termos.\033[m ')
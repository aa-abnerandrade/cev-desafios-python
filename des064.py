import emoji

print(' '*16, 'DESAFIO 64', ' '*16)
import emoji

'''
Ler vários números inteiros. Informar quantos foram inseridos e a soma.
999 para sair. Não considerar o flag na soma/quantidade
'''
print()
print('\033[1;4mCADASTRO TOTAL\033[m'.center(54))
soma = -999
cont = 1
number = 0
print('Insira 999 para encerrar'.center(42))

print()
while number != 999:
    number = int(input('> Infome o {}º valor: '. format(cont)))
    soma += number
    cont += 1

print()
print(emoji.emojize(f' :check_mark: A soma de todos os {cont - 1} valores digitados é {soma}.', use_aliases=True))
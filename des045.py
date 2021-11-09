print(' '*16, 'DESAFIO 45', ' '*16)
'''
Elaborar Jokenpô - pedra, papel, tesoura
'''

print('\033[1;30;44m', ' ' * 14, 'VAMOS JOGAR?', ' ' * 14, '\033[m')
from random import randint
from time import sleep
import emoji

print()
print(
    'Jokenpo é uma brincadeira japonesa, '
    '\nonde dois jogadores escolhem um dentre '
    '\ntrês possíveis itens: Pedra, Papel ou Tesoura.'
    '\n\033[1mAs regras são as seguintes:'
    '\nPedra empata com Pedra e ganha de Tesoura'
    '\nTesoura empata com Tesoura e ganha de Papel'
    '\nPapel empata com Papel e ganha de Pedra\033[m')
print()
print('\033[1;34mVAMOS JOGAR!!!\033[m\n')
enter = input('Enter para Start')
print()
print('\033[30;46m', ' '*7, '... escolhendo um item...', ' ' * 7, '\033[m')
optmac = randint(1, 3)

# Dando nome a escolha da máquina
if optmac == 1:
    chomac = 'Pedra'
elif optmac == 2:
    chomac = 'Tesoura'
elif optmac == 3:
    chomac = 'Papel'

sleep(3)
print('\n\033[34m       PRONTO!!! Agora é a sua vez:\033[m')
#print(optmac)
#print(emoji.emojize('Python is :thumbs_up:'))

optuse = int(input(emoji.emojize('\033[34m      Escolha uma das opções abaixo:\033[m\n'
                   '    \033[30m[1] \033[1;37m:moyai:   \033[0;30m[2] \033[31m:scissors:   \033[0;30m[3] :page_facing_up:\n'
                   '\033[46m                   \033[m\033[1;36m Digite aqui sua opção: \033[m', use_aliases=True)))
# Dando nomes a escolha do usuário
if optuse == 1:
    chouse = 'Pedra'
elif optuse == 2:
    chouse = 'Tesoura'
elif optuse == 3:
    chouse = 'Papel'
else:
    chouse = 'Invalid'
print('\033[33m','.'*42,'\033[m')

sleep(2)
if optmac == optuse:
    print('\033[1;35m               EMPATAMOS!\n     Nós dois escolhemos a carta {}' .format(chomac))
elif (optmac == 1 and optuse == 2) or (optmac == 2 and optuse == 3) or (optmac == 3 and optuse == 1):
    print('\033[1;31m               Você PERDEU!\n'
          '       Eu joguei {} e você {}' .format(chomac, chouse))
elif (optuse == 1 and optmac == 2) or (optuse == 2 and optmac == 3) or (optuse == 3 and optmac == 1):
    print('\033[1;32m                Você VENCEU!\n'
          '       Eu joguei {} e você {} ' .format(chomac, chouse))
elif chouse == 'Invalid':
    print('               Jogada Inválida. '
          '\n   Reinicie o programa e tente novamente. ')

print('\033[m')
print(emoji.emojize('\033[34mQue tal reiniciar o jogo para uma revanche, hein? :fire:\033[m', use_aliases=True))
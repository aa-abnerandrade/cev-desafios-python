print('DESAFIO 58'.center(52))
'''
Melhorar o desafio 28. Número entre 0 e 10.
Jogador terá tentativas infinitas até acertar. Informar a quantidade de palpites. 
'''
from random import randint
from time import sleep

colors = {'clean': '\033[m', 'purple': '\033[35m', 'sistem': '\033[7;40m', 'red': '\033[31m', 'blue': '\033[1;36m'}
tent = 0


print('\n', colors['sistem'], ' = MÁQUINA DA SORTE = '.center(52), colors['clean'])

print('Estou pensando em um número... ', end=' ')
mach = randint(1, 10)
sleep(0.5)
print(colors['purple'], 'PRONTO! Agora é sua vez.', colors['clean'])
answer = 11

print()
while mach != answer:
    answer = int(input('Escolha um número, de 1 a 10: '))
    if answer < mach:
        print('\033[31mErrou. É mais! \033[m', end='')
    elif answer > mach:
        print('\033[31mErrou. É menos! \033[m', end='')
    tent += 1


print()
print(colors['blue'], f'ACERTOU! Após {tent} tentativas. ', colors['clean'])
print('DESAFIO 58'.center(52))
'''
Melhorar o desafio 28. Número entre 0 e 10.
Jogador terá tentativas infinitas até acertar. Informar a quantidade de palpites. 
'''
from random import randint
from time import sleep

colors = {'clean': '\033[m', 'purple': '\033[35m', 'sistem': '\033[7;40m', 'red': '\033[31m', 'blue': '\033[1;36m'}
tent = 1


print('\n', colors['sistem'], ' = MÁQUINA DA SORTE = '.center(52), colors['clean'])

print('Estou pensando em um número... ', end=' ')
mach = randint(1, 10)
sleep(0.5)
print(colors['purple'], 'PRONTO! Agora é sua vez.', colors['clean'])


answer = int(input('\nEscolha um número, de 1 a 10: '))

while mach != answer:
    answer = int(input(colors['red'] + 'Errou, tente novamente: ' + colors['clean']))
    tent += 1

print()
print(colors['blue'], f'ACERTOU! Após {tent} tentativas. ', colors['clean'])
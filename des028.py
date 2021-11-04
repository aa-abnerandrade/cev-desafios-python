# Computador pensar em número inteiro entre 0 e 5 e jogar com o usuário
print('='*5, ' DESAFIO  28', '='*5)
from random import randint
from time import sleep

print('\n = MÁQUINA DA SORTE =')
print('Um momento enquanto escolho um número de 1 a 5...', end=' ')
sleep(1)
print('ESCOLHIDO!\nAgora é sua vez.', end=' ')
mach = randint(1, 5)
user = int(input('Tente adivinhar que número eu escolhi: '))

print(f'\nEu joguei o número {mach}, você jogou o número {user}. ', end='')
if user == mach:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou.')

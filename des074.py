print('DESAFIO 74'.center(40))
'''
Criar programa que vai gerar 5 números aleatórios e colocar em uma tupla
Após isso, mostrar a listagem de números gerados e também indique menor e o maior valor que estão na tupla 
'''
from random import randint
print(f"\033[1;7;40m{' VERIFICADOR DE MAIOR / MENOR ':=^40}\033[m")

numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Números gerados: {numbers}')
print(f" Maior número: {max(numbers)} ")
print(f" Menor número: {min(numbers)}")


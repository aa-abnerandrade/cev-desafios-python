# Ler um número inteiro e mostrar o antecessor e sucessor
print ('===== DESAFIO 05 =====')
number = int(input('Digite um número: '))
print('Analisando o número {}... \nSeu {}antecessor é {}{} e seu {}sucessor é {}{}. ' . format(number, '\033[32;1m', (number-1), '\033[m', '\033[36;1m', (number+1), '\033[m'))
colors = {'clean': '\033[m', 'baw': '\033[7;40m', 'blu': '\033[1;34m'}

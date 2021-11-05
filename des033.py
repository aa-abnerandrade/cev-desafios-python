# Ler 3 números e mostrar qual é o maior e qual é o menor
print('='*8, ' DESAFIO 33', '='*8)
print('\033[1;30;46m VERIFICADOR DE MAIOR/MENOR \033[m')

n1 = int(input('\nDigite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))


if n1 >= n2 and n1 >= n3:
    maior = n1
    if n2 <= n3:
        menor = n2
    else:
        menor = n3
if n2 >= n1 and n2 >= n3:
    maior = n2
    if n1 <= n3:
        menor = n1
    else:
        menor = n3
if n3 >= n1 and n3 >= n2:
    maior = n3
    if n1 <= n2:
        menor = n1
    else:
        menor = n2

print('\n= RESULTADOS: ')
print(f'\033[1;33mO maior valor inserido foi: {maior}\033[m')
print(f'\033[1;34mO menor valor inserido foi: {menor}\033[m')

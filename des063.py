print('DESAFIO 63'.center(50))
'''
Ler quantidade desejada para exibir os primeiros valores de Fibonacci. 
'''
print('\033[1;4mSEQUÊNCIA DE FIBONACCI\033[m'.center(60))

cont = int(input('\nQuantos termos da sequência de Fibonacci deseja visualizar? '))
N1 = 0
N2 = 1

print('\n\033[1mOs {} primeiros termos são: \033[m' .format(cont))
print(N1, end=' ')
while cont > 1:
    print('→ ', N2, end=' ')
    N3 = N1 + N2
    N1 = N2
    N2 = N3
    cont = cont - 1
print('→ \033[7;40m FIM \033[m')

# 0 1 1 2 3 5 8 13 21 34 - 55 89
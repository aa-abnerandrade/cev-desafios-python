print('='*10, ' DESAFIO 38 ', '='*10)
'''
Ler 2 num int e comparar.
Exibir qual é o maior e menor ou se são iguais
'''
print()
X = int(input('Digite o número X: '))
Y = int(input('Digite o número Y: '))
print()

if X > Y:
    print(f'\033[1;31mO número {X} é maior.\033[m \n\033[1;34mO número {Y} é menor.\033[m')
elif X < Y:
    print(f'\033[1;31mO número {Y} é maior.\033[m \n\033[1;34mO número {X} é menor.\033[m')
elif X == Y:
    print('\033[1;33mOs valores X e Y são iguais.\033[m')
else:
    print('\033[1;37;40mOpção inválida. Reinicie o programa.\033[m')

print('\n\033[7;40m = Programa encerrado. Volte sempre! = \033[m')

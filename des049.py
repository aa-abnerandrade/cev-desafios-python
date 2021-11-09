print(' '*16, 'DESAFIO 49', ' '*16)
'''
Refazer a tabuada (Desafio 9), com estrutura FOR
'''
print()
print('\033[7;40m', ' '*16,  'TABUADA', ' '*16, '\033[m')
number = int(input('Insira o número do qual deseja visualizar a tabuada: '))
print('\n--- Vamos lá! \n')

print(' '*14, f'TABUADA DE {number}', ' '*14)
for cont in range(1, 10+1):
    print(cont, f' x {number} = ', number*cont)

print('\nObrigado por usar nossa tabuada. Volte sempre! ;)')
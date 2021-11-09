print(' '*16, 'DESAFIO 47', ' '*16)
'''
Mostrar todos os números pares de 1 a 50
'''

print()
print('De 1 a 50, os números pares são:')
for cont in range(1, 50+1):
    if (cont % 2 == 0):
        print('> \033[1m', cont, end='\033[m ')

print('\n\nObrigado por utilizar nosso contador. Volte sempre. ')
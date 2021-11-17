print('DESAFIO 67'.center(50))
'''
Tabuada
Ler números inteiros e retornar tabuada até que o usuário digite um valor negativo
'''
print('\033[1;36mTABUADA\033[m'.center(60))

cont = 1
print()

while True:
    number = int(input('\033[1mDe qual número deseja visualizar a tabuada? \033[m'))
    if number < 0:
        break
    print()
    print(f' Tabuada de  {number}  '. center(50))
    print('_'*50)
    for cont in range(1, 10+1):
        print(f'{cont} x {number}: {cont*number}'.center(50))
    print('-'*50)
    print()

print('\n\033[30mPrograma Encerrado. Obrigado por utilizar nossa tabuada.'.center(60))






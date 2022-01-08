print('DESAFIO 80'.center(44))
'''
Digitar cinco valores e cadastrar numa lista, já na posição correta de inserção. sem usar sort
no final, exibir a lista ordenada 5 2 4 0 1
'''
print(f" {' ORGANIZADOR DE NÚMEROS ':_^44} ")
numbers = []
for X in range(1, 5+1):
    number = int(input(f'\033[1mDigite o {X}º número: \033[m'))
    if not numbers:
        numbers.append(number)
        print('\033[37mNúmero adicionado ao final da lista.\033[m')
    else:
        numbers.append(number)
        for i in range(0, len(numbers)):
            for j in range(0, len(numbers)):
                if numbers[j] > numbers[i]:
                    reserva = numbers[j]
                    numbers[j] = numbers[i]
                    numbers[i] = reserva
        print('\033[37mNúmero adicionado.\033[m')


print(f"\n\033[40;1mOs valores digitados foram: {numbers}\033[m")
print('DESAFIO 80'.center(44))
'''
Digitar cinco valores e cadastrar numa lista, já na posição correta de inserção. sem usar sort
no final, exibir a lista ordenada
'''

numbers = []
for X in range(0, 5):
    number = int(input('Digite um número: '))
    if not numbers:
        numbers.append(number)
    else:
        while number
        for Y in range(0, len(numbers)):
            if number > numbers[Y] and number < numbers[Y+1]:
                numbers.insert(pos, number)


print(f"\nOs valores digitados foram: {numbers}")
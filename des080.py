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
        print('Número adicionado ao final da lista.')
    else:
        #for pos in range(0, len(numbers)):
        pos = 0
        if number *4* > numbers[pos]: #não usa o X?
            numbers.append(number)
        else:
            numbers.insert(0, number)
        pos += 1

print(f"\nOs valores digitados foram: {numbers}")
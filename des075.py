print('DESAFIO 75'.center(40))
'''
Ler 4 valores pelo teclado e guardar em uma tupla. Após isso, mostre:
a) quantas vezes apareceu o valor 9 / b) em que posição foi digita o primeiro valor 3 / c) quais foram os números pares
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número:  '))
n3 = int(input('Digite o terceiro número: '))
n4 = int(input('Digite o último número: '))

numbers = (n1, n2, n3, n4)
print(numbers)

print(numbers[2])
print(numbers[3] % 2)

pares = 0
for cont in range(1, 4+1):
    print(numbers[cont])
    if (numbers[cont] % 2) == 0:
        if pares == 0:
            pares = numbers[cont]
        else:
            pares += numbers[cont]
print(f'Os números pares são: {pares}')

nrepeat = int(input('Qual número deseja contar: '))
qtdrepeat = numbers.count(nrepeat)
if qtdrepeat == 0:
    print(f'O número {nrepeat} não apareceu na listagem. ')
else:
    print(f'O número {nrepeat} apareceu {qtdrepeat} vez(es). ')

nsearch = int(input('Qual número deseja localizar: '))
nposit = numbers.index(nsearch)
if nposit == 0:
    print(f'Não localizamos o número {nsearch} em nenhuma posição. ')
else:
    print(f'O número {nsearch} foi localizado na posição {nposit}')



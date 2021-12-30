print('DESAFIO 82'.center(44))
'''
Ler vários números e colocar em lista
separar os números pares e ímpares em duas novas listas geradas 
ao final, exibir as 3 listas geradas
'''
numbers = []
numpar = []
numimpar = []
while True:
    numbers.append(int(input('Valor: ')))
    if numbers[-1] % 2 == 0:
        numpar.append(numbers[-1])
    else:
        numimpar.append(numbers[-1])
    cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if cont == 'N':
        break

print(f" Foram digitas os valores {numbers}" )
print(f" Valores pares {numpar}")
print(f" Valores ímpares {numimpar}")




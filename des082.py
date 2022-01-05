print('DESAFIO 82'.center(44))
'''
Ler vários números e colocar em lista
separar os números pares e ímpares em duas novas listas geradas 
ao final, exibir as 3 listas geradas
'''
print(f"\033[40;1m {' PARES E ÍMPARES ':_^44} \033[m")

numbers = []
numpar = []
numimpar = []
while True:
    numbers.append(int(input('\033[1mValor: \033[m')))
    if numbers[-1] % 2 == 0:
        numpar.append(numbers[-1])
    else:
        numimpar.append(numbers[-1])
    cont = str(input('\033[37mDeseja continuar? [S/N]: \033[m')).strip().upper()
    if cont == 'N':
        break

print(f"\n\033[40;1m {'RESULTADOS':.<44} \033[m"
      f'\n Foram digitados os valores: {sorted(numbers)}'
      f'\n Valores pares: {sorted(numpar)}'
      f'\n Valores ímpares: {sorted(numimpar)}')




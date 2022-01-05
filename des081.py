print('DESAFIO 81'.center(40))
'''
Ler vários números e colocar em lista
retornar: a) quantos foram digitados / b) lista em ordem decrescente / c) se o valor 5 foi digitado 
'''
print(f"{'  DADOS NUMÉRICOS  ':*^40}\n")
numbers = []

ordinal = 1
while True:
    number = int(input(f"\033[1mDigite o {ordinal}º número: \033[m"))
    numbers.append(number)
    cont = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if cont == 'N':
        break
    ordinal +=1

print()
print(f'\033[1;40mTotal de números digitados: {len(numbers)} \033[m')
find = str(input('\n\033[33mDeseja encontrar número específico?\033[m [S/N]: ')).strip().upper()
if find == 'S':
    search = int(input('Qual valor deseja checar? '))
    if search in numbers:
        print(f"\033[34mO número {search} consta na lista. ")
    else:
        print(f"\033[31mNão consta o número {search} na lista. ")
    print('\033[m')

numbers.sort(reverse=True)
print(f"\033[1;40mLista em ordem decrescente: {numbers}\033[m\n")
print(f"{' Programa encerrado ':.^44}")



print('DESAFIO 79'.center(44))
'''
Ler vários valores. Não permitir entrada de números repetidos
Exibir em ordem crescente
'''
print(f" {'ENTRADA DE VALORES':_^40} ")
numbers = []

pos = 1
while True:
    number = int(input(f"Digite o {pos}º valor: "))
    if number not in numbers:
        numbers.append(number)
        print('\033[32mValor adicionado com sucesso. \033[m')
        pos += 1
    else:
        print('\033[31mNão é possível inserir um número já existente.\033[m')
    cont = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    if cont == 'N':
        break

print(f"\n\033[1;32m\nPROGRAMA ENCERRADO"
      f"\n>>> Os valores digitados foram: {sorted(numbers)}\033[m")


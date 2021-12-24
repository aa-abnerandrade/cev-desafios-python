print('DESAFIO 79'.center(44))
'''
Ler vários valores. Não permitir entrada de números repetidos
Exibir em ordem crescente
'''
numbers = []
while True:
    number = int(input("Digite um valor:"))
    if number not in numbers:
        numbers.append(number)
    else:
        print('Não é possível inserir um número já existente.')
    cont = str(input("Deseja continuar? [S/N]: ")).strip().upper()
    if cont == 'N':
        break

print(f"Valores digitados: {sorted(numbers)}")


# Ler salário e calcular 15% de aumento
print('='*5, ' DESAFIO 13 ', '='*5)
name = str(input('Informe o nome do colaborador: '))
sal = float(input(f'Digite o salário de {name}: R$'))
print()
print('='*3, 'Cálculos: ')
fifteen = sal * 0.15
new_sal = sal + fifteen
print(f'Salário atual: R${sal:.2f}. \n15% de aumento: R${fifteen:.2f}.  \nNovo Salário: R${new_sal:.2f}.')

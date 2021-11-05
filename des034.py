# Perguntar o salário de um funcionário e calcular: 15% de aumento para salários até 1.250 e 10% para maiores salários
print('='*5, ' DESAFIO 34', '='*5)
print('\nCALCULADORA SALARIAL')
name = str(input('\nDigite o nome do colaborador: ')).strip().title()
sal = float(input(f'Informe o salário de {name}: R$'))

if sal > 1250.00:
    aumento = sal * 0.10
    newsal = sal + aumento
else:
    aumento = sal * 0.15
    newsal = sal + aumento

print('\n\033[7;40m=> QUADRO DE CÁLCULO:\033[m')
print(f'Salário atual: R$ {sal:.2f}.'
      f'\nValor de aumento: R$ {aumento:.2f}.'
      f'\nNovo salário de {name}: R$ {newsal:.2f}')

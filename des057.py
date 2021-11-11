print(' '*16, 'DESAFIO 57', ' '*16)
'''
Ler sexo. Aceitar apenas H ou M. Identificar valor inválido. 
'''
print('Cadastro de Candidatos'.center(42))
sex = 'Blank'
cnh = 'Blank'

print()
fullname = str(input('Nome completo: ')).title().strip()
names = fullname.split()
while sex != 'H' and sex != 'M':
    sex = str(input(f'Qual o sexo de {names[0]} [H/M]: ')).strip().upper()
while cnh != 'A' and cnh != 'B':
    cnh = str(input('Tipo de CNH [A/B]: ')).strip().upper()

print()
print(f'\033[1mO cadastro de {names[0]} foi concluído com sucesso.\033[m')


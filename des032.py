# Ler um ano qualquer e verificar se é bissexto
from calendar import isleap
print('='*5, ' DESAFIO 32', '='*5)
year = int(input('Informe o ano que deseja verificar [xxxx]: '))

print(f'\n= O ano {year}', end=' ')
if isleap(year):
    print('é bissexto.')
else:
    print('NÃO é bissexto. ')
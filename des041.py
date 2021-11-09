print(' '*9,'DESAFIO 41', ' '*9)
'''
Ler ano de nascimento e retornar categoria 
9 - mirim / 14 - infantil / 19 - junior / 20 - senior / acima - master
'''
from datetime import datetime

now = datetime.now()
ycurrent = now.year

print('\nCONFEDERAÇÃO NACIONAL DE NATAÇÃO')
ybirth = int(input('\nDigite o ano de nascimento [xxxx]: '))
age = ycurrent - ybirth

if age >= 7 and age <= 9:
    cat = 'MIRIM'
    min = 7
    max = 9
elif age >= 10 and age <=14:
    cat = 'INFANTIL'
    min = 10
    max = 14
elif age >= 15 and age <= 19:
    cat = 'JÚNIOR'
    min = 15
    max = 19
elif age == 20 or age == 21:
    cat = 'SÊNIOR'
    min = 20
    max = 21
elif age == 22 or age == 23:
    cat = 'MASTER'
    min = 22
    max = 23
else:
    cat = 'NÃO CONSTA'

print()
print ('\033[7;40m Idade do atleta: {:8} ANOS \033[m' .format(age))
print('\033[7;40m', 'Categoria: {:19} \033[m' .format(cat))

if cat != 'NÃO CONSTA':
    print('\033[7;40m De {} a {} anos  ------------- \033[m' .format(min, max))

print()
print('\033[7;40m', '_'*30, '\033[m')



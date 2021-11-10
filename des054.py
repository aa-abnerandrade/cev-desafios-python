print(' '*16, 'DESAFIO 54', ' '*16)
'''
Ler o ano de nascimento de 7 pessoas e mostrar quantas atingiram a maioridade e quantas não 
'''
from datetime import datetime
now = datetime.now()
Ycurrent = now.year

print(' '*14, '\033[7;40m VALIDADOR 21 \033[m', ' '*14)
minor = 0
legal = 0
total = 0

print()
for cont in range(1, 7+1):
    Ybirth = int(input(f'Ano de nascimento da {cont}ª pessoa [xxxx]: '))
    age = Ycurrent - Ybirth
    if (age <= 21):
        minor += + 1
    elif (age > 21):
        legal += + 1
    total += + 1

print('\n\033[1;7;40m RESULTADOS:' + ' '*34 + '\033[m'
      '\nTotal de cadastrados: {}'
      '\nMaiores de idade: {}'
      '\nMenores de idade: {}' .format(total, legal, minor))
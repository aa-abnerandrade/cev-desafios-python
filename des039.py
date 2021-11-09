print('='*17, 'DESAFIO 39', '='*17)
'''
Ler ano de nascimento e informar condição militar
Se ainda vai se alistar, se está em tempo ou se está atrasado
Informar tempo que falta ou que passou
'''
from datetime import datetime

now = datetime.now()
ycurrent = now.year

print()
print('\033[7:40m', '- '*6, ' SERVIÇO MILITAR ', ' -'*6, '\033[m')
name = str(input('Informe seu nome completo: ')).strip().title()
gender = int(input('Informe seu sexo [1]H [2]M:  '))
ybirth = int(input('Informe o ano de nascimento [xxxx]: '))

ydif = ycurrent - ybirth
print('-'*45)

if gender == 1:
    if ydif == 18:
        print('\033[1;33mVocê está com {} anos, idade ideal para se apresentar ao serviço militar obrigatório.\033[m'
                '\nPor favor, procure o serviço de alistamento militar mais próximo da sua residência. ' .format(ydif))
    elif ydif <= 17:
        print('Você tem {} anos e por isso ainda não tem obrigações militares. '
                '\nPor gentileza, procure o serviço militar em {} anos.' .format(ydif, 18 - ydif))
    elif ydif >= 19:
        print('\033[1;31mVocê tem {} anos e possui pendências com junto ao serviço militar. \033[m'
                '\nVocê deveria ter se apresentado há {} anos, no ano de {}.' .format(ydif, ydif - 18, ycurrent-ydif))
else:
    print('\033[1;33mMulheres não tem obrigatoriedade militar.\033[m')

print()
print('\033[7;40m = = Programa Encerrado.  Volte Sempre. =  = \033[m')
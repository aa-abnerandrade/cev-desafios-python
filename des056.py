print(' '*16, 'DESAFIO 56', ' '*16)
'''
Ler nome, idade e sexo de 4 pessoas
Retornar:  média de idade, qual o nome do homem mais velho, mulheres com menos de 21 anos
'''
print(' '*7, '\033[7;40m CADASTRAMENTO DE NOVO SÓCIO \033[m', ' '*7)
print('\033[37mResponda às perguntas a seguir para emitir o relatório.\033[m')
print()

Nwomen = 0
ageoldest = 0
soma_age = 0

qtd = int(input('Quantas sócios deseja cadastrar? -> '))
print('Entendido. Você deseja cadastrar {} novos sócios. '
      '\nVamos lá!'
      '\n ' .format(qtd))

for cont in range(1, qtd+1):
    print('\033[1;4mPreencha os dados referente ao {}º sócio:\033[m' .format(cont))
    name = str(input('NOME -> ')).strip().title()
    age = int(input('IDADE -> '))
    sex = int(input('SEXO | [1] Homem [2] Mulher ->  '))
    print('-'*38)
    soma_age = soma_age + age
    if sex == 1:
        if age > ageoldest:
            ageoldest = age
            nameoldest = name
    elif sex == 2:
        if age <= 21:
            Nwomen = Nwomen + 1

media_age = soma_age/qtd

print('\033[7;40m {:42} \033[m' .format('RESULTADOS: '))
print('A média de idade é {:.1f} .' .format(media_age))
if ageoldest == 0:
    print('\033[33mNenhum homem foi cadastrado. \033[m')
    nameoldest = 'Blank'
else:
    print('O homem mais velho se chama: {}, com {} anos.'.format(nameoldest, ageoldest))

if Nwomen == 0:
    print('\033[33mNenhuma mulher foi cadastrada. \033[m')
else:
    print('Foram cadastradas um total de {} mulheres com 21 anos ou menos. ' .format(Nwomen))


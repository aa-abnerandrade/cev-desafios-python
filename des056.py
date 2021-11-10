print(' '*16, 'DESAFIO 56', ' '*16)
'''
Ler nome, idade e gênero de 4 pessoas
Retornar:  média de idade, qual o nome do homem mais velho, mulheres com menos de 21 anos
'''
print(' '*7, '\033[7;40m CADASTRAMENTO DE NOVO SÓCIO \033[m', ' '*7)
print('\033[37mResponda às perguntas a seguir para emitir o relatório.\033[m')
print()

NFemale = 0
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
    sex = int(input('GÊNERO | [1] Masculino [2] Feminino ->  '))
    print('-'*38)
    soma_age = soma_age + age
    if sex == 1:
        if age > ageoldest:
            ageoldest = age
            nameoldest = name
    elif sex == 2:
        if age <= 21:
            NFemale = NFemale + 1

media_age = soma_age/qtd

print('\n\033[7;40m {:42} \033[m' .format('RESULTADOS: '))
print('A média de idade é {:.1f} .' .format(media_age))
if ageoldest == 0:
    print('\033[33mNenhuma pessoa do gênero masculino  foi cadastrada. \033[m')
    nameoldest = 'Blank'
else:
    print('A pessoa do sexo masculino com mais idade se chama: {}, com {} anos.'.format(nameoldest, ageoldest))

if NFemale == 0:
    print('\033[33mNinguém do gênero feminino, com menos de 21 anos foi cadastrada. \033[m')
else:
    print('Foram cadastradas um total de {} pessoas do sexo feminino, com 21 anos ou menos. ' .format(NFemale))



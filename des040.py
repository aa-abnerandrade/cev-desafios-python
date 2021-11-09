print('='*17, 'DESAFIO 40', '='*17)
'''
Ler 2 notas e mostrar a média
<5 reprova / 5 a 6.9 recupera / >=7 aprova
'''
print()
print('_'*15, 'DIÁRIO DIGITAL', '_'*15)
print(' '*10, 'Calculadora do Professor ', ' '*10)

print()
name = str(input('Informe o nome do aluno: ')).strip().title()
n1 = float(input('Digite a nota da avaliação 1: '))
n2 = float(input('Digite a nota da avaliação 2: '))
media = (n1 + n2) / 2

print('-'*46)
if media < 5:
    status = 'reprovado'
elif media >= 5 and media < 7:
    status = 'em recuperação'
elif media >= 7 and media <= 10:
    status = 'aprovado'
else:
    status = 'com \033[1;41mnotas inválidas\033[m\033[7;40m. Tente novamente'

print(f'\n\033[7;40m A média de {name} é {media:.2f}. O aluno está {status}.\033[m')





print('DESAFIO 69'.center(40))
'''
Ler idade e sexo de várias pessoas
Retornar: a) quantos tem mais de 21 anos; b) quantos homens cadastrados c) quantas garotas com 16 anos ou menos 
'''
age21 = man = girl16 = cont = 0
print('CADASTRO DE NOVOS CLIENTES'.center(40))
print('='*40)

while True:
    cont += 1
    print()
    print(f'= CADASTRO {cont} ='.center(40))
    name = str(input('Nome: ')).title().strip()
    age = int(input('Idade: '))
    sex = 'Blank'
    while sex != 'H' and sex != 'M':
        sex = str(input('Sexo [H/M]:')).upper().strip()

    if age > 21:
        age21 += 1
    if sex == 'H':
        man += 1
    else:
        if age <= 16:
            girl16 += 1

    contin = 'Blank'
    while contin != 'S' and contin != 'N':
        contin = str(input('\n === Deseja continuar? [S/N]: ')).upper().strip()
    if contin == 'N':
        break

print('\n\033[1;7;40m RESULTADOS: \033[m ')
print(f'Ao todo foram cadastradas {cont} pessoas.'
      f'\n{girl16} meninas com 16 anos ou menos'
      f'\n{age21} pessoas com mais de 21 anos'
      f'\n{man} homens')


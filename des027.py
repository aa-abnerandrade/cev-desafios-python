# Ler um nome completo e: mostre o primeiro e último nome separadamente

print('='*5, ' DESAFIO 27', '='*5)
name = str(input('Digite o nome completo, sem abreviações: ')).strip().title()
listname = name.split()
firstname = listname[0]
lastname = listname[-1]
print(f'\nBem vindo, prezado(a) Sr(ª). {firstname} {lastname}!')

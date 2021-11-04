# Ler um nome completo e: nome em maiúscula, em minúscula, quantas letras sem espaços, quantas letras no primeiro nome
print('='*5, ' DESAFIO 22', '='*5)

print()
name = str(input('Digite seu nome completo: ')).strip()
name = name.strip()

print('\n=> RESULTADOS: ')
print(' Em letras maiúsculas: {}' .format(name.upper()))
print(' Em letras minúsculas: {}' .format(name.casefold()))

less_space = name.replace(' ', '')
print(' Quantidade de letras do nome digitado: {}' .format(len(less_space)))

div = name.split()
print(' O primeiro nome é {} e tem {} letras. ' .format(div[0].capitalize(), len(div[0])))

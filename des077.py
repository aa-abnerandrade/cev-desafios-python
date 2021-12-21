print('DESAFIO 77'.center(44))
'''
Criar um programa que tenha uma tupla com várias palavras (sem acentos)
Após isso, mostrar para cada palavra quais são suas vogais
'''
print(f" \033[1m {' VERIFICADOR DE VOGAIS  ':|^42} \033[m")
names = ('Victor', 'Rodrigo', 'João', 'Mayara', 'Ingrid', 'Fábio', 'Jéssica', 'Felipe', 'Antônio')

for name in names:
    letters = name.lower()
    print(f"\n Nome: {name.title():>10}   |   Vogais:  ", end=' \033[1;36m')
    for letter in letters:
        if letter in 'aeiouáéâôã':
            print(letter, end=' ')
    print(end='\033[m')


print(f"\n\n\033[1m{'':|^44} ")
print('Verificador encerrado. Volte sempre.'.center(42))
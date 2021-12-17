print('DESAFIO 77'.center(40))
'''
Criar um programa que tenha uma tupla com várias palavras (sem acentos)
Após isso, mostrar para cada palavra quais são suas vogais
'''
print(f"{' VERIFICADOR DE VOGAIS ':|^38}")
words = ('Notebook', 'Livro', 'Headseat', 'Mouse', 'Webcam', 'Monitor', 'Caderno',
         'Caneta', 'Casaco', 'Teclado', 'Bloco')

cont = 0
while cont < len(words):
    word = words[cont]
    print(f'\n Termo: {(words[cont]).upper():>10} | Vogais:', end=' ')
    for letter in word:
        if letter in 'aeiou':
            print(letter, end=' ')
    cont += 1

print(f"\n{'':|^36} ")
print('Verificador encerrado. Volte sempre.'.center(38))
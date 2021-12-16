print('DESAFIO 77'.center(40))
'''
Criar um programa que tenha uma tupla com várias palavras (sem acentos)
Após isso, mostrar para cada palavra quais são suas vogais
'''
print('VERIFICADOR DE VOGAIS')
words = ('Notebook', 'Livro', 'Headseat', 'Mouse', 'Webcam', 'Monitor', 'Caderno',
         'Caneta', 'Casaco', 'Teclado', 'Bloco')

cont = 0
while cont < len(words):
    print(f'Na palavra {words[cont]} temos as vogais ')
    cont += 1
print('Fim')
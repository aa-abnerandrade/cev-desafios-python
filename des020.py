# Ler 4 alunos e sortear a ordem de apresentação
from random import shuffle
print('='*5, ' DESAFIO 20 ', '='*5)
print('     ================  ')

print()
name1 = str(input('Digite o nome do 1° aluno: '))
name2 = str(input('Digite o nome do 2° aluno: '))
name3 = str(input('Digite o nome do 3° aluno: '))
name4 = str(input('Digite o nome do 4° aluno: '))
lista = [name1, name2, name3, name4]
shuffle(lista)
print(f'\n=... a ordem em que os alunos se apresentarão é:  {lista}.')
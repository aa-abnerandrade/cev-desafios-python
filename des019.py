# Ler nomes de 4 alunos e sortear um deles
import random
print('='*5, ' DESAFIO 19 ', '='*5)
print('     ===  Sorteador  ===  ')

print()
name1 = str(input('Digite o nome do 1° aluno: '))
name2 = str(input('Digite o nome do 2° aluno: '))
name3 = str(input('Digite o nome do 3° aluno: '))
name4 = str(input('Digite o nome do 4° aluno: '))
lista = [name1, name2, name3, name4]
thename = random.choice(lista)
print(f'\n= O aluno sorteado foi {thename}.')

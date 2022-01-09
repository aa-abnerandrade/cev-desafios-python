print('DESAFIO 84'.center(44))
'''
Ler nome e peso de várias pessoas
Retornar: quantas foram cadastradas / pessoas mais pesadas / pessoas mais leves 
'''
print(f" {' ANALISADOR DE PESOS ':_^44} ")
person = []
people = []


while True:
    name = str(input('Digite o nome: ')).title().strip()
    person.append(name)
    weight = float(input(f'Digite o peso de {name}: '))
    person.append(weight)
    people.append(person[:])
    person.clear()

    cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if cont == 'N':
        break

print(f"As pessoas cadastradas são: {people}")
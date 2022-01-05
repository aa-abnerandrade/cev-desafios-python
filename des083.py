print('DESAFIO 83'.center(44))
'''
analisar um expressão qualquer que use parênteses
analisar se a expressão informada está com parênteses abertos e fechados na ordem correta 
'''
expressao = str(input('Digite a expressão que deseja verificar: '))

print(f" Você digitou a expressão {expressao}")
cont = 0
for L in expressao:
    if L == '(':
        cont += 1
    elif L == ')':
        cont -= 1
    elif cont < 0:
        break

if cont == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')

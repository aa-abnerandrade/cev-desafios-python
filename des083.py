print('DESAFIO 83'.center(44))
'''
analisar um expressão qualquer que use parênteses
analisar se a expressão informada está com parênteses abertos e fechados na ordem correta 
'''
print(f" {' VERIFICADOR DE EXPRESSÃO MATEMÁTICA ':_^44} ")

expressao = str(input('\nDigite a expressão que deseja verificar: '))

verificador = 0
for L in expressao:
    if L == '(':
        verificador += 1
    elif L == ')':
        verificador -= 1
    elif verificador < 0:
        break

print("\n\033[1mRESULTADO DA ANÁLISE:\033[m", end=' ')
if verificador == 0:
    print('\033[34mExpressão válida.\033[m')
else:
    print('\033[31mExpressão inválida.\033[m')

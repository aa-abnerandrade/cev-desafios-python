print('DESAFIO 78'.center(44))
'''
Ler 5 valores inteiros e retornar maior e menor, e suas posições
'''
valores = []
for c in range(0, 5+1):
    valores.append(int(input(f" Valor na posição {c}: ")))
print(valores)

qtdmenor = valores.count(min(valores))
if qtdmenor > 1:
    print(f" O valor {min(valores)} aparece {qtdmenor} vezes, nas posições !!!! ")
qtdmaior = valores.count(max(valores))
if qtdmaior > 1:
    print(f" O valor {max(valores)} aparece {qtdmaior} vezes, nas posições !!!!")

# criar uma lista para receber as posições de menor e maior?
# só vai, se joga
# colocar isso dentro do for




print('DESAFIO 78'.center(44))
'''
Ler 5 valores inteiros e retornar maior e menor, e suas posições
'''
print('\033[1mANALISADOR DE VALORES EM LISTA\033[m'.center(50))
valores = []
for c in range(0, 5):
    valores.append(int(input(f" Valor na posição {c}: ")))

print()
print(f" {'RESULTADOS':.^42}")
print(f"\nVocê inseriu os valores: {valores}")

menor = min(valores)
maior = max(valores)

qtdmenor = valores.count(menor)
qtdmaior = valores.count(maior)

print(f"\n\033[1mMenor valor: \033[m{menor}, nas posições: ", end='') # menor
for pos, valor in enumerate(valores):
    if valor == menor:
        print(pos, end='... ')
print(f"\n\033[1mMaior valor: \033[m{maior}, nas posições: ", end='') # maior
for pos, valor in enumerate(valores):
    if valor == maior:
        print(pos, end='... ')
print()


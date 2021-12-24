print('DESAFIO 78'.center(44))
'''
Ler 5 valores inteiros e retornar maior e menor, e suas posições
'''
valores = []
for c in range(0, 5+1):
    valores.append(int(input(f" Valor na posição {c}: ")))
print(valores)

menor = min(valores)
maior = max(valores)

qtdmenor = valores.count(menor)
qtdmaior = valores.count(maior)

print(f"Menor valor: {menor}, nas posições: ", end='') # menor
for pos, valor in enumerate(valores):
    if valor == menor:
        print(pos, end=', ')
print(f"Maior valor: {maior}, nas posições: ", end='') # maior
for pos, valor in enumerate(valores):
    if valor == maior:
        print(pos, end=', ')


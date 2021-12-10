print('DESAFIO 76'.center(40))
'''
Criar tupla única com nomes de produtos com e seus respectivos preços
No final, mostrar uma listagem de preços organizando os dados em forma tabular. Sem interação. 
'''
store = ('Notebook', 5449.00, 'Livro', 114,  'Headseat', 399, 'Mouse', 48, 'Webcam', 1445, 'Monitor', 1099, 'Caderno', 34.90, 'Caneta', 2, 'Casaco', 125)

print(f" \n{'|':|^40} \n{'LISTAGEM DE PREÇOS': ^40} \n{'|':|^40}")

for cont in range(0, len(store), 2):
    print(f' {store[cont]:.<26} R$ {store[cont+1]:>8.2f}')
print(f"{'|':|^40}")

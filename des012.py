# Ler o preço de um produto e mostrar novo valor com 5% de desconto
print('='*5, ' DESAFIO 12 ', '='*5)
price = float(input('Informe o valor do produto: R$'))
new_price = price-(price*0.05)
print(f'\n= Com 5% de desconto, o preço ficará R$ {new_price:.2f}. \n   Desconto de R$ {price*0.05:.2f}.')

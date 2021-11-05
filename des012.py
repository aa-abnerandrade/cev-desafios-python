# Ler o preço de um produto e mostrar novo valor com 5% de desconto
print('='*5, ' DESAFIO 12 ', '='*5)
price = float(input('Informe o valor do produto: R$'))
new_price = price-(price*0.05)
print(f'\n\033[1;32m= Com 5% de desconto, o preço ficará R$ {new_price:.2f}.\033[m \n   \033[1;31mDesconto de R$ {price*0.05:.2f}.\033[m')

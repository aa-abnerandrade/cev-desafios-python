# Converter BRL para USD
print('='*5, ' DESAFIO 10 ', '='*5)
dol = float(input('Informe o valor da cotação do dólar hoje: R$ '))
money = float(input('Informe o valor que deseja converter: R$'))
conv = money / dol

print('\n= Com R${:.2f}, você pode comprar US${:.2f}. ' .format(money, conv))

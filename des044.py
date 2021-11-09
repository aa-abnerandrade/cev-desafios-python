print('DESAFIO 44')
'''
Calcular preço com condições de pagamento diferenciadas
pix 10% - debito 5% - credito 3x preço normal - credito 4x+ juros 20%
'''
print('*'*10, '\033[7mLOJAS GAFANHOTO\033[m', '*'*10)
print('_'*37)
iten = str(input('Digite o nome do Produto: ')).strip()
price = float(input('Insira o valor do produto: R$'))
form = int(input('Informe a forma de pagamento\n'
                 '  [1] À vista (Dinheiro ou PIX)\n'
                 '  [2] À vista (Débito ou Crédito)\n'
                 '  [3] Parcelado em 2x (Crédito)\n'
                 '  [4] Parcelado em 3x ou mais (Crédito)\n'
                 '  Digite aqui: '))
print('\033[7m*'*36, '\033[m\n')
if form == 1:
    desc = price*0.10
    price = price-desc
    print('Para pagamento à vista em dinheiro ou PIX, o produto {} terá \033[36mdesconto de R${:.2f}\033[m,\n'
          '\033[1;30;46mSeu preço final será R${:.2f}.\033[m' .format(iten, desc, price))
elif form == 2:
    desc = price*0.05
    price = price-desc
    print('Para pagamento à vista no Débito ou Cartão de Crédito, o produto {} terá \033[36mdesconto de R${:.2f}\033[m,\n'
          '\033[1;30;46mSeu preço final será de R${:.2f}.\033[m' .format(iten, desc, price))
elif form == 3:
    plot = price/2
    print('Para o pagamento em 2x do produto {}, as condições gerais de pagamento serão:\n'
          '\033[1;32m2 parcelas de R${:.2f}\n'
          'Valor final, \033[1;30;42msem juros: R${:.2f}\033[m' .format(iten, plot, price))
elif form == 4:
    interest = price*0.20
    price = price+interest
    print('Para o pagamento parcelado em 3x ou mais, estão disponíveis as seguintes opções de pagamento:\n'
          '\033[1;33m3 parcelas de R${:.2f}\n'
          '4 parcelas de R${:.2f}\n'
          '5 parcelas de R${:.2f}\n'
          '\033[1;30;41mValor final com 20% de juros da administradora do cartão: R${}\033[m' .format(price/3, price/4, price/5, price))
else:
    print('Não compreendemos as entradas. Por favor, reinicie o simulador.')
print('\033[4m '*36, '\033[m')
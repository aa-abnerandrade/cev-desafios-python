print('='*12, 'DESAFIO 36', '='*12)
'''
Programa para aprovar um empréstimo
Ler: valor da casa, qtd parcelas e salário
Calcular prestação e não permitir que exceda 30% do salário
'''
from time import sleep

print('\033[7:40m', '='*7, ' FINANCEIRA X Y Z ', '='*7, '\033[m')
print('\033[1mPara realizarmos a simulação de financiamento, por favor, informe os dados a seguir: \033[m')
name = str(input('- Nome do solicitante: ')).strip().title()
sal = float(input(f'- Salário de {name}: R$'))
house = float(input('- Informe o valor do imóvel: R$'))
time = int(input('- Informe quantos anos de financiamento: '))
qtd = time * 12
thirty = sal * 0.30
portion = house / qtd

print('\033[1m\n--- Aguarde um momento, enquanto processamos as informações....\033[m\n')
sleep(2)
if portion > thirty:
    print('-'*36)
    print('Simulação negada. Infelizmente, não podemos prosseguir considerando as informações inseridas.'
          '\033[1;33m\nNão conseguimos te informar o motivo, mas você pode solicitar novo orçamento com outras configurações de parcelamento.\033[m')
else:
    print('\033[1;32mÓtima notícia! '
          '\nSeu financiamento foi aprovado! '
          '\nPodemos prosseguir com as seguintes informações:'
          f'\n - Valor do imóvel: R${house:.2f}'
          f'\n - Valor da parcela: R${portion:.2f} '
          f'\n - Quantidade de parcelas: {qtd}\033[m')

print('\n\033[7;40m = Programa encerrado. Obrigado por escolher a Financeira XYZ! = \033[m')
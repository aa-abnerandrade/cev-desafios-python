# Perguntar qtd Km e a quantidade de dias de veículo alugado. Calcule o preço a pagar. R$60 por dia e R$0,15 por Km
print('='*5, ' DESAFIO 15 ', '='*5)
print('\n= LOCADORA DE VEÍCULOS = ')
days = int(input('Informe quantos dias de locação: '))
kms = float(input('Quantos kilômetros rodados: '))
price_days = days * 60
price_kms = kms * 0.15
total = price_days + price_kms

print('\n= DEMOSTRATIVO:  ')
print(f'Cobrança total por diárias: R$ {price_days:.2f}')
print(f'Cobrança total por KM rodado: R$ {price_kms:.2f}')
print(f'PREÇO FINAL: R$ {total:.2f}.')




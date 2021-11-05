# perguntar a distância em km e calcular o preço da passagem 0,50km por até 200km e 0,45km acima de 200km
print('='*5, ' DESAFIO 31', '='*5)
print('\033[7;40;1m = VIAÇÃO CEV = \033[m'.center(23))
cityo = str(input('Qual é a origem do trecho: ')).strip().title()
cityd = str(input('Qual é o destino do trecho: ')).strip().title()
km = int(input('Digite a distância do trecho (em km): '))

print('\n\033[1;40m= ITINERÁRIO: \033[m')
print(f'Você deseja fazer um trecho de {km}kms de {cityo} para {cityd}.')
print('Seu ticket custará R$', end=' ')
if km <= 200:
    price = km * 0.50
    print(f'{price:.2f}.')
else:
    price = km * 0.45
    print(f'{price:.2f}.')

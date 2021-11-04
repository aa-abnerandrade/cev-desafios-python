# Ler nome da cidade e verificar se começa com 'SANTO'
print('='*5, ' DESAFIO 24', '='*5)
city = str(input('Informe o nome da cidade em você nasceu: ')).strip().capitalize()
inicial = city[0:6]
print('A cidade começa com Santo: ', 'Santo ' in inicial)
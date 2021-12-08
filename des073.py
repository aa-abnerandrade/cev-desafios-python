print('DESAFIO 73'.center(50))
'''
Tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação
Depois mostre: a) apenas os 5 primeiros colocados / b) os últimos 4 colocados da tabela 
c) uma lista com os times em ordem alfabética / d) em que posição está o time da Chapecoense 
'''
print(f"\n\033[1m{' BRASILEIRÃO 2021 ':=^50} \033[m")
clubs = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético Mg', 'Botafogo', 'Atlético Pr', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'Ec Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético Go')
print(f"{' Resumo principal dos dados ':_^50} \n")

print()
print(f"\033[1;7;40m{'=== Primeiros colocados ':=<50}\033[m")
for pos, club in enumerate(clubs[0:3+1]):
    print(f" {pos+1}º - {club} ")

print()
print(f"\033[1;7;40m{'=== Zona de rebaixamento ':=<50}\033[m")
for pos in range(-4, -1+1):
    print(f" {clubs.index(clubs[pos])+1}º - {clubs[pos]} ")

print()
print(f"\033[1;7;40m{'=== Ordem alfabética ':=<50}\033[m")
ordem = sorted(clubs)
for pos in range(0, 19+1):
    print(f" {pos+1:2} - {ordem[pos]} ")

print()
print(f"\033[1;7;40m{'=== Localizar time ':=<50}\033[m")
club = str(input('Digite o nome exato do clube, com acentos e espaços:  ')).title().strip()
while club not in clubs:
    club = str(input(f'\033[33mO termo "{club.upper()}" não foi localizado.\033[m Tente novamente:  ')).strip().title()
print(f"\n\033[1m O clube {club} está na {clubs.index(club)+1}ª posição do ranking. \033[m")

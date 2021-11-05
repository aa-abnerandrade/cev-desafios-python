# Ler algura e altura de parede e calcular: áerea e tinta necesária (1L para cada 2m²)
print('='*5, ' DESAFIO 11 ', '='*5)
alt = float(input('Informe a altura da parede: '))
lar = float(input('Informe a largura da parede: '))
area = alt * lar
tinta = area / 2
print()
print(f'= Para a parede de \033[1m{area:.2f}mts²\033[m, serão necessários \033[1m{tinta:.2f}lts\033[m de tinta. ')

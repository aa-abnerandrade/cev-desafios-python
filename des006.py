# Ler número e mostrar dobro, triplo e raiz quadrada
print('='*5, ' DESAFIO 06 ', '='*5)
number = int(input('Digite um número: '))

print()
print('=== Referente ao número {}: \nDobro: {} \nTriplo: {}' .format(number, number*2, number*3))
print('Raiz Quadrada: {:.2f}' .format(number**(1/2)))


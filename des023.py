# Ler um número de 0 9999 e mostrar unidade, dezena, centena e milhar (como string e matematicamente)
print('='*5, ' DESAFIO 23', '='*5)

number = str(input('Digite um número [0 a 9999]: ')).zfill(4)
div = number.split()

print('\n= RESULTADO: ')
print('Unidade: {}  |   Dezena: {}  |    Centena: {}  |    Milhar: {}' .format(number[-1], number[-2], number[-3], number[-4]))

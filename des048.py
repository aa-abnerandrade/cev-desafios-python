print(' '*16, 'DESAFIO 48', ' '*16)
'''
Calcular a soma de: todos os números ímpares, multiplos de 3, de 1 a 500
'''
soma = 0
qtd = 0

print('\033[7;40m', ' '*15, ' CONTADOR ', ' '*15, '\033[m')
for cont in range(1, 500+1):
    if (cont % 3 == 0) and (cont % 2 == 1):
        soma += cont
        qtd += 1

print()
print(f'A SOMA de todos os {qtd} números que são:'
      '\n- Ímpares,'
      '\n- Múltiplos de 3,'
      '\n- Que estão no intervalo de 1 a 500,'
      f'\n\033[32mÉ = {soma}')
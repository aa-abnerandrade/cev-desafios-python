print(' '*16, 'DESAFIO 53', ' '*16)
'''
Ler uma frase qualquer e dizer se é um palíndromo
'''
inverse = ''

print(' '*13, '\033[7;40m PALINDRÔMETRO \033[m', ' '*13)
print('='*40)
answer = str(input('Digite uma frase: ')).title().strip()
phrase = answer.casefold().replace(' ', '')\
    .replace('á', 'o').replace('â', 'a').replace('ã', 'a').replace('é', 'e').replace('ê', 'e').replace('í', 'i').replace('ó', 'o').replace('ô', 'o').replace('ú', 'u')
qtd = len(phrase)

for cont in range(qtd-1, -1, -1):
    inverse += phrase[cont]

print('\n\033[1;40m', ' '*14, 'RESULTADO', ' '*14, '\033[m')
print('\033[1mTexto digitado: {}'
      '\nTexto invertido: {}'
      ' ' .format(answer.upper(), inverse.upper()))

if phrase == inverse:
    print('Sim, é um palíndromo.\033[m')
else:
    print('Não, essa sentença não é um palíndromo.\033[m')

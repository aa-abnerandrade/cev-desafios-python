# Ler um frase e: veriricar letra 'A', e em que posição aparece na primeira e última
print('='*5, ' DESAFIO 26', '='*5)
name = str(input('Informe o nome completo: ')).strip().upper()

print(f'\n= Análise do nome "{name.title()}" ')
name = name.replace('Ã', 'A')
name = name.replace('Á', 'A')
name = name.replace('Â', 'A')
print('Contém letra A: ', 'A' in name)
print('A letra "A" aparece {} vezes. A primeira na posição {} e a última na posição {}.' .format(name.count('A'), name.find('A')+1, name.rfind('A')+1))

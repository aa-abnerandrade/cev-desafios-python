print('DESAFIO 42', '_'*32)
'''
Ler 2 retas, verificar triângulo e tipo de triângulo.
Equilátero, Isósceles, Escaleno
'''
print('\n\033[7;40;1m', ' - '*2, ' VERIFICADOR DE TRIÂNGULOS ', ' - '*2, '\033[m')

R1 = float(input('Informe o valor da 1ª reta: '))
R2 = float(input('Informe o valor do 2ª reta: '))
R3 = float(input('Informe o valor do 3ª reta: '))

print('\n\033[7;40;1m= Resultado da análise: {}\033[m' .format(' '*18))
print('As medidas podem informar um triângulo? ', end=' ')
if (R1 < R2 + R3) and (R2 < R1 + R3) and (R3 < R1 + R2):
    print('\033[1;32m SIM! \033[m')
    if (R1 == R2) and (R2 == R3):
        print('Um triângulo equilátero.')
    elif (R1 != R2) and (R2 != R3) and (R3 != R1):
        print('Um triângulo escaleno. ')
    else:
        print('Um triângulo isósceles. ')
else:
    print('\033[1;31m\nNão, essas medidas não podem formar um triângulo. \033[m')

print('\n= Agradecemos por utilizar nosso verificador. Volte sempre. =')
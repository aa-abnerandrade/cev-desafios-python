# Ler 3 retas e informar se pode ou não formar um triângulo
print('='*7, ' DESAFIO 35', '='*7)
print('\n\033[7;40;1mVERIFICADOR DE TRIÂNGULOS\033[m')

L1 = float(input('Informe o valor do 1° lado: '))
L2 = float(input('Informe o valor do 2° lado: '))
L3 = float(input('Informe o valor do 3° lado: '))

print('\n\033[7;40;1m= Resultado da análise: \033[m')
print('As medidas podem informar um triângulo? ', end=' ')
if (L1 < L2+L3) and (L2 < L1+L3) and (L3 < L1+L2):
    print('SIM!')
    if (L1 == L2) and (L2 == L3):
        print('Um triângulo equilátero.')
    elif (L1 != L2) and (L2 != L3) and (L3 != L1):
        print('Um triângulo escaleno. ')
    else:
        print('Um triângulo isósceles. ')
else:
    print('Não, essas medidas não podem formar um triângulo. ')

print('\n= Agradecemos por utilizar nosso verificador. Volte sempre. =')
# Ler a velocidade do carro e notificar a multa acima de 80km/h. Cada km ultrapassado custa 7 reais
print('='*12, ' DESAFIO 29', '='*12)
import emoji
print('\nDEPARTAMENTO ESTADUAL DE TRÂNSITO')
vel = float(input('Informe a velocidade atingida, em km/hr: '))
if vel > 80:
    danger = vel - 80
    money = danger * 7
    print('\n!!! Você ultrapassou a velocidade e deverá pagar multa no valor de R$ {:.2f}.' .format(money))
else:
    print(emoji.emojize('\nParabéns, você é um ótimo motorista! :thumbs_up:', use_aliases=True))

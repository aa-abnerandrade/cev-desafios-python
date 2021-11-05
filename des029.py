# Ler a velocidade do carro e notificar a multa acima de 80km/h. Cada km ultrapassado custa 7 reais
print('='*12, ' DESAFIO 29', '='*12)
import emoji
print('\n\033[7;40m DEPARTAMENTO ESTADUAL DE TRÂNSITO \033[m')
vel = float(input('Informe a velocidade atingida, em km/hr: '))
if vel > 80:
    danger = vel - 80
    money = danger * 7
    print('\n\033[1;31;40m!!!\033[m\033[1;31m Você ultrapassou a velocidade e deverá pagar multa no valor de R$ {:.2f}.\033[m' .format(money))
else:
    print(emoji.emojize('\n\033[36mParabéns, você é um ótimo motorista! \033[m\033[1;30;46m :thumbs_up: \033[m', use_aliases=True))

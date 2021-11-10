print('\033[30mDESAFIO 46\033[m'.center(52))
'''
Contagem regressiva de 10 segundos para estouro de fogos de artifício
'''
import emoji
from time import sleep

colors = {'clean': '\033[m',
          'bgwhite': '\033[1;40;7m',
          'bgblue': '\033[1;44m',
          'system': '\033[35m',
          'attention': '\033[31m'}

print('{}... CONTAGEM REGRESSIVA ... {}' .format(colors['system'], colors['clean']). center(52))
start = input('Insira S para iniciar o relógio'.center(44)).upper()

if start == 'S':
    print()
    for cont in range(10, 0, -1):
        print(str(cont).center(44))
        sleep(1)
    print(emoji.emojize('{} 🎆 🎆 🎆 {}'.format(colors['bgblue'], colors['clean']).center(52), use_aliases=True))
    print('{}  HAPPY NEW YEAR  {}'.format(colors['bgwhite'], colors['clean']).center(56))
else:
    print('\n{} REINICIE O PROGRAMA PARA PREPARAR O CONTADOR. {}\n' .format(colors['attention'], colors['clean']))


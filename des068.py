print('\033[30mDESAFIO 68\033[m'.center(58))
'''
Par ou ímpar
O jogo só será interrompido quando o jogador perder
Exibir a quantidade de vitórias consecutivas 
'''
from random import randint
colors = {'clean': '\033[m', 'bold': '\033[1m', 'yellowL': '\033[1;33m', 'yellowBG': '\033[1;43m', 'blueL': '\033[1;34m', 'blueBG': '\033[1;44m', 'cyanL': '\033[1;36m', 'cyanBG': '\033[1;46m'}
print()
print('\033[1;43m *** MÁQUINA DA SORTE *** \033[m'.center(60))
print('\033[1;33mVamos jogar par ou ímpar ?\033[m'.center(60))
# wuser = 0
# verificador = 0

mode = 0
while True:
    print()
    print('='*50)
    print(f" {colors['bold']} Qual modalidade deseja jogar? ")
    print(f"[ 1 ] FREQUÊNCIA \n[ 2 ] CAMPEONATO {colors['clean']}\n[ 0 ] Sair ")
    while True:
        mode = int(input('Escolha aqui: '.rjust(50)))
        if mode == 0 or mode == 1 or mode == 2:
            break

    if mode == 1:           # MODO FREQUÊNCIA
        cont = wuser = 0
        print()
        print(f" {colors['blueBG']} MODALIDADE FREQUÊNCIA {colors['clean']} ".center(60))
        while True:
            cont += 1
            print(f"  {colors['blueL']}| PARTIDA {cont} | {colors['clean']} ".center(60))
            opt = 'Blank'
            while opt not in 'PI':
                opt = str(input('[ P ] PAR [ I ] Ímpar: ')).upper().strip()[0]
            nummach = randint(1, 10)
            numuser = 0
            while numuser < 1 or numuser > 10:
                numuser = int(input('Informe um valor entre 1 e 10: '.format(opt)))
            total = numuser + nummach
            result = total % 2

            if opt == 'P' and result == 0:
                wuser += 1
                print(f" {nummach} com {numuser} é {colors['blueBG']}PAR{colors['clean']}.\n ".rjust(60))
            elif opt == 'I' and result == 1:
                wuser += 1
                print(f" {nummach} com {numuser} é {colors['blueBG']}ÍMPAR{colors['clean']}. \n ".rjust(60))
            else:
                break
        print()
        print(f"Eu joguei {nummach}. {colors['blueL']}Você perdeu após {wuser} vitórias.{colors['clean']} ".center(60))

    elif mode == 2:                 # MODO CAMPEONATO
        cont = wuser = qtdpar = qtdimpar = 0
        print()
        print(f" {colors['cyanBG']} MODALIDADE CAMPEONATO {colors['clean']} ".center(60))
        print()
        qtd = 0
        while qtd < 1 or qtd > 7:
            qtd = int(input('\033[1m = Quantas partidas deseja disputar?\033[m (Máx 7): '))
        print()
        print(f'CAMPEONATO DE {qtd} PARTIDAS'.center(50))
        opt = 'Blank'
        while opt not in 'PI':
            opt = str(input(f"{colors['cyanBG']} Escolha seu time [ P ] PAR [ I ] Ímpar: {colors['clean']} ")).upper().strip()[0]
        for cont in range(1, qtd+1):
            print()
            print(f"  {colors['cyanL']}| PARTIDA {cont} | {colors['clean']} ".center(60))
            nummach = randint(1, 10)
            numuser = 0
            while numuser < 1 or numuser > 10:
                numuser = int(input('Informe um valor entre 1 e 10: '.format(opt)))
            total = numuser + nummach
            result = total % 2

            if result == 0:
                qtdpar += 1
                dual = 'PAR'
            elif result == 1:
                qtdimpar += 1
                dual = 'ÍMPAR'
            print(f" {nummach} com {numuser} é {colors['cyanBG']}{dual}{colors['clean']}.\n ".rjust(60))
            cont += 1

        print(colors['cyanL'])
        if opt == 'P' and qtdpar > qtdimpar:
            print(f'Uhhul! Você venceu com {qtdpar} vitórias.'.center(50))
        elif opt == 'I' and qtdpar < qtdimpar:
            print(f'Uhuuul! Você venceu com {qtdimpar} vitórias.'.center(50))
        elif qtdpar == qtdimpar:
            print(f'Inacreditável! Empatamos. {qtdpar} vitórias cada.'.center(50))
        else:
            if qtdpar > qtdimpar:
                print(f'Você perdeu. Eu tive {qtdpar} vitórias.'.center(50))
            elif qtdpar < qtdimpar:
                print(f'Você perdeu. Eu tive {qtdimpar} vitórias.'.center(50))
        print(colors['clean'])

    elif mode == 0:                     # MODO SAIR
        print('\n' + 'Encerrando aplicativo...'.center(50))
        break

print(f"\n{colors['yellowBG']} É sempre divertido te encontrar aqui. Volte sempre! {colors['clean']} ")


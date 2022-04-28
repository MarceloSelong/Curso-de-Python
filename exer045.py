#Crie um programa que faça o computador jogar jokenpô com você.
import random
print('Vamos jogar Pedra, Papel e Tesoura.')
pc = ('PEDRA', 'PAPEL', 'TESOURA')
pc = random.choice(pc)
print('Informe sua jogada: ')
print('(1) para pedra')
print('(2) para papel')
print('(3) para tesoura')
user = int(input())
if pc == 'PEDRA' and user == 1:
    print('O computador escolheu {} deu \033[33mempate\033[m'.format(pc))
elif pc == 'PEDRA' and user == 2:
    print('O computador escolheu {}, você \033[34mganhou\033[m.'.format(pc))
elif pc == 'PEDRA' and user == 3:
    print('O computador escolheu {}, você \033[31mperdeu\033[m.'.format(pc))
elif pc == 'PAPEL' and user == 1:
    print('O computador escolheu {}, você \033[31mperdeu\033[m.'.format(pc))
elif pc == 'PAPEL' and user == 2:
    print('O computador escolheu {}, deu \033[33mempate\033[m.'.format(pc))
elif pc == 'PAPEL' and user == 3:
    print('O computador escolheu {}, você \033[34mganhou\033[m.'.format(pc))
elif pc == 'TESOURA' and user == 1:
    print('O computador escolheu {}, você \033[34mganhou\033[m.'.format(pc))
elif pc == 'TESOURA' and user == 2:
    print('O computador escolheu {}, você \033[31mperdeu\033[m.'.format(pc))
elif pc == 'TESOURA' and user == 3:
    print('O computador escolheu {}, deu \033[33mempate\033[m.'.format(pc))

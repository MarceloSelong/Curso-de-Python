# Faça um programa que jogue par ou ímpar com o computador. O jogo só erá interrompido quando o jogador perder.
# Mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
ganhas = 0
while True:
    valor = int(input('Digite um valor: '))
    pc = randint(0, 11)
    escolha = input('Escolhe par ou ímpar? [P/I]')
    print('=-' * 20)
    while escolha not in 'PpIi':
        print('Escolha corretamente: ')
        escolha = input('Escolhe par ou ímpar? [P/I]')

    if (pc+valor) % 2 == 0:
        print(f'Você jogou {valor} e o computador {pc}. Total de {pc+valor}, deu par.')
        if escolha in 'Pp':
            print('\033[33mVocê ganhou!\033[m')
            ganhas += 1
            print('=-' * 20)
        else:
            print(f'\033[31mGame over!\033[m Você venceu {ganhas} vezes.')
            print('=-' * 20)
            break
    else:
        print(f'Você jogou {valor} e o computador {pc}. Total de {pc + valor}, deu ímpar.')
        if escolha in 'Ii':
            print('\033[33mVocê ganhou!\033[m')
            ganhas += 1
            print('=-' * 20)
        else:
            print(f'\033[31mGame over!\033[m Você venceu {ganhas} vezes.')
            print('=-' * 20)
            break

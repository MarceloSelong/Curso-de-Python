#Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar,
#mostrando no final quantos palpites foram necesários para vencer.
from random import randint
escolha = 0
tentativas = 0
print('Vou pensar em um número de 0 a 10...')
n = randint(0, 10)
print()
print('Consegue adivinhar qual escolhi ?')
print()
while escolha == 0:
    esc = int(input('Digite um número: '))
    if esc != n:
        print('Que pena, você errou. Tente novamente.')
        tentativas += 1
    else:
        print('Parabéns, você acertou. O número escolhido foi \033[31m{}\033[m.'.format(n))
        escolha += 1
        tentativas += 1
        print('Foram necessários \033[34m{}\033[m palpites para acertar'.format(tentativas))
print('Fim')
#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
print('Vou pensar em um número de 0 a 5...')
n = random.choice([0, 1, 2, 3, 4, 5])
print()
print('Consegue adivinhar qual escolhi ?')
print()
esc = int(input('Digite um número: '))
if esc == n:
    print('Parabéns, você acertou. O número escolhido foi {}.'.format(n))
else:
    print('Que pena. Você errou o número escolhido foi {}.'.format(n))


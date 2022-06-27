# Faça um programa que ajude um jogador da mega sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('=-'*10)
print('SORTEIO MEGA SENA')
print('=-'*10, '\n')
jogadas = int(input('Informe a quantidade de jogos que quer realizar: '))
valores = list()
temporaria = list()
for c in range(0, jogadas):
    while len(temporaria) != 6:
        temp = randint(1, 60)
        if temp not in temporaria:
            temporaria.append(temp)
    valores.append(temporaria[:])
    temporaria.clear()
for i in range(0, len(valores)):
    valores[i].sort()
print('Os jogos gerados foram:\n')
for i in range(0, len(valores)):
    print(f'\033[32m{valores[i]}\033[m')
    sleep(1)

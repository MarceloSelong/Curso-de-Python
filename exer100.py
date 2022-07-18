# Faça um programa que tenha uma lista chaamda números e duas funções chamadas sorteia() e somaPart().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista, e a segunda função vai mostrar a soma entre
# todos os valores PARES sorteados pela função anterior.
from random import randint

números = []


def sorteia(*num):
    for i in range(0, 5):
        números.append(randint(1, 15))
    print(f'Os números sorteados foram: {sorted(números)}')


def somaPart(num, soma=0):
    for i in range(len(num)):
        if num[i] % 2 == 0:
            soma += num[i]
    print(f'\nA soma entre os números pares é: {soma}')


sorteia()
somaPart(números)

# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint
def maior(*num):
    maior = 0
    for i in range(len(num)):
        if i == 0:
            maior = num[i]
        else:
            if maior < num[i]:
                maior = num[i]
    print(f'{num}')
    print(f'O maior valor passado foi: {maior}\n')

maior(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
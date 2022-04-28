#Desenvolva um programa que leia o comprimento de três retas.
#E diga ao usuário se ela podem ou não formar um triângulo.
#Refaça o desafio 35 dos triângulos, acrescentando que tipo de triângulo será formado.
#-Equilátero : todos os lados iguais
#-Isósceles: dois lados iguais
#-Escaleno: todos os lados diferentes
r1 = int(input('Informe 3 valores: '))
r2 = int(input())
r3 = int(input())
if r1+r2 > r3 and r1+r3 > r2 and r3+r2 > r1:
    print('\033[34mPode formar um triângulo\033[m.')
    if r1 != r2 and r1 != r3:
        print('O triângulo é \033[31mescaleno\033[m.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo é \033[31misósceles\033[m.')
    elif r1 == r2 and r1 == r3:
        print('O triângulo é \033[31mequilátero\033[m.')
else:
    print('Não pode formar um triângulo.')

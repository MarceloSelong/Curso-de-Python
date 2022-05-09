#Desenvolva um programa que leia o comprimento de três retas.
#E diga ao usuário se ela podem ou não formar um triângulo.
r1 = int(input('Informe o comprimento de 3 retas para calcularmo triângulo: '))
r2 = int(input())
r3 = int(input())
if r1+r2 > r3 and r1+r3 > r2 and r3+r2 > r1:
    print('Pode formar um triângulo.')
else:
    print('Não pode formar um triângulo.')

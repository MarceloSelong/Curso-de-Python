# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5!=5x4x3x2x1=120
# Fazer um com While e outro com for

n = int(input('Informe um valor: '))
resfat = n * (n - 1)
for c in range(n - 2, 0, -1):
    resfat = resfat * c
print('5!=', end='')
for c in range(n, 0, -1):
    if c != 1:
        print(c, end="x")
    else:
        print('{}={}'.format(c, resfat))
print('FIM')
print()
n = str(input('Informe um valor: '))
print(n+'!='+n, end='x')
cont = int(n)
result = int(n)
while cont != 1:
    result = result * (cont-1)
    cont -= 1
    if cont != 1:
        print(cont, end="x")
    else:
        print('{}={}'.format(cont, result))

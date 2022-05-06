# Escreva um programa que leia um número 'n' inteiro qualquer.
# E mostre na tela os 'n' primeiros elementos de uma sequência de Fibonacci.
num = int(input('Informe um número: '))
a = 1
b = 1
x = 0
print()
print('Os {} primeiros elementos da sequência de Fibonacci são:\n'.format(num))
for c in range(0, num-1):
    if c == 0:
        print('\033[31m{}, {}, '.format(a, b), end='')
    elif c != num - 2:
        print('{}, '.format(x), end='')
    else:
        print('{}.\033[m'.format(x))
    x = a + b
    a = b
    b = x

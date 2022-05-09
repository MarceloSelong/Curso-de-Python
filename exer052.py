#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Informe um número inteiro: '))
if n == 1:
    print('O numéro {} não é primo.'.format(n))
elif n == 2 or n == 3 or n == 5 or n == 7:
    print('O número {} é primo.'.format(n))
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print('O número {} não é primo.'.format(n))
else:
    print('O número {} é primo.'.format(n))
print('Fim')

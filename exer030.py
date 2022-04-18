# Crie um programa que leia um número inteiro
# e mostre se ele é par ou ímpar.
print('Verificador de par ou ímpar.')
num = int(input('Informe um valor: '))
if num % 2 == 0:
    print('{} é par'.format(num))
else:
    print('{} é ímpar.'.format(num))

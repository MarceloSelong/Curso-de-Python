#Faça um programa que leia 3 números
#E mostre qual é o maior e qual é o menor.
n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
n3 = int(input('Informe o terceiro valor: '))
if n1 < n2:
    if n1 < n3:
        print('O menor valor é: {}'.format(n1))
    else:
        print('O menor valor é: {}.'.format(n3))
else:
    if n2 >= n3:
        print('O menor valor é: {}.'.format(n3))
    else:
        print('O menor valor é: {}'.format(n2))
print('Fim')

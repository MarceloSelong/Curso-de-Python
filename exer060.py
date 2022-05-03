# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5!=5x4x3x2x1=120
print('---FATORIAL---')
n = int(input('Informe um valor: '))
c = n-1 #Contador
resultado = n #Resultado final do fatorial
print('O fatorial é:\033[31m')
print('{}!={}'.format(n, n), end='x') #Principal
while c > 0:
    resultado *= c
    if c != 1:
        print(c, end='x')
    else:
        print('{}={}'.format(c, resultado))
    c -= 1


#Refaça o desafio 51, lendo o primeiro termo e a razão de uma P.A.,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.
c = 0
a1 = int(input('Informe o primeiro termo da P.A.: '))
r = int(input('Informe a razão da P.A.: '))
x = 10 * r + 1
print()
print('Os 10 primeiros termos desta P.A. são: ')
print()
while c != 10:
    c += 1
    if c != 10:
        print(a1 * c, end=', ')
    else:
        print(a1 * c, end='.')

#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.
a1 = int(input('Informe o primeiro termo da P.A.: '))
r = int(input('Informe a razão da P.A.: '))
x = a1 + (10-1) * r

if r == 0:
    print('Esta é uma P.A. \033[31mconstante\033[m.')
    for c in range(0, 10):
        if c == 9:
            print('{}.'.format(r))
        else:
            print(r, end=', ')
elif r > 0:
    print('Os 10 primeiro termos dessa P.A. \033[31mcrescente\033[m são: ')
    for c in range(a1, x+1, r):
        if c == x:
            print(c, end='.')
        else:
            print(c, end=', ')
else:
    print('Os 10 primeiros termos dessa P.A. \033[31mdecrescente\033[m são: ')
    for c in range(a1, x-1, r):
        if c == x:
            print(c, end='.')
        else:
            print(c, end=', ')
print('Fim')

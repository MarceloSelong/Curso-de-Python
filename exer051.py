#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.
a1 = int(input('Informe o primeiro termo da P.A.: '))
r = int(input('Informe a razão da P.A.: '))
x = 10 * r +1
print('Os 10 primeiro termos dessa P.A. são: ')
for c in range(a1, x, r):
    print(c, end=', ')

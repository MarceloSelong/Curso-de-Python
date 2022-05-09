#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3,
#e que se encontram no intervalo de 1 até 50.
s = 0
print('Os número ímpares e múltiplos de \033[33m3\033[m são: ')
for c in range(0, 50+1):
    if c % 2 == 1 and c % 3 == 0:
        s += c
        print(c, '', end="")
print('A soma entre estes número é: \033[31m{}\033[m.'.format(s))
print('Fim')

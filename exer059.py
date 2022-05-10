#Crie um programa que leia dois valores e mostre um menu na tela.

#[1]somar
#[2]multiplicar
#[3]maior
#[4]novos números
#[5]sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
v1 = input('Informe o primeiro valor: ')
v2 = input('Informe o segundo valor: ')
v1 = float(v1.replace(',', '.'))
v2 = float(v2.replace(',', '.'))
print()
escolha = 0
while escolha != 5:
    escolha = int(input(""""Qual operação gostaria de realizar ?
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos números
    [5]sair do programa """))
    print()
    if escolha == 1:
        print('A soma entre \033[34m{:.0f}\033[m e \033[34m{:.0f}\033[m é igual a: \033[31m{:.0f}\033[m.'.format(v1, v2, v1+v2))
        print()
    elif escolha == 2:
        print('A multiplicação entre \033[34m{:.0f}\033[m e \033[34m{:.0f}\033[m é igual a: \033[31m{:.0f}\033[m.'.format(v1 , v2, v1*v2))
        print()
    elif escolha == 3:
        if v1 > v2:
            print('O maior número digitado entre \033[34m{:.0f}\033[m e \033[34m{:.0f}\033[m é: \033[31m{:.0f}\033[m.'.format(v1, v2, v1))
            print()
        elif v1 < v2:
            print('O maior número digitado entre \033[34m{:.0f}\033[m e \033[34m{:.0f}\033[m é: \033[31m{:.0f}\033[m.'.format(v1, v2, v2))
            print()
        else:
            print('Os números \033[34m{:.0f}\033[m e \033[34m{:.0f}\033[m são \033[31miguais\033[m.'.format(v1, v2))
            print()
    elif escolha == 4:
        v1 = input('Informe o primeiro valor: ')
        v2 = input('Informe o segundo valor: ')
        v1 = float(v1.replace(',', '.'))
        v2 = float(v2.replace(',', '.'))
        print()
    elif escolha == 5:
        print('\033[31mENCERRANDO...\033[m')
        escolha = 5
        sleep(2)
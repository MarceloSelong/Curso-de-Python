#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
from time import sleep
repetir = 1
media, maior, menor = 0, 0, 0
contador = 0
num = 0

while repetir == 1:
    contador += 1
    num = int(input('Informe o {}º valor: '.format(contador)))
    if maior < num:
        maior = num

    menor = num

    if menor <= num:
        pass
    else:
        menor = num

    media += num
    repetir = int(input("""Gostaria de digitar mais valores?
    \033[31m[1]\033[m para sim
    \033[31m[0]\033[m para não: """))
    print()
    if repetir == 1:
        print()
    elif repetir == 0:
        print('\033[38mEncerrando...\033[m')
        print()
        sleep(2)
    else:
        while repetir != 0 and repetir !=1:
            repetir = int(input('Opção incorreta, repita: '))

media = media / contador

print('A média entre todos os valores informados é: \033[34m{:.3f}\033[m.'.format(media))
print('O maior valor digitado foi: \033[31m{}\033[m.'.format(maior))
print('O menor valor digitado foi: \033[35m{}\033[m.'.format(menor))

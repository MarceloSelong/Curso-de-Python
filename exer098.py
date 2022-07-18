# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo
# e realize a contagem.

# Seu programa tem que realizar 3 contagens através da função criada

# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada.
from time import sleep
def contador(início, fim, passo):
    if passo >= 0:
        if início > fim:
            contador(int(input('\033[31mOpção inválida.\033[m Informe que número deseja iniciar aa contagem: ')),
                     int(input('Informe que número deseja parar a contagem: ')),
                     int(input('Informe o passo da contagem: ')))
        else:
            for i in range(início, fim+1, passo):
                sleep(0.5)
                print(i, end=' ')
    elif passo < 0:
        if início < fim:
            contador(int(input('\033[31mOpção inválida.\033[m Informe que número deseja iniciar a contagem: ')),
                     int(input('Informe que número deseja parar a contagem: ')),
                     int(input('Informe o passo da contagem: ')))
        else:
            for i in range(início, fim-1, passo):
                sleep(0.5)
                print(i, end=' ')


contador(1, 10, 1)

print('\n' + '-='*20)
contador(10, -1, -2)
print('\n' + '-='*20)
contador(int(input('Informe que número deseja iniciar a contagem: ')),
         int(input('Informe que número deseja parar a contagem: ')),
         int(input('Informe o passo da contagem: ')))
print('Fim')

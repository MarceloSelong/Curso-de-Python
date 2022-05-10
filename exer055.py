#Faça um programa que leia o peso de 5 pessoas.
#E no final, mostre qual foi o maior e o menor pesos lidos.
menor = 0
maior = 0
for c in range(1, 6):
    peso = input('Informe o peso da {}ª pessoa: '.format(c))
    peso = float(peso.replace(',', '.'))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        elif peso > maior:
            maior = peso
print('O maior peso foi \033[31m{}KG\033[m, e o menor peso foi \033[31m{}KG\033[m.'.format(maior, menor))
print('Fim')
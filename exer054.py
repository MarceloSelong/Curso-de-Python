#Crie um programa que leia o ano de nascimento de 7 pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
data = date.year
maior = 0
menor = 0
for c in range(1, 8, 1):
    num = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(c)))
    if data - num >= 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas são menor de idade e {} pessoas são maiores de idade.'.format(menor, maior))

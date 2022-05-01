#Crie um programa que leia o ano de nascimento de 7 pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
menor = 0
maior = 0
for c in range(1, 8, 1):
    num = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(c)))
    if num < 18:
        menor += 1
    else:
        maior += 1
print('{} pessoas são menor de idade e {} pessoas são maiores de idade.'.format(menor, maior))

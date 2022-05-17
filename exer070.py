# Crie um programa que leia o nome e o preço devários produtos.
# O programa de verá perguntar se o usuário vai continuar.
# No final mostre:
# A) Qual é o total gasto na compra
# B) Quantos produtos custam mais de R$1000,00
# C) Qual é o nome do produto mais barato.
from time import sleep
total = mil = mbarato = preco = 0
produto = ''
while True:
    print('-'*30)
    print('Loja Utilar')
    print('-'*30)
    nome = str(input('Nome do produto: '))
    if preco >= 1000:
        mil += +1
    if produto == '':
        produto = nome
    preco = str(input('Preço: R$')).replace(',', '.')
    preco = float(preco)
    total += preco
    if mbarato == 0:
        mbarato = preco
    if mbarato > preco:
        mbarato = preco
        produto = nome
    continuar = str(input('Quer continuar? [S/N]: ')).upper()
    while continuar not in 'SN':
        continuar = str(input('Informe corretamente! [S/N]: '))
    if continuar == 'N':
        break
    print()
print('\nCalculando...')
sleep(1)
print(f'O total da compra foi R${total:.2f}.')
print(f'Temos {mil} produtos custando mais de R$1000,00.')
print(f'O produto mais barato foi {produto}, que custa R${mbarato:.2f}.')
print('{:-^40}'.format('Fim do programa'))

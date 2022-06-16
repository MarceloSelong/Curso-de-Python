# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
lista = list()
galera = list()
continuar = 'S'
pesados = []
leves = []
while continuar in 'Ss':
    galera.append(str(input('Informe o nome: ')))
    galera.append(float(input('Informe o peso: ')))
    lista.append(galera[:])
    galera.clear()
    continuar = str(input('Quer continuar ? [S/N]'))
    while continuar not in 'SsNn':
        continuar = input('\033[31mOpção inválida.\033[m Deseja continuar? [Digite "S" para sim, ou "N" para não.]')
for p in range(0, len(lista)):
    if lista[p][1] >= 80:
        pesados.append(lista[p])
    else:
        leves.append(lista[p])
print('-'*30)
print('Lista 1', lista)
print('-'*30)
print(f'Foram cadastradas {len(lista):.0f} pessoas.')
print('-'*30)
print(f'Os pesos pesados são: {pesados}.')
print('-'*30)
print(f'Os pesos leves são: {leves}.')


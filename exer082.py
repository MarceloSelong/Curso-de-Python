# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados.
# Ao final, mostre o conteúdo das 3 listas geradas.
lista = []
pares = []
ímpares = []
while True:
    num = int(input('Informe um valor: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        ímpares.append(num)
    continuar = str(input('Quer continuar ? [S/N]'))
    if continuar in 'Nn':
        break
print('-'*30)
print(f'A lista completa é: {lista}.')
print(f'Os números pares digitados são: {pares}')
print(f'Os números ímpares digitados são: {ímpares}')

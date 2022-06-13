# Crie um programa que vai ler vários números e colocar em uma lista. Depois, mostre:
# A) Quantos Números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não está na lista.
lista = []
continuar = 'S'
while continuar in 'Ss':
    lista.append(int(input('Informe um valor: ')))
    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
    else:
        while True:
            continuar = str(input('\033[31mOpção inválida\033[m Quer continuar? [S/N]?'))
            if continuar in 'Ss' or continuar in 'Nn':
                break
print('-'*30)
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista ordenada de forma decrescente fica: {lista}')
if 5 in lista:
    print('O número 5 faz parte da lista.')
else:
    print('O número 5 não está na lista.')

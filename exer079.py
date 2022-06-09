# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista na lista, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitado, em ordem crescente.
lista = [0]
continuar = 'S'
while continuar in 'Ss':
    for i in range(len(lista)):
        num = int(input('Informe um valor: '))
        if i == 0:
            lista.append(num)
        elif num in lista:
            print('O número já existe na lista.')
            continue
        elif num not in lista:
            lista.append(num)
        continuar = input('Quer continuar ? [S/N]')
        if continuar in 'Ss':
            continue
        elif continuar in 'Nn':
            continuar = 'N'
            break
        else:
            while continuar not in 'SsNn':
                continuar = input('\033[31mOPÇÃO INVÁLIDA\033[m Quer continuar ? [S/N]')
lista.pop(0)
lista.sort()
print(f'Os números digitados em ordem crescente foram: {lista}.')

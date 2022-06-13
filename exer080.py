# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta(sem usar o sort()).
# No final, mostre a lista ordenada na tela.
lista = []
for i in range(0, 5):
    num = int(input('Informe um valor: '))
    if i == 0 or num > lista[-1]:
        lista.append(num)
    elif num < lista[0]:
        lista.insert(0, num)
    else:
        for i in range(1, len(lista)):
            if num > lista[i-1] and num < lista[i]:
                lista.insert(i, num)
print(f'Os números digitados em ordem foram: {lista}.')





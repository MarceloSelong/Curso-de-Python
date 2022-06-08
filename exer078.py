# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitados e suas respectivas posições na lista.
lista = []
menor = maior = 0
for i in range(0, 5):
    lista.append(int(input(f'Informe um valor para a posição {i}: ')))
    if i == 0:
        menor = lista[i]
        maior = lista[i]
    if lista[i] > maior:
        maior = lista[i]
    elif lista[i] < menor:
        menor = lista[i]
print(f'O menor valor digitado foi {menor}.')
print(f'O maior valor digitado foi {maior}.')

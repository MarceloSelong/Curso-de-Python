#Escreva um programa que leia dois números inteiros
# e compare-os, mostrando na tela uma mensagen:
#- O primeiro valor é maior
#- O segundo valor é maior
# Não existe valor maior, os dois são iguais
print('Comparador de valores')
n1 = int(input('Informe 2 números inteiros: '))
n2 = int(input())
if n1 > n2:
    print('O \033[34mprimeiro valor\033[m é maior: \033[35m{}\033[m'.format(n1))
elif n2 > n1:
    print('O \033[34msegundo valor\033[m é maior: \033[35m{}\033[m'.format(n2))
elif n1 == n2:
    print('Os \033[36mdois valores\033[m são iguais.')

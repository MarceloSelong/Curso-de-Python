#Algoritmo para criar uma lista aleatória com os nomes informados
from random import shuffle
n1 = input(str('Primeiro aluno: '))
n2 = input(str('Segundo aluno: '))
n3 = input(str('Terceiro aluno: '))
n4 = input(str('Quarto aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: \033[35m{}\033[m'.format(lista)+'.')
print('Fim')
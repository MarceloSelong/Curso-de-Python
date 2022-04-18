#Faça um programa que leia o nome completo de uma pessoa
#Mostrando em seguida o primeiro e
#o último nome da pessoa.
nome= input('Informe seu nome completo: ')
primeiro = nome.split()
ultimo = nome.split()
print('Seu primeiro nome é: {}.'.format(primeiro[0]).title())
print('Seu último nome é: {}.'.format(ultimo[-1]).title())

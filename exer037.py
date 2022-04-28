#Escreva um programa que leia um número inteiro qualquer
#e peça para o usuário escolher qual será a base de conversão
#1 para binário
#2 para octal
#3 para hexadecimal
num = int(input('Informe um número inteiro: '))
print('Deseja converter este numero para:')
print('Pressione 1 para binário')
print('Pressione 2 para octal')
print('Pressione 3 para hexadecimal')
choice = int(input())
if choice == 1:
    print(bin(num)[2:])
elif choice == 2:
    print(oct(num)[2:])
elif choice == 3:
    print(hex(num)[2:])

# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No ínicio, pergunte ao usuário qual será o valor a ser sacado(número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# 100 50 10 1
cem = cinquenta = dez = um = 0
print('='*30)
print('{:-^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Qual valor você quer sacar? R$'))
# Cédulas de Cem#
if valor % 100 == 0:
    cem = valor // 100
    print(f'Total de {cem} cédulas de R$100,00.')
elif valor % 100 != 0:
    cem = valor // 100
    print(f'Total de {cem} cédulas de R$100,00.')
    valor = valor - (cem*100)
    # Cédulas de Cinquenta#
    if valor % 50 == 0:
        cinquenta = valor // 50
        print(f'Total de {cinquenta} cédulas de R$50,00.')
    elif valor < 50:
        if valor % 10 == 0:
            dez = valor // 10
            print(f'Total de {dez} cédulas de R$10,00.')
        elif valor % 10 != 0:
            dez = valor // 10
            print(f'Total de {dez} cédulas de R$10,00.')
            um = valor - (dez*10)
            print(f'Total de {um} cédulas de R$1,00.')
    elif valor > 50:
        cinquenta = valor // 50
        print(f'Total de {cinquenta} cédulas de R$50,00.')
        valor = valor - (cinquenta*50)
        if valor % 10 == 0:
            dez = valor // 10
            print(f'Total de {dez} cédulas de R$10,00.')
        elif valor % 10 != 0:
            dez = valor // 10
            print(f'Total de {dez} cédulas de R$ 10,00.')
            um = valor - (dez*10)
            print(f'Total de {um} cédulas de R$1,00.')




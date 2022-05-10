#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre:
#-A média de idade do grupo
#-Qual é o nome do homem mais velho
#-E quantas mulheres tem menos de 21 anos.
midade = ''
media = 0
anos = 0
mul = 0
for c in range(0, 4,):
    nome = str(input('Informe o nome da passoa: ')).strip()
    idade = int(input('Informe a idade da pessoa: '))
    sexo = int(input("""Qual o sexo dessa pessoa ?
    (1) para masculino:
    (2) para feminino: """))
    media += idade
    if sexo == 1:
        if idade > anos:
            midade = nome
            anos = idade
    elif sexo == 2:
        if idade < 21:
            mul += 1
    else:
        print('Opção inválida.')
print('A média de idade do grupo é {} anos.'.format(media/4))
print('O homem mais velho é {}, com {} anos.'.format(midade, anos))
print('{} mulheres tem menos 21 anos.'.format(mul))
print('Fim')
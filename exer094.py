# Crie um programa que leia nome, sexo, e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário,
# e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média.
continuar = 'S'
cadastro = dict()
lista = list()
média = 0
mulheres = list()
maiores = list()
#-------------------------------------------------Programa principal---------------------------------------------------#
while continuar in 'S':
    cadastro['nome'] = str(input('Nome: '))
    sexo = input('Sexo masculino ou feminino? Pressione [M/F]: ').upper()[0]
    while sexo not in 'MF':
        sexo = input('\033[31mOpção inválida!\033[m Pressione [M] para masculino, ou [F] para feminino: ').upper()[0]
    cadastro['sexo'] = str(sexo)
    cadastro['idade'] = int(input('Informe a idade: '))
    média += cadastro['idade']
    if cadastro['sexo'] == 'F':
        mulheres.append(cadastro.copy())
    if cadastro['idade'] >= 18:
        maiores.append(cadastro.copy())
    lista.append(cadastro.copy())

#-------------------------------------------------Opção de continuar---------------------------------------------------#
    continuar = input('Deseja continuar ? [S/N]: ').upper()[0]
    while continuar not in 'SN':
        continuar = input('\033[31mOpção inválida!\033[m Pressione [S] para sim, ou [N] para não: ').upper()[0]
#----------------------------------------------------------------------------------------------------------------------#
média = média / len(lista)
print(f'\nForam cadastradas {len(lista)} pessoas.')
print(f'\nA média de idade do grupo é {média}')
print('As mulheres listadas são: ', end='')
for k, v in enumerate(mulheres):
    print(v['nome'], end=' ')
print()
print('As pessoas maiores de idade são: ', end='')
for k, v in enumerate(maiores):
    print(v['nome'], end=' ')



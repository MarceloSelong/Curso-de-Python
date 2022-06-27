# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista = list()
temp = list()
# Principal #
continuar = 'S'
while continuar in 'Ss':
    temp.append(str(input('Informe o nome do aluno: ')))
    for i in range(1, 3):
        temp.append(float(input(f'Informe a {i}ª nota do aluno: ').replace(',', '.')))
    lista.append(temp[:])
    temp.clear()
    continuar = str(input('Deseja continuar? [S/N] ').upper())
    while continuar not in "SN":
        continuar = str(input('\033[31mOpção inválida.\033[m Informe corretamente: [S/N]').upper())
print('-='*30)
print(f'{"Nº.":<4}{"Nome":<10}{"Média":<5}')
for i, x in enumerate(lista):
    print(f'{i:<4}{x[0]:<10}{(x[1]+x[2])/2:>5}    ')
print('-='*30)
escolha = input('\nDeseja mostrar as notas de qual aluno ? ["N" encerra o programa]: ')
if escolha in 'Nn':
    print('Encerrando...')
else:
    escolha = int(escolha)
    print(f'\nAs notas do aluno {lista[escolha][0]} foram {lista[escolha][1]} e {lista[escolha][2]}.')
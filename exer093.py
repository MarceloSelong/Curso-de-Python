# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final,  tudo isso será guardado em um dicionário
# incluindo o total de gols feitos durante o campeonato.
#-------------------------------------------------Inicialização--------------------------------------------------------#
cadastro = dict()
cadastro['Nome'] = str(input('Informe o nome do jogador: '))
partidas = int(input(f'Quantas partidas {cadastro["Nome"]} jogou? '))
lista = list()
#----------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------Programa principal-----------------------------------------------------#
for i in range(1, partidas+1):
    lista.append(int(input(f'    Quantos gols na partida {i} ? ')))
cadastro['gols'] = lista.copy()
cadastro['totgols'] = sum(lista)
#----------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------Finalização--------------------------------------------------------#
print('\n', cadastro)
print(f'\nO jogador {cadastro["Nome"]} fez {cadastro["totgols"]} gols no campeonato.')
print(f'\nJogou {partidas} partidas.\n')
for i in range(0, len(lista)):
    print(f'Na partida {i+1}, fez {lista[i]} gols.')
print('-='*30)
print(f'O jogador {cadastro["Nome"]} jogou {len(cadastro["gols"])} partidas.')
for i, v in enumerate(cadastro['gols']):
    print(f'   => Na partida {i+1}, fez {v} gols.')



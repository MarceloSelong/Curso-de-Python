# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# de aproveitamento de cada jogador.
time = []
gols = []
jogadores = {}
continuar = 'S'
cont = 0
while continuar in 'S':
    jogadores['cód'] = cont
    jogadores['nome'] = str(input('Informe o nome do jogador: '))
    jogadores['partidas'] = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    for i in range(0, jogadores['partidas']):
        gols.append(int(input(f'    Quantos gols na partida {i+1} ? ')))
    continuar = input('Quer continuar ? [S/N]: ').upper()[0]
    while continuar not in 'SN':
        continuar = input('\033[31mOpção inválida.\033[m Escolha [S] para sim ou [N] para não : ').upper()[0]
    jogadores['gols'] = gols.copy()
    gols.clear()
    jogadores['total'] = sum(jogadores['gols'])
    cont += 1
    time.append(jogadores.copy())
print()
print('-='*20)
print('{:^3} {:<15} {:<10} {:<5}'.format('Cód', 'nome', 'gols', 'total'))
print('-'*40)
for k, v in enumerate(time):
    print(f'{v["cód"]:<3} {v["nome"]:<15} {str(v["gols"]):<10} {v["total"]:<5}')
print('-='*20)
while True:
    busca = int(input('Digite o código do jogador para mostrar seus dados: [999 para parar]'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO ! Não existe jogador com o código {busca}! ')
    else:
        print(f' -- Levantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo, {i+1} fez {g} gols.')
    print('-' * 40)
print('Encerrando')

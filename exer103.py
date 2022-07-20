# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais
# O nome do jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome='', gols=0):
    dicio = {}
    if nome == '':
        nome = '<desconhecido>'
    if gols.isalpha():
        gols = 0

    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')






ficha(input('Informe o nome do jogador: '), input('Informe quantos gols ele marcou: '))



#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol,
# na ordem de colocação.
# Depois mostre:
# A) Apenas os cinco primeiro colocados
# B) Os últimos 4 colocados da tabela
# C) Uma lista com os times em ordem alfabética
# D) Em que posição na tabela está o time da Chapecoense.
tabela = ('Corinthians', 'Athletico MG', 'São Paulo', 'Botafogo', 'Santos', 'Coritiba', 'Avai',
          'Chapecoense', 'Palmeiras', 'Bragantino', 'Inter', 'Fluminense', 'Goiás', 'Cuiabá', 'Atlético - PR',
          'Flamengo',  'Juventude', 'Ceará', 'Atlético GO', 'Fortaleza')
print('-' * 30)
print(f'Lista de times do brasileirão: {tabela}')
print('-' * 30)
print(f'Os cinco primeiros colocados são: {tabela[0:5]}')
print('-' * 30)
print(f'Os 4 últimos colocados são: {tabela[-4:]}')
print('-' * 30)
print(f'A tabela em ordem alfabética fica: {sorted(tabela)}')
print('-' * 30)
print(f'A Chapecoense está na {tabela.index("Chapecoense")+1}ª posição.')

# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de
# uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL OU OBRIGATÓRIO nas eleições.
from datetime import date
def voto(ano, data=date.today().year):
    if data - ano >= 65 or data - ano == 17:
        return f'Com {data - ano} anos o voto é OPCIONAL'
    elif data - ano >= 18:
        return f'Com {data - ano} anos, o voto é OBRIGATÓRIO'
    else:
        return f'Com {data - ano} anos, NÃO vota.'


print(voto(int(input('Em que ano você nasceu? '))))

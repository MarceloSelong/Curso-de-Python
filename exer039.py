#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se é a hora de se alistar
#Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime
nasc = int(input('Informe seu ano de nascimento: '))
datetime = datetime.datetime.now()
data = datetime.date()
anoatual = int(data.strftime("%Y"))
if anoatual-nasc == 18:
    print('\033[33mVocê deve se alistar este ano!\033[m')
elif anoatual-nasc < 18:
    print('\033[34mVocê deve se alistar em {} anos.\033[m'.format(18-(anoatual-nasc)))
elif anoatual-nasc > 18:
    print('\033[31mVocê deveria ter se alistado á {} anos.\033[m'.format((anoatual-nasc)-18))

# Faça um mini sistema que utilize o interactive help do Python. O usuário vai digitar o comando e o manual vai aparecer
# Quando o usuário digitar a palavra 'fim'. o programa encerrará.
# Obs: use cores
def ajuda(msg):
    """
    -> Função para utilizar interactive help do Python
    :param msg: Recebe a mensagem a ser mostrada formatada
    :return:
    """
    from time import sleep
    while True:
        print('\033[1;97m\033[1;42m~' * (len(msg)+4))
        print(' ', msg)
        print('~' * (len(msg)+4))
        print('\033[m', end='')
        com = str(
            input('Informe o comando que deseja acessar a bibilioteca: \n[Digite "fim" para finalizar.]\n')).lower()
        if com == 'fim':
            print('\033[31mENCERRANDO...\033[m')
            sleep(1)
            break
        print('\033[1;44m', '\033[1;97m', f'ACESSANDO A BIBLIOTECA DO COMANDO: \'{com}\'')
        sleep(2)
        print('\033[1;107m\033[30m')
        help(com)
        print('\033[m\033[m')


ajuda('SISTEMA DE AJUDA PyHELP')

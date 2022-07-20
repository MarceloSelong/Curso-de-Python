# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular
# e o outro chamado show, que será um valor lógico(opcional) indicado se será mostrado ou não na tela o processo
# de cálculo do  fatorial.
def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do Fatorial de um número 'num'.
    """
    if not show:
        fat = num
        for i in range(num, 0, -1):
            fatorial = num
            num = fatorial * (i - 1)
        print(f'\nO fatorial de {fat} é {fatorial}.')
    elif show:
        for i in range(num, 0, -1):
            fatorial = num
            num = fatorial * (i - 1)
            if i != 1:
                print(i, end=' x ')
            else:
                print(f'{i} = {fatorial}')


fatorial(int(input('Informe o valor que deseja saber o fatorial: ')), False)
help(fatorial)

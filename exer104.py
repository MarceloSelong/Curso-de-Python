# Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante a função input() do Python.
# só que fazendo a validação para aceitar apenas um valor númerico.
# Ex: n = leiaint('Digite um n')
def leiaint(msg):
    n = input(msg)
    if n == ' ':
        n = 0
    if n.isnumeric() == True:
        return n
    else:
        print('Opção incorreta, digite novamente:')
        return leiaint('Digite um número: ')




n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}.')

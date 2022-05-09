# Números sucessores e antecessores()
cores = {'limpa': '\033[m',
         'verde': '\033[32m',
         'azul': '\033[4;34m',
         'roxo': '\033[4;35m'}
n = int(input('Informe um valor: '))
a = n-1
s = n+1
print('O antecessor de {}{}{} é {}{}{}. E o sucessor de {}{}{} é {}{}{}.'.format(cores['verde'], n, cores['limpa'],
                                                                                 cores['azul'], a, cores['limpa'],
                                                                                 cores['verde'], n, cores['limpa'],
                                                                                 cores['roxo'], s, cores['limpa']))
print('Fim')

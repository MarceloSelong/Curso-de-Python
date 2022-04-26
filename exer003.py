cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m'}
n1 = int(input('Informe dois valores:'))
n2 = int(input(''))
s = n1 + n2
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}.'.format(cores['amarelo'], n1, cores['limpa'], cores['azul'], n2, cores['limpa'], cores['roxo'], s, cores['limpa']))

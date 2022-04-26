cores = {'limpa': '\033[m',
         'verde': '\033[4;32m',
         'azul': '\033[4:34m',
         'roxo': '\033[4:35m'}
n1 = int(input('Informe um número: '))
print('O dobro deste número é {}{}{}, o triplo é {}{}{} e a raiz quadrada {}{:.2f}{}'.format(cores['verde'], n1*2,
                                                                                             cores['limpa'],
                                                                                             cores['azul'], n1*3,
                                                                                             cores['limpa'],
                                                                                             cores['roxo'], n1**(1/2),
                                                                                             cores['limpa']))

from math import floor
cor = {'azul': '\033[34m',
         'limpa': '\033[m'}
n = str(input('Informe um valor real: '))
n = n.replace(',', '.')
num = float(n)
arr = floor(num)
print('A porção inteira deste número é: \033[31m{:.0f}\033[m'.format(floor(num)))
print('A porção inteira deste número é:', cor['azul'], arr, cor['limpa'])
print('A porção inteira deste número é: \033[36m{}\033[m'.format(arr))
print('Fim')

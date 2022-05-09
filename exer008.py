cores = {'limpa': '\033[m',
         'azul': '\033[1;34m',
         'vermelho': '\033[1;31m',
         'roxo': '\033[1;35m'}
print('Conversor de metros p/ mm e cm.')
m = int(input('Informe quantos metros que deseja converter: '))
print('{}{}{}m equivalem a {}{}{}cm ou {}{}{}mm.'.format(cores['azul'], m, cores['limpa'], cores['vermelho'], m*100, cores['limpa'], cores['roxo'], m*1000, cores['limpa']))
print('Fim')

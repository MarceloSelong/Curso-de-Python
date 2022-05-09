cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m'}
s = input('Escreva algo: ')
print(type(s))
print('É', cores['amarelo'], 'numérico', cores['limpa'], '?', s.isnumeric())
print('É', cores['azul'], 'alfabético', cores['limpa'], '?', s.isalpha())
print('É um', cores['roxo'], 'digito', cores['limpa'], '?', s.isdigit())
print('É', cores['amarelo'], 'decimal', cores['limpa'], '?', s.isdecimal())
print('É', cores['azul'], 'alfanumérico', cores['limpa'], '?', s.isalnum())
print('É um', cores['roxo'], '???', cores['limpa'], s.isascii())
print('É um', cores['amarelo'], 'identificador', cores['limpa'], '?', s.isidentifier())
print('Fim')

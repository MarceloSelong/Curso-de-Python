s = input('Escreva algo:')
print(type(s))
print('É numérico ?', s.isnumeric())
print('É alfabético ?', s.isalpha())
print('É um digito ?', s.isdigit())
print('É decimal ? ', s.isdecimal())
print('É alfanumérico? ', s.isalnum())
print('É um ??? ', s.isascii())
print('É um identificador???', s.isidentifier())

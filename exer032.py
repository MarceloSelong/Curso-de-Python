#Primeira situação: Se o ano de 2015 ou 2016 for uma divisão exata em relação a 4,
# deveremos verificar, em seguida, se não é divisível por 100. Se não for, o ano será bissexto;

#Segunda situação: Se o ano de 2015 ou 2016 não for divisível por 4,
# então deveremos verificar se ele é divisível por 400. Se também não for divisível, o ano de 2015 não será bissexto;

#Terceira situação: Se o ano de 2015 ou 2016 não for divisível por 4,
# então devemos verificar se ele é divisível por 400. Caso seja, o ano de 2015 é bissexto.
print('Ano Bissexto')
ano = int(input('Informe o ano que deseja saber se é bissexto: '))
calc = ano % 4 == 0
if calc == True:
    if ano % 100 == 0:
        print('O ano {} não é bissexto.'.format(ano))
    else:
        print('O ano {} é bissexto.'.format(ano))
else:
    if ano % 400 == 0:
        print('O ano {} é bissexto.'.format(ano))
    else:
        print('O ano {} não é bissexto.'.format(ano))
print('Fim')

s = float(input('Informe o valor do seu sálario: '))
print('Seu novo sálario com reajuste de \033[31m15%\033[m será: \033[34mR${:.2f}\033[m.'.format(s/100*15+s))

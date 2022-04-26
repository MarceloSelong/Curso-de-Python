#Manipulando Strings
nome = input('Informe seu nome completo: ')
print('Seu nome em maiúsculo fica: \033[32m{}\033[m.'.format(nome.upper()))
print('Seu nome em minúsculo fica: \033[33m{}\033[m.'.format(nome.lower()))
print('Seu nome tem \033[4;34m{}\033[m letras sem os espaços.'.format(len(nome.replace(' ',''))))
nome2 = nome.split()
print('O primeiro nome tem \033[4;35m{}\033[m letras.'.format(len(nome2[0])))

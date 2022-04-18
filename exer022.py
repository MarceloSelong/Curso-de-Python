#Manipulando Strings
nome = input('Informe seu nome completo: ')
print('Seu nome em maiúsculo fica: {}.'.format(nome.upper()))
print('Seu nome em minúsculo fica: {}.'.format(nome.lower()))
print('Seu nome tem {} letras sem os espaços.'.format(len(nome.replace(' ',''))))
nome2 = nome.split()
print('O primeiro nome tem {} letras.'.format(len(nome2[0])))

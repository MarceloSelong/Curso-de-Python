# Algoritmo para escolher uma string aleatória informada pelo usuário
import random
nome1 = str(input('Informe o primeiro nome '))
nome2 = str(input('Informe o segundo nome '))
nome3 = str(input('Informe o terceiro nome '))
nome4 = str(input('Informe o quarto nome '))
print('O nome sorteado foi: {}'.format(random.choice([nome1, nome2, nome3, nome4])))

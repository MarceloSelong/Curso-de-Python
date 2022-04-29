#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
#utilizando um laço 'for'.
n = int(input('Informe o número que deseja saber a tabuada: '))
print('Tabuada do', n)
for c in range(0, 10+1):
    print('{} x {:2} = {}'.format(n, c, n*c))

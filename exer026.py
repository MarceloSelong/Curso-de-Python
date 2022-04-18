#Faça um programa que leia uma frase e mostre: Quantas vezes aparece a letra "A",
# em que posição ela aparece pela primeira vez e
# em que posição ela aparece pela última vez.]
frase = str(input('Informe uma frase: ')).lower().strip()
print('A letra "A" aparece {} vezes.'.format(frase.count('a')))
print('A letra "A" apareceu pela primeira vez no microespaço: {}.'.format(frase.find('a')+1))
print('A letra "A" apareceu pela última vez no microespaço: {}.'.format(frase.rfind('a')+1))
print(frase)

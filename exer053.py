#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços e acentos.
#Após a sopa
#A sacada da casa
#A torre da derrota
#O lobo ama o bolo
#Anotaram a data da maratona
frase = str(input('Informe uma frase: '))
palavras = frase.upper().strip().split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('A frase {} é um palíndromo.'.format(frase))
else:
    print('A frase {} não é um palíndromo.'.format(frase))

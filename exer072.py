# Crie um programa que tenha um tupla totalemnte preenchida com uma contagem por extenso, de zero até dez.
# Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso.
contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
num = int(input('Informe um número entre 0 e 10: '))
while True:
    if 0 <= num <= 10:
        break
    else:
        num = int(input('Informe um número entre 0 e 10: '))
print(f'O número {num} escrito por extenso é {contagem[num]}.')
